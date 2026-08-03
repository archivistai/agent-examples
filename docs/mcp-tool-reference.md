# Archivist AI MCP Tool Reference

Complete reference for tools on the Archivist AI MCP server (v2.1).

**Server URL:** `https://mcp.myarchivist.ai/mcp`
**Transport:** Streamable HTTP
**Authentication:** OAuth 2.0 (PKCE) or Bearer token
**Server Card:** `https://mcp.myarchivist.ai/.well-known/mcp/server-card.json`

**67 tools total:** 29 read, 38 write (including four image tools). Read tools are idempotent. Delete tools are destructive but idempotent. OAuth write tools require the `agent_write` scope.

**Wikilinks:** Before editing description, summary, moment content, or journal body fields, read with `with_links: true` on the matching get/list tool. See the [server README](https://github.com/Astrotomic/mcp.myarchivist.ai#wikilinks) for per-entity write contracts.

**Not exposed:** campaign delete, session create/delete, beat reorder/batch-edit, campaign settings, cast/member management, multipart recording uploads, and first-party product-only API routes.

---

## Read Tools

### `list_campaigns`

List your MyArchivist campaigns. Returns a paginated list of campaigns.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `page` | integer | No | Page number (default: 1) |
| `size` | integer | No | Page size (default: 20) |

### `get_campaign`

Get a specific MyArchivist campaign by its ID.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | The campaign ID |

### `get_campaign_stats`

Get statistics for a specific campaign: character count, session count, and more.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | The campaign ID |

---

## Characters

### `list_characters`

List characters in a campaign. Optionally filter by name search, character type, and approval status.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | The campaign ID to list characters from |
| `search` | string | No | Search characters by name |
| `character_type` | string | No | Filter by type, e.g. PC or NPC |
| `approved_only` | boolean | No | When true, only return approved characters (default: true) |

### `get_character`

Get a specific character by ID including aliases, backstory, and speaker linkage.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `character_id` | string | Yes | The character ID |

---

## Sessions

### `list_sessions`

List game sessions in a campaign. Optionally filter by session type or public-only.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | The campaign ID to list sessions from |
| `session_type` | string | No | Filter by session type: audioUpload, playByPost, discordVoice |
| `public_only` | boolean | No | When true, only return publicly visible sessions |

### `get_session`

Get a specific game session by ID. Optionally include related beats and moments.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `session_id` | string | Yes | The session ID |
| `include_beats` | boolean | No | Include beats associated with this session |
| `include_moments` | boolean | No | Include moments associated with this session |

### `get_session_cast_analysis`

Get the cast analysis for a game session, including talk-share breakdown and core session metrics.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `session_id` | string | Yes | The session ID |

### `get_session_handout`

Get the generated session handout for a game session, including summary, outlines, spotlights, and notable moments.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `session_id` | string | Yes | The session ID |

### `get_session_transcript`

Get the cleaned transcript for a game session, including utterances, full text, and aggregate stats.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `session_id` | string | Yes | The session ID |

---

## Beats

### `list_beats`

List beats in a campaign, ordered by index. Beats represent story moments (major, minor, step).

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | The campaign ID |
| `session_id` | string | No | Filter beats by session |
| `page` | integer | No | Page number |
| `size` | integer | No | Page size |

### `get_beat`

Get a specific beat by ID.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `beat_id` | string | Yes | The beat ID |

---

## Moments

### `list_moments`

List moments in a campaign or session. Moments capture memorable quotes and events.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | The campaign ID |
| `session_id` | string | No | Filter moments by session |
| `page` | integer | No | Page number |
| `size` | integer | No | Page size |

### `get_moment`

Get a specific moment by ID.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `moment_id` | string | Yes | The moment ID |

---

## Factions

### `list_factions`

List factions in a campaign. Factions represent guilds, organisations, or other groups.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | The campaign ID |
| `page` | integer | No | Page number |
| `size` | integer | No | Page size |

### `get_faction`

Get a specific faction by ID.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `faction_id` | string | Yes | The faction ID |

---

## Locations

### `list_locations`

List locations in a campaign. Locations can be nested (cities, taverns, dungeons, etc.).

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | The campaign ID |
| `page` | integer | No | Page number |
| `size` | integer | No | Page size |

### `get_location`

Get a specific location by ID.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `location_id` | string | Yes | The location ID |

---

## Items

### `list_items`

List items in a campaign. Items include weapons, armour, artefacts, and other notable objects.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | The campaign ID |
| `page` | integer | No | Page number |
| `size` | integer | No | Page size |

### `get_item`

Get a specific item by ID.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `item_id` | string | Yes | The item ID |

---

## Quests

### `list_quests`

List quests in a campaign with pagination. Filter by status (planned, in-progress, blocked, failed, done, n/a) or category (main, side, faction, personal, n/a).

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | The campaign ID |
| `status` | string | No | Filter by status: planned, in-progress, blocked, failed, done, n/a |
| `category` | string | No | Filter by category: main, side, faction, personal, n/a |
| `page` | integer | No | Page number |
| `size` | integer | No | Page size |

### `get_quest`

Get a fully expanded quest by ID, including objectives, progress log, related entity refs, and session provenance.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `quest_id` | string | Yes | The quest ID |

---

## Journals

### `list_journals`

List journal entries in a campaign. Results are filtered to entries the caller can see. Content is omitted from the list; use `get_journal` to fetch full content.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | The campaign ID |
| `page` | integer | No | Page number |
| `size` | integer | No | Page size |

### `get_journal`

Get a specific journal entry by ID including full content and the caller's effective permission level.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `journal_id` | string | Yes | The journal entry ID |

### `list_journal_folders`

List journal folders for a campaign. Folders are ordered by path and position for tree rendering.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | The campaign ID |

### `get_journal_folder`

Get a specific journal folder by ID.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `folder_id` | string | Yes | The journal folder ID |

---

## Links

### `list_links`

List links between entities in a campaign. Supports filtering by source/target entity and relationship alias.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | The campaign ID |
| `from_id` | string | No | Filter by source entity ID |
| `from_type` | string | No | Filter by source entity type: Character, Faction, Location, Item, Beat, Moment |
| `to_id` | string | No | Filter by target entity ID |
| `to_type` | string | No | Filter by target entity type |
| `alias` | string | No | Filter by relationship alias |

---

## Write Tools

Write tools mirror the REST API. Parameters match the corresponding `POST`, `PATCH`, `PUT`, or `DELETE` routes documented at [developers.myarchivist.ai/api-reference](https://developers.myarchivist.ai/api-reference). Below are the tool names grouped by domain; see the [server README](https://github.com/Astrotomic/mcp.myarchivist.ai#available-tools) for behavioral notes.

### Campaigns

| Tool | Required params | Notes |
|------|-----------------|-------|
| `create_campaign` | `title` | Subject to subscription campaign limit |
| `update_campaign` | `campaign_id` | Partial update (title, description, tones, flags) |

### Sessions

| Tool | Required params | Notes |
|------|-----------------|-------|
| `patch_session` | `session_id` | Partial update; explicit-link wikilink contract |
| `update_session` | `session_id` | Full PUT; explicit-link wikilink contract |

### Story structure

| Tool | Required params | Notes |
|------|-----------------|-------|
| `create_beat` | `campaign_id`, `label` | Explicit-link wikilink contract |
| `update_beat` | `beat_id` | |
| `delete_beat` | `beat_id` | Child beats have `parent_id` cleared |
| `create_moment` | `campaign_id`, `session_id` | Explicit-link wikilink contract |
| `update_moment` | `moment_id` | |
| `delete_moment` | `moment_id` | |

### Compendium

| Tool | Required params | Notes |
|------|-----------------|-------|
| `create_character` | `campaign_id`, `character_name` | Description/backstory auto-resolve wikilinks |
| `update_character` | `character_id` | Read with `with_links: true` before editing text |
| `delete_character` | `character_id` | Inbound wikilinks unbracketed automatically |
| `create_faction` | `campaign_id`, `name` | |
| `update_faction` | `faction_id` | |
| `delete_faction` | `faction_id` | |
| `create_location` | `campaign_id`, `name` | |
| `update_location` | `location_id` | Child locations cleared on delete |
| `delete_location` | `location_id` | |
| `create_item` | `campaign_id`, `name` | |
| `update_item` | `item_id` | |
| `delete_item` | `item_id` | |

### Quests

| Tool | Required params | Notes |
|------|-----------------|-------|
| `create_quest` | `campaign_id`, `quest_name` | No wikilinks; use `related_*` lists |
| `update_quest` | `quest_id` | Sent lists replace stored lists |
| `delete_quest` | `quest_id` | Deletes objectives and related refs |

### Journals

| Tool | Required params | Notes |
|------|-----------------|-------|
| `create_journal` | `campaign_id`, `title` | Returns `{success, id}` |
| `update_journal` | `entry_id` | PUT semantics |
| `delete_journal` | `entry_id` | |
| `create_journal_folder` | `campaign_id`, `name`, `path` | Owners/admins only |
| `update_journal_folder` | `folder_id` | |
| `delete_journal_folder` | `folder_id` | Entries move to campaign root |

### Links

| Tool | Required params | Notes |
|------|-----------------|-------|
| `create_link` | `campaign_id`, `from_id`, `from_type`, `to_id`, `to_type`, `alias` | Upserts on alias collision |
| `update_link` | `campaign_id`, `link_id`, `alias` | |
| `delete_link` | `campaign_id`, `link_id` | Does not rewrite source text |
| `bulk_link_maintenance` | `operation`, `campaign_id`, `target_id`, `target_type` | `add` \| `remove` \| `update`; returns `{success, task_id}` |

---

## Image Tools

Entity images can be attached to campaigns, characters, factions, locations, items, moments, and sessions. Upload only — AI image generation is not exposed as an MCP tool.

### `get_image_usage`

Return the account's image quota for a campaign.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | Campaign ID |

### `init_image_upload`

Step 1 of direct upload: reserve an object key and presigned PUT URL.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | Campaign ID |
| `entity_type` | string | Yes | `campaign`, `character`, `faction`, `location`, `item`, `moment`, `session`, or `gamesession` |
| `entity_id` | string | Yes | Target entity ID |
| `file_name` | string | Yes | Original filename |
| `content_type` | string | Yes | Must be `image/*` |

**Returns:** `object_key`, `upload_url`, `public_url`, `expires_in_seconds`. Client must HTTP PUT bytes to `upload_url` before step 2.

### `complete_image_upload`

Step 2: validate upload, run moderation, optionally attach.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | Campaign ID |
| `object_key` | string | Yes | From `init_image_upload` |
| `entity_type` | string | Yes | Same as init |
| `entity_id` | string | Yes | Same as init |
| `attach` | boolean | No | Attach to entity (default true) |

### `delete_entity_image`

Remove an image by entity or by managed URL.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| `campaign_id` | string | Yes | Campaign ID |
| `entity_type` | string | Conditional | With `entity_id` — detaches and deletes object |
| `entity_id` | string | Conditional | With `entity_type` |
| `image_url` | string | Conditional | Deletes object only (alternative to entity pair) |
