/**
 * Campaign Explorer Agent (TypeScript)
 *
 * Interactive campaign Q&A agent using the Vercel AI SDK + Archivist REST API.
 * Ask questions about your campaign and get answers grounded in your actual data.
 *
 * Usage:
 *   export ARCHIVIST_API_KEY="your-key"
 *   export OPENAI_API_KEY="your-key"
 *   npx tsx campaign-explorer.ts
 */

import { generateText, tool } from "ai";
import { openai } from "@ai-sdk/openai";
import { z } from "zod";
import * as readline from "node:readline/promises";

const ARCHIVIST_BASE_URL = "https://api.myarchivist.ai";
const ARCHIVIST_API_KEY = process.env.ARCHIVIST_API_KEY ?? "";

if (!ARCHIVIST_API_KEY) {
  console.error("Set ARCHIVIST_API_KEY environment variable.");
  console.error("Get your key at: https://app.myarchivist.ai/profile?section=dev");
  process.exit(1);
}

async function archivistGet(path: string, params?: Record<string, string>) {
  const url = new URL(path, ARCHIVIST_BASE_URL);
  if (params) {
    Object.entries(params).forEach(([k, v]) => url.searchParams.set(k, v));
  }
  const resp = await fetch(url, {
    headers: { "x-api-key": ARCHIVIST_API_KEY },
  });
  if (!resp.ok) throw new Error(`Archivist API error: ${resp.status}`);
  return resp.json();
}

async function archivistPost(path: string, body: unknown) {
  const resp = await fetch(new URL(path, ARCHIVIST_BASE_URL), {
    method: "POST",
    headers: {
      "x-api-key": ARCHIVIST_API_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });
  if (!resp.ok) throw new Error(`Archivist API error: ${resp.status}`);
  return resp.json();
}

const archivistTools = {
  listCampaigns: tool({
    description: "List available campaigns.",
    parameters: z.object({}),
    execute: async () => archivistGet("/v1/campaigns"),
  }),

  getCampaignStats: tool({
    description: "Get campaign statistics: session count, character count, etc.",
    parameters: z.object({
      campaignId: z.string().describe("The campaign ID"),
    }),
    execute: async ({ campaignId }) =>
      archivistGet(`/v1/campaigns/${campaignId}/stats`),
  }),

  listCharacters: tool({
    description: "List characters. Optionally filter by type (PC/NPC) or search by name.",
    parameters: z.object({
      campaignId: z.string().describe("The campaign ID"),
      characterType: z.string().optional().describe("PC or NPC"),
      search: z.string().optional().describe("Search by name"),
    }),
    execute: async ({ campaignId, characterType, search }) => {
      const params: Record<string, string> = { campaign_id: campaignId };
      if (characterType) params.character_type = characterType;
      if (search) params.search = search;
      return archivistGet("/v1/characters", params);
    },
  }),

  listSessions: tool({
    description: "List game sessions in a campaign.",
    parameters: z.object({
      campaignId: z.string().describe("The campaign ID"),
    }),
    execute: async ({ campaignId }) =>
      archivistGet("/v1/sessions", { campaign_id: campaignId }),
  }),

  getSession: tool({
    description: "Get a session with beats and moments.",
    parameters: z.object({
      sessionId: z.string().describe("The session ID"),
    }),
    execute: async ({ sessionId }) =>
      archivistGet(`/v1/sessions/${sessionId}`, {
        include_beats: "true",
        include_moments: "true",
      }),
  }),

  listQuests: tool({
    description: "List quests. Filter by status or category.",
    parameters: z.object({
      campaignId: z.string().describe("The campaign ID"),
      status: z.string().optional().describe("planned, in-progress, blocked, failed, done"),
      category: z.string().optional().describe("main, side, faction, personal"),
    }),
    execute: async ({ campaignId, status, category }) => {
      const params: Record<string, string> = { campaign_id: campaignId };
      if (status) params.status = status;
      if (category) params.category = category;
      return archivistGet("/v1/quests", params);
    },
  }),

  listLocations: tool({
    description: "List locations in a campaign.",
    parameters: z.object({
      campaignId: z.string().describe("The campaign ID"),
    }),
    execute: async ({ campaignId }) =>
      archivistGet("/v1/locations", { campaign_id: campaignId }),
  }),

  listFactions: tool({
    description: "List factions in a campaign.",
    parameters: z.object({
      campaignId: z.string().describe("The campaign ID"),
    }),
    execute: async ({ campaignId }) =>
      archivistGet("/v1/factions", { campaign_id: campaignId }),
  }),

  askArchivist: tool({
    description: "Ask a natural language question about the campaign using RAG-powered Q&A.",
    parameters: z.object({
      campaignId: z.string().describe("The campaign ID"),
      question: z.string().describe("The question to ask"),
    }),
    execute: async ({ campaignId, question }) =>
      archivistPost("/v1/ask", {
        campaign_id: campaignId,
        messages: [{ role: "user", content: question }],
        stream: false,
      }),
  }),
};

async function main() {
  console.log("Campaign Explorer Agent (TypeScript)");
  console.log("=".repeat(40));
  console.log("Ask questions about your TTRPG campaign.");
  console.log("Type 'quit' to exit.\n");

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const messages: Array<{ role: "system" | "user" | "assistant"; content: string }> = [
    {
      role: "system",
      content: [
        "You are a campaign explorer agent for TTRPG campaigns powered by Archivist AI.",
        "Help users explore their campaign data: characters, sessions, quests, factions, locations, and lore.",
        "Start by listing campaigns so the user can pick one.",
        "Use Ask Archivist for complex questions that span multiple sessions.",
        "Be specific and reference actual campaign data in your answers.",
      ].join(" "),
    },
  ];

  while (true) {
    const input = await rl.question("\nYou: ");
    if (["quit", "exit", "q"].includes(input.trim().toLowerCase())) break;

    messages.push({ role: "user", content: input });

    const { text } = await generateText({
      model: openai("gpt-4o"),
      tools: archivistTools,
      maxSteps: 10,
      messages,
    });

    console.log(`\nExplorer: ${text}`);
    messages.push({ role: "assistant", content: text });
  }

  rl.close();
}

main().catch(console.error);
