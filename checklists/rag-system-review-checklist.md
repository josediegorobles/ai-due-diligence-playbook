# RAG System Review Checklist

Use this for systems that retrieve documents, records, tickets, source code, policies, knowledge base articles, contracts, or web content and use them as context for generation.

RAG is not grounding by default. It is a retrieval system plus a generation system plus a trust boundary problem.

## 1. Knowledge Scope

- [ ] The corpus is defined.
- [ ] The intended source of truth is identified.
- [ ] Out-of-scope sources are explicitly excluded.
- [ ] Document ownership is clear.
- [ ] Freshness requirements are defined.
- [ ] Deletion, correction, and retention processes exist.
- [ ] The system can explain which sources were used for an answer.

## 2. Ingestion Pipeline

- [ ] Ingestion steps are documented.
- [ ] Chunking strategy is justified and tested.
- [ ] Metadata extraction is reliable.
- [ ] Document permissions are preserved during ingestion.
- [ ] Failed ingestions are detected and reported.
- [ ] Duplicate and stale documents are handled.
- [ ] Embedding model and vector index versions are tracked.
- [ ] Re-indexing is reproducible.

## 3. Retrieval Quality

- [ ] Retrieval is evaluated separately from generation.
- [ ] Test queries reflect real user language.
- [ ] The team measures recall for required source documents.
- [ ] The team measures precision for irrelevant retrieved context.
- [ ] The retriever handles synonyms, acronyms, typos, and domain language.
- [ ] Hybrid search, reranking, filters, or metadata constraints are used where needed.
- [ ] Retrieval failures are visible, not hidden behind fluent answers.

**Senior reviewer question**

> For the top 20 business-critical questions, can the system reliably retrieve the correct source before the LLM ever writes an answer?

## 4. Grounding and Citation

- [ ] The model is instructed to answer only from retrieved sources when required.
- [ ] The system can abstain when retrieval is insufficient.
- [ ] Citations point to specific documents or passages.
- [ ] Citation correctness is evaluated.
- [ ] The system does not cite documents that do not support the answer.
- [ ] The answer distinguishes source facts from model inference.
- [ ] The UI makes source inspection easy.

## 5. Access Control

- [ ] User permissions are enforced before retrieval.
- [ ] Permission filters are applied at query time and index time where appropriate.
- [ ] The model cannot bypass access control through prompt wording.
- [ ] Cross-tenant and cross-user leakage is tested.
- [ ] Admin-only, legal, HR, financial, and customer-confidential sources are isolated.
- [ ] Source snippets in logs are access-controlled.

**Block if**

- The vector index contains mixed-permission documents and retrieval does not enforce user-level access control.

## 6. Prompt Injection from Documents

- [ ] Retrieved documents are treated as untrusted content.
- [ ] The prompt clearly separates system instructions from document content.
- [ ] The system ignores instructions found inside retrieved documents.
- [ ] Tests include malicious documents, emails, tickets, pages, or comments.
- [ ] The model cannot reveal hidden instructions, credentials, policies, or unrelated documents.
- [ ] Tool access is constrained when retrieved content is in the prompt.

## 7. Evaluation

- [ ] The eval set includes query, expected sources, expected answer, and unacceptable answer patterns.
- [ ] Evals include stale, conflicting, missing, and ambiguous documents.
- [ ] Evals include permission-boundary tests.
- [ ] Evals include prompt-injection documents.
- [ ] Metrics track retrieval recall, answer correctness, citation correctness, abstention quality, latency, and cost.
- [ ] Evals run after corpus, chunking, embedding, retrieval, prompt, or model changes.

## 8. Operations

- [ ] Index health is monitored.
- [ ] Retrieval latency is monitored.
- [ ] Corpus freshness is monitored.
- [ ] Top failed queries are reviewed.
- [ ] User feedback maps back to retrieval failures or generation failures.
- [ ] There is a process for emergency document removal.
- [ ] There is a rollback path for bad indexing changes.

## 9. Review Outcome

| Area | Rating | Notes |
| --- | --- | --- |
| Corpus definition | Low / medium / high risk |  |
| Ingestion reliability | Low / medium / high risk |  |
| Retrieval quality | Low / medium / high risk |  |
| Grounding | Low / medium / high risk |  |
| Access control | Low / medium / high risk |  |
| Prompt injection resistance | Low / medium / high risk |  |
| Evaluation | Low / medium / high risk |  |
| Operations | Low / medium / high risk |  |

