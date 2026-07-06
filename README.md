# Archivist AI Agent Examples

Build AI agents powered by your TTRPG campaign data. This repository contains working examples, configuration files, and reference documentation for integrating [Archivist AI](https://www.myarchivist.ai) with AI assistants and agent frameworks.

Archivist AI is a **TTRPG campaign memory platform** for game masters and players. It turns Discord sessions, uploaded audio, transcripts, and play-by-post content into structured campaign history -- characters, locations, factions, items, quests, session timelines, and more -- that can be searched, queried, and used by AI agents.

## Quick Start

### Connect via MCP (Model Context Protocol)

The Archivist MCP server gives AI assistants direct access to your campaign data — read and write. OAuth clients use PKCE; programmatic clients can pass an API key as a Bearer token. Write tools require the `agent_write` OAuth scope.

**MCP Server URL:** `https://mcp.myarchivist.ai/mcp`
**Transport:** Streamable HTTP
**Authentication:** OAuth 2.0 (authorization code + PKCE) or Bearer token

### Claude.ai (Connectors Directory)

Connect Archivist as a remote MCP connector in Claude on the web — no config file required.

1. Open **Settings → Connectors** in [claude.ai](https://claude.ai)
2. Add custom connector URL: `https://mcp.myarchivist.ai/mcp`
3. Complete OAuth sign-in with your Archivist account

Full guide: [examples/claude-ai/README.md](examples/claude-ai/README.md)

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
| [Claude.ai Setup](examples/claude-ai/) | Connect Archivist to Claude on the web via OAuth connector | Config |
| [Claude Desktop Setup](examples/claude-desktop/) | Connect Archivist to Claude Desktop via MCP | Config |
| [Cursor Setup](examples/cursor/) | Connect Archivist to Cursor IDE via MCP | Config |
| [Windsurf Setup](examples/windsurf/) | Connect Archivist to Windsurf IDE via MCP | Config |
| [Session Recap Agent](examples/openai-agents/session_recap_agent.py) | Generate session recaps automatically | Python |
| [NPC Recall Agent](examples/openai-agents/npc_recall_agent.py) | Ask questions about campaign lore and NPCs | Python |
| [GM Copilot](examples/openai-agents/gm_copilot.py) | GM assistant with function calling + Archivist retrieval | Python |
| [Session Recap (TypeScript)](examples/typescript-agents/session-recap.ts) | Generate session recaps with AI SDK | TypeScript |
| [Campaign Explorer](examples/typescript-agents/campaign-explorer.ts) | Interactive campaign Q&A agent | TypeScript |

## MCP Tools Reference

The Archivist MCP server (v2.1) exposes **68 tools**: 28 read tools and 40 write tools (including five image tools). Read tools are idempotent; delete tools are destructive but idempotent.

For the complete parameter reference, see [docs/mcp-tool-reference.md](docs/mcp-tool-reference.md). Source of truth: [mcp.myarchivist.ai README](https://github.com/Astrotomic/mcp.myarchivist.ai).

**Before editing text fields:** pass `with_links: true` on get/list calls for characters, factions, locations, items, beats, moments, sessions, and journals so `[[wikilink]]` markup is preserved on round-trip writes.

### Read Tools

### Campaigns (read)

| Tool | Description |
|------|-------------|
| `list_campaigns` | List your campaigns. Returns a paginated list. |
| `get_campaign` | Get a specific campaign by ID. |
| `get_campaign_stats` | Get statistics for a campaign: character count, session count, and more. |

### Characters (read)

| Tool | Description |
|------|-------------|
| `list_characters` | List characters in a campaign. Filter by name, type (PC/NPC), or approval status. |
| `get_character` | Get a character by ID including aliases, backstory, and speaker linkage. |

### Sessions (read)

| Tool | Description |
|------|-------------|
| `list_sessions` | List game sessions in a campaign. Filter by session type or public-only. |
| `get_session` | Get a session by ID. Optionally include related beats and moments. |
| `get_session_cast_analysis` | Get cast analysis for a session: talk-share breakdown and core metrics. |
| `get_session_handout` | Get the generated session handout: summary, outlines, and spotlights. |
| `get_session_transcript` | Get the cleaned session transcript with utterances and aggregate stats. |

### Story Structure (read)

| Tool | Description |
|------|-------------|
| `list_beats` | List beats in a campaign, ordered by index. Beats represent story moments (major, minor, step). |
| `get_beat` | Get a specific beat by ID. |
| `list_moments` | List moments in a campaign or session. Moments capture memorable quotes and events. |
| `get_moment` | Get a specific moment by ID. |

### World Building (read)

| Tool | Description |
|------|-------------|
| `list_factions` | List factions in a campaign. Factions represent guilds, organisations, or other groups. |
| `get_faction` | Get a specific faction by ID. |
| `list_locations` | List locations in a campaign. Locations can be nested (cities, taverns, dungeons, etc.). |
| `get_location` | Get a specific location by ID. |
| `list_items` | List items in a campaign. Items include weapons, armour, artefacts, and other notable objects. |
| `get_item` | Get a specific item by ID. |

### Quests (read)

| Tool | Description |
|------|-------------|
| `list_quests` | List quests with pagination. Filter by status or category. |
| `get_quest` | Get a fully expanded quest: objectives, progress log, related entities, and session provenance. |

### Journals (read)

| Tool | Description |
|------|-------------|
| `list_journals` | List journal entries in a campaign. Content omitted from list; use get_journal for full content. |
| `get_journal` | Get a journal entry by ID including full content and permission level. |
| `list_journal_folders` | List journal folders for a campaign, ordered by path and position for tree rendering. |
| `get_journal_folder` | Get a specific journal folder by ID. |

### Relationships (read)

| Tool | Description |
|------|-------------|
| `list_links` | List links between entities. Filter by source/target entity and relationship alias. |

### Write Tools

Write tools mirror the REST API. Campaign delete, session delete, beat reorder/batch-edit, campaign settings, cast/member management, and multipart recording uploads are **not** exposed.

| Category | Tools |
|----------|-------|
| Campaigns | `create_campaign`, `update_campaign` |
| Sessions | `create_session`, `patch_session`, `update_session` |
| Beats | `create_beat`, `update_beat`, `delete_beat` |
| Moments | `create_moment`, `update_moment`, `delete_moment` |
| Characters | `create_character`, `update_character`, `delete_character` |
| Factions | `create_faction`, `update_faction`, `delete_faction` |
| Locations | `create_location`, `update_location`, `delete_location` |
| Items | `create_item`, `update_item`, `delete_item` |
| Quests | `create_quest`, `update_quest`, `delete_quest` |
| Journals | `create_journal`, `update_journal`, `delete_journal` |
| Journal folders | `create_journal_folder`, `update_journal_folder`, `delete_journal_folder` |
| Links | `create_link`, `update_link`, `delete_link`, `bulk_link_maintenance` |

### Image Tools

| Tool | Description |
|------|-------------|
| `get_image_usage` | Check image quota for a campaign before generating. |
| `generate_image` | AI-generate an image from entity context; returns a URL (attach via update tool). |
| `init_image_upload` | Step 1: reserve object key and presigned PUT URL. |
| `complete_image_upload` | Step 2: validate upload, moderate, and optionally attach. |
| `delete_entity_image` | Detach/delete by entity or by managed image URL. |

Direct upload requires an HTTP PUT to the presigned URL between init and complete — outside the MCP transport. Prefer `generate_image` when your client cannot make arbitrary PUTs.

## REST API

For direct API access without MCP, use the Archivist REST API:

- **Base URL:** `https://api.myarchivist.ai`
- **Authentication:** `x-api-key` header
- **OpenAPI Spec:** `https://api.myarchivist.ai/openapi.json`
- **Developer Portal:** [developers.myarchivist.ai](https://developers.myarchivist.ai)
- **API Playground:** [developers.myarchivist.ai/playground](https://developers.myarchivist.ai/playground)

Get your API key from the [Developer tab](https://app.myarchivist.ai/profile?section=dev) in your Archivist profile.

## Available On

- [Official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.Astrotomic/archivist-ai) — `io.github.Astrotomic/archivist-ai`
- [Smithery](https://smithery.ai/servers/me-26lt/archivist-ai)
- [Glama](https://glama.ai/mcp/connectors/ai.myarchivist.mcp/mcp-archivist-ai)
- [mcp.so](https://mcp.so/server/archivist-ai/Archivist%20AI)

## Connectors Directory (Anthropic)

Preparing for Claude's Connectors Directory? Start here:

- [Anthropic submission guide](docs/anthropic-connectors-directory.md)
- [Claude.ai setup](examples/claude-ai/README.md)
- [Reviewer guide template](docs/reviewer-guide.md)
- [Tool testing matrix](docs/tool-testing.md)
- [Tools manifest for submission form](docs/tools-directory-manifest.md)

Verify live server metadata:

```bash
./scripts/verify-server-card.sh
```

## Resources

- [Archivist AI](https://www.myarchivist.ai) -- Product homepage
- [Developer Portal](https://developers.myarchivist.ai) -- API docs, playground, guides
- [MCP Server Card](https://mcp.myarchivist.ai/.well-known/mcp/server-card.json) -- Machine-readable server capabilities
- [For AI Agents](docs/for-ai-agents.md) -- Structured guide for LLM tool selection
- [MCP Tool Reference](docs/mcp-tool-reference.md) -- Complete tool documentation
- [Anthropic Connectors Directory](docs/anthropic-connectors-directory.md) -- Submission checklist
- [Privacy Policy](https://www.myarchivist.ai/privacy) -- Required for directory submission
- [Discord](https://discord.gg/t3yk6AWyg7) -- Community and support

## License

MIT
