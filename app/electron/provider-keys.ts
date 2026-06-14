// Keychain-backed provider API keys. Keys are stored under the app's keychain
// service with account `provider-key:<provider>` and a parallel env-var-name
// record under `provider-env:<provider>`. At spawn time we read every stored
// key and expose it as the configured environment variable so opencode.json
// can reference {env:VAR} without secrets ever touching the project file.

const KEYCHAIN_SERVICE = "ai.trie.app"
const KEY_PREFIX = "provider-key:"
const ENV_PREFIX = "provider-env:"

// Fixed provider → env var defaults (mirrors src/settings/opencodeSchema.ts).
const PROVIDER_ENV_DEFAULTS: Record<string, string> = {
  anthropic: "ANTHROPIC_API_KEY",
  openai: "OPENAI_API_KEY",
  google: "GOOGLE_GENERATIVE_AI_API_KEY",
  gemini: "GOOGLE_GENERATIVE_AI_API_KEY",
  groq: "GROQ_API_KEY",
  openrouter: "OPENROUTER_API_KEY",
  mistral: "MISTRAL_API_KEY",
  deepseek: "DEEPSEEK_API_KEY",
  xai: "XAI_API_KEY",
}

function defaultEnvVar(provider: string): string {
  return (
    PROVIDER_ENV_DEFAULTS[provider] ??
    `${provider.toUpperCase().replace(/[^A-Z0-9]/g, "_")}_API_KEY`
  )
}

let keytarModule: typeof import("keytar") | null = null
async function getKeytar() {
  if (!keytarModule) keytarModule = await import("keytar")
  return keytarModule
}

export interface ProviderKeyInfo {
  provider: string
  hasKey: boolean
  envVar: string
}

/** List every provider that has a stored key, with its resolved env var. */
export async function listProviderKeys(): Promise<ProviderKeyInfo[]> {
  try {
    const keytar = await getKeytar()
    const creds = await keytar.findCredentials(KEYCHAIN_SERVICE)
    const out: ProviderKeyInfo[] = []
    for (const c of creds) {
      if (!c.account.startsWith(KEY_PREFIX)) continue
      const provider = c.account.slice(KEY_PREFIX.length)
      out.push({
        provider,
        hasKey: Boolean(c.password),
        envVar: await getEnvVar(provider),
      })
    }
    return out
  } catch {
    return []
  }
}

export async function hasProviderKey(provider: string): Promise<boolean> {
  try {
    const keytar = await getKeytar()
    const v = await keytar.getPassword(KEYCHAIN_SERVICE, KEY_PREFIX + provider)
    return Boolean(v)
  } catch {
    return false
  }
}

async function getEnvVar(provider: string): Promise<string> {
  try {
    const keytar = await getKeytar()
    const custom = await keytar.getPassword(KEYCHAIN_SERVICE, ENV_PREFIX + provider)
    return custom || defaultEnvVar(provider)
  } catch {
    return defaultEnvVar(provider)
  }
}

/** Store (or clear) a provider key and its env-var name. Passing an empty key
 *  deletes the stored secret. */
export async function setProviderKey(
  provider: string,
  key: string,
  envVar?: string,
): Promise<{ ok: boolean; error?: string }> {
  try {
    const keytar = await getKeytar()
    if (key) {
      await keytar.setPassword(KEYCHAIN_SERVICE, KEY_PREFIX + provider, key)
    } else {
      await keytar.deletePassword(KEYCHAIN_SERVICE, KEY_PREFIX + provider)
    }
    if (envVar && envVar !== defaultEnvVar(provider)) {
      await keytar.setPassword(KEYCHAIN_SERVICE, ENV_PREFIX + provider, envVar)
    } else {
      await keytar.deletePassword(KEYCHAIN_SERVICE, ENV_PREFIX + provider)
    }
    return { ok: true }
  } catch (err) {
    return { ok: false, error: String(err) }
  }
}

export async function deleteProviderKey(provider: string): Promise<{ ok: boolean }> {
  try {
    const keytar = await getKeytar()
    await keytar.deletePassword(KEYCHAIN_SERVICE, KEY_PREFIX + provider)
    await keytar.deletePassword(KEYCHAIN_SERVICE, ENV_PREFIX + provider)
    return { ok: true }
  } catch {
    return { ok: false }
  }
}

/** Build the env-var map to inject into the opencode child process. */
export async function providerEnvForSpawn(): Promise<Record<string, string>> {
  const env: Record<string, string> = {}
  try {
    const keytar = await getKeytar()
    const creds = await keytar.findCredentials(KEYCHAIN_SERVICE)
    for (const c of creds) {
      if (!c.account.startsWith(KEY_PREFIX) || !c.password) continue
      const provider = c.account.slice(KEY_PREFIX.length)
      env[await getEnvVar(provider)] = c.password
    }
  } catch {
    /* keychain unavailable — spawn with no injected keys */
  }
  return env
}
