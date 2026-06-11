import { describe, it, expect, beforeEach } from "vitest"
import { useAgentStore } from "./agentStore"
import type { OpencodePart } from "@/api/types"

const reset = () => useAgentStore.setState({ sessions: {}, order: [], activeId: null })

const toolPart = (id: string): OpencodePart =>
  ({
    id,
    type: "tool",
    tool: "read",
    callID: id,
    state: { status: "completed", input: { sym: "foo:bar" } },
  }) as OpencodePart

describe("agentStore: sub-agent (child) sessions", () => {
  beforeEach(reset)

  it("keeps child sessions OUT of the switcher order", () => {
    const s = useAgentStore.getState()
    s.upsertSession({ id: "parent" })
    s.upsertSession({ id: "child", parentID: "parent" })
    const { order, sessions } = useAgentStore.getState()
    expect(order).toEqual(["parent"]) // child excluded
    expect(sessions.child).toBeTruthy() // but present in the store
  })

  it("never makes a child session the active chat", () => {
    const s = useAgentStore.getState()
    s.upsertSession({ id: "child", parentID: "parent" })
    expect(useAgentStore.getState().activeId).toBeNull()
    s.upsertSession({ id: "parent" })
    expect(useAgentStore.getState().activeId).toBe("parent")
  })

  it("setSessions filters child sessions from order", () => {
    useAgentStore.getState().setSessions([
      { id: "a" },
      { id: "b", parentID: "a" },
      { id: "c" },
    ])
    expect(useAgentStore.getState().order.sort()).toEqual(["a", "c"])
  })

  it("auto-registers an unknown session on a part so sub-agent parts aren't dropped", () => {
    useAgentStore.getState().applyPartUpdated("subagent-xyz", "msg1", toolPart("p1"))
    const { sessions, order } = useAgentStore.getState()
    expect(sessions["subagent-xyz"]).toBeTruthy()
    expect(sessions["subagent-xyz"].messages[0].parts[0].id).toBe("p1")
    expect(order).not.toContain("subagent-xyz") // still not in the switcher
  })

  it("auto-registers an unknown session on setRunning", () => {
    useAgentStore.getState().setRunning("subagent-xyz", true)
    expect(useAgentStore.getState().sessions["subagent-xyz"].running).toBe(true)
  })
})
