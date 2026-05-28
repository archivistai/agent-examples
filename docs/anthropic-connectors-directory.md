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
| **Read/write** | Read-only (v1 — all 27 tools) |
| **Registry ID** | `io.github.Astrotomic/archivist-ai` |
| **Privacy policy** | https://www.myarchivist.ai/privacy |
| **Documentation** | https://www.myarchivist.ai/mcp |
| **Technical docs** | https://developers.myarchivist.ai/mcp |
| **Support** | contact@myarchivist.ai |
| **GitHub** | https://github.com/Astrotomic/mcp.myarchivist.ai |

## Pre-submission checklist

### Technical (required)

- [ ] Server live at `https://mcp.myarchivist.ai/mcp`
- [ ] Streamable HTTP transport
- [ ] OAuth works end-to-end in **Claude.ai** as a custom connector ([setup guide](../examples/claude-ai/README.md))
- [ ] Every tool has `title` + `readOnlyHint: true` (verify with `./scripts/verify-server-card.sh`)
- [ ] All 27 tools return useful data for valid inputs ([tool testing matrix](./tool-testing.md))
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
| Read+write in one tool | ✓ All tools read-only, separate endpoints |

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
