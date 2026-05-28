# Anthropic Reviewer Guide (Template)

Use this document when submitting Archivist to the Anthropic Connectors Directory. **Do not commit real passwords** — share credentials only through the official submission form or a secure channel Anthropic provides.

## Test account (fill in before submission)

| Field | Value |
|-------|-------|
| **Archivist login email** | `[REVIEWER_EMAIL@example.com]` |
| **Password** | `[Provide via submission form only]` |
| **Subscription status** | Active paid or trial with campaign data |
| **Recommended campaign name** | `[Campaign title reviewers should use]` |
| **Campaign ID** | `[Optional — from list_campaigns output]` |

The account must include **realistic, populated data**: multiple sessions, characters, quests, journals, and at least one processed transcript or handout if possible.

## Connect Archivist in Claude.ai

1. Sign in to [claude.ai](https://claude.ai) with your Anthropic reviewer account (not the Archivist account).
2. Open **Settings → Connectors**.
3. Add custom connector URL: `https://mcp.myarchivist.ai/mcp`
4. Click **Connect** and complete OAuth using the **Archivist test account** above.
5. Approve scopes: `profile`, `worlds_read`, `sessions_read`, `characters_read`.
6. Open a **new chat** and confirm Archivist tools are available.

Detailed steps: [examples/claude-ai/README.md](../examples/claude-ai/README.md)

## Recommended review flow

Run these prompts in order. Each should succeed without manual IDs on the first try (Claude should call tools automatically).

### 1. Discover campaigns

> List my Archivist campaigns and show stats for each.

**Expected:** `list_campaigns` → `get_campaign_stats` for one or more campaigns.

### 2. Session history

> What happened in my most recent three sessions? Summarize key events and open plot threads.

**Expected:** `list_campaigns` → `list_sessions` → `get_session` (optionally with beats/moments).

### 3. Character lookup

> Who are the main NPCs in my campaign? Give a short summary of each.

**Expected:** `list_characters` → `get_character` for notable NPCs.

### 4. Quest status

> Show all quests that are in progress and summarize their current objectives.

**Expected:** `list_quests` → `get_quest` for active quests.

### 5. Faction / location lore

> What do we know about [named faction or location] across the campaign?

**Expected:** `list_factions` or `list_locations` → `get_faction` or `get_location`.

## Tool smoke checklist

Anthropic may call any tool. Minimum smoke set:

| Tool | Minimal valid call |
|------|-------------------|
| `list_campaigns` | No required params |
| `get_campaign` | `campaign_id` from list |
| `get_campaign_stats` | `campaign_id` from list |
| `list_sessions` | `campaign_id` |
| `get_session` | `session_id` from list |
| `get_session_cast_analysis` | `session_id` |
| `get_session_transcript` | `session_id` (session with transcript) |
| `get_session_handout` | `session_id` (session with handout) |
| `list_characters` | `campaign_id` |
| `get_character` | `character_id` from list |
| `list_quests` | `campaign_id` |
| `get_quest` | `quest_id` from list |

Full matrix: [tool-testing.md](./tool-testing.md)

## Revoke access after review

Reviewers can revoke MCP access from:

**Archivist profile → Connected services → Archivist MCP → Remove**

## Support during review

- **Email:** contact@myarchivist.ai
- **Discord:** https://discord.gg/t3yk6AWyg7
- **Escalation (Anthropic):** mcp-review@anthropic.com
