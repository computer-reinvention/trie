import { useEffect } from "react"
import { useTrieCommandStore } from "@/store/trieCommandStore"
import { useTrieConfigStore } from "@/store/trieConfigStore"
import { useAppStore } from "@/store/appStore"
import { graphClient } from "@/api/graphClient"

// Centralised side-effects for trie CLI commands run from the UI. When a
// state-changing command finishes successfully, the rest of the app must catch
// up to the new on-disk reality:
//
//   init            → trie.toml now exists + graph built → reload config + repopulate graph + refresh summary
//   sync / refresh  → graph + triefacts changed → repopulate graph + refresh project summary
//   verify/status/audit/plan → read-only, no side-effects
//
// Subscribes once; the store invokes every registered listener on a clean exit.
export function useTrieCommandEffects(repopulate: () => void): void {
  // Ensure the IPC event listener is wired even if the trie panel was never
  // opened (so a command kicked off from Settings still streams + completes).
  const subscribe = useTrieCommandStore((s) => s.subscribe)
  const onComplete = useTrieCommandStore((s) => s.onComplete)

  useEffect(() => {
    subscribe()
    const off = onComplete(({ command, ok }) => {
      if (!ok) return
      const { projectDir, setProject } = useAppStore.getState()

      const refreshesGraph =
        command === "init" || command === "sync" || command === "refresh"

      if (command === "init" && projectDir) {
        // trie.toml was just created — re-read it so Settings leaves the
        // "missing" state and shows the live config.
        useTrieConfigStore.getState().load(projectDir)
      }

      if (refreshesGraph) {
        // Re-pull the system model now that the graph changed.
        repopulate()
        // Refresh the title-bar symbol/file counts.
        graphClient
          .summary()
          .then((summary) => {
            if (!projectDir) return
            const dirName = projectDir.split("/").pop() ?? "project"
            setProject(
              projectDir,
              summary.project_name || dirName,
              summary.total_symbols,
              summary.total_files,
            )
          })
          .catch(() => {})
      }
    })
    return off
  }, [subscribe, onComplete, repopulate])
}
