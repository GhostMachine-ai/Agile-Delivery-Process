---
title: Data Availability Matrix Template
description: Discovery-phase template for assessing what data exists to support AI features
---

# Data Availability Matrix: [Service Name]

**Service:**
**Created by:** [Data Analyst / ML Engineer]
**Phase:** Discovery
**Date:** [date]
**Last updated:** [date]

---

## Purpose

This document assesses whether sufficient data exists to support the AI features identified during Discovery. It is completed before Alpha begins and informs the task-model fit assessment.

A data gap identified here is substantially cheaper to resolve than one discovered during Beta.

---

## Candidate AI Features

_List the AI features identified during Discovery that require data assessment._

| Feature ID | Feature Description | User Story | Priority |
|------------|--------------------|-----------|---------:|
| F-001 | | | Must / Should / Could |
| F-002 | | | |

---

## Data Inventory

_For each data type required by the candidate AI features, document availability and quality._

| Data Type | Required For | Source | Format | Volume (approx.) | Quality Assessment | Access Status | Privacy Classification |
|-----------|-------------|--------|--------|-------------------|--------------------|--------------|------------------------|
| [e.g., Historical service requests] | F-001 | [System name] | [CSV / API / DB] | [e.g., 50k records/year] | [High / Medium / Low] | [Available / Restricted / Unavailable] | [Personal / Non-personal / Sensitive] |
| | | | | | | | |

**Quality Assessment Key:**
- **High**: Complete, consistent, labelled, and representative of production usage
- **Medium**: Mostly complete; some gaps, inconsistencies, or labelling required
- **Low**: Significant gaps, bias, inconsistency, or volume insufficient for intended use

---

## Data Gaps

_For each gap between what is needed and what exists, document the impact and path to resolution._

| Required Data | Feature(s) Affected | Gap Description | Impact if Unresolved | Path to Resolution | Owner | Target Date |
|---------------|--------------------|-----------------|--------------------|-------------------|-------|-------------|
| | | | High / Medium / Low | | | |

---

## Data Agreements Required

_List all data sharing, licensing, or access agreements that must be in place before Alpha or Beta._

| Dataset | Agreement Type | Parties | Current Status | Required By | Owner |
|---------|---------------|---------|---------------|------------|-------|
| | [Data Sharing Agreement / Licence / API Terms] | | Not started / In progress / Signed | | |

---

## Preliminary Task-Model Fit Assessment

_Based on data availability, assess each candidate AI feature for suitability to LLM/agent processing._

| Feature | Data Available? | Task Well-Defined? | Failure Mode Acceptable? | Preliminary Fit | Recommendation |
|---------|---------------|-------------------|-------------------------|-----------------|---------------|
| F-001 | Yes / Partial / No | Yes / No | Yes / No / Unknown | Strong / Moderate / Weak / Unknown | Proceed to Alpha / Needs data work / Not recommended |
| F-002 | | | | | |

**Assessment criteria:**

| Criterion | Fit Indicator |
|-----------|--------------|
| Sufficient labelled data | Strong fit |
| Task has clear success criteria | Strong fit |
| Task is well-defined and bounded | Strong fit |
| Failure is low-consequence or detectable | Acceptable |
| Data exists but requires significant cleaning | Moderate fit; budget cleaning time |
| No data exists; requires collection | Weak fit; significant pre-work required |
| Failure could harm users and is hard to detect | Not recommended without robust HITL design |
| Task requires precise, auditable reasoning | Consider non-AI alternative |

---

## Recommendations for Alpha

_Based on this assessment, summarise what the Alpha team should investigate, what data preparation is required, and which features carry data risk._

[Free text summary of recommendations]

---

## Sign-off

| Role | Name | Date |
|------|------|------|
| Data Analyst / ML Engineer | | |
| Product Manager | | |
| Technical Lead | | |
