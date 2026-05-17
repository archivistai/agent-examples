# Windsurf + Archivist AI MCP

Connect your TTRPG campaign data to Windsurf using the Archivist AI MCP server.

## Setup

1. Open Windsurf settings
2. Navigate to the MCP configuration
3. Add the Archivist AI server using the config below

### Configuration

Add to your Windsurf MCP configuration:

```json
{
  "mcpServers": {
    "archivist-ai": {
      "serverUrl": "https://mcp.myarchivist.ai/mcp"
    }
  }
}
```

See [`mcp_config.json`](mcp_config.json) for the ready-to-use config file.

## Authentication

When Windsurf first connects to the Archivist MCP server, you'll be prompted to authenticate via OAuth. Sign in with your Archivist account to grant access.

## What You Can Do

With Archivist connected to Windsurf, you can:

- Reference campaign lore and world data while coding
- Build TTRPG tools with live campaign context
- Query session history, character details, and quest progress

## Example Prompts

- "List my Archivist campaigns and their stats"
- "Who are the NPCs in my campaign?"
- "What happened in session 5?"
- "Show me the quest log"

## Available Tools

Windsurf will have access to 25 read-only MCP tools. See the [MCP Tool Reference](../../docs/mcp-tool-reference.md) for details.
