import { useEffect } from "react"
import { graphClient } from "@/api/graphClient"
import { useGraphStore } from "@/store/graphStore"
import { useAppStore } from "@/store/appStore"

// Load the system model (the high-level "model of the system") + edges into the
// graph store on project open. The model is cached server-side, so this is fast
// after the first call. The store derives the L0 component view from it.
export function useGraphPopulation(opencodePort: number | null): void {
  const appStore = useAppStore()
  const graphStore = useGraphStore()

  useEffect(() => {
    if (!opencodePort) return
    let cancelled = false

    async function populate(): Promise<void> {
      appStore.setGraphLoading(true, "Building the system model…")
      try {
        const [model, edgesRes] = await Promise.all([
          graphClient.systemModel(),
          graphClient.allEdges({ limit: 50000 }),
        ])
        if (cancelled) return
        if (!model?.nodes?.length) {
          console.error("[graph] systemModel returned no nodes:", model)
          appStore.setGraphLoading(false)
          return
        }
        const edges = edgesRes?.edges ?? []
        console.log(
          `[graph] system model: ${model.stats.production_nodes} prod nodes, ` +
            `${model.stats.role_count} roles, ${model.stats.subsystem_count} subsystems, ` +
            `${edges.length} edges`,
        )
        graphStore.setModel(model, edges)
      } catch (err) {
        console.error("Graph population failed:", err)
      } finally {
        if (!cancelled) appStore.setGraphLoading(false)
      }
    }

    populate()
    return () => {
      cancelled = true
    }
  }, [opencodePort])
}
