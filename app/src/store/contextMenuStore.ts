import { create } from "zustand"

// A single app-wide context menu. Any surface (file tree, tabs, graph nodes,
// triefact cards) opens it imperatively with a screen position and a list of
// items; the <ContextMenu/> portal renders it. Keeping one instance avoids
// each surface reinventing positioning, outside-click dismissal, and z-index.

export interface ContextMenuItem {
  label: string
  onSelect: () => void
  // Optional visual grouping / state.
  danger?: boolean
  disabled?: boolean
  // A separator is rendered when label is "-".
}

interface ContextMenuState {
  open: boolean
  x: number
  y: number
  items: ContextMenuItem[]
  show: (x: number, y: number, items: ContextMenuItem[]) => void
  hide: () => void
}

export const useContextMenuStore = create<ContextMenuState>((set) => ({
  open: false,
  x: 0,
  y: 0,
  items: [],
  show: (x, y, items) => set({ open: true, x, y, items }),
  hide: () => set({ open: false, items: [] }),
}))

// Convenience for event handlers: stop the native menu and open ours.
export function openContextMenu(
  e: { preventDefault: () => void; clientX: number; clientY: number },
  items: ContextMenuItem[],
): void {
  e.preventDefault()
  useContextMenuStore.getState().show(e.clientX, e.clientY, items)
}
