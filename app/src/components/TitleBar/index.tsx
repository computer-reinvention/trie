import type { ReactNode } from "react"

// Shared title-bar height. The macOS traffic lights live in this top strip;
// every screen reserves it so content never overlaps the window controls.
export const TITLEBAR_H = 38
// Left clearance so content never sits under the traffic lights.
export const TRAFFIC_LIGHT_CLEARANCE = 80

interface TitleBarProps {
  /** Primary title text shown after the traffic-light clearance. */
  title?: string
  /** Dimmed secondary text next to the title (e.g. stats). */
  subtitle?: string
  /** Right-aligned interactive controls (rendered inside app-no-drag). */
  actions?: ReactNode
  /** Override the whole content area (replaces title/subtitle). */
  children?: ReactNode
}

// The single, reusable macOS title bar. Paired with titleBarStyle:"hiddenInset".
// Used by EVERY screen so the strip height, traffic-light clearance, drag region,
// and vertical alignment are defined exactly once.
export function TitleBar({ title, subtitle, actions, children }: TitleBarProps) {
  return (
    <div
      className="app-drag shrink-0 flex items-center surface-1 border-b border-subtle select-none"
      style={{ height: TITLEBAR_H }}
    >
      {/* traffic-light clearance */}
      <div className="shrink-0" style={{ width: TRAFFIC_LIGHT_CLEARANCE }} />

      {children ?? (
        <div className="flex items-center gap-2 min-w-0 leading-none">
          {title && (
            <span className="text-1 text-xs font-semibold truncate leading-none">
              {title}
            </span>
          )}
          {subtitle && (
            <span className="text-3 text-[11px] tabular-nums leading-none truncate">
              {subtitle}
            </span>
          )}
        </div>
      )}

      <div className="flex-1" />

      {actions && <div className="app-no-drag flex items-center gap-1 pr-3">{actions}</div>}
    </div>
  )
}

export function TitleBarIconButton({
  onClick,
  title,
  label,
  children,
}: {
  onClick: () => void
  title?: string
  label?: string
  children: ReactNode
}) {
  return (
    <button
      className="w-7 h-7 rounded flex items-center justify-center text-2 hover:text-1 hover:surface-3 transition-colors"
      onClick={onClick}
      title={title}
      aria-label={label ?? title}
    >
      {children}
    </button>
  )
}

export function GearIcon() {
  return (
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <circle cx="12" cy="12" r="3" />
      <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" />
    </svg>
  )
}
