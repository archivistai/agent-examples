# TypeScript Agents + Archivist AI

Build AI agents with the [Vercel AI SDK](https://sdk.vercel.ai) that use the Archivist REST API for TTRPG campaign data.

## Prerequisites

- Node.js 20+
- An [Archivist AI](https://www.myarchivist.ai) account with an API key
- An [OpenAI](https://platform.openai.com) API key (or another AI SDK-compatible provider)

## Setup

```bash
cd examples/typescript-agents
npm install
```

Set your environment variables:

```bash
export ARCHIVIST_API_KEY="your-archivist-api-key"
export OPENAI_API_KEY="your-openai-api-key"
```

Get your Archivist API key from the [Developer tab](https://app.myarchivist.ai/profile?section=dev) in your profile.

## Examples

### Session Recap

Generate a narrative recap of your most recent session:

```bash
npx tsx session-recap.ts
```

### Campaign Explorer

Interactive campaign Q&A agent -- ask questions about your campaign and get answers grounded in your actual data:

```bash
npx tsx campaign-explorer.ts
```

## How It Works

These examples use the [AI SDK `generateText`](https://sdk.vercel.ai/docs/reference/ai-sdk-core/generate-text) function with tools that call the Archivist REST API. The AI SDK handles the tool-calling loop automatically.

For a simpler setup without writing any code, use the [Archivist MCP server](../../README.md#connect-via-mcp-model-context-protocol) directly with Claude Desktop or Cursor.
