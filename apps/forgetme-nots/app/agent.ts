import { HttpAgent } from "@ag-ui/client";

const orchestratorUrl = process.env.ORCHESTRATOR_URL || "http://localhost:9000";

/** Creates the one AG-UI agent shared by the web runtime and Channels. */
export function createDefaultAgent(): HttpAgent {
  return new HttpAgent({ url: orchestratorUrl });
}
