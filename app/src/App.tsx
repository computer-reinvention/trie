import { useEffect, useRef, useState } from "react"
import { Editor } from "@/components/Editor"
import { Sidebar } from "@/components/Sidebar"
import { AgentPanel } from "@/components/AgentPanel"
import { TitleBar, TitleBarIconButton, GearIcon } from "@/components/TitleBar"
import { Settings } from "@/components/Settings"
import { useAppStore } from "@/store/appStore"
import { useSettingsStore } from "@/store/settingsStore"
import { setGraphClientBase, graphClient } from "@/api/graphClient"
import { setOpenCodeClientBase } from "@/api/opencodeClient"
import { useOpenCodeSSE } from "@/hooks/useOpenCodeSSE"
import { useGraphPopulation } from "@/hooks/useGraphPopulation"
import { useTrieRefresh } from "@/hooks/useTrieRefresh"
import { useActivityPoll } from "@/hooks/useActivityPoll"
import { useConnectionHealth } from "@/hooks/useConnectionHealth"
import { useTrieCommandEffects } from "@/hooks/useTrieCommandEffects"
import { TriefactStatus } from "@/components/TriefactStatus"
import { ContextMenu } from "@/components/ContextMenu"
import { ActivityBadge } from "@/components/ActivityBadge"
import { ConnectionBanner } from "@/components/ConnectionBanner"
import { useConnectionStore } from "@/store/connectionStore"
import { useTrieConfigStore } from "@/store/trieConfigStore"

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const trie = () => (window as any).trie

function AppShell() {
  const { opencodePort, projectDir, projectName, totalSymbols, totalFiles } = useAppStore()
  const [settingsOpen, setSettingsOpen] = useState(false)
  useOpenCodeSSE(opencodePort ?? 0)
  const { repopulate } = useGraphPopulation(opencodePort && opencodePort > 0 ? opencodePort : null)
  // Stream startup-refresh progress into the status display, and re-pull the
  // graph once the refresh rebuilds/updates it (fresh-checkout population).
  useTrieRefresh(repopulate)
  // Poll the cross-process activity DB to glow syncing/stale files + badge.
  useActivityPoll(!!opencodePort && opencodePort > 0)
  // Surface opencode crashes / stream drops instead of silently hanging.
  useConnectionHealth()
  // After a trie command (init/sync/refresh) finishes, reload config +
  // repopulate the graph + refresh the project summary.
  useTrieCommandEffects(repopulate)

  // ⌘, opens settings; Esc closes it.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === ",") {
        e.preventDefault()
        setSettingsOpen((v) => !v)
      } else if (e.key === "Escape" && settingsOpen) {
        setSettingsOpen(false)
      }
    }
    window.addEventListener("keydown", onKey)
    return () => window.removeEventListener("keydown", onKey)
  }, [settingsOpen])

  if (!projectDir) return null

  return (
    <div className="flex flex-col h-full text-slate-100 overflow-hidden" style={{ background: "var(--bg-app)" }}>
      <TitleBar
        title={projectName || "trie"}
        subtitle={totalSymbols > 0 ? `${totalSymbols} symbols · ${totalFiles} files` : undefined}
        actions={
          <>
            <ActivityBadge />
            <TitleBarIconButton onClick={() => setSettingsOpen(true)} title="Settings (⌘,)">
              <GearIcon />
            </TitleBarIconButton>
          </>
        }
      />
      <div className="flex-1 flex min-h-0 overflow-hidden relative">
        <Sidebar />
        <div className="flex-1 flex flex-col min-w-0">
          <Editor />
        </div>
        <AgentPanel />
        {/* Settings fills the area BELOW the title bar so traffic lights stay clear */}
        {settingsOpen && <Settings onClose={() => setSettingsOpen(false)} />}
      </div>
      <ConnectionBanner />
      <TriefactStatus />
      <ContextMenu />
    </div>
  )
}

function OpenProjectScreen({ onOpen }: { onOpen: () => void }) {
  const [loading, setLoading] = useState(false)
  const [autoOpening, setAutoOpening] = useState(true)
  const [recent, setRecent] = useState<string[]>([])
  const [error, setError] = useState<string | null>(null)
  const attempted = useRef(false)

  const openDir = async (dir: string) => {
    setLoading(true)
    setError(null)
    try {
      await trie().openProject(dir)
      setTimeout(onOpen, 50)
    } catch (err) {
      setError(String(err))
      setLoading(false)
    }
  }

  // Auto-open the most recent project on launch (project persistence).
  useEffect(() => {
    if (attempted.current) return
    attempted.current = true
    ;(async () => {
      try {
        const list: string[] = (await trie().getRecentProjects()) ?? []
        setRecent(list)
        if (list.length > 0) {
          await openDir(list[0])
          return
        }
      } catch {
        /* fall through to manual */
      }
      setAutoOpening(false)
    })()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const handleOpen = async () => {
    const dir = await trie().showOpenDialog()
    if (dir) await openDir(dir)
  }

  return (
    <div className="flex flex-col h-full" style={{ background: "var(--bg-app)" }}>
      <TitleBar title="trie" />
      <div className="flex-1 flex items-center justify-center">
      <div className="flex flex-col items-center gap-6">
        <div className="text-center">
          <h1 className="text-4xl font-bold text-1 font-mono tracking-tight">trie</h1>
          <p className="text-3 text-sm mt-2">graph-based code editor</p>
        </div>
        {error && (
          <p
            className="text-sm rounded px-3 py-2 max-w-sm text-center"
            style={{
              color: "#fda4af",
              background: "var(--danger-soft)",
              border: "1px solid color-mix(in srgb, var(--danger) 40%, transparent)",
            }}
          >
            {error}
          </p>
        )}
        {autoOpening && !error ? (
          <div className="flex items-center gap-2 text-3 text-sm">
            <span
              className="w-4 h-4 border-2 rounded-full animate-spin"
              style={{ borderColor: "var(--border-strong)", borderTopColor: "var(--accent)" }}
            />
            Opening last project…
          </div>
        ) : (
          <>
            <button
              className="bg-accent text-white rounded-lg px-6 py-3 text-sm font-medium transition-colors disabled:opacity-50"
              onClick={handleOpen}
              disabled={loading}
            >
              {loading ? "Opening…" : "Open Project"}
            </button>
            {recent.length > 0 && (
              <div className="flex flex-col items-stretch gap-1 w-72">
                <p className="text-faint text-xs uppercase tracking-wide">Recent</p>
                {recent.slice(0, 5).map((p) => (
                  <button
                    key={p}
                    className="text-left text-2 hover:text-1 hover:surface-2 rounded px-2 py-1.5 text-xs font-mono truncate transition-colors"
                    onClick={() => openDir(p)}
                    disabled={loading}
                    title={p}
                  >
                    {p.split("/").slice(-2).join("/")}
                  </button>
                ))}
              </div>
            )}
          </>
        )}
      </div>
      </div>
    </div>
  )
}

export function App() {
  const [projectOpened, setProjectOpened] = useState(false)
  const { setServers, setProject } = useAppStore()
  const loadSettings = useSettingsStore((s) => s.load)
  // Track whether we've registered the listener to avoid duplicates
  const listenerRegistered = useRef(false)

  // load persisted settings + apply theme as early as possible
  useEffect(() => {
    loadSettings()
  }, [loadSettings])

  useEffect(() => {
    if (listenerRegistered.current) return
    listenerRegistered.current = true

    trie().onServersReady(async (ports: { opencodePort: number; projectDir: string }) => {
      // Wire up clients before doing anything else
      setGraphClientBase(ports.opencodePort)
      setOpenCodeClientBase(ports.opencodePort)
      setServers(ports)
      // The sidecar is up and the clients are wired — mark the connection live.
      // (A later crash/restart flips this via useConnectionHealth.)
      useConnectionStore.getState().setLive()

      // Load trie.toml early so the graph's empty-state knows whether the
      // project is initialised (offers "Initialize trie" vs "Build graph").
      useTrieConfigStore.getState().load(ports.projectDir)

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

      // Sessions are loaded/created by the agent panel (useSessions) once
      // serversReady flips true. Transition to AppShell now that state is set.
      setProjectOpened(true)
    })
  }, [])

  return (
    <div className="h-screen w-screen overflow-hidden" style={{ background: "var(--bg-app)" }}>
      {projectOpened ? <AppShell /> : <OpenProjectScreen onOpen={() => setProjectOpened(true)} />}
    </div>
  )
}
