// HTTP client for opencode session operations.
// Routes through IPC proxy — renderer cannot reach 127.0.0.1 directly.

let baseUrl = ""

export function setOpenCodeClientBase(opencodePort: number): void {
  baseUrl = `http://127.0.0.1:${opencodePort}`
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const trie = () => (window as any).trie

export const opencodeClient = {
  async sendMessage(sessionId: string, content: string): Promise<void> {
    await trie().httpRequest({
      method: "POST",
      url: `${baseUrl}/session/${sessionId}/message`,
      body: JSON.stringify({ content }),
    })
  },

  async getMessages(sessionId: string, limit = 20): Promise<unknown[]> {
    const result = await trie().httpRequest({
      method: "GET",
      url: `${baseUrl}/session/${sessionId}/message?limit=${limit}`,
    }) as { status: number; body: string }
    if (result.status >= 400) return []
    const data = JSON.parse(result.body) as unknown
    if (data && typeof data === "object" && "items" in data) {
      return (data as { items: unknown[] }).items
    }
    return Array.isArray(data) ? data : []
  },
}
