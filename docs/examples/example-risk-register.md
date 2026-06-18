# Example AI Risk Register

This is a lightweight example. Adapt it to your review scope.

| ID | Severity | Area | Risk | Evidence | Impact | Required action | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-001 | Critical | RAG access control | Vector index contains HR and customer documents without user-level permission filtering at retrieval time. | Architecture review, engineer interview | Cross-user or cross-department data leakage | Implement authorization-filtered retrieval or split indexes before production. | Engineering | Open |
| R-002 | High | Evaluation | Eval set has 40 hand-picked examples and no adversarial, ambiguous, or permission-boundary cases. | Eval notebook | Quality claims are not reliable | Build representative eval suite with release thresholds. | ML lead | Open |
| R-003 | High | Vendor dependency | Product depends on one model provider with no tested fallback. | Architecture review | Outage or model change can break core workflow | Add fallback model and regression testing across providers. | CTO | Planned |
| R-004 | Medium | Governance | No documented AI incident process. | Policy review | Slow response to unsafe or incorrect outputs | Add AI incident categories, escalation, and disable path. | Security | Open |
| R-005 | Medium | Cost | No budget alerts for LLM usage spikes. | Cloud billing review | Cost-exhaustion risk | Add rate limits and cost alerts. | Platform | Open |
| R-006 | Low | UX | Users are not clearly told when answers are source-grounded vs inferred. | Product walkthrough | Misplaced trust in generated answers | Add answer labels and source inspection. | Product | Backlog |

## Severity Calibration

- **Critical:** blocks launch, acquisition close, or investment thesis.
- **High:** requires signed remediation plan or explicit risk acceptance.
- **Medium:** should be remediated within normal planning cycle.
- **Low:** track as improvement.


--8<-- "_includes/cta.md"
