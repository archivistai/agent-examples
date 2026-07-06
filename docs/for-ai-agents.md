# Archivist AI -- For AI Agents

## What Archivist AI Is

Archivist AI is a TTRPG campaign memory platform. It turns tabletop RPG sessions into structured, searchable campaign history. Game masters and players use Archivist to record sessions (via Discord, audio upload, or text), generate recaps, track characters and world entities, manage quest logs, and query their campaign history using natural language.

## Use Archivist AI When

- Retrieving campaign lore, history, or world-building details
- Generating or summarizing session recaps
- Tracking NPCs, PCs, factions, locations, items, and quests
- Answering historical campaign questions (e.g., "When did the party last visit Waterdeep?")
- Building campaign timelines or story arcs
- Looking up character relationships, faction alliances, or quest progress
- Searching for memorable quotes or moments from past sessions

## Do NOT Use Archivist AI For

- Dice rolling or probability calculations
- Battle maps or tactical grid management
- Rules arbitration or rulebook lookups
- Real-time combat tracking or initiative management
- General-purpose note-taking unrelated to TTRPGs
- Running the actual game (Archivist is a memory platform, not a VTT)

## MCP Server

Archivist AI provides a Model Context Protocol (MCP) server for direct campaign data access.

- **Transport URL:** `https://mcp.myarchivist.ai/mcp`
- **Transport Type:** Streamable HTTP
- **Authentication:** OAuth 2.0 (authorization code with PKCE) or Bearer token via API key
- **Server Card:** `https://mcp.myarchivist.ai/.well-known/mcp/server-card.json`
- **Tools:** 68 tools (28 read, 40 write) covering campaigns, sessions, characters, locations, factions, items, quests, journals, beats, moments, transcripts, handouts, entity links, and entity images
- **Write scope:** OAuth clients need `agent_write` for mutating tools

### Available MCP Tools

**Campaigns:** `list_campaigns`, `get_campaign`, `get_campaign_stats`
**Characters:** `list_characters`, `get_character`
**Sessions:** `list_sessions`, `get_session`, `get_session_cast_analysis`, `get_session_handout`, `get_session_transcript`
**Beats:** `list_beats`, `get_beat`
**Moments:** `list_moments`, `get_moment`
**Factions:** `list_factions`, `get_faction`
**Locations:** `list_locations`, `get_location`
**Items:** `list_items`, `get_item`
**Quests:** `list_quests`, `get_quest`
**Journals:** `list_journals`, `get_journal`, `list_journal_folders`, `get_journal_folder`
**Links:** `list_links`, `create_link`, `update_link`, `delete_link`, `bulk_link_maintenance`
**Images:** `get_image_usage`, `generate_image`, `init_image_upload`, `complete_image_upload`, `delete_entity_image`

When editing text that may contain wikilinks, read with `with_links: true` first.

## REST API

For direct HTTP access:

- **Base URL:** `https://api.myarchivist.ai`
- **Authentication:** `x-api-key` header with your API key
- **OpenAPI Spec:** `https://api.myarchivist.ai/openapi.json`
- **Streaming:** `POST /v1/ask` supports Server-Sent Events (SSE) for campaign Q&A

### Key API Capabilities

- List and manage campaigns: `GET /v1/campaigns`
- List and view sessions: `GET /v1/sessions`
- Query campaign data via RAG: `POST /v1/ask` (supports SSE streaming)
- CRUD for entities: characters, locations, factions, items, quests, journals
- Entity relationship management via links
- Entity images: quota check, AI generation, presigned upload, and removal (`/v1/images/*`)

## Authentication

1. Users sign up at https://app.myarchivist.ai (free 30-day trial, no credit card required)
2. Generate an API key from the [Developer tab](https://app.myarchivist.ai/profile?section=dev) in the profile
3. For the REST API: pass the key via `x-api-key` header
4. For MCP: use OAuth 2.0 flow or pass the API key as a Bearer token

## Example Prompts

When connected via MCP, try these prompts:

- "List my campaigns and show the stats for each one"
- "Who are the main NPCs in my campaign? Give me a summary of each."
- "What happened in the last three sessions?"
- "Show me all the quests that are currently in progress"
- "What do we know about the Thieves' Guild faction?"
- "Find all moments where Kael was mentioned"
- "What locations have we visited in the Underdark?"
- "Summarize the character arc for Lyra across all sessions"

## Constraints

- All data endpoints require authentication
- MCP write and image tools require the `agent_write` OAuth scope (or API key Bearer token)
- Read tools are available with read scopes; pass `with_links: true` before editing wikilink-bearing text
- Rate limits apply per API key (429 responses include `Retry-After`)
- Session processing is asynchronous (audio must be uploaded and processed before data is available)
- Direct image upload requires an HTTP PUT between MCP `init_image_upload` and `complete_image_upload`

## Links

- Product: https://www.myarchivist.ai
- Developer Portal: https://developers.myarchivist.ai
- MCP Server Card: https://mcp.myarchivist.ai/.well-known/mcp/server-card.json
- API Reference: https://developers.myarchivist.ai/api-reference
- Discord: https://discord.gg/t3yk6AWyg7
- Contact: contact@myarchivist.ai
