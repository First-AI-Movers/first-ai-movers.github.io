# AGENTS.md — `first-ai-movers.github.io`

Instruction surface for any AI coding agent working in this repository. It is
deliberately thin: `README.md` already carries this repository's scope discipline,
file inventory and validation checklist, and restating them here would create two
owners for one fact. Read it.

## The two things the README does not say

**A merge deploys.** This repository *is* the live site at
<https://first-ai-movers.github.io/>. A push to `main` publishes through GitHub
Pages — there is no staging step and no build to fail first. A broken link, a
malformed `sitemap.xml` or an invalid JSON-LD block is live the moment it merges,
so run the README's **Validation** list before you commit, not after.

**This is a public repository, and its whole job is a boundary.** The README's
**Scope discipline** section is the load-bearing rule: this bridge links only to
public, verified surfaces, and the organization's private repositories are
deliberately not linked from it. Adding a link is not a formatting change — it is
a disclosure decision. The same applies to `llms.txt`, which is read by AI answer
engines and is where an internal detail would travel furthest.

## PR lifecycle

Open the PR ready, arm squash auto-merge in the same step while the gate is still
pending (GitHub refuses to arm an already-mergeable PR), do not request review, do
not wait. `aeos-merge-ready` — the organization's required verdict, served from
`First-AI-Movers/.github` — is the one merge-blocking check.

An admitted Issue is the authorization for the work it describes. There are no
authorization levels and no per-turn approval phrases. Ask a person only for
something genuinely human-only: a domain or DNS change, a new legal or financial
commitment, or publishing something whose disclosure decision has not been made.

When an owned next effect is temporarily blocked on a routine dependency — a
pending PR, a gate run, an AI review, or another owner — do exactly one of:
(a) execute the next dependency-ready effect; (b) send one bounded
GitHub-native handoff (an Issue or PR comment) to the existing known owner and
continue disjoint work; or (c) persist a typed wake predicate and yield to the
existing continuation machinery, which wakes exactly one successor when the
predicate changes (`DEPENDENCY_WAIT_PERSISTS_WAKE_PREDICATE`). A successor
session reconstructs from GitHub Issues, PRs and current `main` alone — no
transcript, no operator copy-paste, no operator relay
(`SESSION_ROLLOVER_RECONSTRUCTS_FROM_GITHUB`). A pending PR, gate, or review
state is never a session terminal and never a reason to return to the operator
for `continue`.

## Constraints the stack imposes

Static HTML and CSS. **No JavaScript, no build system, no framework, no external
dependency, system fonts only.** That is a deliberate property of a bridge page,
not an omission waiting to be fixed — adding a bundler or a font CDN would be a
regression. Keep one `<h1>` and a monotonic heading order.

## Where durable canon lives

Live work state — what is planned, blocked or done — is in GitHub Issues, not in
this repository. Organization-wide contribution and security defaults come from
`First-AI-Movers/.github`.
