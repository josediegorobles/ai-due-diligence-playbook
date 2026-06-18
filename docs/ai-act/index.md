---
title: AI Act Compliance
description: A practical map from EU AI Act articles to the AI Act readiness checklist for AI providers, deployers, SMEs, CTOs, and investors.
---

# AI Act Compliance

This page is the AI Act spine for the playbook. It points from the practical [AI Act Readiness Checklist](../checklists/ai-act-readiness-checklist.md) to the articles and annexes that commonly drive readiness work for AI systems touching the EU market.

!!! warning "Not legal advice"
    This is a technical and operational due diligence map, not a legal opinion. Verify classification, obligations, timelines, and national implementation with qualified counsel.

## Fast Start

1. Open the [AI Act Readiness Checklist](../checklists/ai-act-readiness-checklist.md).
2. Identify your role: provider, deployer, importer, distributor, product manufacturer, authorized representative, or GPAI model provider.
3. Classify each AI system: prohibited, high-risk, transparency-obligation, GPAI-related, limited risk, or minimal risk.
4. Use the article map below to collect the evidence that matters.

## Article Map

| Reference | Operational focus | Checklist section |
| --- | --- | --- |
| [Art. 6](#art-6) | High-risk classification | Classification; high-risk system readiness |
| [Art. 9](#art-9) | Risk management system | High-risk system readiness |
| [Art. 10](#art-10) | Data and data governance | High-risk system readiness; technical documentation |
| [Art. 11](#art-11) | Technical documentation | Technical documentation |
| [Art. 12](#art-12) | Record-keeping and logging | High-risk system readiness; operating model |
| [Art. 13](#art-13) | Transparency and instructions for use | Transparency obligations; technical documentation |
| [Art. 14](#art-14) | Human oversight | High-risk system readiness |
| [Art. 15](#art-15) | Accuracy, robustness, and cybersecurity | High-risk system readiness; security review |
| [Art. 50](#art-50) | Transparency obligations for certain AI systems | Transparency obligations |
| [Annex III](#annex-iii) | High-risk use-case areas | Classification |
| [Annex IV](#annex-iv) | Technical documentation contents | Technical documentation |

## Art. 6 - High-Risk Classification { #art-6 }

Use Art. 6 as the classification gate. The readiness question is whether the system is high-risk because of product-safety linkage, because it falls within an Annex III area, or because an exception or narrower use analysis applies.

Evidence to collect:

- system purpose and intended use
- user group and affected persons
- autonomy level and downstream decisions
- product or sector integration
- Annex III mapping and legal review notes

## Art. 9 - Risk Management System { #art-9 }

For high-risk systems, readiness needs an actual risk management process, not a one-time spreadsheet. Map known and reasonably foreseeable risks, controls, residual risk, owners, and review cadence.

## Art. 10 - Data and Data Governance { #art-10 }

Prepare evidence on training, validation, test, and operational data where relevant. Focus on data sources, quality, relevance, representativeness, bias review, lineage, access controls, and retention.

## Art. 11 - Technical Documentation { #art-11 }

Technical documentation should explain the system well enough for conformity assessment, internal governance, customer review, and later incident investigation.

## Art. 12 - Record-Keeping and Logging { #art-12 }

Logging is readiness evidence. Document what events are logged, how long logs are retained, who can access them, and whether logs are enough to reconstruct important system behavior.

## Art. 13 - Transparency and Instructions for Use { #art-13 }

Users and deployers need instructions that match actual system behavior: intended purpose, limitations, required human oversight, expected inputs, output interpretation, and foreseeable misuse.

## Art. 14 - Human Oversight { #art-14 }

Human oversight only works if the human can realistically detect, interpret, override, and escalate system failures. Document the oversight design and test it under realistic conditions.

## Art. 15 - Accuracy, Robustness, and Cybersecurity { #art-15 }

Connect model evaluation, operational monitoring, adversarial testing, cybersecurity controls, and fallback design. A claim of accuracy is not enough without failure-mode evidence.

## Art. 50 - Transparency Obligations { #art-50 }

Review user-facing notices for AI interaction, generated or manipulated content, deepfakes, emotion recognition, biometric categorization, and other transparency-triggering workflows.

## Annex III - High-Risk Use-Case Areas { #annex-iii }

Annex III is a practical classification checklist for many business systems. Pay special attention to biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, justice, and democratic processes.

## Annex IV - Technical Documentation { #annex-iv }

Use Annex IV as a documentation completeness check. The practical output should connect system design, intended purpose, data, model behavior, evaluation, risk controls, human oversight, logging, and post-market monitoring.

## Primary Sources

- [European Commission AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [European Commission AI Act FAQ](https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act)
- [Regulation (EU) 2024/1689 on EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

--8<-- "_includes/cta.md"
