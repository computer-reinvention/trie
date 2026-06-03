---
trie_version: 0.1.5
source: trie_mcp_entry.py
file_fingerprint: 120f8ead96563b26bb426f757e94008d3e22bf6c2413bea7c3e51d27e28a1683
last_synced_at: '2026-06-03T21:17:44Z'
description: PyInstaller entrypoint for the trie MCP stdio server.
defines:
- kind: module
  qualified_name: trie_mcp_entry:__module__
  lines: 1-27
- kind: function
  qualified_name: trie_mcp_entry:main
  lines: 11-22
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=trie_mcp_entry:__module__ fingerprint=12cab91e472dd6fa6de332328a043bfead110fb1327f46925f11c1d800956953 body_fp=cd3a88104c8d81eb80bd0e5b7f59fcd7157948a777aaf6ee4c24e371defeac84 source_ref=eec9478401702ff2153325f116b253c655f1fe15 -->
PyInstaller entrypoint module for the trie MCP stdio server that validates command-line arguments and starts the server.

- Takes project directory path as single command-line argument
- Validates directory exists before starting server
- Exits with error code 1 if arguments invalid or directory missing
<!-- trie:end -->
<!-- trie:section symbol=trie_mcp_entry:main fingerprint=aeab39e048e317b9425e3e40868e1e7fd8dc566f75a74f37008d074c7c9fb0a7 body_fp=4cfb6cc1e089cecbfeb548e24856029a771e88ef285a5849db76bd2d6a461103 source_ref=eec9478401702ff2153325f116b253c655f1fe15 -->
Entry point for the trie MCP stdio server that validates command-line arguments and starts the server.

- Takes project directory path as first command-line argument
- Exits with error message if no argument provided or directory doesn't exist
- Calls `run_stdio` with resolved project path to start the MCP server
<!-- trie:end -->