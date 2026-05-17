"""
NPC Recall Agent
Ask questions about campaign lore, NPCs, and world history using OpenAI + Archivist AI.

Uses the Archivist RAG endpoint (Ask Archivist) for deep campaign Q&A,
plus direct character and faction lookups for structured data.

Usage:
    export ARCHIVIST_API_KEY="your-key"
    export OPENAI_API_KEY="your-key"
    python npc_recall_agent.py
"""

import json
import os

import httpx
from openai import OpenAI

ARCHIVIST_BASE_URL = "https://api.myarchivist.ai"
ARCHIVIST_API_KEY = os.environ.get("ARCHIVIST_API_KEY", "")

client = OpenAI()
http = httpx.Client(
    base_url=ARCHIVIST_BASE_URL,
    headers={"x-api-key": ARCHIVIST_API_KEY},
    timeout=30,
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "list_campaigns",
            "description": "List available campaigns.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_characters",
            "description": "List characters in a campaign. Filter by type (PC/NPC) or search by name.",
            "parameters": {
                "type": "object",
                "properties": {
                    "campaign_id": {"type": "string", "description": "The campaign ID."},
                    "search": {"type": "string", "description": "Search by character name."},
                    "character_type": {"type": "string", "description": "Filter: PC or NPC."},
                },
                "required": ["campaign_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_character",
            "description": "Get full character details including backstory, aliases, and speaker info.",
            "parameters": {
                "type": "object",
                "properties": {
                    "character_id": {"type": "string", "description": "The character ID."},
                },
                "required": ["character_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "ask_archivist",
            "description": "Ask a natural language question about the campaign. Uses RAG over all campaign data.",
            "parameters": {
                "type": "object",
                "properties": {
                    "campaign_id": {"type": "string", "description": "The campaign ID."},
                    "question": {"type": "string", "description": "The question to ask."},
                },
                "required": ["campaign_id", "question"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_factions",
            "description": "List factions (guilds, organizations, groups) in a campaign.",
            "parameters": {
                "type": "object",
                "properties": {
                    "campaign_id": {"type": "string", "description": "The campaign ID."},
                },
                "required": ["campaign_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_links",
            "description": "List relationships between entities in a campaign.",
            "parameters": {
                "type": "object",
                "properties": {
                    "campaign_id": {"type": "string", "description": "The campaign ID."},
                    "from_id": {"type": "string", "description": "Filter by source entity ID."},
                    "from_type": {"type": "string", "description": "Source type: Character, Faction, etc."},
                },
                "required": ["campaign_id"],
            },
        },
    },
]


def call_archivist(name: str, arguments: dict) -> str:
    """Route a function call to the Archivist API."""
    match name:
        case "list_campaigns":
            resp = http.get("/v1/campaigns")
        case "list_characters":
            params = {"campaign_id": arguments["campaign_id"]}
            if "search" in arguments:
                params["search"] = arguments["search"]
            if "character_type" in arguments:
                params["character_type"] = arguments["character_type"]
            resp = http.get("/v1/characters", params=params)
        case "get_character":
            resp = http.get(f"/v1/characters/{arguments['character_id']}")
        case "ask_archivist":
            resp = http.post(
                "/v1/ask",
                json={
                    "campaign_id": arguments["campaign_id"],
                    "messages": [{"role": "user", "content": arguments["question"]}],
                    "stream": False,
                },
            )
        case "list_factions":
            resp = http.get("/v1/factions", params={"campaign_id": arguments["campaign_id"]})
        case "list_links":
            params = {"campaign_id": arguments["campaign_id"]}
            if "from_id" in arguments:
                params["from_id"] = arguments["from_id"]
            if "from_type" in arguments:
                params["from_type"] = arguments["from_type"]
            resp = http.get("/v1/links", params=params)
        case _:
            return json.dumps({"error": f"Unknown function: {name}"})

    resp.raise_for_status()
    return json.dumps(resp.json(), default=str)


def run_npc_recall():
    print("NPC Recall Agent")
    print("=" * 40)
    print("Ask questions about your campaign's NPCs, factions, and lore.")
    print("Type 'quit' to exit.\n")

    system_prompt = (
        "You are an NPC and lore recall agent for a TTRPG campaign. "
        "Help the user remember details about NPCs, factions, locations, and campaign history. "
        "Use the available tools to look up characters, query campaign lore via Ask Archivist, "
        "and explore entity relationships. "
        "Start by listing campaigns so the user can pick one, then answer their questions. "
        "Be specific and cite session details when available."
    )

    messages = [{"role": "system", "content": system_prompt}]

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break

        messages.append({"role": "user", "content": user_input})

        while True:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                tools=tools,
            )

            message = response.choices[0].message

            if message.tool_calls:
                messages.append(message)
                for tool_call in message.tool_calls:
                    arguments = json.loads(tool_call.function.arguments)
                    print(f"  [{tool_call.function.name}]")
                    result = call_archivist(tool_call.function.name, arguments)
                    messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": result,
                        }
                    )
            else:
                print(f"\nAgent: {message.content}")
                messages.append(message)
                break


if __name__ == "__main__":
    if not ARCHIVIST_API_KEY:
        print("Set ARCHIVIST_API_KEY environment variable.")
        print("Get your key at: https://app.myarchivist.ai/profile?section=dev")
        exit(1)
    run_npc_recall()
