# FollowThrough: competitor findings and text-first scope

For the consolidated implementation instructions, use [the standalone build prompt](./followthrough-build-prompt.md). It incorporates the later requirement that task tracking and a two-week review are core, and makes email sending structurally unavailable. The research below records the earlier scope discussion.

Checked September 11, 2026 against official product documentation and announcements. This is a documentation comparison, not hands-on testing. No prototype or external integration was created in this research task.

## Finding

The broad idea already exists. Native Slack email actions, Microsoft agents, and configurable assistants overlap substantially with chat/meeting-to-email follow-up. Automatic triggering, email drafting, and cross-app context are not individually novel. The hackathon opportunity is a focused interaction that resolves a real request accurately and demonstrates what happens when context is ambiguous or has changed.

## Closest products

| Product | Documented behavior | Distinction to keep clear |
| --- | --- | --- |
| **Slackbot** | Can draft email directly in Google Workspace or Microsoft 365 from a request in Slack. The announcement identifies availability on specified Enterprise plans. | Native chat-to-email overlap. The reviewed page does not establish passive detection of an ordinary manager message or automatic matching to the correct existing email conversation. [Official release](https://slack.com/blog/news/slack-feature-drop-april2026) |
| **Microsoft Copilot in Outlook** | Agentic Outlook can identify unanswered email and draft follow-ups on request. | Close overlap with chasers. The documented agentic experience is Frontier preview. [Product announcement](https://techcommunity.microsoft.com/blog/outlook/copilot-in-outlook-new-agentic-experiences-for-email-and-calendar/4514601), [preview support](https://support.microsoft.com/en-us/outlook/use-microsoft-365-copilot-in-outlook-to-manage-your-inbox-frontier) |
| **Microsoft Sales agent in Teams** | A meeting recap can generate a summary/follow-up email and open it in Outlook web. | A documented meeting-driven workflow; it requires the relevant meeting, transcription, and Sales configuration. [Official instructions](https://learn.microsoft.com/en-us/microsoft-sales-copilot/view-meeting-summary-recap) |
| **Microsoft Scout** | A broader background agent spanning Teams, Outlook, files, and other tools. Current docs describe mail and Teams actions with approval. | Significant conceptual competition. It is a preview/experimental Frontier offering; a particular tenant may not have access. [Introduction](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/), [current capabilities](https://learn.microsoft.com/en-us/microsoft-scout/work-with-microsoft-365) |
| **Lindy** | Routines can trigger on Slack messages, apply natural-language filters, and support follow-ups. Its email routines create Gmail/Outlook drafts and bumps for unanswered email. | Closest configurable competitor. Combining these capabilities into the exact manager-request-to-email-thread workflow would require setup and validation. [Routines](https://docs.lindy.ai/teammate/routines), [email drafting](https://docs.lindy.ai/features/inbox-management/email-drafting) |
| **Fyxer** | Prepares replies in Gmail/Outlook; its notetaker joins Teams, Zoom, or Google Meet and suggests follow-up drafts. | Close to the original meeting-assistant idea. The reviewed help page does not document an ordinary Teams-text-message trigger. [Official help](https://support.fyxer.com/article/meet-fyxer-your-ai-email-and-meeting-assistant) |
| **Otter** | Its Gmail connector lets users cross-reference meetings and emails, check whether a follow-up was sent, and draft/send meeting follow-ups from Otter AI Chat. | Cross-app follow-through already exists here too. The documented interaction is user-requested; the source does not confirm automatic Teams-text triggers or exact threaded-draft placement. [Official connector announcement](https://otter.ai/blog/otter-can-now-pull-from-and-send-to-gmail) |

An undocumented capability should be treated as unverified, not absent. These findings do not establish an unoccupied market niche.

## Revised product interaction

One-time setup: Eric enables the agent in one test Teams group chat and connects his test Outlook mailbox. Configure which test participant represents the manager and which user should receive drafts.

**Manager:** "Eric, can you chase Maya on the revised quote for the Northstar rollout?"

The agent detects a request directed to Eric, reads the nearby discussion, and searches recent email for the project, correspondent, and topic. It retrieves the relevant conversation, including later replies and sent messages, and checks whether the request is still outstanding.

- **One clear existing conversation:** create an actual reply draft automatically, with verified recipients, then privately notify Eric: "Draft ready in ‘Northstar rollout — revised quote’. Open draft / Edit / Wrong thread."
- **Multiple plausible conversations:** ask Eric to choose between concise subject/sender/date options before writing to the mailbox.
- **No matching conversation:** create a new draft only when recipient and purpose are clear. Otherwise ask for the missing detail.
- **Already answered:** explain that the relevant answer has arrived and link it. Avoid an unnecessary chaser.

Automatically preparing a private draft removes a redundant approval step. Eric reviews and sends from Outlook. The prototype does not need an email-send permission or a Send button in Teams.

The agent should not copy internal manager commentary into an external email. Repeated message events should update or reuse the same agent draft, not create duplicates; do not overwrite a draft after Eric edits it. Show any partial failure accurately.

## Technical feasibility

Microsoft Graph supports reading messages from a specified Teams chat and subscribing to message changes. For a one-day prototype, polling a single opted-in chat is a reasonable fallback if webhook setup consumes too much time. A channel thread and a group chat use different resource paths; choose the group chat for this scenario. [Read chat messages](https://learn.microsoft.com/en-us/graph/api/chat-list-messages?view=graph-rest-1.0), [change notifications](https://learn.microsoft.com/en-us/graph/teams-changenotifications-chatmessage).

Search and retrieval should operate only in the connected user's mailbox. Relevant Graph capabilities include [email search](https://learn.microsoft.com/en-us/graph/search-concept-messages) and message conversation metadata. The difficult product behavior is choosing the right conversation, not simply generating prose.

| Desired result | Microsoft Graph action |
| --- | --- |
| Reply draft to an existing email | `POST /me/messages/{id}/createReply` |
| Reply-all draft when those recipients are appropriate | `POST /me/messages/{id}/createReplyAll` |
| New email draft | `POST /me/messages` |

Use the reply APIs to maintain the relationship to the original message; adding `Re:` to a new subject does not provide that relationship. Validate To/CC explicitly, especially when the last message was sent by Eric. These examples assume delegated access; application access uses an explicit user path. Draft creation uses `Mail.ReadWrite`; sending is a separate operation. [Reply draft](https://learn.microsoft.com/en-us/graph/api/message-createreply?view=graph-rest-1.0), [reply-all draft](https://learn.microsoft.com/en-us/graph/api/message-createreplyall?view=graph-rest-1.0), [new draft](https://learn.microsoft.com/en-us/graph/api/user-post-messages?view=graph-rest-1.0).

Keep the implementation to a small service, one model, a small state store, Teams, and Outlook. Verify mailbox and chat access before building interpretation logic. A Microsoft 365 test tenant with app permissions still requires the actual relevant grants and working services.

## What to show tomorrow

1. Seed the real test mailbox with two plausible vendor conversations.
2. Send an ordinary manager request in the opted-in Teams chat.
3. Show the agent select the right conversation and create a real threaded reply draft.
4. Run an ambiguous request and show the short clarification instead of a wrong draft.
5. Run a request that has already been answered in email and show the answer surfaced instead of a chaser.

Existing-thread drafting is the main demonstration. New-email drafting is the secondary branch. Live audio, long-term deadline monitoring, multi-chat coverage, and other platforms remain later scope. Meeting transcripts can eventually feed the same interpretation and action layer.

For the rubric, the strongest evidence is correct use of identities, changing context, email conversation history, and actual tool execution. For PM conversations, explain the automatic-draft/manual-send choice, the ambiguity behavior, and measured errors. This is a credible execution and product-judgment story; avoid claiming to have invented AI follow-up.

**Pitch:** "When a manager asks for a follow-up in Teams, FollowThrough finds the right email conversation, checks what still needs doing, and prepares the draft where you'll send it."
