# Anthropic Connectors Directory — Submission Guide

Archivist MCP can be listed in Anthropic's **Connectors Directory** (Claude.ai, Desktop, Mobile, Claude Code). This is separate from the [official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.Astrotomic/archivist-ai).

## Official links

- [Submission requirements](https://claude.com/docs/connectors/building/submission)
- [Pre-submission checklist](https://claude.com/docs/connectors/building/review-criteria)
- [Directory vs custom connectors](https://claude.com/docs/connectors/building/directory-vs-custom)
- **Review contact:** [mcp-review@anthropic.com](mailto:mcp-review@anthropic.com)
- **Form:** Remote MCPs → [MCP directory submission form](https://claude.com/docs/connectors/building/submission) (linked from Anthropic docs)

## Archivist server basics (copy for form)

| Field | Value |
|-------|-------|
| **Name** | Archivist AI |
| **Tagline** | Persistent memory for AI-powered storytelling |
| **Description** | Long-term campaign memory for Claude — characters, sessions, quests, journals, transcripts, handouts, and entity relationships across your Archivist worlds. |
| **Server URL** | `https://mcp.myarchivist.ai/mcp` |
| **Transport** | Streamable HTTP |
| **Auth** | OAuth 2.0 (PKCE) + dynamic client registration |
| **Read/write** | Read + write (67 tools — OAuth `agent_write` for mutations) |
| **Registry ID** | `io.github.Astrotomic/archivist-ai` |
| **Privacy policy** | https://www.myarchivist.ai/privacy |
| **Documentation** | https://www.myarchivist.ai/mcp |
| **Technical docs** | https://developers.myarchivist.ai/mcp |
| **Support** | contact@myarchivist.ai |
| **GitHub** | https://github.com/Astrotomic/mcp.myarchivist.ai |

## Form copy — descriptions

### Short description (55 characters max)

```text
Read/write TTRPG campaign memory for AI assistants
```

(55 characters)

### Long description (50–100 words)

```text
Archivist AI gives Claude persistent memory of your tabletop RPG campaigns. Connect with OAuth to browse campaigns, recap sessions, look up characters and NPCs, track quests, read journals, create and update world entities, manage links, and attach entity images. The connector exposes 67 MCP tools (read and write) backed by Archivist's API. Ideal for session prep, between-session recaps, lore lookup, and maintaining campaign continuity without leaving Claude.
```

## Form copy — use cases + example prompts

Paste into **Use Cases + Examples** on the submission form. Submit at least three; all five are recommended.

Also documented in the MCP repo as ChatGPT app test cases ([`chatgpt-app-submission.json`](https://github.com/Astrotomic/mcp.myarchivist.ai/blob/main/chatgpt-app-submission.json)); the prompts below are natural-language versions suitable for Claude.ai reviewers.

### 1. Session recap (between games)

**Use case:** GMs and players get a quick recap from Archivist session data, handouts, and story beats without digging through notes.

**Example prompt:**

```text
What happened in my last three game sessions? Include major beats and open plot threads.
```

**Tools exercised:** `list_campaigns`, `list_sessions`, `get_session`, `get_session_handout`, `list_beats`

### 2. Quest & plot tracking (session prep)

**Use case:** Surfaces active quests, objectives, and progress from Archivist so Claude can help with prep and continuity.

**Example prompt:**

```text
Show all in-progress quests and summarize what we still need to resolve before the next session.
```

**Tools exercised:** `list_quests`, `get_quest`

### 3. Character & relationship lookup (world lore)

**Use case:** Pulls characters, factions, locations, and entity links so Claude answers lore questions from your actual campaign memory.

**Example prompt:**

```text
Who are the most important NPCs in my campaign? Summarize each and how they relate to other characters and factions.
```

**Tools exercised:** `list_characters`, `get_character`, `list_links`, `list_factions`

### 4. Campaign overview (optional)

**Use case:** Discover campaigns and get a high-level snapshot of each world's size and activity.

**Example prompt:**

```text
List my Archivist campaigns and summarize the stats for each one.
```

**Tools exercised:** `list_campaigns`, `get_campaign_stats`

### 5. Faction or location deep dive (optional)

**Use case:** Cross-session lore lookup for a specific faction, location, or entity without manual search.

**Example prompt:**

```text
What do we know about the Thieves' Guild across all sessions?
```

**Tools exercised:** `list_factions`, `get_faction`, `list_links`, `list_moments`, `list_sessions`

## Pre-submission checklist

### Technical (required)

- [ ] Server live at `https://mcp.myarchivist.ai/mcp`
- [ ] Streamable HTTP transport
- [ ] OAuth works end-to-end in **Claude.ai** as a custom connector ([setup guide](../examples/claude-ai/README.md))
- [ ] Every tool has `title` and appropriate MCP annotations (verify with `./scripts/verify-server-card.sh`)
- [ ] Read and write tools return useful data for valid inputs ([tool testing matrix](./tool-testing.md))
- [ ] Tool handlers complete within 5 minutes; responses stay under 25k tokens where possible
- [ ] Server calls first-party Archivist API only (domain alignment)

### Documentation (required)

- [ ] Public setup guide with ≥3 example prompts ([Claude.ai guide](../examples/claude-ai/README.md))
- [ ] Privacy policy URL in docs
- [ ] Support contact listed
- [ ] Tool manifest for reviewers ([tools-directory-manifest.md](./tools-directory-manifest.md))

### Submission packet (required)

- [ ] Reviewer test account with populated campaign data ([reviewer guide template](./reviewer-guide.md))
- [ ] Credentials shared via submission form (never commit passwords to git)
- [ ] Logo URL or SVG for directory listing
- [ ] Surfaces tested: Claude.ai (minimum), optionally Desktop
- [ ] Policy & requirements checklists completed honestly on form

## Common rejection reasons

| Reason | Archivist status |
|--------|------------------|
| Missing tool annotations | ✓ All tools annotated on live server |
| Missing OAuth callback URLs | DCR accepts HTTPS redirects; test in Claude.ai before submit |
| Generic tool errors | Run [tool-testing.md](./tool-testing.md) before submit |
| Incomplete test account | Create dedicated reviewer account with real campaign data |
| Vague tool descriptions | Descriptions match behavior; see server card |
| Read+write in one tool | ✓ Read and write are separate tools with distinct annotations |

## After approval

Directory listings get a permanent URL:

```text
https://claude.ai/directory/connectors/{slug}
```

Slug is assigned by Anthropic at approval and cannot be changed later.

## Verify before submitting

```bash
./scripts/verify-server-card.sh
```
