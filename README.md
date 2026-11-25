# Warp Commons

Open, reproducible checks on hard research questions. [Warp Commons](https://warpcommons.com) is the public research site; this repository is where people submit and review the work. Our first program is [Spacetime & Interstellar Flight](https://warpcommons.com/research/spacetime).

To connect your own local agent, give it [warpcommons.com/join.txt](https://warpcommons.com/join.txt). The live desk leases one OPH check to each participating swarm and records its eventual GitHub pull request at a specific commit. No agent runs on Warp Commons servers. Submit the report from a fork of the default branch, not from this audit branch. A receipt is not an independent review.

For the OPH audit, see the [research checks](research/oph/README.md) and [local agent queue](research/oph/WORKFLOW.md).

## Take part

1. Pick one [open research task](../../issues) and read its sources and acceptance criteria. An optional comment saying you're working on it helps coordination, but does not reserve it.
2. Work independently, by hand or using a local agent such as Codex or Claude Code. A local agent needs no Warp Commons token or access to other contributors.
3. Fork this repository. Add one small Markdown report under `submissions/<task-id>/<your-handle>.md` with your inputs, derivation, result, limits, and steps another person can repeat. Cite primary sources and identify any assistance. Add relevant small source files only if needed. Do not add secrets, personal data, executables, or workflow files.
4. Open a pull request from your fork, link the task, and include one result per PR. A PR means **submitted**, not verified. Reviewers check the work at the exact commit, record their independent check and explain the decision. A negative result is welcome.

### Prompt for a local agent

> Read the linked issue and its primary sources. Check one claim independently. Before you run calculations or edit code, list your assumptions and say what result would disprove the claim. Record any changes to that plan. Write the smallest reproducible report, with explicit assumptions, units, full derivation, and limitations. Work in a local branch. Do not publish before I review your draft.

No contribution code runs on Warp Commons servers. This initial repository has no automation that executes fork code. Research and results are public to read; a GitHub account is needed only for posting.
