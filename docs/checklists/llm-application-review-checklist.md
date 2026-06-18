# LLM Application Review Checklist

Use this for chatbots, copilots, workflow assistants, summarizers, classifiers, coding tools, agents, and LLM-backed product features.

## 1. System Definition

- [ ] The application has a clear purpose and boundary.
- [ ] The user population is defined.
- [ ] The application states what it must not be used for.
- [ ] The system role, user role, and model role are documented.
- [ ] The model provider, model version, context window, and deployment mode are documented.
- [ ] The application has a defined autonomy level.
- [ ] User-facing claims are accurate and not inflated.

## 2. Prompt and Instruction Control

- [ ] System prompts are version controlled.
- [ ] Prompt changes require review and testing.
- [ ] Instructions separate policy, task behavior, output format, and safety constraints.
- [ ] The application does not rely on hidden prompts as the only security control.
- [ ] The model is not trusted to enforce authorization.
- [ ] The system handles conflicting instructions explicitly.
- [ ] Prompt templates are tested against adversarial and malformed inputs.

**Hard rule**

Never put secrets, privileged instructions, or authorization decisions in places a user can influence.

## 3. Input Handling

- [ ] Input size limits are enforced.
- [ ] File, URL, image, and pasted-content inputs are scanned or constrained.
- [ ] Untrusted content is clearly separated from trusted instructions.
- [ ] The system resists prompt injection from retrieved documents, emails, tickets, web pages, or uploaded files.
- [ ] PII and confidential data handling is defined.
- [ ] The application can refuse unsupported inputs without breaking workflow.

## 4. Output Quality

- [ ] Outputs are evaluated against realistic user tasks.
- [ ] The system has criteria for correctness, completeness, tone, and refusal.
- [ ] The system can abstain when confidence or evidence is insufficient.
- [ ] Hallucination risk is measured, not hand-waved.
- [ ] The system cites sources when source-grounded answers are required.
- [ ] Generated code, queries, contracts, financial analysis, or medical/legal content gets domain-specific review.
- [ ] Users are warned where output requires verification.

## 5. Tool Use and Agents

- [ ] Each tool has a scoped permission model.
- [ ] The model cannot call tools it does not need.
- [ ] Tool calls are logged with inputs, outputs, user, and timestamp.
- [ ] Destructive actions require explicit human confirmation.
- [ ] The system validates tool arguments before execution.
- [ ] The system limits loops, retries, spend, and execution time.
- [ ] The system can recover safely from partial tool failure.
- [ ] Agent plans are observable and interruptible.

**Block if**

- An agent can send messages, spend money, modify production data, delete files, or change permissions without a control outside the model.

## 6. Security

- [ ] Prompt injection is tested.
- [ ] Jailbreak attempts are tested.
- [ ] Data exfiltration paths are tested.
- [ ] Model output is treated as untrusted input to downstream systems.
- [ ] The application prevents cross-user data leakage.
- [ ] Logs do not expose sensitive prompts, documents, credentials, or regulated data.
- [ ] API keys and vendor credentials are managed through standard secrets infrastructure.
- [ ] Rate limits and abuse controls exist.

## 7. Evaluation and Regression

- [ ] There is an automated eval suite.
- [ ] Eval cases include happy path, edge cases, adversarial cases, and refusal cases.
- [ ] Evals are run before model, prompt, retrieval, tool, or policy changes ship.
- [ ] Production feedback feeds back into evals.
- [ ] Results are tracked over time.
- [ ] The team has thresholds for blocking release.
- [ ] The eval suite includes examples of prior incidents and near misses.

## 8. Observability

- [ ] The system logs request metadata, model version, prompt version, tool calls, latency, cost, and outcome.
- [ ] Sensitive content is redacted or access-controlled in logs.
- [ ] There are dashboards for usage, quality, cost, latency, error rates, and refusal rates.
- [ ] There is alerting for abnormal usage, cost spikes, quality drops, and abuse patterns.
- [ ] There is a process to sample and review outputs.

## 9. User Experience and Human Oversight

- [ ] Users can tell when AI is involved.
- [ ] Users can see source material or rationale when needed.
- [ ] Users can correct, report, or escalate bad outputs.
- [ ] Human reviewers have enough context to catch errors.
- [ ] Human review workload is realistic at expected volume.
- [ ] The system does not create automation bias by overstating confidence.

## 10. Release Decision

| Area | Pass / fail | Notes |
| --- | --- | --- |
| Purpose and boundaries |  |  |
| Prompt and instruction control |  |  |
| Input handling |  |  |
| Output quality |  |  |
| Tool safety |  |  |
| Security |  |  |
| Evaluation |  |  |
| Observability |  |  |
| Human oversight |  |  |


--8<-- "_includes/cta.md"
