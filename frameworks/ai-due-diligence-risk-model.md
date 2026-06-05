# AI Due Diligence Risk Model

Use this model to classify AI systems before deployment, acquisition, or investment. It is deliberately simple enough to use in a real review meeting.

## Scoring

Score each dimension from 1 to 5.

- **1:** low risk, limited scope, easy rollback
- **2:** manageable risk, standard controls sufficient
- **3:** material risk, formal review required
- **4:** high risk, executive sign-off and strong controls required
- **5:** severe risk, block unless exceptional evidence exists

## Dimensions

| Dimension | 1 | 3 | 5 |
| --- | --- | --- | --- |
| Business criticality | Convenience feature | Important workflow | Core revenue, safety, legal, or operational function |
| User impact | Internal productivity | Customer-facing decisions | Material effect on rights, money, access, safety, or employment |
| Autonomy | Suggests only | Human approval expected | Acts automatically or triggers downstream action |
| Data sensitivity | Public data | Confidential business data | Regulated, personal, financial, health, legal, or security-sensitive data |
| Security exposure | Internal only | Authenticated external users | Public, multi-tenant, tool-using, or privileged system |
| Regulatory exposure | Minimal | Sector or contract obligations | AI Act, GDPR, employment, credit, healthcare, safety, financial, or public-sector exposure |
| Model dependency | Replaceable model | Provider-specific behavior | Vendor/model lock-in with weak fallback |
| Observability | Full logs and evals | Partial monitoring | Little visibility into behavior or failures |
| Reversibility | Easy rollback | Operational friction | Hard to reverse decisions, outputs, or customer impact |

## Rating Bands

| Total score | Rating | Expected action |
| --- | --- | --- |
| 9-15 | Low | Standard engineering review |
| 16-25 | Medium | Formal AI review and documented controls |
| 26-35 | High | Executive sign-off, security/legal review, monitoring, incident plan |
| 36-45 | Critical | Block or restrict to controlled pilot until evidence improves |

## Override Rules

Automatically escalate to high or critical if any of these are true:

- system affects legal, credit, employment, healthcare, education, insurance, housing, or public-sector outcomes
- system can execute actions without human approval
- system handles sensitive data and uses external model providers
- system uses RAG across mixed-permission corpora
- system is part of an acquisition valuation claim
- vendor cannot explain evaluation methodology
- there is no rollback path
- security review identifies unauthorized data access

## Review Output

| Dimension | Score | Evidence | Notes |
| --- | --- | --- | --- |
| Business criticality |  |  |  |
| User impact |  |  |  |
| Autonomy |  |  |  |
| Data sensitivity |  |  |  |
| Security exposure |  |  |  |
| Regulatory exposure |  |  |  |
| Model dependency |  |  |  |
| Observability |  |  |  |
| Reversibility |  |  |  |
| **Total** |  |  |  |

## Opinionated Guidance

If the system scores high on autonomy, sensitive data, and weak observability, do not debate whether the demo is impressive. Restrict scope first. Evidence can earn back trust later.

