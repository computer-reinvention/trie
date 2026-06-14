declare module "lang-map" {
  /** The shape returned by map(). */
  export interface MapReturn {
    extensions: Record<string, string[]>
  }
  function map(): MapReturn
}

declare const BUILD_ID: string
