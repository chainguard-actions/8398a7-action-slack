<!-- markdownlint-disable -->

# Hardening Report: 8398a7--action-slack/v3.17.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **8398a7--action-slack/v3.17.0** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### unpinned-uses (severity: high)

All 6 workflow files use mutable tag or branch refs in `uses:` steps instead of pinned 40-character SHA commit hashes. This exposes the workflows to supply-chain attacks where a compromised or updated tag could execute malicious code. Affected references include: `actions/checkout@v2`, `actions/checkout@v1`, `actions/setup-node@v2`, `actions/cache@v4`, `actions/create-release@v1`, `codecov/codecov-action@v4`, `8398a7/action-slack@v3`, and `8398a7/action-slack@pre`.

Locations:

- `.github/workflows/release.yml:10`
- `.github/workflows/release.yml:12`
- `.github/workflows/slack-mainline.yml:11`
- `.github/workflows/slack-mainline.yml:20`
- `.github/workflows/slack-mainline.yml:29`
- `.github/workflows/slack-mainline.yml:38`
- `.github/workflows/slack-mainline.yml:47`
- `.github/workflows/slack-mainline.yml:58`
- `.github/workflows/slack-mainline.yml:89`
- `.github/workflows/slack-mainline.yml:107`
- `.github/workflows/slack-mainline.yml:116`
- `.github/workflows/slack-mainline.yml:125`
- `.github/workflows/slack-pre.yml:11`
- `.github/workflows/slack-pre.yml:20`
- `.github/workflows/slack-pre.yml:29`
- `.github/workflows/slack-pre.yml:38`
- `.github/workflows/slack-pre.yml:47`
- `.github/workflows/slack-pre.yml:58`
- `.github/workflows/slack-pre.yml:89`
- `.github/workflows/slack-pre.yml:107`
- `.github/workflows/slack-pre.yml:116`
- `.github/workflows/slack-pre.yml:125`
- `.github/workflows/star.yml:8`
- `.github/workflows/test-build.yml:6`
- `.github/workflows/test-build.yml:7`
- `.github/workflows/test-build.yml:8`
- `.github/workflows/test-build.yml:19`
- `.github/workflows/test-build.yml:21`
- `.github/workflows/test-build.yml:33`
- `.github/workflows/test-build.yml:34`
- `.github/workflows/test-build.yml:35`
- `.github/workflows/uncommitted.yml:11`
- `.github/workflows/uncommitted.yml:12`
- `.github/workflows/uncommitted.yml:13`

### missing-permissions (severity: medium)

None of the 6 workflow files define a `permissions:` key at the top level or at the job level. Without explicit permissions, jobs run with the default GitHub token permissions, which may be overly broad (e.g., write access to repository contents). Each workflow should declare minimal required permissions using a top-level or per-job `permissions:` block.

Locations:

- `.github/workflows/release.yml:1`
- `.github/workflows/slack-mainline.yml:1`
- `.github/workflows/slack-pre.yml:1`
- `.github/workflows/star.yml:1`
- `.github/workflows/test-build.yml:1`
- `.github/workflows/uncommitted.yml:1`

## Iteration Notes

### Iteration 1

**Fixes applied:** unpinned-uses, missing-permissions

**Notes:**

Fixed all 6 workflow files: (1) Pinned all mutable tag/branch action references to full 40-character SHA commit hashes with inline tag comments for readability — actions/checkout@v2 → 0717577d, actions/checkout@v1 → 50fbc622, actions/setup-node@v2 → 7c12f801, actions/cache@v4 → 0057852b, actions/create-release@v1 → 0cb9c9b6, codecov/codecov-action@v4 → b9fd7d16, 8398a7/action-slack@v3 → 77eaa4f1, 8398a7/action-slack@pre → b7b7b004. (2) Added permissions blocks to all 6 workflows — release.yml gets `contents: write` (required for creating releases), all others get `permissions: {}` (no GitHub token permissions needed).

