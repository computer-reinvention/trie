import { useMemo, useState, useEffect, useRef } from "react"
import { useAgentStore, useActiveSession } from "@/store/agentStore"
import { useAppStore } from "@/store/appStore"
import { opencodeClient } from "@/api/opencodeClient"
import { useSessions } from "@/hooks/useSessions"
import { displayTitle, relativeTime, updatedAt } from "@/lib/sessionTitle"
import { Transcript } from "./Transcript"
import { Composer } from "./Composer"
import type { PermissionReply } from "@/api/types"

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
  const menuRef = useRef<HTMLDivElement | null>(null)

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

  // sessions sorted most-recent-first for the dropdown
  const sortedSessions = useMemo(
    () => order.map((id) => sessions[id]).filter(Boolean),
    [order, sessions],
  )

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
    <aside className="w-96 shrink-0 bg-slate-900 border-l border-slate-800 flex flex-col overflow-hidden">
      {/* session switcher */}
      <div className="relative flex items-center gap-1 px-2 py-1.5 border-b border-slate-800 shrink-0">
        <button
          className="flex-1 min-w-0 flex items-center gap-1.5 bg-slate-800 border border-slate-700 rounded text-xs text-slate-200 px-2 py-1 hover:bg-slate-750 outline-none"
          onClick={() => setMenuOpen((v) => !v)}
          title={activeTitle}
        >
          {active?.running && (
            <span className="w-2.5 h-2.5 border-2 border-slate-600 border-t-accent rounded-full animate-spin shrink-0" />
          )}
          <span className="truncate flex-1 text-left">{activeTitle}</span>
          <span className="text-slate-500 shrink-0">▾</span>
        </button>
        <button
          className="shrink-0 rounded px-2 py-1 text-xs text-slate-300 hover:bg-slate-800 border border-slate-700"
          onClick={newSession}
          title="New chat"
        >
          +
        </button>

        {menuOpen && (
          <div
            ref={menuRef}
            className="absolute left-2 right-2 top-full mt-1 z-50 rounded-md border border-slate-700 bg-slate-900 shadow-xl overflow-hidden"
          >
            <div className="max-h-72 overflow-y-auto scroll-thin py-1">
              {sortedSessions.length === 0 && (
                <div className="px-3 py-2 text-xs text-slate-600">No chats yet.</div>
              )}
              {sortedSessions.map((s) => {
                const isActive = s.info.id === activeId
                return (
                  <div
                    key={s.info.id}
                    className={`group flex items-center gap-2 px-3 py-1.5 cursor-pointer ${
                      isActive ? "bg-slate-800" : "hover:bg-slate-800/60"
                    }`}
                    onClick={() => {
                      switchSession(s.info.id)
                      setMenuOpen(false)
                    }}
                  >
                    <div className="min-w-0 flex-1">
                      <div className="text-xs text-slate-200 truncate">{displayTitle(s.info)}</div>
                      <div className="text-[10px] text-slate-500">{relativeTime(updatedAt(s.info))}</div>
                    </div>
                    {sortedSessions.length > 1 && (
                      <button
                        className="shrink-0 text-slate-600 opacity-0 group-hover:opacity-100 hover:text-red-400 text-xs"
                        title="Delete chat"
                        onClick={(e) => {
                          e.stopPropagation()
                          deleteSession(s.info.id)
                        }}
                      >
                        ×
                      </button>
                    )}
                  </div>
                )
              })}
            </div>
            <div className="border-t border-slate-800 flex">
              <button
                className="flex-1 px-3 py-1.5 text-[11px] text-slate-400 hover:bg-slate-800 hover:text-slate-200 text-left"
                onClick={() => {
                  newSession()
                  setMenuOpen(false)
                }}
              >
                + New chat
              </button>
              <button
                className="px-3 py-1.5 text-[11px] text-slate-500 hover:bg-slate-800 hover:text-slate-300 border-l border-slate-800"
                title="Delete all empty chats"
                onClick={() => {
                  clearEmpty()
                  setMenuOpen(false)
                }}
              >
                Clear empty
              </button>
            </div>
          </div>
        )}
      </div>

      {!serversReady ? (
        <div className="flex-1 flex items-center justify-center text-slate-600 text-xs">
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
