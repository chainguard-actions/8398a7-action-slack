<!-- markdownlint-disable -->

# Hardening Report: 8398a7--action-slack/v3.19.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **8398a7--action-slack/v3.19.0** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### unpinned-uses (severity: high)

All workflow files use mutable tag or branch refs instead of pinned 40-character commit SHAs, making them vulnerable to supply-chain attacks if the referenced action tags are moved or compromised.

release.yml: uses: actions/checkout@v2 (line 13), uses: actions/create-release@v1 (line 15)

slack-mainline.yml: uses: 8398a7/action-slack@v3 (lines 12, 18, 24, 30, 36, 47, 89, 101, 107, 113)

slack-pre.yml: uses: 8398a7/action-slack@pre (lines 12, 18, 24, 30, 41, 65, 79, 85, 91, 101)

test-build.yml: uses: actions/checkout@v2 (line 7), uses: actions/setup-node@v2 (line 8), uses: actions/cache@v4 (line 10), uses: codecov/codecov-action@v4 (line 22), uses: 8398a7/action-slack@v3 (line 25), uses: actions/checkout@v1 (line 36), uses: actions/setup-node@v2 (line 38), uses: actions/cache@v4 (line 40)

uncommitted.yml: uses: actions/checkout@v2 (line 9), uses: actions/setup-node@v2 (line 10), uses: actions/cache@v4 (line 12)

Locations:

- `.github/workflows/release.yml:13`
- `.github/workflows/release.yml:15`
- `.github/workflows/slack-mainline.yml:12`
- `.github/workflows/slack-pre.yml:12`
- `.github/workflows/test-build.yml:7`
- `.github/workflows/uncommitted.yml:9`

### missing-permissions (severity: medium)

None of the workflow files define a top-level `permissions:` block, and no individual job defines its own `permissions:` block. Without explicit permissions, workflows run with the default (potentially broad) token permissions, violating the principle of least privilege.

Locations:

- `.github/workflows/release.yml:1`
- `.github/workflows/slack-mainline.yml:1`
- `.github/workflows/slack-pre.yml:1`
- `.github/workflows/test-build.yml:1`
- `.github/workflows/uncommitted.yml:1`

## Iteration Notes

### Iteration 1

**Fixes applied:** unpinned-uses, missing-permissions

**Notes:**

Fixed all 5 workflow files:

1. release.yml: Pinned actions/checkout@v2 → SHA 0717577d..., actions/create-release@v1 → SHA 0cb9c9b6...; added `permissions: contents: write` (needed to create GitHub releases).

2. slack-mainline.yml: Pinned all 10 uses of 8398a7/action-slack@v3 → SHA 77eaa4f1...; added `permissions: {}`.

3. slack-pre.yml: Pinned all 10 uses of 8398a7/action-slack@pre → SHA b7b7b004...; added `permissions: {}`.

4. test-build.yml: Pinned actions/checkout@v2 → SHA 0717577d..., actions/checkout@v1 → SHA 50fbc622..., actions/setup-node@v2 → SHA 7c12f801..., actions/cache@v4 → SHA 0057852b..., codecov/codecov-action@v4 → SHA b9fd7d16..., 8398a7/action-slack@v3 → SHA 77eaa4f1...; added `permissions: {}`.

5. uncommitted.yml: Pinned actions/checkout@v2 → SHA 0717577d..., actions/setup-node@v2 → SHA 7c12f801..., actions/cache@v4 → SHA 0057852b...; added `permissions: {}`.

