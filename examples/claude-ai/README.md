# Connect Archivist to Claude.ai

Use Archivist as a **remote MCP connector** in Claude on the web (claude.ai). No JSON config file required — connect through Settings.

## Server details

| Field | Value |
|-------|-------|
| **Server URL** | `https://mcp.myarchivist.ai/mcp` |
| **Transport** | Streamable HTTP |
| **Authentication** | OAuth 2.0 (PKCE) via your Archivist account |
| **Tools** | 27 read-only campaign memory tools |

## Connect (Claude.ai)

1. Open [claude.ai](https://claude.ai) and sign in.
2. Go to **Settings → Connectors** (or **Integrations**, depending on your plan).
3. Choose **Add connector** / **Add custom connector**.
4. Enter the server URL: `https://mcp.myarchivist.ai/mcp`
5. Save and click **Connect** on the Archivist connector.
6. Complete OAuth sign-in with your Archivist account and approve requested scopes.
7. Start a new chat and ask Claude to use your campaign data.

## Connect (Claude Desktop)

Claude Desktop also supports remote MCP connectors. Use the same URL in **Settings → Connectors**, or add to `claude_desktop_config.json`:

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

Config path:
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

## Example prompts

Copy these into Claude after connecting:

1. **Discover campaigns:** “List my Archivist campaigns and summarize the stats for each one.”
2. **Session recap:** “What happened in my last three game sessions? Include major beats and open threads.”
3. **Character lookup:** “Who are the most important NPCs in my campaign? Summarize each with their relationships.”
4. **Quest status:** “Show all in-progress quests and what we still need to resolve.”
5. **World lore:** “What do we know about [faction or location name] across all sessions?”

## Troubleshooting

| Issue | What to try |
|-------|-------------|
| OAuth fails after redirect | Ensure you have an active Archivist subscription and can sign in at [app.myarchivist.ai](https://app.myarchivist.ai). |
| No tools appear | Disconnect and reconnect the connector; start a **new** chat after authorizing. |
| Empty campaign data | Confirm your Archivist account has at least one campaign with processed sessions. |
| Permission errors | Revoke and reconnect from [Connected services](https://app.myarchivist.ai/profile) in your Archivist profile. |

## Privacy & support

- **Privacy policy:** [myarchivist.ai/privacy](https://www.myarchivist.ai/privacy)
- **Documentation:** [developers.myarchivist.ai/mcp](https://developers.myarchivist.ai/mcp)
- **Support:** [contact@myarchivist.ai](mailto:contact@myarchivist.ai) · [Discord](https://discord.gg/t3yk6AWyg7)

## Related

- [Anthropic Connectors Directory checklist](../../docs/anthropic-connectors-directory.md)
- [Reviewer guide (for directory submission)](../../docs/reviewer-guide.md)
- [Tool testing matrix](../../docs/tool-testing.md)
