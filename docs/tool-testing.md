# MCP Tool Testing Matrix

Run before Anthropic Connectors Directory submission. Anthropic reviewers **call every tool** with valid parameters.

Verify live metadata first:

```bash
./scripts/verify-server-card.sh
```

## Naming note

| Context | Example |
|---------|---------|
| MCP server card / Claude | `list-campaigns-tool` |
| Docs / snake_case API style | `list_campaigns` |

Same tool, different identifiers.

## Pre-requisites

- Archivist account with at least one campaign containing sessions, characters, and quests
- OAuth-connected client (Claude.ai custom connector recommended) or Bearer token for MCP Inspector
- Note `campaign_id`, `session_id`, `character_id`, etc. from `list_*` calls

## Full tool matrix

Mark each row after a successful call with valid params and a non-error response.

| # | MCP name | Snake name | Required params | Notes |
|---|----------|------------|-----------------|-------|
| 1 | list-campaigns-tool | list_campaigns | — | Start here |
| 2 | get-campaign-tool | get_campaign | campaign_id | |
| 3 | get-campaign-stats-tool | get_campaign_stats | campaign_id | |
| 4 | list-characters-tool | list_characters | campaign_id | |
| 5 | get-character-tool | get_character | character_id | |
| 6 | list-sessions-tool | list_sessions | campaign_id | |
| 7 | get-session-tool | get_session | session_id | Try include_beats, include_moments |
| 8 | get-session-cast-analysis-tool | get_session_cast_analysis | session_id | |
| 9 | get-session-handout-tool | get_session_handout | session_id | Needs generated handout |
| 10 | get-session-transcript-tool | get_session_transcript | session_id | Needs processed transcript |
| 11 | list-beats-tool | list_beats | campaign_id | |
| 12 | get-beat-tool | get_beat | beat_id | |
| 13 | list-moments-tool | list_moments | campaign_id | |
| 14 | get-moment-tool | get_moment | moment_id | |
| 15 | list-factions-tool | list_factions | campaign_id | |
| 16 | get-faction-tool | get_faction | faction_id | |
| 17 | list-locations-tool | list_locations | campaign_id | |
| 18 | get-location-tool | get_location | location_id | |
| 19 | list-items-tool | list_items | campaign_id | |
| 20 | get-item-tool | get_item | item_id | |
| 21 | list-quests-tool | list_quests | campaign_id | |
| 22 | get-quest-tool | get_quest | quest_id | |
| 23 | list-journals-tool | list_journals | campaign_id | |
| 24 | get-journal-tool | get_journal | journal_id | |
| 25 | list-journal-folders-tool | list_journal_folders | campaign_id | |
| 26 | get-journal-folder-tool | get_journal_folder | folder_id | |
| 27 | list-links-tool | list_links | campaign_id | Optional filters |

## Testing surfaces

| Surface | How to test |
|---------|-------------|
| **Claude.ai** | Settings → Connectors → add `https://mcp.myarchivist.ai/mcp` |
| **Claude Desktop** | Same URL in Connectors or `claude_desktop_config.json` |
| **MCP Inspector** | Connect with Bearer token; exercise tools manually |
| **Cursor** | `.cursor/mcp.json` with streamable-http URL |

## Failure patterns to fix before submit

- **401/403** — OAuth or token issue; re-authorize
- **500 with no detail** — fix server-side; reviewers reject generic errors
- **Empty arrays on populated campaign** — wrong campaign_id or scope issue
- **Timeout on transcript/handout** — verify session has processed content; check response size
- **Missing annotations** — re-run `verify-server-card.sh`

## Automated server-card check

```bash
./scripts/verify-server-card.sh
```

Checks: tool count, every tool has title, readOnlyHint or destructiveHint, server URL reachable.
