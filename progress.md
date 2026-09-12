# Forget-me-nots — progress

Files in this repository are the source of truth; this file is the live index and handoff. It also records the confirmed skeleton for a separate progress context for each Slack user.

## HANDOFF (for a fresh session — read this first)

### Where we are

Forget-me-nots is a CopilotKit Slack / Channels proof of concept using one Google ADK assistant for Slack and web. The user explicitly requested fixing the runtime to match commit `813e46b`, which removed specialized research/analysis agents and A2A routing. The merged source baseline is `6b7ea4d` on `jerel/app-layout-cleanup`; the canonical local Git checkout is on `codex/run-single-agent`, tracking that remote branch. Root verification now compiles only the remaining assistant, and generated preflight no longer requires the removed OpenAI research backend. Clean Node/Python installs, dependency consistency, assistant initialization, and root verification passed. Runtime replacement, production build, and a 50-character single-agent greeting passed; the managed Slack listener is online. Ports 9001/9002 are unused and no research/analysis processes remain. Current observations are in `docs/VALIDATION.md`. Earlier 93-test/build/greeting evidence remains historical. Successful real Slack responses, subscription/silence behavior, hosted web thread operations, and per-user progress storage remain unverified. The user confirmed one progress skeleton with distinct context for every Slack user. This root file is the shared development handoff, not a private user's deployed record. No per-user progress persistence, retrieval, updating, or access enforcement is implemented. Next: verify a real Slack interaction, then align and confirm the per-user identity/storage/update contract. Source event dates are 2026-09-12–2026-09-13; the applicable local deadline and build-window confirmation are TBD.

Canonical repository: `/Users/eric/Documents/ChatGPT/planned projects/forget-me-nots`; active runtime directory: `apps/forgetme-nots`. The original `/Users/eric/Documents/ChatGPT/planned projects/forgetme-nots` path now aliases the canonical active app, so commands using that path load the single assistant. The obsolete standalone code is preserved at `/Users/eric/Documents/ChatGPT/planned projects/forgetme-nots-pre-single-agent-backup`; do not run that backup. Its private environment was preserved in the canonical app and remains ignored by Git. The inherited `/Users/eric/Documents/ChatGPT/planned projects/agents-everywhere-starter-kit` checkout remains on `main`; it is not the active app. Inspect actual process state before starting duplicate services.

### Parked / not yet confirmed

- FollowThrough as the product direction and final product name; PM/delivery-lead as the target persona. The current confirmed working app name is `forgetme-nots`.
- Teams/Outlook as the intended replacement or additional surface. Slack is the confirmed surface.
- Automatic private Outlook drafts, draft-only architecture, SQLite task tracking, reminders, task lifecycle, two-week review, and the benchmark/quality targets prescribed by the planning prompt.
- Microsoft 365 test tenant availability, actual grants, mailbox/chat access, and participant identities.
- Connecting the standalone Exa helper to the active agent.
- Permanent model/provider choices. Current defaults and pins are observed implementation facts.
- Whether a Slack user's context is scoped per project, channel, workspace, or some combination; which authenticated identifiers form the key; how to handle one user in several channels/workspaces.
- Storage backend, physical file paths, retention, deletion, backup, and access boundaries for user-specific records. The approved logical filename does not select a physical storage design.
- Who can read or edit a user's record, whether/how users share progress, project ownership, onboarding, migration, and channel-visible output.
- Commands/triggers for generating a record, updating progress, confirming decisions, and showing diffs in Slack; whether the document skill is ever invoked by the runtime.
- Proposed sequence after the authorized runtime fix: successful real Slack greeting → propose user identity and record lifecycle → align → obtain confirmation → implement one vertical slice. This does not lock the unresolved architecture.
- Eligibility, exact submission deadline, final domain workflow, user evaluation, video, and social submission.

### To resume (do exactly this)

1. Read this file in full. Check `git status --short --branch` and compare current files to the recorded commits; repository facts take precedence over a stale handoff. Preserve existing edits.
2. Read `README.md`, `AGENTS.md`, `hackathon-overview.md`, `hackathon-rules.md`, and `using-sponsor-tools.md`, in that order.
3. Read `apps/forgetme-nots/AGENTS.md`, `apps/forgetme-nots/README.md`, `.agents/skills/build-channels-agent/SKILL.md`, then its identity/adapter and approval references when needed.
4. Read `docs/VALIDATION.md`, `apps/forgetme-nots/channels.mts`, `channel-host.mts`, and `app/agent.ts`. Identify verified platform identity APIs. A conversation thread ID alone does not demonstrate a user's private progress boundary.
5. Read `docs/planning/README.md`, the consolidated build prompt, competitor notes, and Toronto brief as proposed reference material. Their imperative wording does not confirm a platform migration or start that build.
6. Inspect local configuration without displaying secrets, and check ports 3000/9000 before starting; ports 9001/9002 must remain unused by this app. For the configured active app, root commands are `npm run dev:forgetme-nots` and, in a separate terminal, `npm run channel:forgetme-nots`. A clean checkout needs both Node installs, the Python environment, and its own private credentials as documented in README.
7. Propose a bounded real Slack delivery check and a per-user progress contract covering authenticated identity, project scope, ownership, persistence, retrieval, confirmation, and update/diff behavior. Align with the user, then explicitly confirm unresolved choices before recording them as locked. Do not send messages to other people without explicit authorization.
8. After confirmation, implement and verify the smallest relevant vertical slice. Keep verified results distinct from user acceptance. Update this handoff using the house rules; do not mark planned product behavior as implemented.

### Locked decisions

Earlier explicit user instructions below are preserved from supplied notes; their individual confirmation dates are unavailable and marked TBD rather than invented.

- Date TBD — Platform: use CopilotKit for the project.
- Date TBD — Surface: select the Slack / Channels agent.
- Date TBD — App: use the user-created `forgetme-nots`; starting and connecting the app was explicitly authorized.
- Date TBD — Repository: sync existing work to `ericnc09/forget-me-nots` and follow the five supplied hackathon/convention/Channels references.
- 2026-09-12 — Runtime: use the single ADK assistant from commit `813e46b`; remove the old research/analysis services and A2A route from the running app.
- 2026-09-12 — Step 3a: create a single standalone `progress.md` at this repository root using the approved structure; do not install it inside agents.
- 2026-09-12 — Step 3b: the progress skeleton is shared, but each Slack user's progress context must be different. Storage, access policy, and implementation are not selected.
- 2026-09-12 — Change evidence: use per-file historical summaries and exact Git diff references, with compact embedded patches for subsequent changes.
- 2026-09-12 — Checkpoint scope: leave File Changes untouched unless separately authorized.

### House rules

- Files are the source of truth. Write durable facts, never a conversation narrative. Verify implementation claims against source and dated evidence.
- Lock only explicitly confirmed decisions. Keep recommendations, assumptions, and unconfirmed source-document prescriptions in Parked. Unknown facts and unknown confirmation dates are TBD.
- Use absolute dates, plain Markdown, no HTML, and the section order in this document.
- This is a standalone document/skill specification; do not install or copy it into agent skill directories or change agent system prompts.
- Every user's instantiated record uses this structure and that user's own confirmed project context. Do not populate another user's document with Eric's project, private settings, or decisions. Owner/project identifiers, source folder, files, state, and deadline start as TBD until sourced or supplied.
- Per-user separation is a requirement, not a claim of implemented authorization. Channel membership and the existing thread-based factory do not by themselves establish record ownership or sharing consent. Keep per-user records and credentials out of the public development repository.
- Propose → align → confirm unresolved scope and architecture; continue already authorized independent work. A go-ahead for this document does not authorize unrelated feature implementation or contacting colleagues.
- Preserve dependency pairs, isolated agent runs, and the existing active app. Read actual Channels APIs before extending behavior.
- Separate inherited code, verified setup, original event work, and future features. Do not claim eligibility, user feedback, or demo readiness without evidence.
- On “checkpoint” or “update progress”: rewrite HANDOFF; update Steps and File map; add newly locked entries above existing Decision log entries without editing/deleting old entries; remove confirmed items from Parked. Change no other section, including this instruction, the design briefing, and File Changes, unless separately authorized. Show the resulting diff.
- For separately authorized file-change logging: summarize each touched source file and retain an exact baseline/result Git diff reference; use compact relevant patches for new changes. Do not fabricate missing pre-Git history or log secrets.

## File map

Paths below are relative to the repository root. One row covers each tracked real file or tracked alias plus this new document. Ignored dependencies, build output, provider artifacts, private environments, and external original source folders are not repository source files and are not enumerated here. A listed test or demo asset is not evidence of a new user's workflow.

| File | Holds | State |
| --- | --- | --- |
| `.agents/skills/README.md` | Documentation / reference: README.md | Existing setup / API reference; progress skill not installed |
| `.agents/skills/build-channels-agent/SKILL.md` | Documentation / reference: SKILL.md | Existing setup / API reference; progress skill not installed |
| `.agents/skills/build-channels-agent/evals/evals.json` | Channels skill instructions, API reference, or evaluation data | Existing setup / API reference; progress skill not installed |
| `.agents/skills/build-channels-agent/references/adapter-authoring.md` | Documentation / reference: adapter-authoring.md | Existing setup / API reference; progress skill not installed |
| `.agents/skills/build-channels-agent/references/hitl-patterns.md` | Documentation / reference: hitl-patterns.md | Existing setup / API reference; progress skill not installed |
| `.agents/skills/build-channels-agent/references/ui-components.md` | Documentation / reference: ui-components.md | Existing setup / API reference; progress skill not installed |
| `.agents/skills/channels-setup/SKILL.md` | Documentation / reference: SKILL.md | Existing setup / API reference; progress skill not installed |
| `.claude/skills` | Skill directory alias | Existing setup / API reference; progress skill not installed |
| `.cursor/skills` | Skill directory alias | Existing setup / API reference; progress skill not installed |
| `.env.example` | Placeholder configuration; no real credentials | Tracked project guidance / configuration |
| `.gitignore` | Version-control exclusions | Tracked project guidance / configuration |
| `.mcp.json` | Build, runtime, or tool configuration | Tracked project guidance / configuration |
| `.nvmrc` | Build, runtime, or tool configuration | Tracked project guidance / configuration |
| `AGENTS.md` | Repository conventions and required checks | Tracked project guidance / configuration |
| `LICENSE` | Inherited license and attribution | Tracked project guidance / configuration |
| `README.md` | Current project quickstart and capability boundaries | Tracked project guidance / configuration |
| `STARTER-KIT.md` | Preserved starter instructions | Tracked project guidance / configuration |
| `SUBMISSION.md` | Inherited-work disclosure and deliverable checklist | Tracked project guidance / configuration |
| `apps/channel/README.md` | Documentation / reference: README.md | Inherited reference |
| `apps/channel/package.json` | Package metadata, dependencies, and commands | Inherited reference |
| `apps/channel/src/agent-factory.test.tsx` | Inherited or reference test: agent-factory.test.tsx | Inherited reference |
| `apps/channel/src/agent.ts` | Implementation source: agent.ts | Inherited reference |
| `apps/channel/src/channel.tsx` | UI or Channels component source: channel.tsx | Inherited reference |
| `apps/channel/src/components.test.tsx` | Inherited or reference test: components.test.tsx | Inherited reference |
| `apps/channel/src/components.tsx` | UI or Channels component source: components.tsx | Inherited reference |
| `apps/channel/src/delivery.test.tsx` | Inherited or reference test: delivery.test.tsx | Inherited reference |
| `apps/channel/src/env.ts` | Implementation source: env.ts | Inherited reference |
| `apps/channel/src/search.test.tsx` | Inherited or reference test: search.test.tsx | Inherited reference |
| `apps/channel/src/search.tsx` | UI or Channels component source: search.tsx | Inherited reference |
| `apps/channel/src/server.ts` | Implementation source: server.ts | Inherited reference |
| `apps/channel/src/testing/managed-gateway.ts` | Implementation source: managed-gateway.ts | Inherited reference |
| `apps/channel/src/tools.test.tsx` | Inherited or reference test: tools.test.tsx | Inherited reference |
| `apps/channel/src/tools.tsx` | UI or Channels component source: tools.tsx | Inherited reference |
| `apps/channel/tsconfig.json` | Build, runtime, or tool configuration | Inherited reference |
| `apps/forgetme-nots/.copilotkit/channels.json` | Tracked Channel declaration; no secret values | Active prototype; per-user progress absent |
| `apps/forgetme-nots/.env.example` | Placeholder configuration; no real credentials | Active prototype; per-user progress absent |
| `apps/forgetme-nots/.gitignore` | Version-control exclusions | Active prototype; per-user progress absent |
| `apps/forgetme-nots/AGENTS.md` | App-specific editing and verification guidance | Active prototype; per-user progress absent |
| `apps/forgetme-nots/README.md` | Documentation / reference: README.md | Active prototype; per-user progress absent |
| `apps/forgetme-nots/agents/orchestrator.py` | Single Google ADK assistant and AG-UI service | Active prototype; per-user progress absent |
| `apps/forgetme-nots/agents/requirements.txt` | Pinned single-assistant Python dependencies | Active prototype; per-user progress absent |
| `apps/forgetme-nots/app/agent.ts` | Single HttpAgent factory for Slack/web | Active prototype; per-user progress absent |
| `apps/forgetme-nots/app/api/copilotkit/[[...slug]]/route.ts` | Implementation source: route.ts | Active prototype; per-user progress absent |
| `apps/forgetme-nots/app/globals.css` | UI styling: globals.css | Active prototype; per-user progress absent |
| `apps/forgetme-nots/app/layout.tsx` | UI or Channels component source: layout.tsx | Active prototype; per-user progress absent |
| `apps/forgetme-nots/app/page.module.css` | UI styling: page.module.css | Active prototype; per-user progress absent |
| `apps/forgetme-nots/app/page.tsx` | UI or Channels component source: page.tsx | Active prototype; per-user progress absent |
| `apps/forgetme-nots/channel-host.mts` | Managed listener lifecycle | Active prototype; per-user progress absent |
| `apps/forgetme-nots/channels.mts` | Channel declaration, platform identity, and message handler | Active prototype; per-user progress absent |
| `apps/forgetme-nots/components/chat.tsx` | UI or Channels component source: chat.tsx | Active prototype; per-user progress absent |
| `apps/forgetme-nots/demo.png` | Inherited/reference image, logo, or demo asset | Active prototype; per-user progress absent |
| `apps/forgetme-nots/next.config.ts` | Build, runtime, or tool configuration | Active prototype; per-user progress absent |
| `apps/forgetme-nots/package-lock.json` | Dependency or installed-skill lock record | Active prototype; per-user progress absent |
| `apps/forgetme-nots/package.json` | Package metadata, dependencies, and commands | Active prototype; per-user progress absent |
| `apps/forgetme-nots/postcss.config.mjs` | Build, runtime, or tool configuration | Active prototype; per-user progress absent |
| `apps/forgetme-nots/scripts/copilotkit-dev-infra.mjs` | Startup, setup, or verification script: copilotkit-dev-infra.mjs | Active prototype; per-user progress absent |
| `apps/forgetme-nots/scripts/smoke-agent.mts` | Opt-in synthetic greeting through actual agent factory | Active prototype; per-user progress absent |
| `apps/forgetme-nots/tailwind.config.ts` | Build, runtime, or tool configuration | Active prototype; per-user progress absent |
| `apps/forgetme-nots/tsconfig.channel.json` | Build, runtime, or tool configuration | Active prototype; per-user progress absent |
| `apps/forgetme-nots/tsconfig.json` | Build, runtime, or tool configuration | Active prototype; per-user progress absent |
| `apps/mobile/.env.example` | Placeholder configuration; no real credentials | Inherited reference |
| `apps/mobile/App.tsx` | UI or Channels component source: App.tsx | Inherited reference |
| `apps/mobile/README.md` | Documentation / reference: README.md | Inherited reference |
| `apps/mobile/app.json` | Build, runtime, or tool configuration | Inherited reference |
| `apps/mobile/index.js` | Implementation source: index.js | Inherited reference |
| `apps/mobile/metro.config.js` | Build, runtime, or tool configuration | Inherited reference |
| `apps/mobile/package-lock.json` | Dependency or installed-skill lock record | Inherited reference |
| `apps/mobile/package.json` | Package metadata, dependencies, and commands | Inherited reference |
| `apps/mobile/src/assistant-links.ts` | Implementation source: assistant-links.ts | Inherited reference |
| `apps/mobile/src/assistant-markdown.tsx` | UI or Channels component source: assistant-markdown.tsx | Inherited reference |
| `apps/mobile/src/chat.tsx` | UI or Channels component source: chat.tsx | Inherited reference |
| `apps/mobile/src/config.ts` | Implementation source: config.ts | Inherited reference |
| `apps/mobile/src/finance.ts` | Implementation source: finance.ts | Inherited reference |
| `apps/mobile/src/message-id.ts` | Implementation source: message-id.ts | Inherited reference |
| `apps/mobile/src/styles.ts` | Implementation source: styles.ts | Inherited reference |
| `apps/mobile/src/tools.tsx` | UI or Channels component source: tools.tsx | Inherited reference |
| `apps/mobile/test/assistant-markdown.test.ts` | Inherited or reference test: assistant-markdown.test.ts | Inherited reference |
| `apps/mobile/test/currency.test.ts` | Inherited or reference test: currency.test.ts | Inherited reference |
| `apps/mobile/test/finance.test.ts` | Inherited or reference test: finance.test.ts | Inherited reference |
| `apps/mobile/test/message-id.test.ts` | Inherited or reference test: message-id.test.ts | Inherited reference |
| `apps/mobile/test/spending-summary.test.ts` | Inherited or reference test: spending-summary.test.ts | Inherited reference |
| `apps/mobile/tsconfig.json` | Build, runtime, or tool configuration | Inherited reference |
| `apps/web/README.md` | Documentation / reference: README.md | Inherited reference |
| `apps/web/next.config.ts` | Build, runtime, or tool configuration | Inherited reference |
| `apps/web/package.json` | Package metadata, dependencies, and commands | Inherited reference |
| `apps/web/scripts/check-workplace.ts` | Startup, setup, or verification script: check-workplace.ts | Inherited reference |
| `apps/web/src/app/api/copilotkit/[[...path]]/route.ts` | Implementation source: route.ts | Inherited reference |
| `apps/web/src/app/api/followups/route.ts` | Implementation source: route.ts | Inherited reference |
| `apps/web/src/app/api/mobile-copilotkit/[[...path]]/route.ts` | Implementation source: route.ts | Inherited reference |
| `apps/web/src/app/api/realtime-token/route.ts` | Implementation source: route.ts | Inherited reference |
| `apps/web/src/app/api/search/route.ts` | Implementation source: route.ts | Inherited reference |
| `apps/web/src/app/globals.css` | UI styling: globals.css | Inherited reference |
| `apps/web/src/app/layout.tsx` | UI or Channels component source: layout.tsx | Inherited reference |
| `apps/web/src/app/page.tsx` | UI or Channels component source: page.tsx | Inherited reference |
| `apps/web/src/app/voice/page.tsx` | UI or Channels component source: page.tsx | Inherited reference |
| `apps/web/src/components/app-control.tsx` | UI or Channels component source: app-control.tsx | Inherited reference |
| `apps/web/src/components/generative-ui.tsx` | UI or Channels component source: generative-ui.tsx | Inherited reference |
| `apps/web/src/components/providers.tsx` | UI or Channels component source: providers.tsx | Inherited reference |
| `apps/web/src/components/streamed-cards.test.ts` | Inherited or reference test: streamed-cards.test.ts | Inherited reference |
| `apps/web/src/components/streamed-cards.tsx` | UI or Channels component source: streamed-cards.tsx | Inherited reference |
| `apps/web/src/components/workplace-followups.tsx` | UI or Channels component source: workplace-followups.tsx | Inherited reference |
| `apps/web/src/lib/followup-client.test.ts` | Inherited or reference test: followup-client.test.ts | Inherited reference |
| `apps/web/src/lib/followup-client.ts` | Implementation source: followup-client.ts | Inherited reference |
| `apps/web/src/lib/followup-types.ts` | Implementation source: followup-types.ts | Inherited reference |
| `apps/web/src/lib/incidents.test.ts` | Inherited or reference test: incidents.test.ts | Inherited reference |
| `apps/web/src/lib/incidents.ts` | Implementation source: incidents.ts | Inherited reference |
| `apps/web/src/lib/realtime-config.ts` | Implementation source: realtime-config.ts | Inherited reference |
| `apps/web/src/lib/server/followup-error.ts` | Implementation source: followup-error.ts | Inherited reference |
| `apps/web/src/lib/server/followup-http.test.ts` | Inherited or reference test: followup-http.test.ts | Inherited reference |
| `apps/web/src/lib/server/followup-http.ts` | Implementation source: followup-http.ts | Inherited reference |
| `apps/web/src/lib/server/followups.test.ts` | Inherited or reference test: followups.test.ts | Inherited reference |
| `apps/web/src/lib/server/followups.ts` | Implementation source: followups.ts | Inherited reference |
| `apps/web/src/lib/server/workplace.test.ts` | Inherited or reference test: workplace.test.ts | Inherited reference |
| `apps/web/src/lib/server/workplace.ts` | Implementation source: workplace.ts | Inherited reference |
| `apps/web/src/lib/use-workplace.ts` | Implementation source: use-workplace.ts | Inherited reference |
| `apps/web/tsconfig.json` | Build, runtime, or tool configuration | Inherited reference |
| `assets/banner.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `assets/banner.svg` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `assets/copilotkit-logo-full.svg` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `assets/demos/mobile.gif` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `assets/demos/mobile.mp4` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `assets/demos/slack.gif` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `assets/demos/slack.mp4` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `assets/demos/web.gif` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `assets/demos/web.mp4` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `assets/sponsors/ambiguous.svg` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `assets/sponsors/auth0.svg` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `assets/sponsors/exa.svg` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `assets/sponsors/openai.svg` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `assets/sponsors/openrouter.svg` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `assets/verify.gif` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/README.md` | Documentation / reference: README.md | Inherited reference |
| `dev-docs/auth0/README.md` | Documentation / reference: README.md | Inherited reference |
| `dev-docs/auth0/client.mjs` | Implementation source: client.mjs | Inherited reference |
| `dev-docs/auth0/package-lock.json` | Dependency or installed-skill lock record | Inherited reference |
| `dev-docs/auth0/package.json` | Package metadata, dependencies, and commands | Inherited reference |
| `dev-docs/auth0/server.mjs` | Implementation source: server.mjs | Inherited reference |
| `dev-docs/auth0/test.mjs` | Inherited or reference test: test.mjs | Inherited reference |
| `dev-docs/channels-sdk-walkthrough/README.md` | Documentation / reference: README.md | Inherited reference |
| `dev-docs/channels-sdk-walkthrough/images/04-create-project.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/channels-sdk-walkthrough/images/06-channel-name-slack.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/channels-sdk-walkthrough/images/07-slack-setup-instructions.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/channels-sdk-walkthrough/images/10-slack-install-consent.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/channels-sdk-walkthrough/images/14-channel-online.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/channels-sdk-walkthrough/images/15-live-incident-card.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/channels-sdk-walkthrough/images/16-contextual-follow-up.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/channels.md` | Documentation / reference: channels.md | Inherited reference |
| `dev-docs/demo-prompts.md` | Documentation / reference: demo-prompts.md | Inherited reference |
| `dev-docs/deploy.md` | Documentation / reference: deploy.md | Inherited reference |
| `dev-docs/model-switching.md` | Documentation / reference: model-switching.md | Inherited reference |
| `dev-docs/scaffolds/forgetme-not/.copilotkit/channels.json` | Tracked Channel declaration; no secret values | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/.gitignore` | Version-control exclusions | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/AGENTS.md` | App-specific editing and verification guidance | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/LICENSE` | Inherited license and attribution | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/README.md` | Documentation / reference: README.md | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/agent/main.py` | Implementation source: main.py | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/agent/pyproject.toml` | Package metadata, dependencies, and commands | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/agent/src/__init__.py` | Implementation source: __init__.py | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/agent/src/a2ui/__init__.py` | Implementation source: __init__.py | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/agent/src/a2ui/schemas/__init__.py` | Implementation source: __init__.py | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/agent/src/a2ui/schemas/flight_schema.json` | Reference data or schema: flight_schema.json | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/agent/src/a2ui_dynamic_schema.py` | Implementation source: a2ui_dynamic_schema.py | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/agent/src/a2ui_fixed_schema.py` | Implementation source: a2ui_fixed_schema.py | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/agent/src/agent.py` | Implementation source: agent.py | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/agent/src/db.csv` | Reference data or schema: db.csv | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/agent/src/model.py` | Implementation source: model.py | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/agent/src/query.py` | Implementation source: query.py | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/agent/uv.lock` | Dependency or installed-skill lock record | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/channel-host.mts` | Implementation source: channel-host.mts | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/channels.mts` | Implementation source: channels.mts | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/entrypoint.sh` | Startup, setup, or verification script: entrypoint.sh | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/next.config.ts` | Build, runtime, or tool configuration | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/package-lock.json` | Dependency or installed-skill lock record | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/package.json` | Package metadata, dependencies, and commands | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/postcss.config.mjs` | Build, runtime, or tool configuration | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/public/copilotkit-logo-mark.svg` | Inherited/reference image, logo, or demo asset | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/public/copilotkit-logo.svg` | Inherited/reference image, logo, or demo asset | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/public/file.svg` | Inherited/reference image, logo, or demo asset | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/public/globe.svg` | Inherited/reference image, logo, or demo asset | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/public/next.svg` | Inherited/reference image, logo, or demo asset | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/public/vercel.svg` | Inherited/reference image, logo, or demo asset | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/public/window.svg` | Inherited/reference image, logo, or demo asset | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/scripts/copilotkit-dev-infra.mjs` | Startup, setup, or verification script: copilotkit-dev-infra.mjs | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/scripts/run-agent.bat` | Startup, setup, or verification script: run-agent.bat | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/scripts/run-agent.sh` | Startup, setup, or verification script: run-agent.sh | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/scripts/setup-agent.bat` | Startup, setup, or verification script: setup-agent.bat | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/scripts/setup-agent.sh` | Startup, setup, or verification script: setup-agent.sh | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/showcase.json` | Reference data or schema: showcase.json | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/agent.ts` | Implementation source: agent.ts | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/app/api/copilotkit/[[...slug]]/route.ts` | Implementation source: route.ts | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/app/declarative-generative-ui/definitions.ts` | Implementation source: definitions.ts | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/app/declarative-generative-ui/renderers.tsx` | UI or Channels component source: renderers.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/app/favicon.ico` | Inherited/reference image, logo, or demo asset | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/app/globals.css` | UI styling: globals.css | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/app/layout.tsx` | UI or Channels component source: layout.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/app/page.module.css` | UI styling: page.module.css | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/app/page.tsx` | UI or Channels component source: page.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/example-canvas/index.tsx` | UI or Channels component source: index.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/example-canvas/todo-card.tsx` | UI or Channels component source: todo-card.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/example-canvas/todo-column.tsx` | UI or Channels component source: todo-column.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/example-canvas/todo-list.tsx` | UI or Channels component source: todo-list.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/example-layout/index.tsx` | UI or Channels component source: index.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/example-layout/mode-toggle.tsx` | UI or Channels component source: mode-toggle.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/generative-ui/charts/bar-chart.tsx` | UI or Channels component source: bar-chart.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/generative-ui/charts/config.ts` | Implementation source: config.ts | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/generative-ui/charts/pie-chart.tsx` | UI or Channels component source: pie-chart.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/generative-ui/meeting-time-picker.tsx` | UI or Channels component source: meeting-time-picker.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/headless-chat.tsx` | UI or Channels component source: headless-chat.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/tool-rendering.tsx` | UI or Channels component source: tool-rendering.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/ui/badge.tsx` | UI or Channels component source: badge.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/ui/button.tsx` | UI or Channels component source: button.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/ui/card.tsx` | UI or Channels component source: card.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/ui/checkbox.tsx` | UI or Channels component source: checkbox.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/ui/input.tsx` | UI or Channels component source: input.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/ui/separator.tsx` | UI or Channels component source: separator.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/components/ui/spinner.tsx` | UI or Channels component source: spinner.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/hooks/index.ts` | Implementation source: index.ts | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/hooks/use-example-suggestions.tsx` | UI or Channels component source: use-example-suggestions.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/hooks/use-generative-ui-examples.tsx` | UI or Channels component source: use-generative-ui-examples.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/hooks/use-theme.tsx` | UI or Channels component source: use-theme.tsx | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/lib/a2ui-theme.css` | UI styling: a2ui-theme.css | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/src/lib/utils.ts` | Implementation source: utils.ts | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/tsconfig.channel.json` | Build, runtime, or tool configuration | Earlier scaffold; reference only |
| `dev-docs/scaffolds/forgetme-not/tsconfig.json` | Build, runtime, or tool configuration | Earlier scaffold; reference only |
| `dev-docs/setup.md` | Documentation / reference: setup.md | Inherited reference |
| `dev-docs/sponsors.md` | Documentation / reference: sponsors.md | Inherited reference |
| `dev-docs/surfaces.md` | Documentation / reference: surfaces.md | Inherited reference |
| `dev-docs/template-walkthroughs/mobile/README.md` | Documentation / reference: README.md | Inherited reference |
| `dev-docs/template-walkthroughs/mobile/images/01-start.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/template-walkthroughs/mobile/images/02-account-card.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/template-walkthroughs/mobile/images/03-approve-expense.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/template-walkthroughs/mobile/images/04-expense-saved.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/template-walkthroughs/mobile/images/05-cancel-expense.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/template-walkthroughs/mobile/images/06-expense-cancelled.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/template-walkthroughs/mobile/images/07-formatted-response.png` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/template-walkthroughs/mobile/images/react-native-walkthrough.gif` | Inherited/reference image, logo, or demo asset | Inherited reference |
| `dev-docs/tools-and-context.md` | Documentation / reference: tools-and-context.md | Inherited reference |
| `dev-docs/troubleshooting.md` | Documentation / reference: troubleshooting.md | Inherited reference |
| `docs/VALIDATION.md` | Dated observed checks and unverified behavior | Evidence through 2026-09-12 |
| `docs/planning/README.md` | Planning index and implementation disclaimer | Proposed / reference; product direction not locked |
| `docs/planning/followthrough-build-prompt.md` | Proposed Teams/Outlook build, task lifecycle, controls, and evaluation | Proposed / reference; product direction not locked |
| `docs/planning/followthrough-competitors-and-text-first-scope.md` | Dated competitor research and earlier proposed scope | Proposed / reference; product direction not locked |
| `docs/planning/toronto-hackathon-brief.md` | Earlier alternatives, scope, demo, and career notes | Proposed / reference; product direction not locked |
| `hackathon-overview.md` | Challenge, surfaces, and judging rubric | Tracked project guidance / configuration |
| `hackathon-rules.md` | Eligibility and required deliverables | Tracked project guidance / configuration |
| `package-lock.json` | Dependency or installed-skill lock record | Tracked project guidance / configuration |
| `package.json` | Package metadata, dependencies, and commands | Tracked project guidance / configuration |
| `packages/agent-core/package.json` | Package metadata, dependencies, and commands | Inherited reference |
| `packages/agent-core/src/agent.ts` | Implementation source: agent.ts | Inherited reference |
| `packages/agent-core/src/capabilities/search.ts` | Implementation source: search.ts | Inherited reference |
| `packages/agent-core/src/capabilities/workplace.ts` | Implementation source: workplace.ts | Inherited reference |
| `packages/agent-core/src/index.ts` | Implementation source: index.ts | Inherited reference |
| `packages/agent-core/src/mobile-finance-prompt.ts` | Implementation source: mobile-finance-prompt.ts | Inherited reference |
| `packages/agent-core/src/model-meta.ts` | Implementation source: model-meta.ts | Inherited reference |
| `packages/agent-core/src/model.test.ts` | Inherited or reference test: model.test.ts | Inherited reference |
| `packages/agent-core/src/model.ts` | Implementation source: model.ts | Inherited reference |
| `packages/agent-core/src/prompt.ts` | Implementation source: prompt.ts | Inherited reference |
| `packages/agent-core/src/schemas.ts` | Implementation source: schemas.ts | Inherited reference |
| `packages/agent-core/src/shared.ts` | Implementation source: shared.ts | Inherited reference |
| `packages/agent-core/tsconfig.json` | Build, runtime, or tool configuration | Inherited reference |
| `progress.md` | Live project handoff and per-user progress-record specification | Created 2026-09-12; structure confirmed; runtime not integrated |
| `skills-lock.json` | Dependency or installed-skill lock record | Tracked project guidance / configuration |
| `tools/exa-search/.env.example` | Placeholder configuration; no real credentials | Standalone helper; not integrated; live access unverified |
| `tools/exa-search/.gitignore` | Version-control exclusions | Standalone helper; not integrated; live access unverified |
| `tools/exa-search/README.md` | Documentation / reference: README.md | Standalone helper; not integrated; live access unverified |
| `tools/exa-search/exa_search.py` | Standalone Exa retrieval CLI | Standalone helper; not integrated; live access unverified |
| `tools/exa-search/requirements.txt` | Package metadata, dependencies, and commands | Standalone helper; not integrated; live access unverified |
| `using-sponsor-tools.md` | Sponsor setup recipes and active-app distinctions | Tracked project guidance / configuration |

## State of the design so far (durable facts a cold session needs)

**Project and confirmed surface.** Forget-me-nots is being developed as an agent inside Slack using CopilotKit. The active runnable implementation is one Google ADK assistant for Slack and web, not yet a project-management product. The user confirmed replacing the old multi-agent runtime with commit `813e46b`. A PM/delivery-lead follow-up workflow is described in planning files but is not confirmed as the final product. The repository is the shared development source for the project; a user's individual record must describe that user's project and supported facts rather than copying this development briefing.

**User-specific progress is the confirmed new requirement.** Every Slack user must have distinct progress context built from the same document skeleton. An instance needs a source-backed project description, where its files live, current state and deadline, confirmed decisions, parked proposals, resumable instructions, file map, steps, append-only decisions, and file-change evidence. The owner identity, project scope, source location, physical storage, permissions, and persistence contract are currently TBD. The skeleton requirement neither mandates a global channel record nor chooses one file per user on a local disk. Implementation must wait for those unresolved design choices to be aligned and confirmed.

**Document role and lifecycle are locked.** This root file is the live development index and handoff, written as a standalone document/skill specification. It is not installed in agent directories and is not injected into agent system prompts by this change. A fresh session should understand the current project from this file, then follow the literal source-reading instructions before acting. Locked and proposed records remain separate; absence of evidence is recorded as TBD. Checkpoints have the deliberately narrow update scope in House rules. Individual users may have different projects and decisions while retaining this structure.

**Confirmed repository scope; observed implementation.** The user authorized synchronizing existing work and preserving repository conventions, then requested the runtime fix to match `813e46b`. That commit is merged in remote baseline `6b7ea4d`. The canonical app keeps its independent Node install, Channels 0.9.2 / Runtime 1.70.2 pair, and AG-UI client/core 0.0.59 overrides. The active factory now returns `HttpAgent` for the single AG-UI endpoint on port 9000. Application-level A2A middleware, LangGraph research, and analysis services were removed. ADK dependencies may still include SDK libraries transitively; installed libraries do not register specialized agents. The assistant defaults to `gemini-3.6-flash`, overridable by `ORCHESTRATOR_MODEL`. These package/model settings remain implementation facts rather than permanent architecture choices.

**Observed identity and agent boundary.** `channels.mts` retains `identifyUser: "platform"`, creates a fresh HTTP agent for the supplied conversation thread, and drives it from the inherited `onMessage` handler. The Python assistant has no specialized research or analysis delegation tools. No source reads/writes progress Markdown or selects a user's record. Platform identity and thread separation are infrastructure, not evidence of durable per-user storage or authorization. The web identity remains a demo stub with unverified multi-user behavior.

**Evidence and completion boundaries.** `docs/VALIDATION.md` preserves the original three-agent setup as historical evidence. For the single-assistant runtime repair, clean installs, dependency consistency, initialization, root verification, production build, canonical-process/port checks, managed listener online status, and a synthetic greeting have passed and are recorded there. Real Slack replies, hosted web thread operations, per-user isolation/persistence, scheduling, Teams, Outlook, native cards in this app, and integrated Exa remain unverified or unimplemented. Research/analysis delegation is no longer an active acceptance requirement. A greeting or inherited test suite does not establish domain acceptance.

**Planning hierarchy and unresolved contradictions.** `docs/planning/README.md` calls the consolidated build prompt the successor to earlier recommendations. That is a documentary hierarchy, not evidence of user confirmation. The Toronto brief starts with one Teams channel thread, approval before drafting, and a minimal commitment watcher; later notes move to group-chat requests and automatic private drafts; the consolidated prompt adds task tracking, lifecycle, no-send controls, and a two-week review. These prescriptions differ from the confirmed Slack surface. Keep them available as proposals; do not silently execute the build prompt or transplant its choices into locked decisions.

**Hackathon reporting.** The five user-supplied references govern challenge understanding, eligibility, sponsor setup, conventions, and verified Channels APIs. The kit, generated apps, reference assets, and inherited tests remain attributed infrastructure. Setup/compatibility fixes are documented work; a new domain-specific core workflow and complete live demonstration remain outstanding. Official local build-window confirmation, submission deadline, video, and social submission are TBD. No claim of complete eligibility or final submission is made by this document.

## Steps

| # | Step | Output file | Status |
| --- | --- | --- | --- |
| 1a | Establish CopilotKit and Slack / Channels scope | `README.md` | Done (confirmed by user) |
| 1b | Use and start/connect the created `forgetme-nots` app | `apps/forgetme-nots/channels.mts` | In progress — startup authorized; end-to-end Slack success unverified |
| 2a | Preserve compatible single-assistant environment and record checks | `apps/forgetme-nots/agents/requirements.txt`, `docs/VALIDATION.md` | In progress — offline/build/greeting checks passed; real Slack acceptance unverified |
| 2b | Synchronize existing work to the requested GitHub repository | `README.md`, `SUBMISSION.md`, Git commit `2034a04` | In progress — published; user acceptance not explicitly recorded |
| 3a | Confirm and create standalone progress skeleton | `progress.md` | Done (confirmed by user) — structure approved; initial file created |
| 3b | Record distinct progress context for every Slack user | `progress.md` | Done (confirmed by user) — requirement only |
| 3c | Select authenticated owner/project scope and storage/access contract | `progress.md` | Not started — decisions parked |
| 3d | Implement per-user progress loading, updates, persistence, and diffs | TBD | Not started |
| 3e | Verify two users in the same channel remain distinct across updates/restarts | TBD | Not started |
| 4a | Verify successful real Slack greeting with the single assistant | `docs/VALIDATION.md` | Proposed, not locked |
| 4b | Switch runtime to confirmed single-assistant code and verify old services are absent | `apps/forgetme-nots/app/agent.ts`, `docs/VALIDATION.md` | Done (confirmed by user) — runtime fix requested; source/process/port/greeting checks passed |
| 5a | Align and confirm target persona and one new core workflow | TBD | Proposed, not locked |
| 5b | Implement and evaluate the confirmed domain workflow | TBD | Not started |
| 6a | Confirm applicable deadline/build window and substantiate eligibility | `SUBMISSION.md` | Not started |
| 6b | Prepare verified demo, video, description, and social submission | `SUBMISSION.md` | Not started |

Legend: Not started · In progress · Proposed, not locked · Done (confirmed by user).
“In progress” may describe an executed artifact awaiting verification or acceptance; the qualifier specifies which. “Done” for the skeleton and per-user requirement confirms the decision, not runtime feature completion.

## Decision log

Add new entries at the top; never edit or delete existing entries. Historical user-choice entries with no reliable confirmation timestamp use Date TBD. The 2026-09-12 go-ahead confirms the reviewed document structure and distinctions; parked items remain parked.

### 2026-09-12 — **Run the single ADK assistant from commit 813e46b**

Decided: fix the running app to use the referenced single-assistant implementation. Stop the old research/analysis services and A2A listener route; use the canonical Git checkout for subsequent starts. Rejected: continuing to restart the obsolete standalone multi-agent copy. Supersedes: the old research-first runtime and planned full research/analysis delegation checks. Per-user progress storage and all other parked product choices remain unconfirmed.

### 2026-09-12 — **One progress skeleton, distinct context for every Slack user**

Decided: create the approved `progress.md` handoff skeleton; each Slack user has different project/progress context. Rejected: treating the development project's context as every user's record. Supersedes: any assumption that a single shared channel progress context satisfies the requirement. Does not select storage, identity key, sharing permissions, or authorize runtime implementation.

### 2026-09-12 — **Standalone handoff and controlled updates approved**

Decided: create one root `progress.md` with the specified sections, source-backed facts, locked/proposed separation, dated decisions, and narrow checkpoint updates. Historical changes use per-file summaries plus exact Git diff references; subsequent changes use compact embedded patches. File Changes is excluded from checkpoint updates unless separately authorized. Rejected: installing this document inside agents or promoting source-file recommendations into confirmed decisions. Supersedes: no prior progress-file record exists.

### Date TBD — **Publish existing work with repository guidance**

Decided: synchronize existing project work to `ericnc09/forget-me-nots` and follow hackathon overview, rules, sponsor guidance, AGENTS conventions, and verified Channels APIs. Rejected: TBD; no explicit rejection was supplied. Supersedes: no prior repository-publication decision is evidenced here. Observed result is commit `2034a04`; publication success and user acceptance remain distinct.

### Date TBD — **Use the created app on Slack with CopilotKit**

Decided: use CopilotKit, select the Slack / Channels agent, work with the user-created `forgetme-nots`, and start/connect it. Rejected: TBD; no permanent rejection of other scaffolds is evidenced. The earlier singular-name scaffold is retained reference material. Supersedes: the earlier setup preference for the existing starter as the only active app. Final platform migration, domain persona, and feature scope were not confirmed.

## File Changes

### 2026-09-12 — Single-assistant runtime repair and source alignment

Application routing and UI are the already merged `813e46b` code in source baseline `6b7ea4d`. The runtime fix stops the obsolete standalone services and starts the canonical Git checkout. The original `forgetme-nots` path is now a compatibility alias to that active app; old files are preserved in `forgetme-nots-pre-single-agent-backup`. Private `.env` and virtual-environment files remain ignored. This repair changes only the tracked files listed below. Earlier change records and decision entries are preserved.

For the complete tracked patch, use `git diff 6b7ea4d -- <path>` before commit; after the repair commit, use `git show ':/Align runtime checks and handoff with single ADK assistant' -- <path>`. That revision identifies this repair by its unique commit subject. No earlier private-folder diff or secret settings are retained in the public document.

| File | Change summary |
| --- | --- |
| `package.json` | Compile only the remaining assistant during active-app verification. |
| `apps/forgetme-nots/scripts/copilotkit-dev-infra.mjs` | Require only the Google model key; remove obsolete OpenAI mock-base-URL metadata. |
| `README.md` | Document one assistant, current credentials/ports, and remaining live verification. |
| `SUBMISSION.md` | Preserve attribution to the original scaffold while labeling the active single-assistant scope accurately. |
| `using-sponsor-tools.md` | Update active-app model/provider claims; keep inherited sponsor recipes. |
| `docs/planning/README.md` | Identify the current single-assistant runtime; planned integrations remain proposed. |
| `docs/VALIDATION.md` | Preserve historical checks and add observed canonical-runtime repair evidence. |
| `progress.md` | Refresh current context, remove retired files from the live map, qualify steps, and add the confirmed runtime decision above prior entries. |

```diff
- verify:forgetme-nots: compile orchestrator.py, research_agent.py, analysis_agent.py
+ verify:forgetme-nots: compile only orchestrator.py
- startup preflight: require OPENAI_API_KEY and GOOGLE_API_KEY
+ startup preflight: require GOOGLE_API_KEY
- running source: old standalone forgetme-nots; UI + research + analysis + orchestrator
+ running source: canonical forget-me-nots/apps/forgetme-nots; UI + one ADK assistant
```

### 2026-09-12 — Initial progress document

Only `progress.md` is changed by this documentation task. Added: project handoff, approved per-user skeleton requirement, locked/proposed separation, a complete tracked-file map, source-backed design briefing, qualified steps, append-only decisions, and historical per-file diff references. No agent code, system prompt, installation, storage, Slack post, or user-record data is changed.

Compact addition outline below; the exact complete addition is available before staging with `git diff --no-index -- /dev/null progress.md` (exit 1 means differences), while staged with `git diff --cached -- progress.md`, and after commit with `git show <commit> -- progress.md`. Replace `<commit>` only with an actual recorded commit identifier in a separately authorized change-log update.

```diff
+ # Forget-me-nots — progress
+ ## HANDOFF (for a fresh session — read this first)
+ Locked: standalone skeleton; distinct context for each Slack user.
+ Parked: authenticated owner/project key, storage, access, and runtime lifecycle.
+ ## File map
+ ## State of the design so far (durable facts a cold session needs)
+ ## Steps
+ ## Decision log
+ ## File Changes
```

### 2026-09-12 — Historical repository synchronization

Source-backed diff baselines:

- Original remote branch: `a93e3fef63318b79be9b27b9a54a1347e8f9132e` (`a93e3fe`).
- Matching local/upstream kit: `86f547d74e8bd32e047226b0e1fb862cca02a5c7` (`86f547d`).
- Published synchronization: `2034a046d8cdef49d1e0adc90feafa0bcb813246` (`2034a04`).
- Inherited kit updates: `git diff a93e3fe..86f547d`.
- Added local work and portability/disclosure edits: `git diff 86f547d..2034a04`.
- Complete sync: `git diff a93e3fe..2034a04` — 174 changed files, 46,526 added lines and 942 deleted lines, including generated lockfiles and inherited updates. Binary changes require their committed blobs.

The table retains a summary and exact full-diff command for each changed path, including deleted inherited files. A/D/M are Git Added/Deleted/Modified. Historical source creation before these Git baselines cannot be reconstructed reliably and is not invented. Planning work is not reclassified as confirmed merely because it was published.

| File | Change | Diff size | Summary | Exact retained diff |
| --- | --- | --- | --- | --- |
| `.agents/skills/README.md` | M | +11 / -6 | Bring inherited file forward from upstream main: Documentation / reference: README.md | `git diff a93e3fe..2034a04 -- '.agents/skills/README.md'` |
| `.agents/skills/build-channels-agent/SKILL.md` | M | +18 / -15 | Bring inherited file forward from upstream main: Documentation / reference: SKILL.md | `git diff a93e3fe..2034a04 -- '.agents/skills/build-channels-agent/SKILL.md'` |
| `.agents/skills/channels-setup/SKILL.md` | A | +56 / -0 | Preserve installed Channels setup instructions / lock | `git diff a93e3fe..2034a04 -- '.agents/skills/channels-setup/SKILL.md'` |
| `.env.example` | M | +4 / -4 | Bring inherited file forward from upstream main: Placeholder configuration; no real credentials | `git diff a93e3fe..2034a04 -- '.env.example'` |
| `.github/workflows/ci.yml` | D | +0 / -50 | Upstream main removes inherited file: Implementation source: ci.yml | `git diff a93e3fe..2034a04 -- '.github/workflows/ci.yml'` |
| `.gitignore` | M | +11 / -0 | Exclude secrets, generated provider data, and local environments | `git diff a93e3fe..2034a04 -- '.gitignore'` |
| `AGENTS.md` | M | +8 / -0 | Identify the active app, reference scaffolds, and verification boundaries | `git diff a93e3fe..2034a04 -- 'AGENTS.md'` |
| `CREDITS.md` | D | +0 / -27 | Upstream main removes inherited file: Documentation / reference: CREDITS.md | `git diff a93e3fe..2034a04 -- 'CREDITS.md'` |
| `README.md` | M | +53 / -86 | Replace kit landing page with portable active-app quickstart and honest capability map | `git diff a93e3fe..2034a04 -- 'README.md'` |
| `STARTER-KIT.md` | A | +150 / -0 | Preserve inherited README and its relative links | `git diff a93e3fe..2034a04 -- 'STARTER-KIT.md'` |
| `SUBMISSION.md` | M | +19 / -1 | Disclose inherited work, setup fixes, and missing original core/deliverables | `git diff a93e3fe..2034a04 -- 'SUBMISSION.md'` |
| `apps/channel/README.md` | M | +38 / -21 | Bring inherited file forward from upstream main: Documentation / reference: README.md | `git diff a93e3fe..2034a04 -- 'apps/channel/README.md'` |
| `apps/channel/src/agent-factory.test.tsx` | A | +263 / -0 | Bring inherited file forward from upstream main: Inherited or reference test: agent-factory.test.tsx | `git diff a93e3fe..2034a04 -- 'apps/channel/src/agent-factory.test.tsx'` |
| `apps/channel/src/agent.ts` | A | +85 / -0 | Bring inherited file forward from upstream main: Implementation source: agent.ts | `git diff a93e3fe..2034a04 -- 'apps/channel/src/agent.ts'` |
| `apps/channel/src/channel.tsx` | M | +3 / -5 | Bring inherited file forward from upstream main: UI or Channels component source: channel.tsx | `git diff a93e3fe..2034a04 -- 'apps/channel/src/channel.tsx'` |
| `apps/channel/src/delivery.test.tsx` | A | +230 / -0 | Bring inherited file forward from upstream main: Inherited or reference test: delivery.test.tsx | `git diff a93e3fe..2034a04 -- 'apps/channel/src/delivery.test.tsx'` |
| `apps/channel/src/env.ts` | M | +2 / -2 | Bring inherited file forward from upstream main: Implementation source: env.ts | `git diff a93e3fe..2034a04 -- 'apps/channel/src/env.ts'` |
| `apps/channel/src/search.test.tsx` | A | +202 / -0 | Bring inherited file forward from upstream main: Inherited or reference test: search.test.tsx | `git diff a93e3fe..2034a04 -- 'apps/channel/src/search.test.tsx'` |
| `apps/channel/src/search.tsx` | A | +75 / -0 | Bring inherited file forward from upstream main: UI or Channels component source: search.tsx | `git diff a93e3fe..2034a04 -- 'apps/channel/src/search.tsx'` |
| `apps/channel/src/testing/managed-gateway.ts` | A | +37 / -0 | Bring inherited file forward from upstream main: Implementation source: managed-gateway.ts | `git diff a93e3fe..2034a04 -- 'apps/channel/src/testing/managed-gateway.ts'` |
| `apps/channel/src/tools.test.tsx` | M | +165 / -93 | Bring inherited file forward from upstream main: Inherited or reference test: tools.test.tsx | `git diff a93e3fe..2034a04 -- 'apps/channel/src/tools.test.tsx'` |
| `apps/channel/src/tools.tsx` | M | +37 / -20 | Bring inherited file forward from upstream main: UI or Channels component source: tools.tsx | `git diff a93e3fe..2034a04 -- 'apps/channel/src/tools.tsx'` |
| `apps/forgetme-nots/.copilotkit/channels.json` | A | +17 / -0 | Add active generated app: Tracked Channel declaration; no secret values | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/.copilotkit/channels.json'` |
| `apps/forgetme-nots/.env.example` | A | +59 / -0 | Add active generated app: Placeholder configuration; no real credentials | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/.env.example'` |
| `apps/forgetme-nots/.gitignore` | A | +89 / -0 | Add active generated app: Version-control exclusions | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/.gitignore'` |
| `apps/forgetme-nots/AGENTS.md` | A | +14 / -0 | Add active generated app: App-specific editing and verification guidance | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/AGENTS.md'` |
| `apps/forgetme-nots/README.md` | A | +326 / -0 | Add active generated app: Documentation / reference: README.md | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/README.md'` |
| `apps/forgetme-nots/agents/analysis_agent.py` | A | +232 / -0 | Add active generated app: Google ADK analysis A2A service | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/agents/analysis_agent.py'` |
| `apps/forgetme-nots/agents/orchestrator.py` | A | +86 / -0 | Add active generated app: Google ADK orchestrator and AG-UI service | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/agents/orchestrator.py'` |
| `apps/forgetme-nots/agents/requirements.txt` | A | +62 / -0 | Add active generated app: Pinned Python dependencies | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/agents/requirements.txt'` |
| `apps/forgetme-nots/agents/research_agent.py` | A | +180 / -0 | Add active generated app: LangGraph/OpenAI research A2A service | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/agents/research_agent.py'` |
| `apps/forgetme-nots/app/agent.ts` | A | +132 / -0 | Add active generated app: A2A agent factory and isolated middleware runs | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/app/agent.ts'` |
| `apps/forgetme-nots/app/api/copilotkit/[[...slug]]/route.ts` | A | +44 / -0 | Add active generated app: Implementation source: route.ts | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/app/api/copilotkit/[[...slug]]/route.ts'` |
| `apps/forgetme-nots/app/globals.css` | A | +87 / -0 | Add active generated app: UI styling: globals.css | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/app/globals.css'` |
| `apps/forgetme-nots/app/layout.tsx` | A | +36 / -0 | Add active generated app: UI or Channels component source: layout.tsx | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/app/layout.tsx'` |
| `apps/forgetme-nots/app/page.module.css` | A | +50 / -0 | Add active generated app: UI styling: page.module.css | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/app/page.module.css'` |
| `apps/forgetme-nots/app/page.tsx` | A | +225 / -0 | Add active generated app: UI or Channels component source: page.tsx | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/app/page.tsx'` |
| `apps/forgetme-nots/channel-host.mts` | A | +121 / -0 | Add active generated app: Managed listener lifecycle | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/channel-host.mts'` |
| `apps/forgetme-nots/channels.mts` | A | +110 / -0 | Add active generated app: Channel declaration, platform identity, and message handler | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/channels.mts'` |
| `apps/forgetme-nots/components/a2a/MessageFromA2A.tsx` | A | +67 / -0 | Add active generated app: UI or Channels component source: MessageFromA2A.tsx | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/components/a2a/MessageFromA2A.tsx'` |
| `apps/forgetme-nots/components/a2a/MessageToA2A.tsx` | A | +72 / -0 | Add active generated app: UI or Channels component source: MessageToA2A.tsx | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/components/a2a/MessageToA2A.tsx'` |
| `apps/forgetme-nots/components/a2a/agent-styles.ts` | A | +61 / -0 | Add active generated app: Implementation source: agent-styles.ts | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/components/a2a/agent-styles.ts'` |
| `apps/forgetme-nots/components/chat.tsx` | A | +116 / -0 | Add active generated app: UI or Channels component source: chat.tsx | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/components/chat.tsx'` |
| `apps/forgetme-nots/demo.png` | A | binary | Add active generated app: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/demo.png'` |
| `apps/forgetme-nots/next.config.ts` | A | +13 / -0 | Add active generated app: Build, runtime, or tool configuration | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/next.config.ts'` |
| `apps/forgetme-nots/package-lock.json` | A | +14674 / -0 | Add active generated app: Dependency or installed-skill lock record | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/package-lock.json'` |
| `apps/forgetme-nots/package.json` | A | +53 / -0 | Add active generated app: Package metadata, dependencies, and commands | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/package.json'` |
| `apps/forgetme-nots/postcss.config.mjs` | A | +6 / -0 | Add active generated app: Build, runtime, or tool configuration | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/postcss.config.mjs'` |
| `apps/forgetme-nots/scripts/copilotkit-dev-infra.mjs` | A | +186 / -0 | Add active generated app: Startup, setup, or verification script: copilotkit-dev-infra.mjs | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/scripts/copilotkit-dev-infra.mjs'` |
| `apps/forgetme-nots/scripts/smoke-agent.mts` | A | +41 / -0 | Add active generated app: Opt-in synthetic greeting through actual agent factory | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/scripts/smoke-agent.mts'` |
| `apps/forgetme-nots/tailwind.config.ts` | A | +81 / -0 | Add active generated app: Build, runtime, or tool configuration | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/tailwind.config.ts'` |
| `apps/forgetme-nots/tsconfig.channel.json` | A | +11 / -0 | Add active generated app: Build, runtime, or tool configuration | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/tsconfig.channel.json'` |
| `apps/forgetme-nots/tsconfig.json` | A | +41 / -0 | Add active generated app: Build, runtime, or tool configuration | `git diff a93e3fe..2034a04 -- 'apps/forgetme-nots/tsconfig.json'` |
| `apps/mobile/README.md` | M | +34 / -33 | Bring inherited file forward from upstream main: Documentation / reference: README.md | `git diff a93e3fe..2034a04 -- 'apps/mobile/README.md'` |
| `apps/web/README.md` | M | +36 / -24 | Bring inherited file forward from upstream main: Documentation / reference: README.md | `git diff a93e3fe..2034a04 -- 'apps/web/README.md'` |
| `assets/demos/mobile.gif` | A | binary | Bring inherited file forward from upstream main: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'assets/demos/mobile.gif'` |
| `assets/demos/mobile.mp4` | A | binary | Bring inherited file forward from upstream main: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'assets/demos/mobile.mp4'` |
| `assets/demos/slack.gif` | A | binary | Bring inherited file forward from upstream main: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'assets/demos/slack.gif'` |
| `assets/demos/slack.mp4` | A | binary | Bring inherited file forward from upstream main: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'assets/demos/slack.mp4'` |
| `assets/demos/web.gif` | A | binary | Bring inherited file forward from upstream main: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'assets/demos/web.gif'` |
| `assets/demos/web.mp4` | A | binary | Bring inherited file forward from upstream main: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'assets/demos/web.mp4'` |
| `dev-docs/README.md` | M | +1 / -0 | Bring inherited file forward from upstream main: Documentation / reference: README.md | `git diff a93e3fe..2034a04 -- 'dev-docs/README.md'` |
| `dev-docs/auth0/README.md` | A | +20 / -0 | Bring inherited file forward from upstream main: Documentation / reference: README.md | `git diff a93e3fe..2034a04 -- 'dev-docs/auth0/README.md'` |
| `examples/auth0/client.mjs	dev-docs/auth0/client.mjs` | R100 | TBD | Bring inherited file forward from upstream main: Implementation source: client.mjs | `git diff a93e3fe..2034a04 -- 'examples/auth0/client.mjs	dev-docs/auth0/client.mjs'` |
| `examples/auth0/package-lock.json	dev-docs/auth0/package-lock.json` | R100 | TBD | Bring inherited file forward from upstream main: Dependency or installed-skill lock record | `git diff a93e3fe..2034a04 -- 'examples/auth0/package-lock.json	dev-docs/auth0/package-lock.json'` |
| `examples/auth0/package.json	dev-docs/auth0/package.json` | R100 | TBD | Bring inherited file forward from upstream main: Package metadata, dependencies, and commands | `git diff a93e3fe..2034a04 -- 'examples/auth0/package.json	dev-docs/auth0/package.json'` |
| `examples/auth0/server.mjs	dev-docs/auth0/server.mjs` | R100 | TBD | Bring inherited file forward from upstream main: Implementation source: server.mjs | `git diff a93e3fe..2034a04 -- 'examples/auth0/server.mjs	dev-docs/auth0/server.mjs'` |
| `examples/auth0/test.mjs	dev-docs/auth0/test.mjs` | R100 | TBD | Bring inherited file forward from upstream main: Inherited or reference test: test.mjs | `git diff a93e3fe..2034a04 -- 'examples/auth0/test.mjs	dev-docs/auth0/test.mjs'` |
| `dev-docs/channels-sdk-walkthrough/README.md` | M | +2 / -0 | Bring inherited file forward from upstream main: Documentation / reference: README.md | `git diff a93e3fe..2034a04 -- 'dev-docs/channels-sdk-walkthrough/README.md'` |
| `dev-docs/demo-prompts.md` | M | +2 / -2 | Bring inherited file forward from upstream main: Documentation / reference: demo-prompts.md | `git diff a93e3fe..2034a04 -- 'dev-docs/demo-prompts.md'` |
| `dev-docs/model-switching.md` | M | +2 / -3 | Bring inherited file forward from upstream main: Documentation / reference: model-switching.md | `git diff a93e3fe..2034a04 -- 'dev-docs/model-switching.md'` |
| `dev-docs/scaffolds/forgetme-not/.copilotkit/channels.json` | A | +17 / -0 | Preserve earlier generated scaffold: Tracked Channel declaration; no secret values | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/.copilotkit/channels.json'` |
| `dev-docs/scaffolds/forgetme-not/.gitignore` | A | +55 / -0 | Preserve earlier generated scaffold: Version-control exclusions | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/.gitignore'` |
| `dev-docs/scaffolds/forgetme-not/AGENTS.md` | A | +3 / -0 | Preserve earlier generated scaffold: App-specific editing and verification guidance | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/AGENTS.md'` |
| `dev-docs/scaffolds/forgetme-not/LICENSE` | A | +21 / -0 | Preserve earlier generated scaffold: Inherited license and attribution | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/LICENSE'` |
| `dev-docs/scaffolds/forgetme-not/README.md` | A | +187 / -0 | Preserve earlier generated scaffold: Documentation / reference: README.md | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/README.md'` |
| `dev-docs/scaffolds/forgetme-not/agent/main.py` | A | +30 / -0 | Preserve earlier generated scaffold: Implementation source: main.py | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/agent/main.py'` |
| `dev-docs/scaffolds/forgetme-not/agent/pyproject.toml` | A | +18 / -0 | Preserve earlier generated scaffold: Package metadata, dependencies, and commands | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/agent/pyproject.toml'` |
| `dev-docs/scaffolds/forgetme-not/agent/src/__init__.py` | A | +0 / -0 | Preserve earlier generated scaffold: Implementation source: __init__.py | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/agent/src/__init__.py'` |
| `dev-docs/scaffolds/forgetme-not/agent/src/a2ui/__init__.py` | A | +0 / -0 | Preserve earlier generated scaffold: Implementation source: __init__.py | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/agent/src/a2ui/__init__.py'` |
| `dev-docs/scaffolds/forgetme-not/agent/src/a2ui/schemas/__init__.py` | A | +0 / -0 | Preserve earlier generated scaffold: Implementation source: __init__.py | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/agent/src/a2ui/schemas/__init__.py'` |
| `dev-docs/scaffolds/forgetme-not/agent/src/a2ui/schemas/flight_schema.json` | A | +37 / -0 | Preserve earlier generated scaffold: Reference data or schema: flight_schema.json | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/agent/src/a2ui/schemas/flight_schema.json'` |
| `dev-docs/scaffolds/forgetme-not/agent/src/a2ui_dynamic_schema.py` | A | +106 / -0 | Preserve earlier generated scaffold: Implementation source: a2ui_dynamic_schema.py | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/agent/src/a2ui_dynamic_schema.py'` |
| `dev-docs/scaffolds/forgetme-not/agent/src/a2ui_fixed_schema.py` | A | +64 / -0 | Preserve earlier generated scaffold: Implementation source: a2ui_fixed_schema.py | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/agent/src/a2ui_fixed_schema.py'` |
| `dev-docs/scaffolds/forgetme-not/agent/src/agent.py` | A | +67 / -0 | Preserve earlier generated scaffold: Implementation source: agent.py | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/agent/src/agent.py'` |
| `dev-docs/scaffolds/forgetme-not/agent/src/db.csv` | A | +41 / -0 | Preserve earlier generated scaffold: Reference data or schema: db.csv | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/agent/src/db.csv'` |
| `dev-docs/scaffolds/forgetme-not/agent/src/model.py` | A | +22 / -0 | Preserve earlier generated scaffold: Implementation source: model.py | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/agent/src/model.py'` |
| `dev-docs/scaffolds/forgetme-not/agent/src/query.py` | A | +36 / -0 | Preserve earlier generated scaffold: Implementation source: query.py | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/agent/src/query.py'` |
| `dev-docs/scaffolds/forgetme-not/agent/uv.lock` | A | +1352 / -0 | Preserve earlier generated scaffold: Dependency or installed-skill lock record | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/agent/uv.lock'` |
| `dev-docs/scaffolds/forgetme-not/channel-host.mts` | A | +121 / -0 | Preserve earlier generated scaffold: Implementation source: channel-host.mts | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/channel-host.mts'` |
| `dev-docs/scaffolds/forgetme-not/channels.mts` | A | +110 / -0 | Preserve earlier generated scaffold: Implementation source: channels.mts | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/channels.mts'` |
| `dev-docs/scaffolds/forgetme-not/entrypoint.sh` | A | +32 / -0 | Preserve earlier generated scaffold: Startup, setup, or verification script: entrypoint.sh | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/entrypoint.sh'` |
| `dev-docs/scaffolds/forgetme-not/next.config.ts` | A | +20 / -0 | Preserve earlier generated scaffold: Build, runtime, or tool configuration | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/next.config.ts'` |
| `dev-docs/scaffolds/forgetme-not/package-lock.json` | A | +21127 / -0 | Preserve earlier generated scaffold: Dependency or installed-skill lock record | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/package-lock.json'` |
| `dev-docs/scaffolds/forgetme-not/package.json` | A | +57 / -0 | Preserve earlier generated scaffold: Package metadata, dependencies, and commands | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/package.json'` |
| `dev-docs/scaffolds/forgetme-not/postcss.config.mjs` | A | +5 / -0 | Preserve earlier generated scaffold: Build, runtime, or tool configuration | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/postcss.config.mjs'` |
| `dev-docs/scaffolds/forgetme-not/public/copilotkit-logo-mark.svg` | A | +30 / -0 | Preserve earlier generated scaffold: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/public/copilotkit-logo-mark.svg'` |
| `dev-docs/scaffolds/forgetme-not/public/copilotkit-logo.svg` | A | +46 / -0 | Preserve earlier generated scaffold: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/public/copilotkit-logo.svg'` |
| `dev-docs/scaffolds/forgetme-not/public/file.svg` | A | +1 / -0 | Preserve earlier generated scaffold: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/public/file.svg'` |
| `dev-docs/scaffolds/forgetme-not/public/globe.svg` | A | +1 / -0 | Preserve earlier generated scaffold: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/public/globe.svg'` |
| `dev-docs/scaffolds/forgetme-not/public/next.svg` | A | +1 / -0 | Preserve earlier generated scaffold: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/public/next.svg'` |
| `dev-docs/scaffolds/forgetme-not/public/vercel.svg` | A | +1 / -0 | Preserve earlier generated scaffold: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/public/vercel.svg'` |
| `dev-docs/scaffolds/forgetme-not/public/window.svg` | A | +1 / -0 | Preserve earlier generated scaffold: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/public/window.svg'` |
| `dev-docs/scaffolds/forgetme-not/scripts/copilotkit-dev-infra.mjs` | A | +180 / -0 | Preserve earlier generated scaffold: Startup, setup, or verification script: copilotkit-dev-infra.mjs | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/scripts/copilotkit-dev-infra.mjs'` |
| `dev-docs/scaffolds/forgetme-not/scripts/run-agent.bat` | A | +6 / -0 | Preserve earlier generated scaffold: Startup, setup, or verification script: run-agent.bat | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/scripts/run-agent.bat'` |
| `dev-docs/scaffolds/forgetme-not/scripts/run-agent.sh` | A | +7 / -0 | Preserve earlier generated scaffold: Startup, setup, or verification script: run-agent.sh | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/scripts/run-agent.sh'` |
| `dev-docs/scaffolds/forgetme-not/scripts/setup-agent.bat` | A | +6 / -0 | Preserve earlier generated scaffold: Startup, setup, or verification script: setup-agent.bat | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/scripts/setup-agent.bat'` |
| `dev-docs/scaffolds/forgetme-not/scripts/setup-agent.sh` | A | +7 / -0 | Preserve earlier generated scaffold: Startup, setup, or verification script: setup-agent.sh | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/scripts/setup-agent.sh'` |
| `dev-docs/scaffolds/forgetme-not/showcase.json` | A | +3 / -0 | Preserve earlier generated scaffold: Reference data or schema: showcase.json | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/showcase.json'` |
| `dev-docs/scaffolds/forgetme-not/src/agent.ts` | A | +10 / -0 | Preserve earlier generated scaffold: Implementation source: agent.ts | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/agent.ts'` |
| `dev-docs/scaffolds/forgetme-not/src/app/api/copilotkit/[[...slug]]/route.ts` | A | +62 / -0 | Preserve earlier generated scaffold: Implementation source: route.ts | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/app/api/copilotkit/[[...slug]]/route.ts'` |
| `dev-docs/scaffolds/forgetme-not/src/app/declarative-generative-ui/definitions.ts` | A | +184 / -0 | Preserve earlier generated scaffold: Implementation source: definitions.ts | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/app/declarative-generative-ui/definitions.ts'` |
| `dev-docs/scaffolds/forgetme-not/src/app/declarative-generative-ui/renderers.tsx` | A | +601 / -0 | Preserve earlier generated scaffold: UI or Channels component source: renderers.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/app/declarative-generative-ui/renderers.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/app/favicon.ico` | A | binary | Preserve earlier generated scaffold: Inherited/reference image, logo, or demo asset | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/app/favicon.ico'` |
| `dev-docs/scaffolds/forgetme-not/src/app/globals.css` | A | +125 / -0 | Preserve earlier generated scaffold: UI styling: globals.css | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/app/globals.css'` |
| `dev-docs/scaffolds/forgetme-not/src/app/layout.tsx` | A | +58 / -0 | Preserve earlier generated scaffold: UI or Channels component source: layout.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/app/layout.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/app/page.module.css` | A | +67 / -0 | Preserve earlier generated scaffold: UI styling: page.module.css | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/app/page.module.css'` |
| `dev-docs/scaffolds/forgetme-not/src/app/page.tsx` | A | +49 / -0 | Preserve earlier generated scaffold: UI or Channels component source: page.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/app/page.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/example-canvas/index.tsx` | A | +20 / -0 | Preserve earlier generated scaffold: UI or Channels component source: index.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/example-canvas/index.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/example-canvas/todo-card.tsx` | A | +197 / -0 | Preserve earlier generated scaffold: UI or Channels component source: todo-card.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/example-canvas/todo-card.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/example-canvas/todo-column.tsx` | A | +88 / -0 | Preserve earlier generated scaffold: UI or Channels component source: todo-column.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/example-canvas/todo-column.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/example-canvas/todo-list.tsx` | A | +115 / -0 | Preserve earlier generated scaffold: UI or Channels component source: todo-list.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/example-canvas/todo-list.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/example-layout/index.tsx` | A | +83 / -0 | Preserve earlier generated scaffold: UI or Channels component source: index.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/example-layout/index.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/example-layout/mode-toggle.tsx` | A | +39 / -0 | Preserve earlier generated scaffold: UI or Channels component source: mode-toggle.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/example-layout/mode-toggle.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/generative-ui/charts/bar-chart.tsx` | A | +158 / -0 | Preserve earlier generated scaffold: UI or Channels component source: bar-chart.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/generative-ui/charts/bar-chart.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/generative-ui/charts/config.ts` | A | +25 / -0 | Preserve earlier generated scaffold: Implementation source: config.ts | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/generative-ui/charts/config.ts'` |
| `dev-docs/scaffolds/forgetme-not/src/components/generative-ui/charts/pie-chart.tsx` | A | +155 / -0 | Preserve earlier generated scaffold: UI or Channels component source: pie-chart.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/generative-ui/charts/pie-chart.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/generative-ui/meeting-time-picker.tsx` | A | +177 / -0 | Preserve earlier generated scaffold: UI or Channels component source: meeting-time-picker.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/generative-ui/meeting-time-picker.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/headless-chat.tsx` | A | +48 / -0 | Preserve earlier generated scaffold: UI or Channels component source: headless-chat.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/headless-chat.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/tool-rendering.tsx` | A | +95 / -0 | Preserve earlier generated scaffold: UI or Channels component source: tool-rendering.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/tool-rendering.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/ui/badge.tsx` | A | +35 / -0 | Preserve earlier generated scaffold: UI or Channels component source: badge.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/ui/badge.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/ui/button.tsx` | A | +52 / -0 | Preserve earlier generated scaffold: UI or Channels component source: button.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/ui/button.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/ui/card.tsx` | A | +85 / -0 | Preserve earlier generated scaffold: UI or Channels component source: card.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/ui/card.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/ui/checkbox.tsx` | A | +27 / -0 | Preserve earlier generated scaffold: UI or Channels component source: checkbox.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/ui/checkbox.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/ui/input.tsx` | A | +19 / -0 | Preserve earlier generated scaffold: UI or Channels component source: input.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/ui/input.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/ui/separator.tsx` | A | +30 / -0 | Preserve earlier generated scaffold: UI or Channels component source: separator.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/ui/separator.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/components/ui/spinner.tsx` | A | +24 / -0 | Preserve earlier generated scaffold: UI or Channels component source: spinner.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/components/ui/spinner.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/hooks/index.ts` | A | +3 / -0 | Preserve earlier generated scaffold: Implementation source: index.ts | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/hooks/index.ts'` |
| `dev-docs/scaffolds/forgetme-not/src/hooks/use-example-suggestions.tsx` | A | +69 / -0 | Preserve earlier generated scaffold: UI or Channels component source: use-example-suggestions.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/hooks/use-example-suggestions.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/hooks/use-generative-ui-examples.tsx` | A | +83 / -0 | Preserve earlier generated scaffold: UI or Channels component source: use-generative-ui-examples.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/hooks/use-generative-ui-examples.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/hooks/use-theme.tsx` | A | +43 / -0 | Preserve earlier generated scaffold: UI or Channels component source: use-theme.tsx | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/hooks/use-theme.tsx'` |
| `dev-docs/scaffolds/forgetme-not/src/lib/a2ui-theme.css` | A | +162 / -0 | Preserve earlier generated scaffold: UI styling: a2ui-theme.css | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/lib/a2ui-theme.css'` |
| `dev-docs/scaffolds/forgetme-not/src/lib/utils.ts` | A | +7 / -0 | Preserve earlier generated scaffold: Implementation source: utils.ts | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/src/lib/utils.ts'` |
| `dev-docs/scaffolds/forgetme-not/tsconfig.channel.json` | A | +11 / -0 | Preserve earlier generated scaffold: Build, runtime, or tool configuration | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/tsconfig.channel.json'` |
| `dev-docs/scaffolds/forgetme-not/tsconfig.json` | A | +33 / -0 | Preserve earlier generated scaffold: Build, runtime, or tool configuration | `git diff a93e3fe..2034a04 -- 'dev-docs/scaffolds/forgetme-not/tsconfig.json'` |
| `dev-docs/setup.md` | M | +8 / -7 | Bring inherited file forward from upstream main: Documentation / reference: setup.md | `git diff a93e3fe..2034a04 -- 'dev-docs/setup.md'` |
| `dev-docs/sponsors.md` | M | +1 / -1 | Bring inherited file forward from upstream main: Documentation / reference: sponsors.md | `git diff a93e3fe..2034a04 -- 'dev-docs/sponsors.md'` |
| `dev-docs/surfaces.md` | M | +3 / -3 | Bring inherited file forward from upstream main: Documentation / reference: surfaces.md | `git diff a93e3fe..2034a04 -- 'dev-docs/surfaces.md'` |
| `dev-docs/troubleshooting.md` | M | +22 / -9 | Bring inherited file forward from upstream main: Documentation / reference: troubleshooting.md | `git diff a93e3fe..2034a04 -- 'dev-docs/troubleshooting.md'` |
| `docs/VALIDATION.md` | A | +43 / -0 | Record offline, build, model, and live-integration evidence separately | `git diff a93e3fe..2034a04 -- 'docs/VALIDATION.md'` |
| `docs/planning/README.md` | A | +9 / -0 | Label plans as proposals; distinguish them from implemented behavior | `git diff a93e3fe..2034a04 -- 'docs/planning/README.md'` |
| `docs/planning/followthrough-build-prompt.md` | A | +208 / -0 | Preserve proposed planning; redact private local reference links | `git diff a93e3fe..2034a04 -- 'docs/planning/followthrough-build-prompt.md'` |
| `docs/planning/followthrough-competitors-and-text-first-scope.md` | A | +70 / -0 | Preserve proposed planning; redact private local reference links | `git diff a93e3fe..2034a04 -- 'docs/planning/followthrough-competitors-and-text-first-scope.md'` |
| `docs/planning/toronto-hackathon-brief.md` | A | +107 / -0 | Preserve proposed planning; redact private local reference links | `git diff a93e3fe..2034a04 -- 'docs/planning/toronto-hackathon-brief.md'` |
| `examples/auth0/README.md` | D | +0 / -20 | Upstream main removes inherited file: Documentation / reference: README.md | `git diff a93e3fe..2034a04 -- 'examples/auth0/README.md'` |
| `hackathon-overview.md` | M | +3 / -3 | Bring inherited file forward from upstream main: Challenge, surfaces, and judging rubric | `git diff a93e3fe..2034a04 -- 'hackathon-overview.md'` |
| `hackathon-rules.md` | M | +2 / -2 | Bring inherited file forward from upstream main: Eligibility and required deliverables | `git diff a93e3fe..2034a04 -- 'hackathon-rules.md'` |
| `package-lock.json` | M | +2 / -81 | Refresh project metadata and npm lock state | `git diff a93e3fe..2034a04 -- 'package-lock.json'` |
| `package.json` | M | +8 / -7 | Name project and add active-app startup/channel/verification scripts | `git diff a93e3fe..2034a04 -- 'package.json'` |
| `packages/agent-core/package.json` | M | +2 / -1 | Bring inherited file forward from upstream main: Package metadata, dependencies, and commands | `git diff a93e3fe..2034a04 -- 'packages/agent-core/package.json'` |
| `packages/agent-core/src/model.test.ts` | A | +118 / -0 | Bring inherited file forward from upstream main: Inherited or reference test: model.test.ts | `git diff a93e3fe..2034a04 -- 'packages/agent-core/src/model.test.ts'` |
| `packages/agent-core/src/model.ts` | M | +1 / -1 | Bring inherited file forward from upstream main: Implementation source: model.ts | `git diff a93e3fe..2034a04 -- 'packages/agent-core/src/model.ts'` |
| `scripts/check-env.sh` | D | +0 / -162 | Upstream main removes inherited file: Startup, setup, or verification script: check-env.sh | `git diff a93e3fe..2034a04 -- 'scripts/check-env.sh'` |
| `scripts/check-env.test.ts` | D | +0 / -148 | Upstream main removes inherited file: Inherited or reference test: check-env.test.ts | `git diff a93e3fe..2034a04 -- 'scripts/check-env.test.ts'` |
| `scripts/dev.sh` | D | +0 / -15 | Upstream main removes inherited file: Startup, setup, or verification script: dev.sh | `git diff a93e3fe..2034a04 -- 'scripts/dev.sh'` |
| `scripts/verify.sh` | D | +0 / -33 | Upstream main removes inherited file: Startup, setup, or verification script: verify.sh | `git diff a93e3fe..2034a04 -- 'scripts/verify.sh'` |
| `scripts/verify.test.mjs` | D | +0 / -44 | Upstream main removes inherited file: Inherited or reference test: verify.test.mjs | `git diff a93e3fe..2034a04 -- 'scripts/verify.test.mjs'` |
| `skills-lock.json` | A | +11 / -0 | Preserve installed Channels setup instructions / lock | `git diff a93e3fe..2034a04 -- 'skills-lock.json'` |
| `tools/exa-search/.env.example` | A | +1 / -0 | Preserve standalone helper and portable setup | `git diff a93e3fe..2034a04 -- 'tools/exa-search/.env.example'` |
| `tools/exa-search/.gitignore` | A | +6 / -0 | Preserve standalone helper and portable setup | `git diff a93e3fe..2034a04 -- 'tools/exa-search/.gitignore'` |
| `tools/exa-search/README.md` | A | +69 / -0 | Preserve standalone helper and portable setup | `git diff a93e3fe..2034a04 -- 'tools/exa-search/README.md'` |
| `tools/exa-search/exa_search.py` | A | +97 / -0 | Preserve standalone helper and portable setup | `git diff a93e3fe..2034a04 -- 'tools/exa-search/exa_search.py'` |
| `tools/exa-search/requirements.txt` | A | +2 / -0 | Preserve standalone helper and portable setup | `git diff a93e3fe..2034a04 -- 'tools/exa-search/requirements.txt'` |
| `using-sponsor-tools.md` | M | +20 / -13 | Document active-app credentials, model defaults, and standalone Exa status | `git diff a93e3fe..2034a04 -- 'using-sponsor-tools.md'` |
