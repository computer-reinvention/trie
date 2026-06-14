import { useEffect } from "react"
import { useConnectionStore } from "@/store/connectionStore"

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const trie = () => (window as any).trie

/**
 * Bridge the main-process health signals (opencode process exit, stderr, SSE
 * stream errors) into the connection store so the UI can show a crash/degraded
 * banner instead of silently appearing to hang.
 *
 * Registers once on mount; each preload subscriber swaps any prior listener and
 * returns an unsubscribe fn, so dev hot-reload doesn't stack handlers.
 */
export function useConnectionHealth(): void {
  useEffect(() => {
    const t = trie()
    if (!t) return

    const setDegraded = useConnectionStore.getState().setDegraded
    const setCrashed = useConnectionStore.getState().setCrashed
    const noteError = useConnectionStore.getState().noteError

    const offExited = t.onOpencodeExited?.((info: { code: number | null; expected?: boolean }) => {
      // An intentional teardown (restart/quit) is not a crash.
      if (info.expected) return
      setCrashed(info.code, `opencode exited with code ${info.code ?? "unknown"}`)
    })

    const offStderr = t.onOpencodeStderr?.((line: string) => {
      if (line?.trim()) noteError(line)
    })

    const offSseError = t.onSseError?.((msg: string) => {
      // The stream dropped but the process may still be alive — the main
      // process auto-reconnects, so this is a transient degradation.
      setDegraded(msg)
    })

    return () => {
      if (typeof offExited === "function") offExited()
      if (typeof offStderr === "function") offStderr()
      if (typeof offSseError === "function") offSseError()
    }
  }, [])
}
