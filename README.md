# Forget-me-nots

A Slack agent prototype for the **Agents, Everywhere** hackathon. The current runnable app is [apps/forgetme-nots](apps/forgetme-nots/README.md). It connects a Google ADK orchestrator to LangGraph/OpenAI research and Google ADK analysis agents through A2A and CopilotKit Channels.

The current build is a research starter with setup and compatibility fixes. The FollowThrough task tracking, reminders, Teams, and Outlook draft workflows in [the planning documents](docs/planning/README.md) are proposed work, not implemented capabilities. Running or renaming a starter alone does not establish a new hackathon submission.

## Get started

Use Node.js 22+ and Python 3.10+. The active app has a separate Node install from the inherited kit to preserve its tested dependency pair.

```bash
git clone https://github.com/ericnc09/forget-me-nots.git
cd forget-me-nots
npm ci
npm --prefix apps/forgetme-nots ci
cd apps/forgetme-nots
python3 -m venv agents/.venv
agents/.venv/bin/python -m pip install -r agents/requirements.txt
cp .env.example .env
```

Set `GOOGLE_API_KEY`, `OPENAI_API_KEY`, and `CPK_INTELLIGENCE_API_KEY` in `apps/forgetme-nots/.env`. Use a project-scoped CopilotKit key for the project containing the declared Channel `forgetme-nots`. Managed provider credentials remain in CopilotKit Intelligence. Never commit actual credentials. Existing configured users should preserve their `.env` instead of copying the example over it.

From the repository root, use two terminals:

```bash
# Terminal 1: UI and three Python agent services
npm run dev:forgetme-nots
```

```bash
# Terminal 2: long-running managed Slack listener
npm run channel:forgetme-nots
```

The listener should report `Channel "forgetme-nots" is online.` The UI is at `http://localhost:3000`; the orchestrator, research, and analysis services use ports 9000, 9001, and 9002. The inherited web template uses port 3100 and is a separate app.

Invite the app in your Slack test channel, then select it from the mention dropdown:

```text
/invite @forgetme-nots
@forgetme-nots hello
```

Keep both processes running. Press Ctrl+C in each terminal to stop them. The current scaffold binds its development servers to all interfaces; use a trusted development environment. Its web identity is a demo stub and has not been validated for multiple users or production.

## CopilotKit onboarding

The tracked `apps/forgetme-nots/.copilotkit/channels.json` declares the Channel and credential variable names, not secret values. A fresh clone still requires sign-in, hosted project selection, and a Slack app attachment for an account you control. Follow the installed [Channels setup skill](.agents/skills/channels-setup/SKILL.md) and the current [official guide](https://copilotkit.ai/channels-guide.md). Creating the Slack app, running the model services, and connecting the listener are separate steps.

For the inherited kit's selected app workflow, see [starter onboarding](STARTER-KIT.md#copilotkit-onboarding). The inherited listener reads `INTELLIGENCE_API_KEY`; the active generated app reads `CPK_INTELLIGENCE_API_KEY`. Their environment files are separate.

## Verification

After both Node installs:

```bash
npm run verify
```

This runs the inherited workspace typechecks and offline tests, the active app's channel typecheck, and Python syntax checks. It does not prove model credentials or Slack delivery.

With the agent services running, an opt-in model test is available:

```bash
cd apps/forgetme-nots
npm run smoke:agent
```

It sends a synthetic greeting through the same agent factory used by Slack, makes a real model call, and fails on an error or empty response. Full research/analysis delegation and a successful Slack reply after the model fix still need live verification. See [validation evidence](docs/VALIDATION.md).

## Repository map

| Path | What it contains |
| --- | --- |
| `apps/forgetme-nots/` | Active generated Slack/A2A app, compatibility fixes, and Gemini model configuration |
| `apps/channel/`, `apps/web/`, `apps/mobile/`, `packages/` | Inherited CopilotKit hackathon templates and tests |
| `tools/exa-search/` | Standalone Python Exa retrieval helper; not registered as a tool in the active app |
| `docs/planning/` | FollowThrough brief, competitor notes, and Toronto planning; proposed functionality |
| `dev-docs/scaffolds/forgetme-not/` | Earlier singular-name scaffold, retained as reference; not the active listener |
| `STARTER-KIT.md` | Maintained starter kit instructions and sponsor references |

Before development, read [AGENTS.md](AGENTS.md), [hackathon-overview.md](hackathon-overview.md), [hackathon-rules.md](hackathon-rules.md), [using-sponsor-tools.md](using-sponsor-tools.md), and the [Channels API skill](.agents/skills/build-channels-agent/SKILL.md). [SUBMISSION.md](SUBMISSION.md) records inherited work and outstanding deliverables. Do not claim planned integrations or untested outcomes as implemented.
