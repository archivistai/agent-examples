# Archivist AI Agent Examples

Build AI agents powered by your TTRPG campaign data. This repository contains working examples, configuration files, and reference documentation for integrating [Archivist AI](https://www.myarchivist.ai) with AI assistants and agent frameworks.

Archivist AI is a **TTRPG campaign memory platform** for game masters and players. It turns Discord sessions, uploaded audio, transcripts, and play-by-post content into structured campaign history -- characters, locations, factions, items, quests, session timelines, and more -- that can be searched, queried, and used by AI agents.

## Quick Start

### Connect via MCP (Model Context Protocol)

The Archivist MCP server gives AI assistants direct, read-only access to your campaign data. No SDK or API key wrangling required -- just point your client at the server.

**MCP Server URL:** `https://mcp.myarchivist.ai/mcp`
**Transport:** Streamable HTTP
**Authentication:** OAuth 2.0 (authorization code + PKCE) or Bearer token

### Claude Desktop

Add to your `claude_desktop_config.json`:

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

### Cursor

Add to your `.cursor/mcp.json`:

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

### Windsurf

Add to your MCP configuration:

```json
{
  "mcpServers": {
    "archivist-ai": {
      "serverUrl": "https://mcp.myarchivist.ai/mcp"
    }
  }
}
```

## Examples

| Example | Description | Language |
|---------|-------------|----------|
| [Claude Desktop Setup](examples/claude-desktop/) | Connect Archivist to Claude Desktop via MCP | Config |
| [Cursor Setup](examples/cursor/) | Connect Archivist to Cursor IDE via MCP | Config |
| [Windsurf Setup](examples/windsurf/) | Connect Archivist to Windsurf IDE via MCP | Config |
| [Session Recap Agent](examples/openai-agents/session_recap_agent.py) | Generate session recaps automatically | Python |
| [NPC Recall Agent](examples/openai-agents/npc_recall_agent.py) | Ask questions about campaign lore and NPCs | Python |
| [GM Copilot](examples/openai-agents/gm_copilot.py) | GM assistant with function calling + Archivist retrieval | Python |
| [Session Recap (TypeScript)](examples/typescript-agents/session-recap.ts) | Generate session recaps with AI SDK | TypeScript |
| [Campaign Explorer](examples/typescript-agents/campaign-explorer.ts) | Interactive campaign Q&A agent | TypeScript |

## MCP Tools Reference

The Archivist MCP server exposes 25 read-only tools for accessing campaign data:

### Campaigns

| Tool | Description |
|------|-------------|
| `list_campaigns` | List your campaigns. Returns a paginated list. |
| `get_campaign` | Get a specific campaign by ID. |
| `get_campaign_stats` | Get statistics for a campaign: character count, session count, and more. |

### Characters

| Tool | Description |
|------|-------------|
| `list_characters` | List characters in a campaign. Filter by name, type (PC/NPC), or approval status. |
| `get_character` | Get a character by ID including aliases, backstory, and speaker linkage. |

### Sessions

| Tool | Description |
|------|-------------|
| `list_sessions` | List game sessions in a campaign. Filter by session type or public-only. |
| `get_session` | Get a session by ID. Optionally include related beats and moments. |
| `get_session_cast_analysis` | Get cast analysis for a session: talk-share breakdown and core metrics. |

### Story Structure

| Tool | Description |
|------|-------------|
| `list_beats` | List beats in a campaign, ordered by index. Beats represent story moments (major, minor, step). |
| `get_beat` | Get a specific beat by ID. |
| `list_moments` | List moments in a campaign or session. Moments capture memorable quotes and events. |
| `get_moment` | Get a specific moment by ID. |

### World Building

| Tool | Description |
|------|-------------|
| `list_factions` | List factions in a campaign. Factions represent guilds, organisations, or other groups. |
| `get_faction` | Get a specific faction by ID. |
| `list_locations` | List locations in a campaign. Locations can be nested (cities, taverns, dungeons, etc.). |
| `get_location` | Get a specific location by ID. |
| `list_items` | List items in a campaign. Items include weapons, armour, artefacts, and other notable objects. |
| `get_item` | Get a specific item by ID. |

### Quests

| Tool | Description |
|------|-------------|
| `list_quests` | List quests with pagination. Filter by status or category. |
| `get_quest` | Get a fully expanded quest: objectives, progress log, related entities, and session provenance. |

### Journals

| Tool | Description |
|------|-------------|
| `list_journals` | List journal entries in a campaign. Content omitted from list; use get_journal for full content. |
| `get_journal` | Get a journal entry by ID including full content and permission level. |
| `list_journal_folders` | List journal folders for a campaign, ordered by path and position for tree rendering. |
| `get_journal_folder` | Get a specific journal folder by ID. |

### Relationships

| Tool | Description |
|------|-------------|
| `list_links` | List links between entities. Filter by source/target entity and relationship alias. |

## REST API

For direct API access without MCP, use the Archivist REST API:

- **Base URL:** `https://api.myarchivist.ai`
- **Authentication:** `x-api-key` header
- **OpenAPI Spec:** `https://api.myarchivist.ai/openapi.json`
- **Developer Portal:** [developers.myarchivist.ai](https://developers.myarchivist.ai)
- **API Playground:** [developers.myarchivist.ai/playground](https://developers.myarchivist.ai/playground)

Get your API key from the [Developer tab](https://app.myarchivist.ai/profile?section=dev) in your Archivist profile.

## Available On

- [Smithery](https://smithery.ai/servers/me-26lt/archivist-ai)
- [Glama](https://glama.ai/mcp/connectors/ai.myarchivist.mcp/mcp-archivist-ai)
- [mcp.so](https://mcp.so/server/archivist-ai/Archivist%20AI)

## Resources

- [Archivist AI](https://www.myarchivist.ai) -- Product homepage
- [Developer Portal](https://developers.myarchivist.ai) -- API docs, playground, guides
- [MCP Server Card](https://mcp.myarchivist.ai/.well-known/mcp/server-card.json) -- Machine-readable server capabilities
- [For AI Agents](docs/for-ai-agents.md) -- Structured guide for LLM tool selection
- [MCP Tool Reference](docs/mcp-tool-reference.md) -- Complete tool documentation
- [Discord](https://discord.gg/t3yk6AWyg7) -- Community and support

## License

MIT
