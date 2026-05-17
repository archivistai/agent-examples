/**
 * Session Recap Agent (TypeScript)
 *
 * Generate a narrative session recap using the Vercel AI SDK + Archivist REST API.
 *
 * Usage:
 *   export ARCHIVIST_API_KEY="your-key"
 *   export OPENAI_API_KEY="your-key"
 *   npx tsx session-recap.ts
 */

import { generateText, tool } from "ai";
import { openai } from "@ai-sdk/openai";
import { z } from "zod";

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

const archivistTools = {
  listCampaigns: tool({
    description: "List the user's Archivist AI campaigns.",
    parameters: z.object({}),
    execute: async () => archivistGet("/v1/campaigns"),
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
    description: "Get a session with its beats and moments.",
    parameters: z.object({
      sessionId: z.string().describe("The session ID"),
    }),
    execute: async ({ sessionId }) =>
      archivistGet(`/v1/sessions/${sessionId}`, {
        include_beats: "true",
        include_moments: "true",
      }),
  }),

  listCharacters: tool({
    description: "List characters in a campaign.",
    parameters: z.object({
      campaignId: z.string().describe("The campaign ID"),
    }),
    execute: async ({ campaignId }) =>
      archivistGet("/v1/characters", { campaign_id: campaignId }),
  }),
};

async function main() {
  console.log("Session Recap Agent (TypeScript)");
  console.log("=".repeat(40));
  console.log("Generating a recap of your most recent session...\n");

  const { text } = await generateText({
    model: openai("gpt-4o"),
    tools: archivistTools,
    maxSteps: 10,
    system: [
      "You are a TTRPG session recap writer.",
      "Use the available tools to:",
      "1) List the user's campaigns",
      "2) Find the most recent session",
      "3) Get full session details including beats and moments",
      "4) Get the character roster",
      "Then write an engaging narrative recap of the session.",
      "Include character names, key events, memorable moments, and plot developments.",
      "Write in past tense, third person.",
    ].join(" "),
    prompt: "Generate a recap of my most recent session.",
  });

  console.log(text);
}

main().catch(console.error);
