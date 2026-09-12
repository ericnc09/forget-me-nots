# Forget-me-nots Assistant

This proof of concept exposes one Google ADK assistant through both the web UI
and CopilotKit Intelligence Channels such as Slack.

```text
Web UI ─┐
        ├─> CopilotKit runtime ─> AG-UI endpoint ─> ADK assistant
Slack ──┘
```

## Setup

Requirements: Node.js 22+, Python 3.10+, and a Google API key.

```bash
npm install
cd agents
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd ..
cp .env.example .env
```

Set `GOOGLE_API_KEY` in `.env`. The default model and agent port can be
overridden with `ORCHESTRATOR_MODEL` and `ORCHESTRATOR_PORT`.

## Run the web app

```bash
npm run dev
```

This starts the Next.js UI and the single ADK agent:

- UI: `http://localhost:3000`
- Agent: `http://localhost:9000`

## Run Slack Channels

Configure `CPK_INTELLIGENCE_API_KEY` and declare the Channel with the
CopilotKit CLI. Then run:

```bash
npm run channel
```

The Channel creates one agent thread per conversation and uses the same ADK
agent endpoint as the web runtime.

## Useful commands

```bash
npm run build
npm run typecheck:channel
npm run smoke:agent
```

The smoke test makes a real model request and requires the agent to be running.
