import { useState } from "react"
import { useAgentStore } from "@/store/agentStore"

export function TurnHistory() {
  const [expanded, setExpanded] = useState(false)
  const { currentTurn, history, responseText, running } = useAgentStore()

  const activeTurn = currentTurn
  const lastCompleted = history[0]

  const toolCallCount = activeTurn.filter((e) => e.type === "tool_call").length
  const lastDuration = lastCompleted
    ? ((lastCompleted.completedAt - lastCompleted.startedAt) / 1000).toFixed(1)
    : null

  return (
    <div className="border-t border-slate-800 bg-slate-900/80">
      {/* Summary bar */}
      <button
        className="w-full px-3 py-1.5 flex items-center gap-2 text-left hover:bg-slate-800/50 transition-colors"
        onClick={() => setExpanded((e) => !e)}
      >
        <span className="text-slate-600 text-xs">
          {expanded ? "▾" : "▸"}
        </span>
        {running ? (
          <span className="text-slate-400 text-xs">
            {toolCallCount} tool call{toolCallCount !== 1 ? "s" : ""}…
          </span>
        ) : lastCompleted ? (
          <span className="text-slate-500 text-xs">
            {lastCompleted.events.filter((e) => e.type === "tool_call").length} tool calls · {lastDuration}s
          </span>
        ) : (
          <span className="text-slate-700 text-xs">No turns yet</span>
        )}
      </button>

      {/* Response text */}
      {responseText && (
        <div className="px-3 pb-2">
          <p className="text-slate-300 text-sm leading-relaxed whitespace-pre-wrap">{responseText}</p>
        </div>
      )}

      {/* Expanded tool call log */}
      {expanded && (
        <div className="max-h-40 overflow-y-auto px-3 pb-2 border-t border-slate-800">
          {[...activeTurn, ...(lastCompleted?.events ?? [])].map((event, i) => (
            <div key={i} className="flex items-center gap-2 py-0.5">
              <span
                className={`text-[10px] font-mono ${
                  event.type === "tool_call" ? "text-indigo-400" : "text-slate-500"
                }`}
              >
                {event.tool}
              </span>
              {event.input && Object.keys(event.input).length > 0 && (
                <span className="text-slate-600 text-[10px] font-mono truncate flex-1">
                  {JSON.stringify(event.input).slice(0, 60)}
                </span>
              )}
              {event.type === "tool_result" && (
                <span className={`text-[10px] ml-auto ${event.error ? "text-red-400" : "text-green-500"}`}>
                  {event.error ? "✗" : "✓"}
                  {event.durationMs != null && ` ${(event.durationMs / 1000).toFixed(1)}s`}
                </span>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
