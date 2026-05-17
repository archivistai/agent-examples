# Claude Desktop + Archivist AI MCP

Connect your TTRPG campaign data to Claude Desktop using the Archivist AI MCP server.

## Setup

1. Open Claude Desktop settings
2. Navigate to the MCP servers configuration
3. Add the Archivist AI server using the config below
4. Restart Claude Desktop

### Configuration

Copy the contents of [`claude_desktop_config.json`](claude_desktop_config.json) into your Claude Desktop MCP configuration:

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

On macOS, the config file is at: `~/Library/Application Support/Claude/claude_desktop_config.json`

On Windows: `%APPDATA%\Claude\claude_desktop_config.json`

## Authentication

When you first use an Archivist tool, Claude will prompt you to authenticate via OAuth. You'll be redirected to sign in with your Archivist account.

Alternatively, if you have an API key, you can pass it as a Bearer token in the server configuration.

## What You Can Do

Once connected, try prompts like:

- "List my campaigns and tell me about them"
- "Who are the major NPCs in my campaign?"
- "Summarize what happened in the last three sessions"
- "What quests are currently in progress?"
- "Tell me about the faction called the Thieves' Guild"
- "What items has the party collected?"
- "Find moments where a character named Kael was mentioned"

## Available Tools

Claude will have access to 25 read-only tools for accessing your campaign data including campaigns, characters, sessions, beats, moments, factions, locations, items, quests, journals, and entity links. See the [MCP Tool Reference](../../docs/mcp-tool-reference.md) for the complete list.
