/** Base class others extend. */
export class Base {
  id: number = 0
  describe(): string {
    return "base"
  }
}

/** Contract for runnable things. */
export interface Runnable {
  run(): void
}

export type Identifier = string | number

export enum Status {
  Active = 1,
  Inactive,
  Pending,
}
