import { GraphCanvas } from "@/components/GraphCanvas"
import { AGMCanvas } from "@/components/AGMCanvas"
import { TabStrip } from "./TabStrip"
import { FileTabContent } from "./FileTabContent"
import { PatchesPanel } from "./PatchesPanel"
import { useTabsStore, GRAPH_TAB_ID, PATCHES_TAB_ID } from "@/store/tabsStore"
import { useSetting } from "@/store/settingsStore"

// The central editor area: a tab strip over a stacked content region. The
// graph canvas is mounted once and kept alive (so its force layout / zoom
// survive tab switches); it is merely hidden when a file tab is active.
// File tabs are mounted lazily and likewise kept alive once opened, so
// switching back to a tab is instant and preserves scroll position.

export function Editor() {
  const tabs = useTabsStore((s) => s.tabs)
  const activeId = useTabsStore((s) => s.activeId)
  const graphActive = activeId === GRAPH_TAB_ID
  const patchesActive = activeId === PATCHES_TAB_ID
  const vizEngine = useSetting<string>("viz.engine")

  return (
    <div className="flex-1 flex flex-col min-w-0 min-h-0">
      <TabStrip />
      <div className="relative flex-1 min-h-0">
        {/* Graph: always mounted, hidden (not unmounted) when a file tab is up. */}
        <div
          className="absolute inset-0"
          style={{ visibility: graphActive ? "visible" : "hidden", zIndex: graphActive ? 1 : 0 }}
        >
          {vizEngine === "agm" ? (
            <AGMCanvas className="h-full min-h-0" />
          ) : (
            <GraphCanvas className="h-full min-h-0" />
          )}
        </div>

        {/* Patches: permanent review surface, shown when its tab is active. */}
        <div
          className="absolute inset-0"
          style={{ visibility: patchesActive ? "visible" : "hidden", zIndex: patchesActive ? 2 : 0 }}
        >
          <PatchesPanel />
        </div>

        {/* File tabs: each kept mounted once opened, shown only when active. */}
        {tabs.map((tab) =>
          tab.kind === "file" ? (
            <div
              key={tab.id}
              className="absolute inset-0 bg-slate-950"
              style={{
                visibility: activeId === tab.id ? "visible" : "hidden",
                zIndex: activeId === tab.id ? 2 : 0,
              }}
            >
              <FileTabContent tab={tab} />
            </div>
          ) : null,
        )}
      </div>
    </div>
  )
}
