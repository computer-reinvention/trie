import { double, compute } from "@/util"
import { Base, Runnable, Status } from "@/base"
import { makeStore } from "@/store"
import * as core from "@oc/core"
import { map } from "lang-map"
import { unknownThing } from "nonexistent-package"

/** Application entry that ties the pieces together. */
export class App extends Base implements Runnable {
  status: Status = Status.Active

  run(): void {
    double(this.id)
    compute(2)
    makeStore()
    core.greet()
    map()
    unknownThing()
  }
}
