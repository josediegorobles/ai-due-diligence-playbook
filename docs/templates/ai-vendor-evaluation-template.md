# AI Vendor Evaluation Template

Use this before buying, partnering with, investing in, or deeply integrating an AI vendor.

## Vendor Snapshot

| Field | Answer |
| --- | --- |
| Vendor |  |
| Product |  |
| Primary use case |  |
| Buyer / sponsor |  |
| Data involved |  |
| Deployment model | SaaS / private cloud / self-hosted / API / embedded |
| Criticality | Low / medium / high |
| Review owner |  |
| Date |  |

## 1. Business Fit

- What problem does the vendor solve?
- What workflow does it replace or augment?
- What is the measurable business outcome?
- What does the vendor do that an internal team cannot reasonably build?
- What happens if the vendor is unavailable for 24 hours?
- What happens if the vendor shuts down, changes pricing, or removes a model?

## 2. Product Claims

Request evidence for every material claim.

| Claim | Evidence requested | Evidence received | Assessment |
| --- | --- | --- | --- |
| Accuracy / quality | Eval results, test methodology, sample failures |  |  |
| Cost reduction | Customer data, baseline comparison |  |  |
| Security | Audit reports, architecture, controls |  |  |
| Compliance | Legal mapping, certifications, policies |  |  |
| Differentiation | Technical explanation, defensibility |  |  |

**Red flag**

The vendor can show a demo but cannot show how they evaluate failures.

## 3. Technical Architecture

- [ ] Architecture diagram provided.
- [ ] Model providers and model versions disclosed.
- [ ] Fine-tuning, RAG, agents, or proprietary models are explained clearly.
- [ ] Data flow is documented.
- [ ] Tenant isolation is documented.
- [ ] Availability and disaster recovery posture is documented.
- [ ] Latency and scale limits are disclosed.
- [ ] Roadmap dependencies on third-party model providers are disclosed.

## 4. Data Handling

- [ ] Data processed by the vendor is inventoried.
- [ ] Data retention period is defined.
- [ ] Training/fine-tuning use of customer data is contractually addressed.
- [ ] Subprocessors are disclosed.
- [ ] Cross-border transfers are disclosed.
- [ ] Deletion process is documented.
- [ ] Logs and support access are controlled.
- [ ] Customer data can be exported in usable form.

**Contract must say**

- whether customer data is used for training
- how long prompts, outputs, files, and logs are retained
- who can access customer data
- what happens on termination

## 5. Security

- [ ] SOC 2, ISO 27001, or equivalent evidence reviewed.
- [ ] Security report covers the actual AI product, not just corporate IT.
- [ ] Penetration testing includes AI-specific abuse paths.
- [ ] Prompt injection, data exfiltration, and tool misuse are tested.
- [ ] Secrets management is described.
- [ ] Access control model is documented.
- [ ] Incident notification terms are acceptable.
- [ ] Vulnerability disclosure or security contact exists.

## 6. AI Evaluation

- [ ] Vendor has a documented evaluation methodology.
- [ ] Eval set resembles the buyer's use case.
- [ ] Vendor tracks known failure modes.
- [ ] Vendor can provide false positive / false negative examples.
- [ ] Vendor can explain model, prompt, retrieval, and data changes over time.
- [ ] Vendor has regression tests.
- [ ] Vendor has production monitoring for quality drift.

## 7. Governance and Compliance

- [ ] Vendor can identify whether the system may fall under regulated AI use.
- [ ] Vendor supports audit logs and review workflows.
- [ ] Vendor provides documentation for customer governance needs.
- [ ] Vendor has a responsible AI policy that maps to actual controls.
- [ ] Vendor can support data subject, deletion, or access obligations where relevant.
- [ ] Vendor can provide AI Act, GDPR, sector, or procurement support where relevant.

## 8. Commercial and Strategic Risk

- [ ] Pricing model is understood at realistic usage levels.
- [ ] Unit economics are acceptable if usage scales.
- [ ] There is no hidden dependency on expensive model calls.
- [ ] Switching cost is assessed.
- [ ] Export path is available.
- [ ] SLAs match business criticality.
- [ ] Indemnity, liability cap, and termination terms are reviewed.
- [ ] Vendor roadmap risk is acceptable.

## 9. Diligence Questions to Ask Live

1. What are the most common failure modes in production?
2. What customer use cases have you rejected?
3. How do you test prompt injection and data leakage?
4. Which model changes have degraded quality in the past?
5. How would we leave your platform in 90 days?
6. What customer data do your support engineers see?
7. What happens when the underlying model provider has an outage?
8. What is your strongest evidence that this system works in our environment?

## 10. Recommendation

| Area | Rating | Notes |
| --- | --- | --- |
| Business fit | Strong / acceptable / weak |  |
| Technical quality | Strong / acceptable / weak |  |
| Security | Strong / acceptable / weak |  |
| Data handling | Strong / acceptable / weak |  |
| Evaluation maturity | Strong / acceptable / weak |  |
| Governance | Strong / acceptable / weak |  |
| Commercial risk | Strong / acceptable / weak |  |

Final decision:

- [ ] Approve
- [ ] Approve with controls
- [ ] Pilot only
- [ ] Reject
- [ ] Escalate to legal/security/board


--8<-- "_includes/cta.md"
