import { useCallback, useEffect } from "react"
import { graphClient } from "@/api/graphClient"
import { useGraphStore } from "@/store/graphStore"
import { useAppStore } from "@/store/appStore"
import { useSettingsStore } from "@/store/settingsStore"
import type { GroupingAxis } from "@/api/types"
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
