---
title: AI Evaluation Rubric Template
description: Template for defining how AI/agent behaviour is measured against success criteria
---

# AI Evaluation Rubric: [Feature or Agent Name]

**Service:**
**Feature / Agent:**
**Created in Phase:** Alpha
**Owner:** [Evaluation Specialist / ML Engineer]
**Version:** 1.0
**Last updated:** [date]

---

## Purpose

[What is being evaluated, why it matters, and what decisions this rubric informs. 2–3 sentences.]

---

## Evaluation Dimensions

_Define each dimension that will be scored. Weights must sum to 100%._

| Dimension | Weight | Description | Scoring Scale | Minimum Acceptable Score |
|-----------|--------|-------------|---------------|---------------------------|
| Accuracy | % | [What "accurate" means for this feature] | 1–5 | |
| Completeness | % | [What "complete" means] | 1–5 | |
| Tone / Safety | % | [What constitutes safe, appropriate output] | 1–5 | |
| Groundedness | % | [Is the output grounded in source material or facts?] | 1–5 | |
| Tool Efficiency | % | [Does the agent use tools appropriately and minimally?] | 1–5 | |
| Latency | % | [Is the response time acceptable for the use case?] | 1–5 | |

**Composite pass threshold:** [e.g., "Weighted average ≥ 3.5 AND no dimension below 2"]

---

## Scoring Guide

_Provide concrete anchors for each score point to reduce inter-rater variance._

### [Dimension 1: Accuracy]

| Score | Meaning | Example |
|-------|---------|----------|
| 5 | Fully accurate; no errors | |
| 4 | Mostly accurate; minor, inconsequential error | |
| 3 | Partially accurate; error present but not misleading | |
| 2 | Significant inaccuracy; could mislead a user | |
| 1 | Substantially wrong; harmful if acted upon | |

_[Repeat for each dimension]_

---

## Test Cases

_Document representative inputs with expected output characteristics. These form the evaluation dataset._

| ID | Input / Scenario | Key Expected Characteristics | Notes |
|----|-----------------|------------------------------|-------|
| TC-001 | [Input description] | [What a good output looks like] | [Edge case? Known difficult?] |
| TC-002 | | | |

---

## Failure Mode Catalogue

_Document known failure modes, the conditions that trigger them, and mitigations._

| ID | Failure Mode | Trigger Conditions | User Impact | Mitigation |
|----|-------------|-------------------|-------------|------------|
| FM-001 | [e.g., Hallucination of specific facts] | [e.g., Query about recent events beyond training cutoff] | [High / Medium / Low] | [e.g., Retrieval-augmented approach; citation requirement] |
| FM-002 | | | | |

---

## Baseline and Targets

_Establish baseline scores from Alpha manual prototype testing. Set targets for Beta launch and Live steady-state._

| Metric | Alpha Baseline | Beta Launch Target | Live Steady-State Target |
|--------|---------------|-------------------|---------------------------|
| Composite score | | | |
| [Dimension 1] score | | | |
| [Dimension 2] score | | | |
| P95 Latency | | | |
| Cost per interaction | | | |

---

## Evaluation Method

**Evaluation approach:** Human annotation / LLM-as-judge / Hybrid _(circle one)_

**In Alpha:** [e.g., "100% of prototype outputs reviewed by two human annotators; adjudicate on disagreements"]

**In Beta:** [e.g., "5% production sample reviewed weekly; LLM-as-judge for speed, human spot-check on 10% of judge outputs"]

**In Live:** [e.g., "2% production sample; alert if composite score drops more than 0.3 points from baseline over a 7-day rolling window"]

**Annotator agreement threshold:** [e.g., "Cohen's kappa ≥ 0.7 required; if below, calibrate and re-annotate"]

---

## Human Review Criteria

_Specify which outputs require human review before being shown to users._

| Condition | Action | Reviewer | SLA |
|-----------|--------|----------|-----|
| [e.g., Any output scoring < 2 on Safety dimension] | Hold; send to human review queue | [Role] | [e.g., 4 hours] |
| [e.g., Any output flagged by automated toxicity check] | Hold; send to human review queue | [Role] | |

---

## Change Log

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | [date] | | Initial rubric created in Alpha |
