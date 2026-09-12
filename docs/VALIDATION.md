# Validation evidence

Observed during the September 12, 2026 setup session. A passed local check is not proof of a complete product or hackathon eligibility.

## Inherited kit

`npm run verify` in the local kit passed all three workspace typechecks and 93 offline tests: 37 agent-core, 22 Channels, and 34 web. These tests were inherited, not newly authored event work. A clean checkout run is recorded below after synchronization.

## Active Forget-me-nots app

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

The starter's hard-coded Gemini 2.5 models returned 404 for this account. Gemini 3.1 Pro was listed but returned a zero free-tier quota error. Gemini 3.6 Flash responded successfully, so both Google agents now default to it. `ORCHESTRATOR_MODEL` and `GEMINI_MODEL` can override the defaults. No credentials or private message bodies are included in this report.

## Still unverified

- A successful real Slack reply after the model fix, subscribed follow-up behavior, and silence in an unrelated conversation.
- Full research → analysis delegation and its OpenAI model access.
- The generated Next.js UI's hosted thread operations; its identity callback remains a demo stub.
- Native cards in the active generated app, restart persistence, scheduling, reminders, Teams, Outlook, and a task tracker. These are not implemented by this sync.
- Live Exa retrieval from the standalone helper. Its source README records prior mocked checks, not an authenticated search.
- A new domain-specific core workflow, end-user evaluation, a demo video, and a social submission.

## Clean checkout verification

Verified in an isolated checkout of this repository on September 12, 2026 using Node 24.15.0, npm 11.12.0, and Python 3.10:

- Root `npm ci --no-audit --no-fund` and the independent active app install both completed from their committed lockfiles.
- Root `npm run verify` passed: three inherited workspace typechecks, all 93 inherited offline tests, the active channel/smoke-script typecheck, and syntax compilation of all three Python agents.
- Active `npm run build` completed successfully, including the Next.js typecheck and production page generation. It reported nonblocking workspace-root and module-type warnings. This build used no private environment file and does not prove hosted UI thread operations.
- The committed smoke script returned a nonempty greeting (34 characters) through `createDefaultAgent`, using the existing private local configuration and running agent services. No Slack message was sent by this check.
- `git diff --check` passed. Environment files, Python/Node environments, build output, and CopilotKit project credentials/artifacts are excluded from the sync.
