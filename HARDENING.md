<!-- markdownlint-disable -->

# Hardening Report: 8398a7--action-slack/v3.18.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **8398a7--action-slack/v3.18.0** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### unpinned-uses (severity: high)

All `uses:` references across all workflow files use mutable tags or branch names instead of pinned 40-character commit SHAs, making the workflows vulnerable to supply-chain attacks if any referenced action is compromised or its tag is moved.

- release.yml: `actions/checkout@v2`, `actions/create-release@v1`
- slack-mainline.yml: `8398a7/action-slack@v3` (multiple steps)
- slack-pre.yml: `8398a7/action-slack@pre` (multiple steps)
- star.yml: `8398a7/action-slack@v3`
- test-build.yml: `actions/checkout@v2`, `actions/checkout@v1`, `actions/setup-node@v2` (×2), `actions/cache@v4` (×2), `codecov/codecov-action@v4`, `8398a7/action-slack@v3`
- uncommitted.yml: `actions/checkout@v2`, `actions/setup-node@v2`, `actions/cache@v4`

Locations:

- `.github/workflows/release.yml:9`
- `.github/workflows/release.yml:11`
- `.github/workflows/slack-mainline.yml:10`
- `.github/workflows/slack-pre.yml:10`
- `.github/workflows/star.yml:8`
- `.github/workflows/test-build.yml:6`
- `.github/workflows/test-build.yml:7`
- `.github/workflows/test-build.yml:8`
- `.github/workflows/test-build.yml:22`
- `.github/workflows/test-build.yml:25`
- `.github/workflows/uncommitted.yml:10`
- `.github/workflows/uncommitted.yml:11`
- `.github/workflows/uncommitted.yml:12`

### missing-permissions (severity: medium)

None of the 6 workflow files define a top-level `permissions:` block, and no individual job within any of these files defines a `permissions:` block either. Without explicit permissions, workflows run with the default (often broad) token permissions, violating the principle of least privilege.

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

Fixed all 6 workflow files:

1. release.yml: Pinned actions/checkout@v2 → SHA 0717577d, actions/create-release@v1 → SHA 0cb9c9b6. Added `permissions: contents: write` (needed to create releases).

2. slack-mainline.yml: Pinned all 10 occurrences of 8398a7/action-slack@v3 → SHA 77eaa4f1. Added `permissions: {}`.

3. slack-pre.yml: Pinned all 10 occurrences of 8398a7/action-slack@pre → SHA b7b7b004. Added `permissions: {}`.

4. star.yml: Pinned 8398a7/action-slack@v3 → SHA 77eaa4f1. Added `permissions: {}`.

5. test-build.yml: Pinned actions/checkout@v2 → SHA 0717577d, actions/checkout@v1 → SHA 50fbc622, actions/setup-node@v2 (×2) → SHA 7c12f801, actions/cache@v4 (×2) → SHA 0057852b, codecov/codecov-action@v4 → SHA b9fd7d16, 8398a7/action-slack@v3 → SHA 77eaa4f1. Added `permissions: {}`.

6. uncommitted.yml: Pinned actions/checkout@v2 → SHA 0717577d, actions/setup-node@v2 → SHA 7c12f801, actions/cache@v4 → SHA 0057852b. Added `permissions: {}`.

