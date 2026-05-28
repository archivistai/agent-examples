# Tools Directory Manifest

Human-readable tool list for Anthropic Connectors Directory submission. Generated from live server card at `https://mcp.myarchivist.ai/.well-known/mcp/server-card.json`.

**Tool count:** 27 · **All read-only** · **Annotations:** `readOnlyHint: true`, `destructiveHint: false`

| MCP name | Title | Snake alias | Description |
|----------|-------|-------------|-------------|
| list-campaigns-tool | List Campaigns Tool | list_campaigns | List your campaigns. Returns a paginated list. |
| get-campaign-tool | Get Campaign Tool | get_campaign | Get a specific campaign by ID. |
| get-campaign-stats-tool | Get Campaign Stats Tool | get_campaign_stats | Get statistics: character count, session count, and more. |
| list-characters-tool | List Characters Tool | list_characters | List characters. Filter by name, type (PC/NPC), or approval status. |
| get-character-tool | Get Character Tool | get_character | Get a character including aliases, backstory, and speaker linkage. |
| list-sessions-tool | List Sessions Tool | list_sessions | List game sessions. Filter by type or public-only. |
| get-session-tool | Get Session Tool | get_session | Get a session with optional beats and moments. |
| get-session-cast-analysis-tool | Get Session Cast Analysis Tool | get_session_cast_analysis | Get cast analysis: talk-share breakdown and metrics. |
| get-session-handout-tool | Get Session Handout Tool | get_session_handout | Get generated session handout: summary, outlines, spotlights. |
| get-session-transcript-tool | Get Session Transcript Tool | get_session_transcript | Get cleaned session transcript with utterances and stats. |
| list-beats-tool | List Beats Tool | list_beats | List beats ordered by index (major, minor, step). |
| get-beat-tool | Get Beat Tool | get_beat | Get a specific beat by ID. |
| list-moments-tool | List Moments Tool | list_moments | List moments: memorable quotes and events. |
| get-moment-tool | Get Moment Tool | get_moment | Get a specific moment by ID. |
| list-factions-tool | List Factions Tool | list_factions | List factions (guilds, organisations, groups). |
| get-faction-tool | Get Faction Tool | get_faction | Get a specific faction by ID. |
| list-locations-tool | List Locations Tool | list_locations | List locations (nested: cities, taverns, dungeons). |
| get-location-tool | Get Location Tool | get_location | Get a specific location by ID. |
| list-items-tool | List Items Tool | list_items | List items (weapons, armour, artefacts). |
| get-item-tool | Get Item Tool | get_item | Get a specific item by ID. |
| list-quests-tool | List Quests Tool | list_quests | List quests. Filter by status or category. |
| get-quest-tool | Get Quest Tool | get_quest | Get expanded quest: objectives, progress, entities. |
| list-journals-tool | List Journals Tool | list_journals | List journal entries (content omitted; use get_journal). |
| get-journal-tool | Get Journal Tool | get_journal | Get journal entry with full content and permissions. |
| list-journal-folders-tool | List Journal Folders Tool | list_journal_folders | List journal folders for tree rendering. |
| get-journal-folder-tool | Get Journal Folder Tool | get_journal_folder | Get a specific journal folder by ID. |
| list-links-tool | List Links Tool | list_links | List entity links. Filter by source/target and alias. |

Refresh from production:

```bash
curl -s https://mcp.myarchivist.ai/.well-known/mcp/server-card.json | jq '.tools[] | {name, title, description}'
```
