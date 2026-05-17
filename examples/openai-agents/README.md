# OpenAI Agents + Archivist AI

Build AI agents that use the Archivist REST API for TTRPG campaign data retrieval using the OpenAI Agents SDK.

These examples use OpenAI function calling to query campaign data from the [Archivist AI API](https://developers.myarchivist.ai).

## Prerequisites

- Python 3.11+
- An [Archivist AI](https://www.myarchivist.ai) account with an API key
- An [OpenAI](https://platform.openai.com) API key

## Setup

```bash
cd examples/openai-agents
pip install -r requirements.txt
```

Set your environment variables:

```bash
export ARCHIVIST_API_KEY="your-archivist-api-key"
export OPENAI_API_KEY="your-openai-api-key"
```

Get your Archivist API key from the [Developer tab](https://app.myarchivist.ai/profile?section=dev) in your profile.

## Examples

### Session Recap Agent

Automatically generate session recaps by pulling session data, beats, moments, and character information.

```bash
python session_recap_agent.py
```

### NPC Recall Agent

Ask natural language questions about NPCs, their backstories, relationships, and appearances across sessions.

```bash
python npc_recall_agent.py
```

### GM Copilot

A game master assistant that combines Archivist campaign retrieval with OpenAI for prep, improvisation, and continuity.

```bash
python gm_copilot.py
```

## How It Works

Each agent defines Archivist API calls as OpenAI function tools. When the model decides it needs campaign data, it calls the appropriate function, which hits the Archivist REST API at `https://api.myarchivist.ai/v1/`. The results are fed back to the model for synthesis.

This is a **REST API** approach. For a simpler setup, consider using the [Archivist MCP server](../../README.md#connect-via-mcp-model-context-protocol) with Claude Desktop or Cursor, which handles tool registration automatically.
