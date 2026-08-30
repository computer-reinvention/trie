// Fixture: TS file with BOTH Express routes AND fetch/axios calls (monorepo pattern)
// This tests that both client call sites and Express endpoints are detected in the same file.
import express from "express";

const app = express();

// This file acts as a gateway: it defines Express routes AND calls upstream APIs via fetch.

export function setupGateway() {
  // Express route definition (server endpoint)
  app.get("/api/gateway/status", (req, res) => {
    res.json({ gateway: "running" });
  });

  // Express route that proxies to an upstream service
  app.get("/api/gateway/users", async (req, res) => {
    // Client call site (fetch to upstream)
    const upstream = await fetch("/api/users");
    const data = await upstream.json();
    res.json(data);
  });
}

export async function checkHealth() {
  // Client call site
  const response = await fetch("/api/health");
  return response.json();
}
