"use client";

import Chat from "@/components/chat";
import {
  CopilotChatConfigurationProvider,
  CopilotThreadsDrawer,
  CopilotKitProvider,
} from "@copilotkit/react-core/v2";
import styles from "./page.module.css";

export const dynamic = "force-dynamic";

export default function Home() {
  return (
    <CopilotKitProvider runtimeUrl="/api/copilotkit" useSingleEndpoint={false}>
      <CopilotChatConfigurationProvider agentId="a2a_chat">
        <div className={`${styles.layout} threadsLayout`}>
          <CopilotThreadsDrawer agentId="a2a_chat" />
          <main className={styles.mainPanel}>
            <div className="relative flex min-h-dvh overflow-hidden bg-[#DEDEE9] p-2">
              <div
                className="absolute left-[1040px] top-[11px] z-0 h-[445px] w-[445px] rounded-full"
                style={{ background: "rgba(255, 172, 77, 0.2)", filter: "blur(103px)" }}
              />
              <div
                className="absolute bottom-[-100px] right-[-100px] z-0 h-[609px] w-[609px] rounded-full"
                style={{ background: "#C9C9DA", filter: "blur(103px)" }}
              />

              <div className="relative z-10 flex min-h-[calc(100dvh-1rem)] w-full flex-col overflow-hidden rounded-lg border-2 border-white bg-white/50 shadow-elevation-lg backdrop-blur-md">
                <header className="border-b border-[#DBDBE5] p-6 max-lg:pl-16">
                  <h1 className="mb-1 text-2xl font-semibold text-[#010507]">
                    Forget-me-nots Assistant
                  </h1>
                  <p className="text-sm leading-relaxed text-[#57575B]">
                    A single assistant to help you pick up work where you left off.
                  </p>
                </header>
                <div className="flex-1 overflow-hidden">
                  <Chat />
                </div>
              </div>
            </div>
          </main>
        </div>
      </CopilotChatConfigurationProvider>
    </CopilotKitProvider>
  );
}
