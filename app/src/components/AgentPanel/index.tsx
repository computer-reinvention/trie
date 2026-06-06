import { useMemo } from "react"
import { useAgentStore, useActiveSession } from "@/store/agentStore"
import { useAppStore } from "@/store/appStore"
import { opencodeClient } from "@/api/opencodeClient"
import { useSessions } from "@/hooks/useSessions"
import { openContextMenu } from "@/store/contextMenuStore"
import { Transcript } from "./Transcript"
import { Composer } from "./Composer"
import type { PermissionReply } from "@/api/types"

// The fixed right-hand agent panel — the whole agentic interface: a session
// switcher, the scrolling transcript, and the composer. This replaces the old
// bottom input bar and the standalone inspector.
export function AgentPanel() {
  const { newSession, switchSession, deleteSession, send, abort } = useSessions()
  const sessions = useAgentStore((s) => s.sessions)
  const order = useAgentStore((s) => s.order)
  const activeId = useAgentStore((s) => s.activeId)
  const active = useActiveSession()
  const serversReady = useAppStore((s) => s.serversReady)

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

  const activeTitle = active?.info.title || "chat"

  return (
    <aside className="w-96 shrink-0 bg-slate-900 border-l border-slate-800 flex flex-col overflow-hidden">
      {/* session switcher */}
      <div className="flex items-center gap-1 px-2 py-1.5 border-b border-slate-800 shrink-0">
        <select
          className="flex-1 min-w-0 bg-slate-800 border border-slate-700 rounded text-xs text-slate-200 px-2 py-1 outline-none"
          value={activeId ?? ""}
          onChange={(e) => switchSession(e.target.value)}
          title={activeTitle}
        >
          {order.map((id) => {
            const s = sessions[id]
            return (
              <option key={id} value={id}>
                {s?.info.title || id.slice(0, 8)}
              </option>
            )
          })}
        </select>
        <button
          className="shrink-0 rounded px-2 py-1 text-xs text-slate-300 hover:bg-slate-800 border border-slate-700"
          onClick={newSession}
          title="New chat"
        >
          +
        </button>
        <button
          className="shrink-0 rounded px-1.5 py-1 text-xs text-slate-500 hover:bg-slate-800"
          title="Session actions"
          onClick={(e) =>
            activeId &&
            openContextMenu(e, [
              {
                label: "New chat",
                onSelect: () => newSession(),
              },
              {
                label: "Delete chat",
                danger: true,
                disabled: order.length <= 1,
                onSelect: () => deleteSession(activeId),
              },
            ])
          }
        >
          ⋯
        </button>
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
