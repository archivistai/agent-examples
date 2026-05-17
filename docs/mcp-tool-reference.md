# Archivist AI MCP Tool Reference

Complete reference for all tools available on the Archivist AI MCP server.

**Server URL:** `https://mcp.myarchivist.ai/mcp`
**Transport:** Streamable HTTP
**Authentication:** OAuth 2.0 or Bearer token
**Server Card:** `https://mcp.myarchivist.ai/.well-known/mcp/server-card.json`

All tools are **read-only**, **non-destructive**, and **idempotent**.

---

## Campaigns

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
