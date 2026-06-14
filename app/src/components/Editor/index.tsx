import { GraphCanvas } from "@/components/GraphCanvas"
import { AGMCanvas } from "@/components/AGMCanvas"
import { TabStrip } from "./TabStrip"
import { FileTabContent } from "./FileTabContent"
import { PatchesPanel } from "./PatchesPanel"
import { TriePanel } from "./TriePanel"
import {
  useTabsStore,
  GRAPH_TAB_ID,
  TOPOLOGY_TAB_ID,
  PATCHES_TAB_ID,
  TRIE_TAB_ID,
} from "@/store/tabsStore"

// The central editor area: a tab strip over a stacked content region. Two
// permanent graph views are mounted once and kept alive (so layout/zoom survive
// tab switches): ATTENTION (AGM live cognitive monitor) and TOPOLOGY (legacy
// structural map). Both stay mounted so the topology view keeps reacting to live
// agent activity even while hidden. File tabs are mounted lazily.

export function Editor() {
  const tabs = useTabsStore((s) => s.tabs)
  const activeId = useTabsStore((s) => s.activeId)
  const attentionActive = activeId === GRAPH_TAB_ID
  const topologyActive = activeId === TOPOLOGY_TAB_ID
  const patchesActive = activeId === PATCHES_TAB_ID
  const trieActive = activeId === TRIE_TAB_ID

  return (
    <div className="flex-1 flex flex-col min-w-0 min-h-0">
      <TabStrip />
      <div className="relative flex-1 min-h-0">
        {/* Attention (AGM): always mounted; the live cognitive monitor. */}
        <div
          className="absolute inset-0"
          style={{
            visibility: attentionActive ? "visible" : "hidden",
            zIndex: attentionActive ? 1 : 0,
          }}
        >
          <AGMCanvas className="h-full min-h-0" />
        </div>

        {/* Topology (legacy): always mounted so it keeps reacting to live
            activity even when hidden; the structural / dependency map. */}
        <div
          className="absolute inset-0"
          style={{
            visibility: topologyActive ? "visible" : "hidden",
            zIndex: topologyActive ? 1 : 0,
          }}
        >
          <GraphCanvas className="h-full min-h-0" />
        </div>

        {/* Patches: permanent review surface, shown when its tab is active. */}
        <div
          className="absolute inset-0"
          style={{ visibility: patchesActive ? "visible" : "hidden", zIndex: patchesActive ? 2 : 0 }}
        >
          <PatchesPanel />
        </div>

        {/* trie: lifecycle command runner + live output. Always mounted so a
            long-running sync keeps streaming while you look at other tabs. */}
        <div
          className="absolute inset-0"
          style={{ visibility: trieActive ? "visible" : "hidden", zIndex: trieActive ? 2 : 0 }}
        >
          <TriePanel />
        </div>

        {/* File tabs: each kept mounted once opened, shown only when active. */}
        {tabs.map((tab) =>
          tab.kind === "file" ? (
            <div
              key={tab.id}
              className="absolute inset-0"
              // file body sits on the app background so it reads as the deepest surface
              style={{
                background: "var(--bg-app)",
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
