import { useEffect, useRef, useState } from "react"
import { ReactFlowProvider } from "@xyflow/react"
import { GraphCanvas } from "@/components/GraphCanvas"
import { Sidebar } from "@/components/Sidebar"
import { InputBar } from "@/components/InputBar"
import { TurnHistory } from "@/components/TurnHistory"
import { useAppStore } from "@/store/appStore"
import { useAgentStore } from "@/store/agentStore"
import { setGraphClientBase, graphClient } from "@/api/graphClient"
import { setOpenCodeClientBase } from "@/api/opencodeClient"
import { useOpenCodeSSE } from "@/hooks/useOpenCodeSSE"
import { useGraphPopulation } from "@/hooks/useGraphPopulation"

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const trie = () => (window as any).trie

function AppShell() {
  const { opencodePort, projectDir } = useAppStore()
  useOpenCodeSSE(opencodePort ?? 0)
  useGraphPopulation(opencodePort && opencodePort > 0 ? opencodePort : null)

  if (!projectDir) return null

  return (
    <div className="flex h-screen bg-slate-950 text-slate-100 overflow-hidden">
      <Sidebar />
      <div className="flex-1 flex flex-col min-w-0">
        <GraphCanvas className="flex-1" />
        <TurnHistory />
        <InputBar />
      </div>
    </div>
  )
}

function OpenProjectScreen({ onOpen }: { onOpen: () => void }) {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleOpen = async () => {
    setLoading(true)
    setError(null)
    try {
      const dir = await trie().showOpenDialog()
      if (dir) {
        // openProject spawns opencode and waits for it to be ready.
        // ipc:servers-ready fires during this call; onServersReady in App
        // will handle the transition to AppShell — onOpen() is called from there.
        await trie().openProject(dir)
        // openProject resolved means the server is up; onServersReady already
        // fired and called onOpen(). If for some reason it hasn't (timing),
        // wait a tick to let the IPC event process.
        setTimeout(onOpen, 50)
      }
    } catch (err) {
      setError(String(err))
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="flex h-screen bg-slate-950 items-center justify-center">
      <div className="flex flex-col items-center gap-6">
        <div className="text-center">
          <h1 className="text-4xl font-bold text-slate-100 font-mono tracking-tight">trie</h1>
          <p className="text-slate-500 text-sm mt-2">graph-based code editor</p>
        </div>
        {error && (
          <p className="text-red-400 text-sm bg-red-900/20 border border-red-800 rounded px-3 py-2 max-w-sm text-center">
            {error}
          </p>
        )}
        <button
          className="bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg px-6 py-3 text-sm font-medium transition-colors disabled:opacity-50"
          onClick={handleOpen}
          disabled={loading}
        >
          {loading ? "Opening…" : "Open Project"}
        </button>
      </div>
    </div>
  )
}

export function App() {
  const [projectOpened, setProjectOpened] = useState(false)
  const { setServers, setProject } = useAppStore()
  const { setSession } = useAgentStore()
  // Track whether we've registered the listener to avoid duplicates
  const listenerRegistered = useRef(false)

  useEffect(() => {
    if (listenerRegistered.current) return
    listenerRegistered.current = true

    trie().onServersReady(async (ports: { opencodePort: number; projectDir: string }) => {
      // Wire up clients before doing anything else
      setGraphClientBase(ports.opencodePort)
      setOpenCodeClientBase(ports.opencodePort)
      setServers(ports)

      try {
        const summary = await graphClient.summary()
        const dirName = ports.projectDir.split("/").pop() ?? "project"
        setProject(
          ports.projectDir,
          summary.project_name || dirName,
          summary.total_symbols,
          summary.total_files,
        )
      } catch (err) {
        console.error("Failed to fetch project summary:", err)
      }

      try {
        const session = await graphClient.createSession("trie desktop")
        if (session?.id) setSession(session.id)
      } catch (err) {
        console.error("Failed to create session:", err)
      }

      // Transition to AppShell only after state is fully set
      setProjectOpened(true)
    })
  }, [])

  if (!projectOpened) {
    return <OpenProjectScreen onOpen={() => setProjectOpened(true)} />
  }

  return (
    <ReactFlowProvider>
      <AppShell />
    </ReactFlowProvider>
  )
}
