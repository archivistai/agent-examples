# Cursor + Archivist AI MCP

Connect your TTRPG campaign data to Cursor IDE using the Archivist AI MCP server.

## Setup

1. Open your project in Cursor
2. Create a `.cursor/mcp.json` file in your project root (or edit the global one)
3. Add the Archivist AI server config below
4. The MCP server will appear in Cursor's MCP panel

### Project-Level Configuration

Create `.cursor/mcp.json` in your project:

```json
{
  "mcpServers": {
    "archivist-ai": {
      "type": "streamable-http",
      "url": "https://mcp.myarchivist.ai/mcp"
    }
  }
}
```

See [`mcp.json`](mcp.json) for the ready-to-use config file.

## Authentication

When Cursor first connects to the Archivist MCP server, you'll be prompted to authenticate via OAuth. Sign in with your Archivist account to grant access.

## What You Can Do

With Archivist connected to Cursor, you can:

- Query campaign data while coding TTRPG tools or integrations
- Reference character details, session history, and quest logs in your development context
- Build applications that use campaign data by having the AI pull live examples
- Test and iterate on Archivist API integrations with real campaign data in context

## Example Prompts

- "List my Archivist campaigns"
- "Get the cast analysis for my latest session"
- "Show me all characters in this campaign"
- "What are the active quests?"

## Available Tools

Cursor will have access to 25 read-only MCP tools. See the [MCP Tool Reference](../../docs/mcp-tool-reference.md) for details.
