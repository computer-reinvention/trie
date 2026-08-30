// Fixture: TS file with Express route definitions
import express from "express";

const app = express();
const router = express.Router();

export function setupRoutes() {
  app.get("/api/health", (req, res) => {
    res.json({ status: "ok" });
  });

  router.get("/api/products", (req, res) => {
    res.json([{ id: 1, name: "Widget" }]);
  });

  router.post("/api/products", (req, res) => {
    res.json({ created: true });
  });
}
