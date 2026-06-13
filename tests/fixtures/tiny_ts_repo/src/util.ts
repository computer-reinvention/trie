/** Double a number. */
export function double(n: number): number {
  return n * 2
}

/** A private helper, not exported. */
function secretHelper(n: number): number {
  return n - 1
}

export const PI = 3.14

export const compute = (x: number): number => double(x) + secretHelper(x)
