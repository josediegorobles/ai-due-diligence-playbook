# AI Technical Due Diligence Report Template

Use this for acquisition, investment, board review, vendor selection, or production approval.

## 1. Executive Summary

**Subject:**  
**Review date:**  
**Reviewer(s):**  
**Review scope:**  
**Recommended decision:** Approve / approve with controls / pilot only / block / do not invest / do not acquire

### Bottom Line

Write the decision in plain language. Avoid vague language.

Example:

> The system is commercially promising but not production-ready for regulated customer workflows. The main blockers are missing evaluation evidence, weak tenant-level retrieval controls, and no incident process for AI-specific failures.

### Top Findings

| Severity | Finding | Business impact | Required action |
| --- | --- | --- | --- |
| Critical |  |  |  |
| High |  |  |  |
| Medium |  |  |  |

## 2. Scope

### In Scope

- systems reviewed
- repositories reviewed
- vendor documentation reviewed
- interviews conducted
- environments inspected
- datasets or evals reviewed

### Out of Scope

- legal opinion
- full penetration test
- full code audit
- financial audit
- model training reproduction
- items not made available

## 3. System Overview

| Area | Summary |
| --- | --- |
| Use case |  |
| Users |  |
| AI components | LLM / RAG / agent / classifier / recommender / computer vision / other |
| Model providers |  |
| Data sources |  |
| Deployment model |  |
| External dependencies |  |
| Autonomy level | Advisory / assisted / approval-gated / automated |

Include a simple architecture diagram or link.

## 4. Evidence Reviewed

| Evidence | Provided | Quality | Notes |
| --- | --- | --- | --- |
| Architecture diagram | Yes / no | Strong / weak |  |
| Data flow diagram | Yes / no | Strong / weak |  |
| Model documentation | Yes / no | Strong / weak |  |
| Eval results | Yes / no | Strong / weak |  |
| Security documentation | Yes / no | Strong / weak |  |
| Incident history | Yes / no | Strong / weak |  |
| Vendor contracts | Yes / no | Strong / weak |  |
| Compliance mapping | Yes / no | Strong / weak |  |

## 5. Technical Assessment

### Architecture

- key design choices
- strengths
- weaknesses
- scalability constraints
- operational dependencies

### Model and Prompt Layer

- model selection rationale
- prompt management
- versioning
- known limitations
- regression process

### Data and Retrieval

- data sources
- data quality
- permissions
- RAG design
- retention
- lineage

### Evaluation

- eval methodology
- realism of eval set
- failure modes tested
- evidence of improvement
- release thresholds
- gaps

### Security

- threat model
- prompt injection risk
- data exfiltration risk
- tool/agent risk
- tenant isolation
- supply chain risk
- logging and secrets

### Operations

- monitoring
- alerting
- rollback
- incident response
- support workflow
- ownership

## 6. Governance and Compliance

Assess whether the organization can explain, control, monitor, and audit the system.

- AI inventory
- owner and accountability
- acceptable use policy
- human oversight
- change management
- audit logs
- user notices
- regulatory mapping
- third-party obligations

## 7. Risk Register

| ID | Severity | Risk | Evidence | Impact | Recommendation | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| R-001 | Critical |  |  |  |  |  |
| R-002 | High |  |  |  |  |  |
| R-003 | Medium |  |  |  |  |  |

Severity definitions:

- **Critical:** must block transaction, launch, or deployment until remediated.
- **High:** material risk requiring executive acceptance or concrete remediation plan.
- **Medium:** should be remediated but may not block if compensating controls exist.
- **Low:** track as normal engineering or governance debt.

## 8. Valuation or Deployment Impact

For investment/acquisition:

- Does the AI system create defensibility?
- Is the claimed moat real or just model access plus workflow UI?
- Are there hidden cloud/model costs?
- Is customer data a legitimate advantage?
- Are there regulatory or security liabilities?
- What must be rebuilt post-close?

For deployment:

- What controls are required before launch?
- What scope restrictions are needed?
- What monitoring must be in place?
- Who owns incident response?
- What rollback path exists?

## 9. Final Recommendation

Use direct language.

| Decision | Conditions |
| --- | --- |
| Approve |  |
| Approve with controls |  |
| Pilot only |  |
| Block |  |
| Do not acquire / invest |  |

## 10. Appendix

- reviewed documents
- interview notes
- open questions
- screenshots
- eval summaries
- source links

