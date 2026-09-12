import { google } from "googleapis";

const DRIVE_READONLY_SCOPE =
  "https://www.googleapis.com/auth/drive.readonly";

export function isGoogleDriveConfigured(): boolean {
  return Boolean(
    process.env.GOOGLE_SERVICE_ACCOUNT_JSON &&
      process.env.GOOGLE_DRIVE_FILE_ID,
  );
}

function requiredGoogleDriveEnv(name: string): string {
  const value = process.env[name];
  if (!value) {
    throw new Error(
      `Missing ${name}. Add it to the repository root .env file to enable Google Drive.`,
    );
  }
  return value;
}

function serviceAccountCredentials(): Record<string, unknown> {
  const raw = requiredGoogleDriveEnv("GOOGLE_SERVICE_ACCOUNT_JSON");

  try {
    return JSON.parse(raw) as Record<string, unknown>;
  } catch {
    throw new Error(
      "GOOGLE_SERVICE_ACCOUNT_JSON must contain valid service-account JSON.",
    );
  }
}

/** Read the configured Markdown file as a regular Google Drive blob. */
export async function readMarkdownFile(): Promise<string> {
  const auth = new google.auth.GoogleAuth({
    credentials: serviceAccountCredentials(),
    scopes: [DRIVE_READONLY_SCOPE],
  });
  const drive = google.drive({ version: "v3", auth });
  const fileId = requiredGoogleDriveEnv("GOOGLE_DRIVE_FILE_ID");

  const response = await drive.files.get(
    { fileId, alt: "media" },
    { responseType: "text" },
  );

  if (typeof response.data !== "string") {
    throw new Error("Google Drive returned non-text content for the Markdown file.");
  }

  return response.data;
}
