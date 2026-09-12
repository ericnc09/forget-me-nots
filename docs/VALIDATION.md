# Validation evidence

Observed during the September 12, 2026 setup session. A passed local check is not proof of a complete product or hackathon eligibility.

## Inherited kit

`npm run verify` in the local kit passed all three workspace typechecks and 93 offline tests: 37 agent-core, 22 Channels, and 34 web. These tests were inherited, not newly authored event work. A clean checkout run is recorded below after synchronization.

## Historical three-agent setup (before commit 813e46b)

| Check | Observed result |
| --- | --- |
| Channel typecheck | Passed after aligning Channels 0.9.2 with Runtime 1.70.2 |
| Python installation | Installed; dependency consistency check passed after selecting A2A SDK 0.3.26 |
| Agent initialization | Orchestrator, research, and analysis modules loaded and initialized |
| Local endpoints | Orchestrator OpenAPI and both A2A agent cards returned HTTP 200 |
| Hosted CLI reconcile/status | `channels status --json` returned completed; `forgetme-nots` was declared, source/server present, Slack attached |
| Listener | Reported `Channel "forgetme-nots" is online.` |
| Slack ingress/error delivery | A user mention reached the agent; its original Gemini 2.5 request failed and the listener posted an error |
| Google replacement model | A synthetic probe against `gemini-3.6-flash` returned text using the configured account |
| Agent greeting after fix | Passed through `createDefaultAgent`, the same factory used by Slack; returned a nonempty greeting |
| Python syntax | Orchestrator and analysis syntax checks passed |

The starter's hard-coded Gemini 2.5 models returned 404 for this account. Gemini 3.1 Pro was listed but returned a zero free-tier quota error. Gemini 3.6 Flash responded successfully, so the original two Google agents were configured to default to it. Commit `813e46b` subsequently replaced that architecture with one assistant using `ORCHESTRATOR_MODEL`. No credentials or private message bodies are included in this report.

## Still unverified

- A successful real Slack reply after the model fix, subscribed follow-up behavior, and silence in an unrelated conversation.
- The old research → analysis workflow was not fully live-verified before removal; it is no longer an acceptance requirement for the active single-assistant app.
- The generated Next.js UI's hosted thread operations; its identity callback remains a demo stub.
- Native cards in the active generated app, restart persistence, scheduling, reminders, Teams, Outlook, and a task tracker. These are not implemented by this sync.
- Live Exa retrieval from the standalone helper. Its source README records prior mocked checks, not an authenticated search.
- A new domain-specific core workflow, end-user evaluation, a demo video, and a social submission.

## Historical clean checkout verification (commit 2034a04)

Verified in an isolated checkout of this repository on September 12, 2026 using Node 24.15.0, npm 11.12.0, and Python 3.10:

- Root `npm ci --no-audit --no-fund` and the independent active app install both completed from their committed lockfiles.
- Root `npm run verify` passed: three inherited workspace typechecks, all 93 inherited offline tests, the active channel/smoke-script typecheck, and syntax compilation of all three Python agents.
- Active `npm run build` completed successfully, including the Next.js typecheck and production page generation. It reported nonblocking workspace-root and module-type warnings. This build used no private environment file and does not prove hosted UI thread operations.
- The committed smoke script returned a nonempty greeting (34 characters) through `createDefaultAgent`, using the existing private local configuration and running agent services. No Slack message was sent by this check.
- `git diff --check` passed. Environment files, Python/Node environments, build output, and CopilotKit project credentials/artifacts are excluded from the sync.

## Single-assistant runtime repair — 2026-09-12

The merged source baseline `6b7ea4d` includes commit `813e46b`. The prior restart used an obsolete standalone source folder; restarting it could still register and run research/analysis agents. The services now run from the canonical Git checkout at `/Users/eric/Documents/ChatGPT/planned projects/forget-me-nots/apps/forgetme-nots`. The old source is retained in `forgetme-nots-pre-single-agent-backup` and is not running. The original `forgetme-nots` path aliases the canonical active app to prevent another restart from loading the obsolete source.

- Root and independent active-app clean Node installs passed; Python dependencies installed in a clean private virtual environment and `pip check` reported no broken requirements.
- The single assistant initialized as `ForgetMeNotsAssistant`.
- Root `npm run verify` passed: inherited typechecks and all 93 inherited offline tests, active Channel/smoke-script typecheck, and syntax compilation of only the remaining assistant. The verification command was corrected to remove deleted research/analysis file paths.
- Active `npm run build` passed; the existing nonblocking workspace-root and module-type warnings remain.
- Old multi-agent supervisor and Slack listener stopped. The replacement supervisor starts only UI and the assistant. Process inspection verified the assistant, UI, and listener use the canonical checkout.
- Port 9000 OpenAPI returned HTTP 200 with title `Forget-me-nots Assistant (ADK + AG-UI)`; UI listens on port 3000. No service listens on ports 9001 or 9002, and no research/analysis Python processes remain.
- `npm ls @ag-ui/a2a-middleware @a2a-js/sdk --all` returned an empty graph. The active factory is the single `HttpAgent` from `813e46b`; there is no specialized delegation route. Transitive Python SDK dependencies do not create or run specialized agents.
- The managed Slack listener reported `Channel "forgetme-nots" is online.`
- `npm run smoke:agent` returned a nonempty synthetic greeting (50 characters) through the actual single-assistant factory. This made a real model call and sent no Slack message.
- Generated startup preflight now requires the single assistant's Google key, not the removed OpenAI research backend. Private configuration was preserved and excluded from publication.

Successful real Slack replies, subscription/silence behavior, hosted web identity/thread operations, and per-user progress persistence/access enforcement remain unverified. No new product-domain workflow is claimed.
