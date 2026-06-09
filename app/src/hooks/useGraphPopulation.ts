import { useCallback, useEffect } from "react"
import { graphClient } from "@/api/graphClient"
import { useGraphStore } from "@/store/graphStore"
import { useAGMStore } from "@/store/agmStore"
import { useAppStore } from "@/store/appStore"
import { useSettingsStore } from "@/store/settingsStore"
import type { GroupingAxis, AttentionEventType, TypedEdge } from "@/api/types"
import type { MemberGrouping } from "@/store/graphStore"

// Load the system model (the high-level "model of the system") + edges into the
// graph store on project open. The model is cached server-side, so this is fast
// after the first call. The store derives the L0 component view from it.
//
// Returns a `repopulate` callback so callers can force a re-fetch — used by the
// startup-refresh flow: when `trie refresh` rebuilds an empty graph, the canvas
// must re-query rather than stay stuck on the empty-graph result it got first.
export function useGraphPopulation(opencodePort: number | null): { repopulate: () => void } {
  const appStore = useAppStore()
  const graphStore = useGraphStore()

  const populate = useCallback(
    async function populate(cancelledRef?: { cancelled: boolean }): Promise<void> {
      const isCancelled = () => cancelledRef?.cancelled ?? false
      appStore.setGraphLoading(true, "Building the system model…")
      try {
        const settings = useSettingsStore.getState()
        const includeTests = settings.get<boolean>("graph.showTests")
        const [model, edgesRes] = await Promise.all([
          graphClient.systemModel({ includeTests }),
          graphClient.allEdges({ limit: 50000 }),
        ])
        if (isCancelled()) return
        if (!model?.nodes?.length) {
          // An empty model here is expected on a fresh checkout while the
          // startup refresh is still rebuilding the graph. Don't treat it as
          // a hard error — the refresh hook calls repopulate() once the
          // rebuild lands. Leave the loading state up so the canvas shows the
          // triefact-generation status rather than a bare "no model" message.
          console.warn("[graph] systemModel returned no nodes yet (refresh may be in flight)")
          return
        }
        const edges = edgesRes?.edges ?? []
        console.log(
          `[graph] system model: ${model.stats.production_nodes} prod nodes, ` +
            `${model.stats.role_count} roles, ${model.stats.subsystem_count} subsystems, ` +
            `${edges.length} edges`,
        )
        graphStore.setModel(model, edges)
        // apply user setting overrides for grouping
        graphStore.setAxis(settings.get<GroupingAxis>("graph.defaultAxis"))
        graphStore.setMemberGrouping(settings.get<MemberGrouping>("graph.memberGrouping"))

        // AGM: load the same model + typed edges into the attention engine.
        // setModel seeds HISTORICAL mass from the model (stable angular
        // geography). We do NOT replay the event log as live mass — a fresh
        // session must start blank (live mass = current focus only). Live mass
        // is rebuilt from this session's own SSE activity. Only events from a
        // short recent window are restored, so reconnecting mid-investigation
        // doesn't lose the live picture; older events are intentionally dropped.
        useAGMStore.getState().setModel(model, edges as TypedEdge[])
        try {
          const now = Date.now() / 1000
          const RECENT_WINDOW_S = 600 // 10 min — only genuinely-live attention
          const att = await graphClient.attention({ since: now - RECENT_WINDOW_S })
          if (!isCancelled() && att?.events?.length) {
            const agm = useAGMStore.getState()
            for (const e of att.events) {
              if (e.investigation_id) agm.graph.setInvestigation(e.investigation_id)
              agm.ingest(e.target, e.event_type as AttentionEventType, e.ts)
            }
            agm.recompute()
          }
        } catch (err) {
          console.warn("[agm] attention hydrate skipped:", err)
        }

        appStore.setGraphLoading(false)
      } catch (err) {
        console.error("Graph population failed:", err)
        if (!isCancelled()) appStore.setGraphLoading(false)
      }
    },
    // appStore/graphStore are stable zustand hook results within a render; the
    // effective dep is opencodePort, which gates whether a fetch makes sense.
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [opencodePort],
  )

  useEffect(() => {
    if (!opencodePort) return
    const ref = { cancelled: false }
    populate(ref)
    return () => {
      ref.cancelled = true
    }
  }, [opencodePort, populate])

  const repopulate = useCallback(() => {
    if (!opencodePort) return
    populate()
  }, [opencodePort, populate])

  return { repopulate }
}
