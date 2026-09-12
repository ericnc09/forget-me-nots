import "dotenv/config";
import { randomUUID } from "node:crypto";
import { createDefaultAgent } from "../app/agent";

const agent = createDefaultAgent();
agent.threadId = randomUUID();
agent.setMessages([
  {
    id: randomUUID(),
    role: "user",
    content: "Hello. Reply with one short greeting.",
  },
]);

let output = "";
let failure: string | undefined;
const timeout = setTimeout(() => {
  console.error("Agent greeting FAIL: timed out after 60 seconds.");
  process.exit(1);
}, 60_000);

try {
  await agent.runAgent({}, {
    onTextMessageContentEvent({ event }) {
      output += event.delta;
    },
    onRunErrorEvent({ event }) {
      failure = event.code ?? "RUN_ERROR";
    },
  });
  if (failure) throw new Error(failure);
  if (!output.trim()) throw new Error("No agent text returned.");
  console.log(`Agent greeting PASS: received ${output.trim().length} characters.`);
  clearTimeout(timeout);
  process.exit(0);
} catch (error) {
  clearTimeout(timeout);
  // Provider errors can include request details. Print only the error type.
  console.error(`Agent greeting FAIL: ${error instanceof Error ? error.name : "unknown error"}. Check agent service logs locally.`);
  process.exit(1);
}
