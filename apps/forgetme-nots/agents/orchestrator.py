"""Single Forget-me-nots assistant exposed through AG-UI."""

from __future__ import annotations

from dotenv import load_dotenv

load_dotenv()

import os
import uvicorn
from fastapi import FastAPI
from ag_ui_adk import ADKAgent, add_adk_fastapi_endpoint
from google.adk.agents import LlmAgent

orchestrator_agent = LlmAgent(
    name="ForgetMeNotsAssistant",
    model=os.getenv("ORCHESTRATOR_MODEL", "gemini-3.6-flash"),
    instruction="""
    You are the Forget-me-nots assistant. Help the user pick up work exactly where
    they left off without requiring them to reconstruct old context.

    Be concise, practical, and transparent about what you know. When the user asks
    about ongoing work, summarize the relevant context, distinguish completed work
    from open work, and identify the next useful action. When the request is
    ambiguous, ask one focused clarifying question instead of guessing.

    Do not claim to have access to systems, files, conversations, or integrations
    that are not present in the current conversation. Do not invent status,
    deadlines, owners, or completed work.

    Prefer a short answer with clear next steps. Use headings or bullets only when
    they make the answer easier to scan.
    """,
)

# Wrap with AG-UI middleware to expose via AG-UI Protocol
adk_orchestrator_agent = ADKAgent(
    adk_agent=orchestrator_agent,
    app_name="orchestrator_app",
    user_id="demo_user",
    session_timeout_seconds=3600,
    use_in_memory_services=True,
)

app = FastAPI(title="Forget-me-nots Assistant (ADK + AG-UI)")
add_adk_fastapi_endpoint(app, adk_orchestrator_agent, path="/")

if __name__ == "__main__":
    if not os.getenv("GOOGLE_API_KEY"):
        print("⚠️  Warning: GOOGLE_API_KEY not set!")
        print("   Set it with: export GOOGLE_API_KEY='your-key-here'")
        print("   Get a key from: https://aistudio.google.com/app/apikey")
        print()

    port = int(os.getenv("ORCHESTRATOR_PORT", 9000))
    print(f"🚀 Starting Orchestrator Agent (ADK + AG-UI) on http://localhost:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
