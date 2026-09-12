"""
Analysis Agent - Analyzes research findings using ADK + Gemini.
Exposes A2A Protocol endpoint, returns structured JSON.
"""

import uvicorn
import os
import json
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message
from google.adk.agents.llm_agent import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.memory.in_memory_memory_service import InMemoryMemoryService
from google.adk.artifacts import InMemoryArtifactService
from google.genai import types


class InsightItem(BaseModel):
    title: str = Field(description="Title of the insight")
    description: str = Field(description="Detailed description of the insight")
    importance: str = Field(description="Why this insight matters")


class StructuredAnalysis(BaseModel):
    topic: str = Field(description="The topic being analyzed")
    overview: str = Field(description="Brief overview of the analysis")
    insights: List[InsightItem] = Field(description="List of key insights")
    conclusion: str = Field(description="Concluding thoughts")


class AnalysisAgent:
    def __init__(self):
        self._agent = self._build_agent()
        self._user_id = "remote_agent"
        self._runner = Runner(
            app_name=self._agent.name,
            agent=self._agent,
            artifact_service=InMemoryArtifactService(),
            session_service=InMemorySessionService(),
            memory_service=InMemoryMemoryService(),
        )

    def _build_agent(self) -> LlmAgent:
        model_name = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")
        return LlmAgent(
            model=model_name,
            name="WILO_agent",
            description="An agent that helps the user pick up work exactly where they left off",
            instruction="""
You are a Project Manager agent designed to help the user pick up work exactly where they left off without needing to review old files or context.

CORE GOAL:
Synthesize project history and recent chat discussions into a clear, structured "Where I Left Off" (WILO) status report.

INPUT SOURCES:
- Project Context: Read `progress.md` for the specified project (Note: standard input for now; future iterations will connect via Google Drive).
- Priority Context: Inspect recent messages from @forgetme-nots (C0C0Z04F15M) Slack channel to identify ad-hoc requests, recent activity, and shifting priorities.

WORKFLOW:
1. Identify Target Project:
   - If the user specifies a project name, retrieve its `progress.md` and check the corresponding Slack channel.
   - If the request is ambiguous or vague (e.g., "What should I work on?"):
     a. Inspect recent Slack channel logs first to determine active project context.
     b. If still ambiguous, list all open projects with their last modified dates and ask the user which project they want a WILO for.

2. Synthesize Context:
   - Extract previous state from `progress.md`.
   - Cross-reference with Slack channel conversations to extract updated status, completed items, and new ad-hoc action items.

3. Output Format (STRICT ORDER REQUIRED):
   Always format the final response using this structure:

   WILO
   [Project Name]
   last modified: [Date]

   - [Bullet points summarizing recent work done, branches, investigations, etc.]

   plan:
   [Summary of current overall plan/direction]

   TODO:
   - [Item] - [done / in progress / pending]
   - [Item]

   Next:
   - [Immediate next action item 1]
   - [Immediate next action item 2]

CONSTRAINTS:
- Read-Only: Do not attempt to update files or write back to `progress.md`.
- Keep descriptions clear and detailed enough so the user does not need to re-read project documentation.
            """,
            tools=[],
        )

    async def invoke(self, query: str, session_id: str) -> str:
        """Generate analysis and return JSON string."""
        session = await self._runner.session_service.get_session(
            app_name=self._agent.name,
            user_id=self._user_id,
            session_id=session_id,
        )

        content = types.Content(role="user", parts=[types.Part.from_text(text=query)])

        if session is None:
            session = await self._runner.session_service.create_session(
                app_name=self._agent.name,
                user_id=self._user_id,
                state={},
                session_id=session_id,
            )

        response_text = ""
        async for event in self._runner.run_async(
            user_id=self._user_id, session_id=session.id, new_message=content
        ):
            if event.is_final_response():
                if (
                    event.content
                    and event.content.parts
                    and event.content.parts[0].text
                ):
                    response_text = "\n".join(
                        [p.text for p in event.content.parts if p.text]
                    )
                break

        content_str = response_text.strip()

        if "```json" in content_str:
            content_str = content_str.split("```json")[1].split("```")[0].strip()
        elif "```" in content_str:
            content_str = content_str.split("```")[1].split("```")[0].strip()

        try:
            structured_data = json.loads(content_str)
            validated_analysis = StructuredAnalysis(**structured_data)
            final_response = json.dumps(validated_analysis.model_dump(), indent=2)
            print("✅ Successfully created structured analysis")
            return final_response
        except json.JSONDecodeError as e:
            print(f"❌ JSON parsing error: {e}")
            print(f"Content: {content_str}")
            return json.dumps(
                {
                    "error": "Failed to generate structured analysis",
                    "raw_content": content_str[:200],
                }
            )
        except Exception as e:
            print(f"❌ Validation error: {e}")
            return json.dumps({"error": f"Validation failed: {str(e)}"})


# A2A Protocol executor wraps the ADK agent
class AnalysisAgentExecutor(AgentExecutor):
    def __init__(self):
        self.agent = AnalysisAgent()

    async def execute(
        self,
        context: RequestContext,
        event_queue: EventQueue,
    ) -> None:
        query = context.get_user_input()
        session_id = getattr(context, "context_id", "default_session")
        final_content = await self.agent.invoke(query, session_id)
        await event_queue.enqueue_event(new_agent_text_message(final_content))

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        raise Exception("cancel not supported")


port = int(os.getenv("ANALYSIS_PORT", 9002))

skill = AgentSkill(
    id="analysis_agent",
    name="Analysis Agent",
    description="Analyzes research findings and provides meaningful insights using ADK",
    tags=["research", "analysis", "insights", "adk"],
    examples=[
        "Analyze this research about quantum computing",
        "What are the key insights from this data?",
        "Provide analysis of these research findings",
    ],
)

public_agent_card = AgentCard(
    name="Analysis Agent",
    description="ADK-powered agent that analyzes research findings and provides meaningful insights",
    url=f"http://localhost:{port}/",
    version="1.0.0",
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    capabilities=AgentCapabilities(streaming=True),
    skills=[skill],
    supportsAuthenticatedExtendedCard=False,
)


def main():
    if not os.getenv("GOOGLE_API_KEY") and not os.getenv("GEMINI_API_KEY"):
        print("⚠️  Warning: No API key found!")
        print("   Set GOOGLE_API_KEY or GEMINI_API_KEY")
        print("   Get a key from: https://aistudio.google.com/app/apikey")
        print()

    request_handler = DefaultRequestHandler(
        agent_executor=AnalysisAgentExecutor(),
        task_store=InMemoryTaskStore(),
    )

    server = A2AStarletteApplication(
        agent_card=public_agent_card,
        http_handler=request_handler,
        extended_agent_card=public_agent_card,
    )

    print(f"💡 Starting Analysis Agent (ADK + A2A) on http://localhost:{port}")
    print(f"   Agent: {public_agent_card.name}")
    print(f"   Description: {public_agent_card.description}")
    uvicorn.run(server.build(), host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
