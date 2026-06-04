import { useAppStore } from "@/store/appStore"

// Shared title-bar height. The macOS traffic lights live in this top strip;
// every screen reserves it so content never overlaps the window controls.
export const TITLEBAR_H = 38
// Left clearance so content never sits under the traffic lights.
export const TRAFFIC_LIGHT_CLEARANCE = 80

interface TitleBarProps {
  onOpenSettings: () => void
}

// Custom macOS title bar paired with titleBarStyle:"hiddenInset". The left
// padding clears the traffic-light buttons; the whole bar is a drag region
// except the interactive controls (app-no-drag).
export function TitleBar({ onOpenSettings }: TitleBarProps) {
  const { projectName, totalSymbols, totalFiles } = useAppStore()

  return (
    <div
      className="app-drag shrink-0 flex items-center bg-slate-900 border-b border-slate-800 select-none"
      style={{ height: TITLEBAR_H }}
    >
      {/* traffic-light clearance */}
      <div style={{ width: TRAFFIC_LIGHT_CLEARANCE }} />

      <div className="flex items-center gap-2 min-w-0 leading-none">
        <span className="text-slate-200 text-xs font-medium truncate leading-none">
          {projectName || "trie"}
        </span>
        {totalSymbols > 0 && (
          <span className="text-slate-600 text-[11px] tabular-nums leading-none">
            {totalSymbols} symbols · {totalFiles} files
          </span>
        )}
      </div>

      <div className="flex-1" />

      <div className="app-no-drag flex items-center gap-1 pr-3">
        <button
          className="w-7 h-7 rounded flex items-center justify-center text-slate-400 hover:text-slate-100 hover:bg-slate-800 transition-colors"
          onClick={onOpenSettings}
          title="Settings (⌘,)"
          aria-label="Settings"
        >
          <GearIcon />
        </button>
      </div>
    </div>
  )
}

function GearIcon() {
  return (
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <circle cx="12" cy="12" r="3" />
      <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" />
    </svg>
  )
}
