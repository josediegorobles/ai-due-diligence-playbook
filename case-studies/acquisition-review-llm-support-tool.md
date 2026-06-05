# Case Study: Acquisition Review of an LLM Support Tool

This fictional case study shows how to apply the playbook during technical due diligence.

## Scenario

A SaaS company claims its AI support tool reduces support workload by 45 percent. The buyer is considering acquisition. The product uses an LLM with RAG over customer documentation, support tickets, and account data.

## Claimed Strengths

- fast deployment into existing help desks
- strong demo quality
- integrations with common ticketing systems
- claimed proprietary support-resolution dataset
- customer logos in mid-market SaaS

## Review Findings

### 1. The Moat Was Weaker Than Claimed

The system used a standard LLM API, basic vector search, and prompt templates. The proprietary dataset was mostly customer-specific historical tickets that could not transfer cleanly between customers.

**Impact:** reduce valuation credit for technical defensibility.

### 2. RAG Permissions Were Underbuilt

The product relied on source connector permissions during ingestion but did not consistently enforce user-level permissions during retrieval.

**Impact:** critical data leakage risk for enterprise customers.

### 3. Evaluation Evidence Was Thin

The vendor showed aggregate "resolution quality" metrics but could not provide:

- representative eval set construction
- citation correctness measurement
- permission-boundary tests
- known bad examples
- regression results across model changes

**Impact:** quality claims could not be trusted.

### 4. Human Review Was Not a Real Control

The vendor described human approval as the main safety mechanism, but most customers used auto-draft and bulk-send workflows. Reviewers often approved AI replies without checking source documents.

**Impact:** automation bias and customer-risk exposure.

### 5. Cost Model Was Fragile

The product depended on long-context calls for complex accounts. Gross margin degraded sharply for large customers with extensive documentation.

**Impact:** revise margin assumptions and enterprise pricing model.

## Risk Register

| Severity | Finding | Recommendation |
| --- | --- | --- |
| Critical | Retrieval access control does not enforce user-level permissions reliably. | Block enterprise deployment until retrieval authorization is redesigned. |
| High | Eval methodology does not support claimed quality. | Build buyer-observed eval suite before closing. |
| High | Technical moat overstated. | Reduce valuation multiple attributed to AI defensibility. |
| Medium | Human oversight design creates automation bias. | Improve UI, sampling, and review workflow. |
| Medium | LLM cost exposure not modeled under heavy usage. | Add contract pricing guardrails and model fallback. |

## Diligence Recommendation

Proceed only with price adjustment and closing conditions:

- remediate retrieval authorization
- produce representative eval results
- disclose model/provider dependencies
- provide customer-data rights analysis
- add production monitoring and incident process

## Lesson

The demo was good. The diligence evidence was not.

That distinction is the job.

