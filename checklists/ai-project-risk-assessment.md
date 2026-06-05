# AI Project Risk Assessment

Use this checklist before approving an AI project, pilot, production launch, acquisition target, or material vendor dependency.

## Decision Summary

| Field | Answer |
| --- | --- |
| System / project |  |
| Business owner |  |
| Technical owner |  |
| Review date |  |
| Intended users |  |
| Deployment environment | Internal / customer-facing / embedded / third-party |
| Recommended decision | Approve / approve with controls / pilot only / block |
| Top 3 risks |  |

## 1. Business Case

- [ ] The project has a named business owner with budget authority.
- [ ] The intended decision, workflow, or user outcome is specific.
- [ ] The project has measurable success criteria beyond "uses AI".
- [ ] The expected benefit is material enough to justify operational risk.
- [ ] There is a non-AI baseline or current-process benchmark.
- [ ] There is a clear kill condition if the project underperforms.
- [ ] The project does not depend on speculative future model capabilities.

**Red flags**

- No one can name the decision the system improves.
- ROI depends on full automation before validation.
- The project exists mainly because a competitor announced something AI-related.

## 2. Use Case Risk

- [ ] The system's users and affected parties are identified.
- [ ] Potential harms from incorrect, delayed, biased, or unavailable outputs are documented.
- [ ] The system's autonomy level is defined: advisory, assisted action, human approval, or automated action.
- [ ] The system is classified by business criticality.
- [ ] The system is classified by regulatory exposure.
- [ ] There is a defined maximum allowed blast radius for a failure.
- [ ] The team has documented reasonably foreseeable misuse.

**Block if**

- The system can materially affect people, money, safety, employment, healthcare, credit, legal status, or access to essential services and there is no formal risk review.

## 3. Data Readiness

- [ ] Input data sources are inventoried.
- [ ] Data owners are identified.
- [ ] Data quality issues are documented.
- [ ] Sensitive data classes are identified.
- [ ] Data retention rules are defined.
- [ ] Data sharing with vendors or model providers is reviewed.
- [ ] Training, fine-tuning, evaluation, and production data are separated.
- [ ] The system can operate when upstream data is incomplete, stale, or unavailable.

**Evidence to request**

- data flow diagram
- data inventory
- sample inputs and outputs
- retention policy
- vendor data-processing terms

## 4. Technical Feasibility

- [ ] The architecture is documented at a level a senior engineer can review.
- [ ] Model choice is justified against cheaper or simpler alternatives.
- [ ] Known model limitations are documented.
- [ ] Integration points and dependencies are mapped.
- [ ] Latency, cost, scale, and availability requirements are quantified.
- [ ] The system has a fallback mode.
- [ ] The team has tested realistic edge cases, not just happy paths.
- [ ] The team can explain how behavior will be monitored after launch.

## 5. Evaluation

- [ ] There is an evaluation dataset representative of real use.
- [ ] Evaluation data includes negative, ambiguous, adversarial, and edge cases.
- [ ] Metrics map to business and risk outcomes.
- [ ] Evaluation includes human review where judgment is required.
- [ ] Evaluation tracks false positives, false negatives, abstentions, and unsafe outputs.
- [ ] Evaluation is versioned across prompt, model, retrieval, code, and data changes.
- [ ] There is a regression test suite for high-risk behaviors.

**Senior reviewer question**

> What failures did the evals find that changed the design?

If the answer is "none", the evals are probably decorative.

## 6. Security and Abuse

- [ ] AI-specific threats are included in the threat model.
- [ ] Prompt injection, data exfiltration, model abuse, and tool misuse are assessed.
- [ ] Access control is enforced outside the model.
- [ ] Secrets are never placed in prompts, context windows, logs, or retrieval corpora.
- [ ] Outputs are treated as untrusted until validated.
- [ ] Tool-using agents have scoped permissions and execution limits.
- [ ] Abuse monitoring is in place for customer-facing systems.

## 7. Governance and Operations

- [ ] There is an accountable system owner after launch.
- [ ] There is an incident response path for AI failures.
- [ ] There is a rollback plan.
- [ ] There is monitoring for quality, cost, latency, safety, and security.
- [ ] User feedback is captured and triaged.
- [ ] Material changes require review.
- [ ] Documentation is sufficient for a new team to operate the system.

## 8. Final Recommendation

Use this table for the review decision.

| Area | Rating | Required action |
| --- | --- | --- |
| Business case | Low / medium / high risk |  |
| Data readiness | Low / medium / high risk |  |
| Technical feasibility | Low / medium / high risk |  |
| Evaluation quality | Low / medium / high risk |  |
| Security | Low / medium / high risk |  |
| Governance | Low / medium / high risk |  |
| Regulatory exposure | Low / medium / high risk |  |

## Minimum Approval Bar

Do not approve production deployment unless:

- there is a named owner
- data flows are understood
- material failure modes are tested
- monitoring exists
- users understand system limits
- rollback is possible
- security review is complete
- legal/compliance review is complete where applicable

