# Active Slack prototype

Read the root AGENTS.md, hackathon overview, rules, sponsor guide, and Channels skill. This directory is the active app. The incident app in `../channel` and earlier scaffold in `../../dev-docs/scaffolds/forgetme-not` are reference code.

- This app has a separate Node install and `.env`; do not add it to the inherited npm workspaces without reconciling both runtime dependency graphs.
- Keep Channels 0.9.2 and Runtime 1.70.2 paired and exact. Preserve the AG-UI client/core overrides at 0.0.59 and check deduplication when changing dependencies.
- `channels.mts` holds the declaration and handlers. `channel-host.mts` owns lifecycle. `app/agent.ts` creates the shared AG-UI HTTP agent used by web and Slack.
- The managed listener reads CPK_INTELLIGENCE_API_KEY. Slack provider credentials remain in Intelligence. Track channels.json; ignore actual `.env`, project identity files, provider artifacts, and environments.
- The single Google ADK agent defaults to gemini-3.6-flash. Respect the ORCHESTRATOR_MODEL override. Verify account access before changing the default.
- Handlers must return void. Use only installed Channels APIs; do not invent components, props, or commands. Apply the documented mention/subscription and managed approval patterns when extending behavior. The current scaffold's onMessage handler is inherited and has not been tested for unrelated-conversation silence.
- Use `.tsx` and the Channels JSX transform when introducing native components. The active app currently has no registered Channel component; do not claim card support from the inherited incident app.
- Before publishing changes, run `npm run typecheck:channel`, the root `npm run verify`, and the appropriate Python syntax/dependency checks. `npm run smoke:agent` makes a real model call and requires running agent services. Keep live Slack tests distinct from offline checks.
- FollowThrough capabilities in docs/planning are proposed work. Do not imply reminders, persistent tasks, Teams, Outlook drafts, or mailbox permissions have been implemented.
