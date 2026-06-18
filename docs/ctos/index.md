---
title: For CTOs
description: Technical AI diligence path for CTOs reviewing LLM apps, RAG systems, security controls, and production readiness.
---

# For CTOs

AI diligence for CTOs is evidence work: system boundaries, model dependencies, eval quality, security controls, retrieval permissions, observability, incident handling, and rollback plans.

## Recommended Path

1. [AI Project Risk Assessment](../checklists/ai-project-risk-assessment.md): decide the risk class and launch posture.
2. [LLM Application Review Checklist](../checklists/llm-application-review-checklist.md): inspect prompts, inputs, outputs, autonomy, evals, monitoring, and user claims.
3. [RAG System Review Checklist](../checklists/rag-system-review-checklist.md): test retrieval quality, permission boundaries, citations, freshness, and grounding.
4. [AI Security Review Checklist](../checklists/ai-security-review-checklist.md): threat-model prompt injection, tool abuse, data exfiltration, model supply chain, and runtime security.
5. [AI Due Diligence Risk Model](../frameworks/ai-due-diligence-risk-model.md): score business, technical, regulatory, and operational exposure.

## CTO Review Questions

| Area | Ask |
| --- | --- |
| Product boundary | What is the system allowed to decide, recommend, or automate? |
| Evaluation | Which eval set proves readiness for real user behavior and failure modes? |
| Security | What data and tools can the AI path reach, and where is authorization enforced? |
| Operations | Who can disable the system, roll it back, and investigate incidents? |
| Vendor risk | What breaks if the model provider changes behavior, pricing, policy, or availability? |

--8<-- "_includes/cta.md"
