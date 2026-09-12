# FollowThrough — Toronto hackathon brief

**Ready-to-run instructions:** [standalone FollowThrough build prompt](./followthrough-build-prompt.md), including task tracking, a two-week review, draft-only controls, and the eval harness.

Latest recommendation after competitor research: start with Teams text requests and automatically prepare an Outlook reply draft when the intended thread is clear. See [competitor findings and revised scope](./followthrough-competitors-and-text-first-scope.md). The original watch-a-commitment design below remains useful later scope.

Prepared September 11, 2026. Planning brief; no prototype has been built or tested. Assumes a Microsoft 365 test tenant with app permissions. Scope is a one-day Teams prototype for a PM or delivery lead coordinating a vendor dependency.

## Three ideas to take

| Idea | Core interaction | Distinctive use of context | One-day scope |
| --- | --- | --- | --- |
| **FollowThrough — recommended** | Watch an agreed deliverable, prepare a follow-up when due, revise it as replies arrive, and create an Outlook draft after approval. | Later replies can fulfill part of a request or change the deadline. The agent must update its proposed action. | One Teams channel thread, one owner, one action type. |
| **Handoff Builder** | Turn a planning thread into an approved handoff containing the decision, owner, next step, and unresolved dependency. | Reconcile corrections and commitments across the thread; preserve source links. | One thread and one posted handoff. |
| **Decision Keeper** | Detect when a new proposal conflicts with a recorded decision and ask whether that decision has changed. | Compare current discussion against the agreed decision in the same channel. | One stored decision, one thread, and an approved update. |

FollowThrough is the closest match to Eric's original meeting-assistant idea and gives a concrete enterprise workflow to discuss with PM and AI-product contacts.

## Product hypothesis

PMs and delivery leads spend effort remembering dependencies and checking whether to chase them. An agent could reduce that effort by following one agreed commitment in Teams and preparing an accurate next action at the right time.

The environment supplies identities, source messages, timestamps, later corrections, and the place to approve work. Persistent attention to those changes is the central value. Use a synthetic vendor-delivery scenario inspired by enterprise coordination; do not use employer material.

Microsoft already provides meeting notes and task management through [Facilitator](https://support.microsoft.com/en-us/teams/copilot/facilitator-in-microsoft-teams-meetings). The proposed distinction to test is accurate follow-through as a commitment changes, including avoiding unnecessary chasers. This is a product hypothesis, not a claim of market uniqueness.

## The minimum working agent

1. Eric selects a top-level message in one Teams test channel and starts **Watch this commitment**.
2. The backend reads the message and its replies. It extracts the deliverable, responsible person, explicit deadline, and supporting source. Missing owners or dates require clarification.
3. Save the watched commitment. Poll only that thread at a modest interval and check the deadline. A simple local process can do this during the demo.
4. When follow-up is appropriate, privately show Eric the proposed recipient, subject, body, evidence, and **Create draft / Edit / Dismiss** controls.
5. If the conversation changes, revise or withdraw the proposal. Recheck the thread immediately before creating the draft.
6. After approval, create one real Outlook draft and show the result in Teams. Repeated clicks must not create another draft.

Limit claims to the watched thread: "No completion found in this thread" is more accurate than "They have not done it." A file link alone is not proof that an entire request is complete; the demo should include explicit confirmation of what was delivered.

The model interprets commitments and updates and drafts language. Ordinary code owns timing, approval identity, allowed actions, and duplicate prevention. The demo executes a real draft creation; email delivery remains a separate user action.

## Integration route

| Piece | Suggested approach | First check |
| --- | --- | --- |
| Start watching | Teams Workflows / Power Automate **For a selected message** | Create in the default environment and confirm the action appears in Teams. |
| Context | Microsoft Graph: get the root channel message and list its replies | Confirm permissions and retrieval of a new reply. The selected-message trigger alone does not provide the whole thread. |
| Reasoning and state | Small Node or Python service, one model, SQLite | Extract structured fields; persist thread ID, deadline, evidence, state, and action ID. |
| Approval | Power Automate **Post adaptive card and wait for a response**, privately to Eric | Confirm Workflows is enabled and the intended user can respond. |
| Action | Microsoft Graph create-message endpoint | Confirm an actual draft appears in the test mailbox. |

Official references: [selected-message trigger](https://learn.microsoft.com/en-us/power-automate/trigger-flow-teams-message), [channel replies and permissions](https://learn.microsoft.com/en-us/graph/api/chatmessage-list-replies?view=graph-rest-1.0), [Teams connector and current card actions](https://learn.microsoft.com/en-gb/connectors/teams/), [Outlook draft creation](https://learn.microsoft.com/en-us/graph/api/user-post-messages?view=graph-rest-1.0).

App permissions do not by themselves establish that all required Workflows, mailbox, and model-connector access is available. Prove the full connection path in the first hour. If Outlook access blocks progress, make the one action an approved follow-up posted by the bot to the test thread. If Workflows blocks progress, assess a Teams bot or Slack route early; do not split the day's build across platforms.

Live meeting attendance is later scope. Microsoft's [application-hosted media path](https://learn.microsoft.com/en-us/microsoftteams/platform/bots/calls-and-meetings/requirements-considerations-application-hosted-media-bots) has substantial runtime and hosting requirements. The [transcript API](https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/meeting-transcripts/overview-transcripts) provides a post-meeting route subject to permissions and tenant controls; it is not a live transcript feed. A later call participant should be visible and opt-in, with private suggestions to the requesting user.

## Ninety-second demo

- **0–15 seconds:** Show a test thread: "Maya will send the revised quote and delivery date by 2 pm." Eric starts watching it. Maya is a mapped test identity with a known email address.
- **15–35 seconds:** Advance a clearly labeled demo clock beyond the deadline. The agent proposes a follow-up for both items.
- **35–55 seconds:** Add a real Teams reply: "The revised quote is attached; delivery date is still pending." The agent updates the proposed email to request only the delivery date.
- **55–75 seconds:** Eric approves the revised draft. Open the real Outlook draft and show the correct recipient and wording.
- **75–90 seconds:** Show a completed example where no chaser is proposed, then state the limitation: one opted-in thread and one action type.

Only time is accelerated. Clearly distinguish fixture inputs from live integration behavior. Keep a short backup recording of the working flow.

## Evidence for the judging rubric

| Criterion | What to show |
| --- | --- |
| Core Requirements & Functionality | Start inside Teams, observe a real reply, approve inside Teams, and open the real resulting draft. |
| Innovation & Theme Alignment | A later reply materially changes the next action without Eric repasting context. |
| Technical Execution & Integration | Persistent state, source links, identity checks, fresh-context checks, duplicate prevention, and an honest retry/failure result. |
| Usefulness & Agentic Experience | A quiet agent that notices when help is needed and offers one specific, editable action. |

These are evidence targets, not predicted scores.

Test six cases: an explicit overdue commitment, a hypothetical suggestion, an unclear owner, a revised deadline, a partially or fully completed request, and repeated approval clicks. Record actual pass/fail results. Also demonstrate that a failed API call is reported as failed rather than completed.

Suggested outcome measures: correctly created approved follow-ups, unnecessary chasers avoided, and time needed to review a suggestion. Report measured results only; a hackathon demo does not establish retention or long-term time savings.

## Build schedule

| Time | Deliverable |
| --- | --- |
| First hour | Teams input, approval response, and one real draft creation connected. |
| Hours 2–3 | Commitment extraction, state, thread polling, and deadline check. |
| Hours 4–5 | Changed-context behavior, editable approval, duplicate prevention, and error handling. |
| Hour 6 | Run evaluation cases and let two or three people try the interaction. |
| Final hour | Fix the largest observed problem, rehearse, record backup, and prepare the short case study. |

Cut live audio, multi-meeting coverage, a separate dashboard, CRM/Planner integration, and a second chat platform from this prototype.

## Career and networking use

The Job Search OS supports a Toronto/Canada PM move grounded in enterprise operating experience and personal AI builds. This project can demonstrate problem selection, prioritization, a working workflow, and evaluation. Keep formal employment titles and personal-project ownership accurate, following the claim ledger (private local reference, not published) and career plan (private local reference, not published).

**Introduction:** "I'm Eric. I work on product planning for Rogers' in-building portfolio, and I build AI tools independently. Today I'm building a Teams agent that follows commitments and checks later replies before preparing a chaser. I'm exploring AI product and PM roles in Toronto."

If asked about the role, the formal Rogers title is Sr Network Designer; Product Manager describes the functional role. A Toronto-specific example available for a deeper conversation is the confirmed system planning and funding-allocation work for the Rogers Centre 5G upgrade.

**Discovery questions:** "Tell me about the last follow-up you had to chase after a meeting." Then: "How did you work out whether it still needed chasing?" After a demo: "What would you change before using this with your team?"

**Useful event targets:** three substantive conversations, two hands-on trials, and one agreed follow-up. These are flexible intentions, not a contact quota. Be explicit about looking for a product role when it becomes relevant; ask about the work and team needs.

**Follow-up template:** "Good meeting you at AI Tinkerers. Your point about [specific issue] helped me change [specific behavior]. Here's the short demo: [link]. As mentioned, I'm exploring AI product / PM roles in Toronto. I'd be interested to continue our conversation about [specific team or problem]."

Capture one short demo, one page explaining the user/problem/scope trade-off, the actual evaluation results, and one change prompted by feedback. Record new contacts and agreed next actions in the existing Job Search OS tracker after the event. Nothing has been sent or added to those trackers by this planning task.
