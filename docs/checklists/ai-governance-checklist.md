# AI Governance Checklist

Use this to assess whether an organization can responsibly operate AI systems after launch. Governance is not a policy PDF. Governance is who decides, who monitors, who can stop the system, and what evidence exists.

## 1. Inventory and Ownership

- [ ] There is an inventory of AI systems, features, vendors, models, and datasets.
- [ ] Each AI system has a business owner.
- [ ] Each AI system has a technical owner.
- [ ] Each AI system has a risk classification.
- [ ] Shadow AI usage is tracked or actively discovered.
- [ ] Vendor AI features embedded in existing tools are included.
- [ ] Ownership survives team reorgs and vendor changes.

## 2. Risk Classification

- [ ] Systems are classified by impact, autonomy, data sensitivity, security exposure, and regulatory exposure.
- [ ] High-risk systems require formal review before launch.
- [ ] Material changes trigger re-review.
- [ ] There is a defined approval authority for each risk level.
- [ ] Risk acceptance must be documented by an accountable executive.

## 3. Policies That Actually Matter

- [ ] Acceptable AI use policy exists.
- [ ] Sensitive data rules are clear.
- [ ] Human oversight requirements are defined.
- [ ] Vendor approval process includes AI-specific questions.
- [ ] User disclosure rules are defined.
- [ ] Logging and retention rules are defined.
- [ ] AI-generated code, content, decisions, or recommendations have review rules.

## 4. Change Management

- [ ] Model changes are tracked.
- [ ] Prompt changes are tracked.
- [ ] Retrieval corpus changes are tracked.
- [ ] Tool and agent permission changes are tracked.
- [ ] Evals run before material changes ship.
- [ ] Rollback plans exist for high-impact systems.
- [ ] Emergency changes are logged and reviewed after the fact.

## 5. Evaluation Standards

- [ ] Every production AI system has defined eval criteria.
- [ ] Evals include failure modes and edge cases.
- [ ] Evals map to business risk.
- [ ] Evals are run on representative data.
- [ ] Evals are versioned.
- [ ] Eval failures can block release.
- [ ] Teams review qualitative examples, not just aggregate scores.

## 6. Monitoring and Incident Response

- [ ] Production systems are monitored for quality, latency, cost, abuse, and security.
- [ ] High-risk outputs are sampled.
- [ ] Users can report failures.
- [ ] There is an AI incident classification process.
- [ ] There is an escalation path to engineering, security, legal, and business owners.
- [ ] There is a rollback or disable mechanism.
- [ ] Incidents feed back into evals and controls.

## 7. Third-Party AI Governance

- [ ] Vendor AI systems are inventoried.
- [ ] Vendor data-use terms are reviewed.
- [ ] Vendor model and subprocessor dependencies are reviewed.
- [ ] Vendor changes are monitored.
- [ ] Vendor audit evidence is updated regularly.
- [ ] Exit plans exist for critical vendors.

## 8. Board and Executive Reporting

- [ ] Leadership receives a regular AI risk report.
- [ ] Report includes active systems, high-risk initiatives, incidents, open findings, vendor exposure, and major upcoming changes.
- [ ] AI risk is not buried inside generic innovation reporting.
- [ ] Executives understand where AI can affect customers, revenue, compliance, or operations.

## 9. Minimum Governance Bar

Do not claim AI governance maturity unless the organization can produce:

- AI system inventory
- owner list
- risk classification method
- approval records
- evaluation evidence
- vendor AI inventory
- incident process
- monitoring evidence
- change history


--8<-- "_includes/cta.md"
