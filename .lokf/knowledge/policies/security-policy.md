---
type: Policy
id: https://w3id.org/lmodel/nist-csf-v2/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, and the three repository settings that are not yet in force.
resource: SECURITY.md
sources:
  - id: security.md
    resource: SECURITY.md
    title: every section
  - id: dependabot.yml
    resource: .github/dependabot.yml
    title: the three update entries
generated:
  by: process:ktl-librarian
  at: "2026-10-29T21:41:10Z"
status: draft
---

# Security policy

`SECURITY.md` asks for a vulnerability to be reported through GitHub's private vulnerability reporting, not in a public issue. It says that one person maintains the repository, so a first reply takes days and there is no bounty, and that only the latest release receives fixes.[^security.md]

The repository releases the schema, the Python models generated from it, and the adapt copy as a release asset; nothing is published to PyPI. Its table of surfaces names each workflow and what holds it. The pull request checks run read-only. The release job runs only on a push to `main`, in the `release` Environment. The website's deploy job alone holds the Pages scopes. The upstream watch writes only issues. The librarian's agent runs without a write token, and its `publish` job runs no agent.

Every workflow declares `permissions: {}` at the top, pins its actions to commit hashes and runs harden-runner in audit mode. Dependabot keeps the pins, the package's lock and the sidecar's lock current, each monthly.[^dependabot.yml] The policy says that three settings are not yet in force: required reviewers on the `release` Environment, a rule against deleting or force-pushing `main`, and secret scanning with push protection. It leaves out the CSF itself, LinkML, a compromised runner or harness, and whether the knowledge bundle is true.

[^security.md]: SECURITY.md, every section
[^dependabot.yml]: .github/dependabot.yml, the three entries
