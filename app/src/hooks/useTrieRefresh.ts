import { useEffect } from "react"
import { useRefreshStore, type RefreshEvent } from "@/store/refreshStore"

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const trie = () => (window as any).trie

/**
 * Subscribe to the `trie refresh --json` progress stream relayed by the main
 * process and feed it into the refresh store. When a run finishes and the graph
 * actually changed (or was rebuilt from an empty store), invoke `onRefreshed`
 * so the caller can re-fetch the system model — this is what makes a fresh
 * checkout populate the canvas without a manual reload.
 *
 * Registers once on mount; the preload's onTrieRefresh swaps any prior listener
 * so dev hot-reload doesn't stack handlers.
 */
export function useTrieRefresh(onRefreshed: () => void): void {
  const apply = useRefreshStore((s) => s.apply)

  useEffect(() => {
    const t = trie()
    if (!t?.onTrieRefresh) return

    const unsubscribe = t.onTrieRefresh((event: RefreshEvent) => {
      apply(event)
      // When the gate reports it changed the graph, re-pull. Also re-pull on a
      // clean exit as a safety net for the first-run rebuild, where the canvas
      // may have queried the empty graph before the rebuild landed.
      if (event.kind === "summary" && event.refreshed) onRefreshed()
      else if (event.kind === "exit" && event.code === 0) onRefreshed()
    })

    return () => {
      if (typeof unsubscribe === "function") unsubscribe()
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])
}
