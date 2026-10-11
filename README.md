# 🌌 Quantum Multiversal Nexus

## Purpose

Quantum Multiversal Nexus is the ecosystem map and manifest coordination layer for the Sovereign repositories. It describes intended architecture and displays independently sourced status; it does not independently prove that a runtime, quantum backend, business, repository, or hardware device is operational.

> **Current evidence posture:** repository documentation and integration contracts are being established. Do not interpret this README as proof of deployed services, connected quantum hardware, measured quantum coherence, or passing tests unless linked evidence independently supports each claim.

## Evidence-first status policy

Use the shared labels in [the Sovereign Event Contract v1](docs/sovereign-event-contract-v1.md):

- **PROPOSED** — planned capability or architecture.
- **SIMULATED** — synthetic/modelled/emulated behavior.
- **DEMONSTRATED** — reproducibly observed behavior in a stated test environment.
- **MEASURED** — raw observation tied to an identified source or instrument.
- **UNVERIFIED** — reported but not independently substantiated.
- **VALIDATED** — a named acceptance criterion passed with evidence references.

A missing, stale, or invalid report is **UNKNOWN**, not healthy. Never infer a green status from a directory name, an activation script, a README assertion, or a successful process launch alone.

## Repository boundaries

| Repository | Authoritative responsibility |
|---|---|
| [photonic-codex](https://github.com/onegayunicorn/photonic-codex) | Local operations, dashboard, event capture, and provenance |
| [unicorn-sovereign-platform](https://github.com/onegayunicorn/unicorn-sovereign-platform) | Runtime modules, AI orchestration, sandbox and simulation evidence |
| quantum-multiversal-nexus | Ecosystem manifests, architecture maps, cross-repository status presentation |

Repositories retain their own histories, releases, tests, and claims. Nexus mirrors reports and links to their original evidence; it does not overwrite source evidence.

## Integration phases

1. **Read-only contracts:** validate shared JSON fixtures and schema versions.
2. **Read-only status:** fetch health and capability reports from configured, authenticated endpoints. Stale or failed requests show UNKNOWN/UNAVAILABLE.
3. **Event mirrors:** retain source event IDs, labels, timestamps, and revision/provenance metadata.
4. **Coordinated operations:** out of scope until separately designed, threat-modelled, explicitly approved, and tested.

## Activation scripts

Scripts are not proof of activation. Before any script is treated as operational, it must provide a dry-run mode, dependency checks, least-privilege execution, bounded timeouts, safe shutdown, and tests. The v1 integration contract does not authorize commands or remote writes.

## Shared protocol

See [docs/sovereign-event-contract-v1.md](docs/sovereign-event-contract-v1.md). The document is a proposed contract; live interoperability is not yet established.
