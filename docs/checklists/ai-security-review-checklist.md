# AI Security Review Checklist

Use this to review AI-specific security risks in LLM applications, RAG systems, AI agents, ML pipelines, model APIs, and vendor integrations.

Security review must cover the application around the model. The model is not the security boundary.

## 1. Asset and Trust Boundary Mapping

- [ ] AI components are included in the system architecture.
- [ ] Prompts, retrieved context, model outputs, tools, embeddings, logs, and eval datasets are treated as assets.
- [ ] Trust boundaries are documented.
- [ ] User-controlled input paths are documented.
- [ ] Vendor-controlled components are documented.
- [ ] Data crossing model/provider boundaries is documented.
- [ ] Sensitive outputs and downstream actions are documented.

## 2. Prompt Injection and Instruction Attacks

- [ ] Direct prompt injection is tested.
- [ ] Indirect prompt injection from documents, web pages, emails, tickets, PDFs, and code comments is tested.
- [ ] The system separates trusted instructions from untrusted content.
- [ ] The system does not rely on the model to keep secrets.
- [ ] The system can refuse malicious instructions inside retrieved content.
- [ ] Tool execution is protected from injected instructions.
- [ ] Regression tests include known attack strings and realistic malicious documents.

## 3. Data Exfiltration

- [ ] The model cannot access data the user is not authorized to see.
- [ ] Retrieval filters enforce permissions outside the model.
- [ ] The system prevents cross-tenant leakage.
- [ ] Sensitive data is not exposed through citations, summaries, logs, or debug traces.
- [ ] The system resists attempts to reveal hidden prompts, policies, credentials, or unrelated context.
- [ ] Output filters or policy checks exist where sensitive data risk is high.

## 4. Agent and Tool Security

- [ ] Tools are allowlisted.
- [ ] Tool permissions are least-privilege.
- [ ] Destructive actions require deterministic confirmation outside the model.
- [ ] Tool inputs are validated.
- [ ] Tool outputs are treated as untrusted.
- [ ] Execution time, loop count, spend, and retries are limited.
- [ ] The system logs tool calls.
- [ ] The system can disable tools quickly during incident response.

## 5. Model and Dependency Supply Chain

- [ ] Model provider is approved.
- [ ] Model version changes are tracked.
- [ ] Open-source model provenance is reviewed.
- [ ] Fine-tuned model artifacts are access-controlled.
- [ ] Training and eval datasets are protected.
- [ ] Dependencies for orchestration, vector DBs, plugins, and AI SDKs are scanned.
- [ ] Vendor terms for data usage and retention are reviewed.
- [ ] Fallback model behavior is tested.

## 6. API and Application Security

- [ ] Standard application security review is complete.
- [ ] Authentication and authorization are enforced before AI calls.
- [ ] Rate limiting exists.
- [ ] Abuse detection exists for public-facing systems.
- [ ] Cost-exhaustion attacks are considered.
- [ ] Uploads and URLs are scanned or constrained.
- [ ] Model responses are not rendered unsafely as HTML, SQL, code, shell commands, or privileged instructions.
- [ ] Secrets are managed through standard infrastructure.

## 7. Logging and Privacy

- [ ] Logs are access-controlled.
- [ ] Sensitive prompts and outputs are redacted where needed.
- [ ] Retention periods are defined.
- [ ] Debug traces are disabled or protected in production.
- [ ] User feedback workflows do not leak confidential data.
- [ ] Vendor logging and retention are contractually understood.

## 8. Abuse and Misuse

- [ ] The system has misuse cases documented.
- [ ] High-risk content generation is restricted where relevant.
- [ ] Automated scraping, spam, fraud, malware, or impersonation abuse is considered.
- [ ] Account-level abuse signals are monitored.
- [ ] There is an escalation path for abuse reports.
- [ ] The system can suspend or throttle abusive usage.

## 9. Incident Response

- [ ] AI-specific incident types are defined.
- [ ] Security team knows how to retrieve relevant AI logs.
- [ ] The team can disable prompts, tools, retrieval sources, vendors, or models quickly.
- [ ] Customer notification paths are defined.
- [ ] Vendor notification paths are defined.
- [ ] Incidents create new regression tests.

## 10. Minimum Security Bar

Do not ship if:

- the model can access unauthorized data
- tools can perform destructive actions without external controls
- prompt injection has not been tested
- logs expose sensitive data
- vendor data handling is unknown
- there is no incident disable path


--8<-- "_includes/cta.md"
