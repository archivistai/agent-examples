"""
Session Recap Agent
Generate session recaps automatically using OpenAI + Archivist AI.

Pulls session data, beats, moments, and characters from your campaign,
then synthesizes them into a narrative recap.

Usage:
    export ARCHIVIST_API_KEY="your-key"
    export OPENAI_API_KEY="your-key"
    python session_recap_agent.py
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
            "description": "List the user's Archivist AI campaigns.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_sessions",
            "description": "List game sessions in a campaign, ordered by date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "campaign_id": {
                        "type": "string",
                        "description": "The campaign ID.",
                    },
                },
                "required": ["campaign_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_session",
            "description": "Get a session with its beats and moments.",
            "parameters": {
                "type": "object",
                "properties": {
                    "session_id": {
                        "type": "string",
                        "description": "The session ID.",
                    },
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
                    "campaign_id": {
                        "type": "string",
                        "description": "The campaign ID.",
                    },
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
        case "list_sessions":
            resp = http.get("/v1/sessions", params={"campaign_id": arguments["campaign_id"]})
        case "get_session":
            resp = http.get(
                f"/v1/sessions/{arguments['session_id']}",
                params={"include_beats": "true", "include_moments": "true"},
            )
        case "list_characters":
            resp = http.get("/v1/characters", params={"campaign_id": arguments["campaign_id"]})
        case _:
            return json.dumps({"error": f"Unknown function: {name}"})

    resp.raise_for_status()
    return json.dumps(resp.json(), default=str)


def run_recap_agent():
    print("Session Recap Agent")
    print("=" * 40)
    print("Generating a recap of your most recent session...\n")

    messages = [
        {
            "role": "system",
            "content": (
                "You are a TTRPG session recap writer. Use the available tools to: "
                "1) List the user's campaigns, "
                "2) Find the most recent session, "
                "3) Get full session details including beats and moments, "
                "4) Get the character roster. "
                "Then write an engaging narrative recap of the session. "
                "Include character names, key events, memorable moments, and plot developments. "
                "Write in past tense, third person."
            ),
        },
        {
            "role": "user",
            "content": "Generate a recap of my most recent session.",
        },
    ]

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
                print(f"  Calling {tool_call.function.name}({arguments})")
                result = call_archivist(tool_call.function.name, arguments)
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result,
                    }
                )
        else:
            print("\n" + message.content)
            break


if __name__ == "__main__":
    if not ARCHIVIST_API_KEY:
        print("Set ARCHIVIST_API_KEY environment variable.")
        print("Get your key at: https://app.myarchivist.ai/profile?section=dev")
        exit(1)
    run_recap_agent()
