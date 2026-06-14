import { useEffect, useLayoutEffect, useRef, useState } from "react"
import { createPortal } from "react-dom"
import { useContextMenuStore } from "@/store/contextMenuStore"

// The single app-wide context menu portal. Mount once near the app root.
// Reads position + items from the store; dismisses on outside click, Escape,
// scroll, or after an item is selected. Clamps to the viewport so it never
// overflows off-screen.

export function ContextMenu() {
  const { open, x, y, items, hide } = useContextMenuStore()
  const ref = useRef<HTMLDivElement | null>(null)
  const [pos, setPos] = useState({ x, y })

  useLayoutEffect(() => {
    if (!open || !ref.current) return
    const rect = ref.current.getBoundingClientRect()
    const nx = Math.min(x, window.innerWidth - rect.width - 8)
    const ny = Math.min(y, window.innerHeight - rect.height - 8)
    setPos({ x: Math.max(4, nx), y: Math.max(4, ny) })
  }, [open, x, y, items])

  useEffect(() => {
    if (!open) return
    const onDown = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) hide()
    }
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") hide()
    }
    window.addEventListener("mousedown", onDown)
    window.addEventListener("keydown", onKey)
    window.addEventListener("scroll", hide, true)
    window.addEventListener("resize", hide)
    return () => {
      window.removeEventListener("mousedown", onDown)
      window.removeEventListener("keydown", onKey)
      window.removeEventListener("scroll", hide, true)
      window.removeEventListener("resize", hide)
    }
  }, [open, hide])

  if (!open) return null

  return createPortal(
    <div
      ref={ref}
      className="fixed z-[1000] min-w-[160px] rounded-md border border-strong surface-pop elev-2 py-1 text-xs font-mono"
      style={{ left: pos.x, top: pos.y }}
    >
      {items.map((item, i) =>
        item.label === "-" ? (
          <div key={i} className="my-1 border-t border-subtle" />
        ) : (
          <button
            key={i}
            disabled={item.disabled}
            className={`block w-full text-left px-3 py-1.5 transition-colors ${
              item.disabled
                ? "text-faint cursor-default"
                : item.danger
                  ? "hover:bg-[color-mix(in_srgb,var(--danger)_12%,transparent)]"
                  : "text-2 hover:surface-3 hover:text-1"
            }`}
            style={item.danger && !item.disabled ? { color: "var(--danger)" } : undefined}
            onClick={() => {
              if (item.disabled) return
              hide()
              item.onSelect()
            }}
          >
            {item.label}
          </button>
        ),
      )}
    </div>,
    document.body,
  )
}
