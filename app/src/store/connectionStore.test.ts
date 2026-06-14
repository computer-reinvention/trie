import { beforeEach, describe, expect, it } from "vitest"
import { useConnectionStore } from "./connectionStore"

function reset() {
  useConnectionStore.setState({ status: "connecting", exitCode: null, lastError: null })
}

describe("connectionStore", () => {
  beforeEach(reset)

  it("starts connecting", () => {
    expect(useConnectionStore.getState().status).toBe("connecting")
  })

  it("setLive clears the exit code", () => {
    useConnectionStore.getState().setCrashed(1, "boom")
    useConnectionStore.getState().setLive()
    const s = useConnectionStore.getState()
    expect(s.status).toBe("live")
    expect(s.exitCode).toBeNull()
  })

  it("setCrashed records code + error", () => {
    useConnectionStore.getState().setCrashed(137, "killed")
    const s = useConnectionStore.getState()
    expect(s.status).toBe("crashed")
    expect(s.exitCode).toBe(137)
    expect(s.lastError).toBe("killed")
  })

  it("a crash is not downgraded to degraded by a trailing SSE error", () => {
    useConnectionStore.getState().setCrashed(1, "boom")
    useConnectionStore.getState().setDegraded("stream dropped")
    const s = useConnectionStore.getState()
    // status stays crashed; the error line still updates for diagnostics.
    expect(s.status).toBe("crashed")
    expect(s.lastError).toBe("stream dropped")
  })

  it("degraded → live recovers when the stream resumes", () => {
    useConnectionStore.getState().setLive()
    useConnectionStore.getState().setDegraded("stream dropped")
    expect(useConnectionStore.getState().status).toBe("degraded")
    useConnectionStore.getState().setLive()
    expect(useConnectionStore.getState().status).toBe("live")
  })
})
