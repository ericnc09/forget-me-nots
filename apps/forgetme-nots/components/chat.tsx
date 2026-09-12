"use client";

import { CopilotChat } from "@copilotkit/react-core/v2";

/** Main chat interface shared by the web UI and the single assistant. */
export default function Chat() {
  return (
    <CopilotChat
      labels={{
        modalHeaderTitle: "Forget-me-nots Assistant",
        welcomeMessageText:
          "👋 Hi! I’m your assistant. Tell me what you’re working on and I’ll help you pick up where you left off.",
      }}
      className="h-full"
    />
  );
}
