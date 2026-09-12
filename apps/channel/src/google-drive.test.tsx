import assert from "node:assert/strict";
import { afterEach, test } from "node:test";

import {
  isGoogleDriveConfigured,
  readMarkdownFile,
} from "./google-drive";

const originalServiceAccount = process.env.GOOGLE_SERVICE_ACCOUNT_JSON;
const originalFileId = process.env.GOOGLE_DRIVE_FILE_ID;

afterEach(() => {
  if (originalServiceAccount === undefined) {
    delete process.env.GOOGLE_SERVICE_ACCOUNT_JSON;
  } else {
    process.env.GOOGLE_SERVICE_ACCOUNT_JSON = originalServiceAccount;
  }

  if (originalFileId === undefined) {
    delete process.env.GOOGLE_DRIVE_FILE_ID;
  } else {
    process.env.GOOGLE_DRIVE_FILE_ID = originalFileId;
  }
});

test("Google Drive is configured only when both required values are present", () => {
  delete process.env.GOOGLE_SERVICE_ACCOUNT_JSON;
  delete process.env.GOOGLE_DRIVE_FILE_ID;
  assert.equal(isGoogleDriveConfigured(), false);

  process.env.GOOGLE_SERVICE_ACCOUNT_JSON = "{}";
  assert.equal(isGoogleDriveConfigured(), false);

  process.env.GOOGLE_DRIVE_FILE_ID = "markdown-file-id";
  assert.equal(isGoogleDriveConfigured(), true);
});

test("invalid service-account JSON fails before making a Drive request", async () => {
  process.env.GOOGLE_SERVICE_ACCOUNT_JSON = "not-json";
  process.env.GOOGLE_DRIVE_FILE_ID = "markdown-file-id";

  await assert.rejects(
    readMarkdownFile(),
    /GOOGLE_SERVICE_ACCOUNT_JSON must contain valid service-account JSON/,
  );
});
