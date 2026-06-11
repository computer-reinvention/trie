import { useMemo, useState, useEffect, useRef, useCallback } from "react"
import { useAgentStore, useActiveSession } from "@/store/agentStore"
import { useAppStore } from "@/store/appStore"
import { opencodeClient } from "@/api/opencodeClient"
import { useSessions } from "@/hooks/useSessions"
import { displayTitle, relativeTime, updatedAt } from "@/lib/sessionTitle"
import { Transcript } from "./Transcript"
import { Composer } from "./Composer"
import {
  ChevronDown,
  Plus,
  Trash2,
  Loader2,
  Search,
  MessageSquarePlus,
  Eraser,
} from "./icons"
import type { PermissionReply } from "@/api/types"

const PANEL_WIDTH_KEY = "trie.agentPanel.width"
const MIN_WIDTH = 320
const MAX_WIDTH = 720
const DEFAULT_WIDTH = 384

// Drag-to-resize the panel from its left edge. Width is clamped and persisted to
// localStorage so it survives reloads. Dragging sets a body cursor + disables
// text selection for the duration.
function usePanelResize() {
  const [width, setWidth] = useState<number>(() => {
    const stored = Number(localStorage.getItem(PANEL_WIDTH_KEY))
    return stored >= MIN_WIDTH && stored <= MAX_WIDTH ? stored : DEFAULT_WIDTH
  })
  const [resizing, setResizing] = useState(false)

  const onResizeStart = useCallback(
    (e: React.MouseEvent) => {
      e.preventDefault()
      setResizing(true)
      const startX = e.clientX
      const startWidth = width
      const prevCursor = document.body.style.cursor
      const prevSelect = document.body.style.userSelect
      document.body.style.cursor = "col-resize"
      document.body.style.userSelect = "none"

      const onMove = (ev: MouseEvent) => {
        // dragging left (smaller clientX) widens the right-hand panel
        const next = Math.min(MAX_WIDTH, Math.max(MIN_WIDTH, startWidth + (startX - ev.clientX)))
        setWidth(next)
      }
      const onUp = () => {
        setResizing(false)
        document.body.style.cursor = prevCursor
        document.body.style.userSelect = prevSelect
        window.removeEventListener("mousemove", onMove)
        window.removeEventListener("mouseup", onUp)
        setWidth((w) => {
          localStorage.setItem(PANEL_WIDTH_KEY, String(w))
          return w
        })
      }
      window.addEventListener("mousemove", onMove)
      window.addEventListener("mouseup", onUp)
    },
    [width],
  )

  return { width, onResizeStart, resizing }
}

// The fixed right-hand agent panel — the whole agentic interface: a session
// switcher, the scrolling transcript, and the composer. This replaces the old
// bottom input bar and the standalone inspector.
export function AgentPanel() {
  const { newSession, switchSession, deleteSession, clearEmpty, send, abort } = useSessions()
  const sessions = useAgentStore((s) => s.sessions)
  const order = useAgentStore((s) => s.order)
  const activeId = useAgentStore((s) => s.activeId)
  const active = useActiveSession()
  const serversReady = useAppStore((s) => s.serversReady)
  const [menuOpen, setMenuOpen] = useState(false)
  const [filter, setFilter] = useState("")
  const menuRef = useRef<HTMLDivElement | null>(null)
  const { width, onResizeStart, resizing } = usePanelResize()

  // dismiss the session list on outside click / Escape
  useEffect(() => {
    if (!menuOpen) return
    const onDown = (e: MouseEvent) => {
      if (menuRef.current && !menuRef.current.contains(e.target as Node)) setMenuOpen(false)
    }
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && setMenuOpen(false)
    window.addEventListener("mousedown", onDown)
    window.addEventListener("keydown", onKey)
    return () => {
      window.removeEventListener("mousedown", onDown)
      window.removeEventListener("keydown", onKey)
    }
  }, [menuOpen])

  // reset the filter whenever the popover closes
  useEffect(() => {
    if (!menuOpen) setFilter("")
  }, [menuOpen])

  // sessions sorted most-recent-first for the dropdown
  const sortedSessions = useMemo(
    () => order.map((id) => sessions[id]).filter(Boolean),
    [order, sessions],
  )

  const visibleSessions = useMemo(() => {
    const q = filter.trim().toLowerCase()
    if (!q) return sortedSessions
    return sortedSessions.filter((s) => displayTitle(s.info).toLowerCase().includes(q))
  }, [sortedSessions, filter])

  const showFilter = sortedSessions.length > 6

  // Index pending permissions by the tool callID they belong to.
  const permissionsByCallID = useMemo(() => {
    const map: Record<string, import("@/api/types").PermissionRequest> = {}
    if (active) {
      for (const req of Object.values(active.permissions)) {
        if (req.callID) map[req.callID] = req
      }
    }
    return map
  }, [active])

  const resolvePermission = async (requestID: string, reply: PermissionReply) => {
    if (active) useAgentStore.getState().removePermission(active.info.id, requestID)
    await opencodeClient.replyPermission(requestID, reply)
  }

  const activeTitle = active ? displayTitle(active.info) : "chat"

  return (
    <aside
      className="relative shrink-0 surface-1 border-l border-subtle flex flex-col overflow-hidden"
      style={{ width }}
    >
      {/* drag-to-resize handle on the panel's left edge */}
      <div
        onMouseDown={onResizeStart}
        className="absolute left-0 top-0 bottom-0 w-1 -ml-0.5 z-30 cursor-col-resize group"
        title="Drag to resize"
      >
        <div
          className="absolute inset-y-0 left-0 w-0.5 transition-colors group-hover:bg-accent"
          style={{ background: resizing ? "var(--accent)" : "transparent" }}
        />
      </div>

      {/* session switcher */}
      <div className="relative flex items-center gap-1.5 px-2.5 py-2 border-b border-subtle shrink-0">
        <button
          className="flex-1 min-w-0 flex items-center gap-2 surface-2 border border-subtle rounded-lg text-sm text-1 px-2.5 py-1.5 hover:surface-3 transition-colors outline-none"
          onClick={() => setMenuOpen((v) => !v)}
          title={activeTitle}
        >
          {active?.running && (
            <Loader2 size={13} className="animate-spin shrink-0" style={{ color: "var(--accent)" }} />
          )}
          <span className="truncate flex-1 text-left">{activeTitle}</span>
          <ChevronDown size={14} className="text-3 shrink-0" />
        </button>
        <button
          className="shrink-0 inline-flex items-center justify-center w-8 h-8 rounded-lg text-2 hover:text-1 surface-2 hover:surface-3 border border-subtle transition-colors"
          onClick={newSession}
          title="New chat"
        >
          <Plus size={16} />
        </button>

        {menuOpen && (
          <div
            ref={menuRef}
            className="absolute left-2.5 right-2.5 top-full mt-1.5 z-50 rounded-xl border border-strong surface-pop elev-2 overflow-hidden"
          >
            {showFilter && (
              <div className="flex items-center gap-2 px-3 py-2 border-b border-subtle">
                <Search size={13} className="text-faint shrink-0" />
                <input
                  autoFocus
                  className="flex-1 bg-transparent text-sm text-1 outline-none placeholder:text-faint"
                  placeholder="Filter chats…"
                  value={filter}
                  onChange={(e) => setFilter(e.target.value)}
                />
              </div>
            )}
            <div className="max-h-72 overflow-y-auto scroll-thin py-1">
              {visibleSessions.length === 0 && (
                <div className="px-3 py-3 text-xs text-faint text-center">
                  {filter ? "No matching chats." : "No chats yet."}
                </div>
              )}
              {visibleSessions.map((s) => {
                const isActive = s.info.id === activeId
                return (
                  <div
                    key={s.info.id}
                    className={`group relative flex items-center gap-2 mx-1 px-2.5 py-1.5 rounded-lg cursor-pointer transition-colors ${
                      isActive ? "surface-3" : "hover:surface-2"
                    }`}
                    onClick={() => {
                      switchSession(s.info.id)
                      setMenuOpen(false)
                    }}
                  >
                    {isActive && (
                      <span
                        className="absolute left-0 top-1.5 bottom-1.5 w-0.5 rounded-full"
                        style={{ background: "var(--accent)" }}
                      />
                    )}
                    <div className="min-w-0 flex-1">
                      <div className="text-xs text-1 truncate">{displayTitle(s.info)}</div>
                      <div className="text-[10px] text-faint">
                        {relativeTime(updatedAt(s.info))}
                      </div>
                    </div>
                    {s.running && (
                      <Loader2
                        size={12}
                        className="animate-spin shrink-0"
                        style={{ color: "var(--accent)" }}
                      />
                    )}
                    {sortedSessions.length > 1 && (
                      <button
                        className="shrink-0 inline-flex items-center justify-center w-6 h-6 rounded-md text-faint opacity-0 group-hover:opacity-100 hover:text-1 transition-all"
                        style={{ ["--hover" as string]: "var(--danger)" }}
                        title="Delete chat"
                        onClick={(e) => {
                          e.stopPropagation()
                          deleteSession(s.info.id)
                        }}
                      >
                        <Trash2 size={13} />
                      </button>
                    )}
                  </div>
                )
              })}
            </div>
            <div className="border-t border-subtle flex">
              <button
                className="flex-1 inline-flex items-center gap-1.5 px-3 py-2 text-[11px] text-2 hover:surface-2 hover:text-1 transition-colors"
                onClick={() => {
                  newSession()
                  setMenuOpen(false)
                }}
              >
                <MessageSquarePlus size={13} />
                New chat
              </button>
              <button
                className="inline-flex items-center gap-1.5 px-3 py-2 text-[11px] text-3 hover:surface-2 hover:text-2 border-l border-subtle transition-colors"
                title="Delete all empty chats"
                onClick={() => {
                  clearEmpty()
                  setMenuOpen(false)
                }}
              >
                <Eraser size={13} />
                Clear empty
              </button>
            </div>
          </div>
        )}
      </div>

      {!serversReady ? (
        <div className="flex-1 flex flex-col items-center justify-center gap-2 text-3 text-xs">
          <Loader2 size={18} className="animate-spin" style={{ color: "var(--accent)" }} />
          Connecting to opencode…
        </div>
      ) : (
        <>
          <Transcript
            messages={active?.messages ?? []}
            permissionsByCallID={permissionsByCallID}
            onResolvePermission={resolvePermission}
            running={active?.running ?? false}
            error={active?.error ?? null}
          />
          <Composer
            running={active?.running ?? false}
            disabled={!serversReady || !activeId}
            onSend={send}
            onStop={abort}
          />
        </>
      )}
    </aside>
  )
}
