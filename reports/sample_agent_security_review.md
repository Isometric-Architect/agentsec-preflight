# Sample Agent Security Review

## Summary

This sample review shows how AgentSec Preflight can turn synthetic runtime descriptors into local PASS/HOLD/BLOCK reports before an AI agent attempts a tool call.

## What Was Inspected

- OpenClaw-like tool surfaces: web search, shell exec, browser login, message send.
- Hermes-like skill surfaces: skill creation, skill install, scheduled automation, memory write.
- MCP-like protocol surfaces: read-only database query, external side-effect tool, payment tool, deploy tool.

## PASS Examples

- Read-only web search with source receipt.
- Read-only database query with schema, scope, and receipt.

## HOLD Examples

- Exec write without diff review or rollback plan.
- Browser login or form submit without credential boundary and approval.
- Skill install without source trace and review.
- Scheduled automation without operator policy and cancel path.

## BLOCK Examples

- Payment tool call without separate authorization.
- Deploy tool call without explicit approval and rollback.
- No-match fallback to pretrained memory for runtime schema or action availability.

## Key Risk Families

- draft-to-send confusion
- read-tool-to-write-tool confusion
- browser-read-to-form-submit confusion
- exec-readonly-to-exec-write confusion
- scheduled task without operator policy
- payment or deploy without approval
- no-match to pretrained-memory fallback

## Required Human Review

Human review is required for external sends, credentialed browser actions, shell writes, skill installation, scheduled automation, payment, deploy, merge, and other external side-effect actions.

## Receipts Generated

The sample reports link to no-action, hold, block, and pass/draft-only receipt examples. Receipts record what happened, what did not happen, and what must not be claimed.

## Scope

This is local synthetic fixture material. It does not run OpenClaw, Hermes, MCP servers, live tools, browsers, accounts, or external systems.

## Not A Security Certification

This sample review is a local preflight report example. Final deployment, security review, legal review, and action authorization stay with the operator workflow.

## Next Safe Actions

- Use the fixtures to test report parsing and PASS/HOLD/BLOCK interpretation.
- Add project-specific descriptors before any real runtime evaluation.
- Request separate approval before read-only source clone or live sandbox work.
