"""
GM Copilot
A game master assistant that combines Archivist campaign retrieval with OpenAI
for session prep, improvisation support, and continuity tracking.

Usage:
    export ARCHIVIST_API_KEY="your-key"
    export OPENAI_API_KEY="your-key"
    python gm_copilot.py
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
            "name": "get_campaign_stats",
            "description": "Get campaign statistics: session count, character count, and more.",
            "parameters": {
                "type": "object",
                "properties": {
                    "campaign_id": {"type": "string"},
                },
                "required": ["campaign_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_sessions",
            "description": "List game sessions in a campaign.",
            "parameters": {
                "type": "object",
                "properties": {
                    "campaign_id": {"type": "string"},
                },
                "required": ["campaign_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_session",
            "description": "Get a session with beats and moments.",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {"type": "string"},
                },
                "required": ["session_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_characters",
            "description": "List characters in a campaign.",
            "parameters": {
                "type": "object",
                "properties": {
                    "campaign_id": {"type": "string"},
                    "character_type": {"type": "string", "description": "PC or NPC"},
                },
                "required": ["campaign_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_quests",
            "description": "List quests. Filter by status or category.",
            "parameters": {
                "type": "object",
                "properties": {
                    "campaign_id": {"type": "string"},
                    "status": {"type": "string", "description": "planned, in-progress, blocked, failed, done, n/a"},
                    "category": {"type": "string", "description": "main, side, faction, personal, n/a"},
                },
                "required": ["campaign_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_quest",
            "description": "Get full quest details: objectives, progress, related entities.",
            "parameters": {
                "type": "object",
                "properties": {
                    "quest_id": {"type": "string"},
                },
                "required": ["quest_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_locations",
            "description": "List locations in a campaign.",
            "parameters": {
                "type": "object",
                "properties": {
                    "campaign_id": {"type": "string"},
                },
                "required": ["campaign_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_factions",
            "description": "List factions in a campaign.",
            "parameters": {
                "type": "object",
                "properties": {
                    "campaign_id": {"type": "string"},
                },
                "required": ["campaign_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "ask_archivist",
            "description": "Ask a question about the campaign using RAG-powered Q&A.",
            "parameters": {
                "type": "object",
                "properties": {
                    "campaign_id": {"type": "string"},
                    "question": {"type": "string"},
                },
                "required": ["campaign_id", "question"],
            },
        },
    },
]


def call_archivist(name: str, arguments: dict) -> str:
    """Route a function call to the Archivist API."""
    match name:
        case "list_campaigns":
            resp = http.get("/v1/campaigns")
        case "get_campaign_stats":
            resp = http.get(f"/v1/campaigns/{arguments['campaign_id']}/stats")
        case "list_sessions":
            resp = http.get("/v1/sessions", params={"campaign_id": arguments["campaign_id"]})
        case "get_session":
            resp = http.get(
                f"/v1/sessions/{arguments['session_id']}",
                params={"include_beats": "true", "include_moments": "true"},
            )
        case "list_characters":
            params = {"campaign_id": arguments["campaign_id"]}
            if "character_type" in arguments:
                params["character_type"] = arguments["character_type"]
            resp = http.get("/v1/characters", params=params)
        case "list_quests":
            params = {"campaign_id": arguments["campaign_id"]}
            if "status" in arguments:
                params["status"] = arguments["status"]
            if "category" in arguments:
                params["category"] = arguments["category"]
            resp = http.get("/v1/quests", params=params)
        case "get_quest":
            resp = http.get(f"/v1/quests/{arguments['quest_id']}")
        case "list_locations":
            resp = http.get("/v1/locations", params={"campaign_id": arguments["campaign_id"]})
        case "list_factions":
            resp = http.get("/v1/factions", params={"campaign_id": arguments["campaign_id"]})
        case "ask_archivist":
            resp = http.post(
                "/v1/ask",
                json={
                    "campaign_id": arguments["campaign_id"],
                    "messages": [{"role": "user", "content": arguments["question"]}],
                    "stream": False,
                },
            )
        case _:
            return json.dumps({"error": f"Unknown function: {name}"})

    resp.raise_for_status()
    return json.dumps(resp.json(), default=str)


def run_gm_copilot():
    print("GM Copilot")
    print("=" * 40)
    print("Your AI-powered game master assistant.")
    print("Powered by Archivist AI campaign data + OpenAI.")
    print()
    print("Try:")
    print("  - 'Help me prep for next session'")
    print("  - 'What threads should I pick up?'")
    print("  - 'Summarize the active quests'")
    print("  - 'What do the players know about the Crimson Court?'")
    print("  - 'Generate a recap I can read to my players'")
    print()
    print("Type 'quit' to exit.\n")

    system_prompt = (
        "You are a GM Copilot -- an AI assistant for tabletop RPG game masters. "
        "You have access to the user's full campaign history through Archivist AI. "
        "Help with session prep, continuity tracking, NPC improvisation, quest management, "
        "and recap generation. "
        "\n\n"
        "Start by listing campaigns so the user can select one. Then proactively gather "
        "context: campaign stats, recent sessions, active quests, and key NPCs. "
        "\n\n"
        "When helping with prep:\n"
        "- Review recent sessions for dangling threads\n"
        "- Check active and blocked quests\n"
        "- Note which NPCs appeared recently\n"
        "- Suggest plot hooks based on campaign history\n"
        "\n"
        "When generating recaps:\n"
        "- Use beats for structure and moments for flavor\n"
        "- Include character names and key decisions\n"
        "- Write in an engaging narrative style\n"
        "\n"
        "Use Ask Archivist for deep questions about campaign history that span multiple sessions."
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
                print(f"\nGM Copilot: {message.content}")
                messages.append(message)
                break


if __name__ == "__main__":
    if not ARCHIVIST_API_KEY:
        print("Set ARCHIVIST_API_KEY environment variable.")
        print("Get your key at: https://app.myarchivist.ai/profile?section=dev")
        exit(1)
    run_gm_copilot()
