---
title: AI Agent Delivery
description: Adapting the agile delivery process for teams building AI agent systems
---

# AI Agent Delivery

## What is AI Agent Delivery?

AI agent delivery is the practice of applying the standard agile delivery process — Alignment, Discovery, Alpha, Beta, Live — to teams building services powered by AI agents and large language models.

The five phases remain the same. The activities, artefacts, staffing, and exit criteria change significantly.

This document is a supplement to the five phase files. It explains *why* AI delivery is different and provides a unified view of AI-specific concerns across all phases. Each phase file contains the detailed AI-specific checklists and staffing guidance.

## Why AI Delivery is Different

Four properties of AI systems create delivery challenges that do not exist in traditional software:

### 1. Non-Determinism

Traditional software is deterministic: the same input produces the same output. AI systems are not. The same prompt sent twice to the same model may produce different outputs. This affects:

- **Testing**: you cannot test by comparing outputs to a fixed expected value; you must use rubric-based evaluation with statistical sampling
- **Debugging**: a single wrong output is not evidence of a bug; a statistical pattern of wrong outputs is
- **Monitoring**: production monitoring requires drift detection, not binary error-rate checks

### 2. Evaluation-Driven Development

In traditional software, "does it work?" is answered by passing tests. In AI systems, "does it work well enough?" is answered by rubric-based evaluation against a defined threshold.

The evaluation rubric — what dimensions matter, how they are scored, what threshold must be met — must be defined **before** building begins in Beta. Defining success after the fact leads to optimising for the wrong thing.

**Evaluation-driven development** means:
1. Define your rubric in Alpha
2. Establish baseline scores in Alpha using manual prototypes
3. Build to the rubric in Beta
4. Monitor against the rubric in Live

### 3. Model Dependency

Traditional software depends on libraries and APIs that rarely change behaviour without notice. AI systems depend on models that:
- may be updated by providers without notice (same model name, different behaviour)
- are deprecated on the provider's schedule, not yours
- have variable per-call costs that change with usage patterns
- may impose rate limits and capacity constraints

Treating the model as a stable dependency is a project risk. Model version pinning, change testing, and deprecation planning are delivery requirements, not operational nice-to-haves.

### 4. Human-in-the-Loop Design

AI systems make probabilistic decisions. Some of those decisions affect users in consequential ways. "Human-in-the-loop" design — specifying which decisions must be reviewed by a human before affecting a user — is a core design requirement for most AI services, not an optional safety measure.

The Human-in-the-Loop Map (HITL Map) is a delivery artefact that specifies, for every AI decision the system makes, who reviews it, what information they need, what threshold triggers review, and what happens on approval or rejection. It is drafted in Discovery, tested in Alpha, implemented in Beta, and monitored in Live.

---

## Phase-by-Phase AI Activities

| Phase | Standard Focus | AI-Specific Additional Activities |
|-------|---------------|----------------------------------|
| Alignment | Stakeholder alignment, funding, governance | AI ethics review initiated; data ownership identified; model vendor constraints established |
| Discovery | User research, needs identification, problem framing | Candidate AI tasks identified; Data Availability Matrix produced; draft HITL Map created |
| Alpha | Prototyping and testing hypotheses | Manual prototype validation; evaluation rubric defined; multiple model approaches compared; evaluation harness built |
| Beta | Build and publicly release MVP | Prompt versioning in place; production monitoring active; rubric-based sampling running; model deprecation plan documented |
| Live | Continuous improvement | Drift detection running; model version pinned; deprecation plan maintained; evaluation sampling continuous |

---

## AI Team Roles

| Role | Phase(s) Active | Primary Responsibilities | Key Skills |
|------|----------------|------------------------|------------|
| AI/ML Systems Thinker | Alignment | Feasibility assessment; data landscape scan; vendor constraint identification | Systems architecture; ML fundamentals; data governance |
| Data Analyst / ML Engineer | Discovery | Data Availability Matrix; task-model fit assessment; data access agreements | Data engineering; ML; statistical analysis |
| ML Engineer / Prompt Engineer | Alpha, Beta | Prototype development; prompt engineering; model evaluation; production deployment | LLM APIs; prompt design; MLOps; evaluation harness development |
| Evaluation Specialist | Alpha, Beta, Live | Evaluation rubric design; baseline establishment; production sampling programme; drift monitoring | Statistical evaluation; LLM-as-judge; data analysis |
| AI Safety / Evaluation Lead | Beta, Live | Monitors model behaviour in production; flags regressions; owns bias review | AI safety; evaluation; statistical monitoring |
| MLOps / DevOps Engineer | Beta, Live | Model serving infrastructure; CI/CD for prompt and model changes; cost monitoring | Infrastructure; MLOps; observability tooling |

---

## Key Artefacts for AI Delivery

| Artefact | Phase Created | Phase(s) Updated | Owner | Description |
|----------|--------------|-----------------|-------|-------------|
| Task-Model Fit Assessment | Discovery | — | ML Engineer | Evaluates which candidate AI tasks are tractable given available data and model capabilities |
| Data Availability Matrix | Discovery | Alpha | Data Analyst | Inventory of data required for AI features, current availability, gaps, and access agreements needed |
| Human-in-the-Loop Map | Discovery (draft) | Alpha (tested), Beta (implemented) | Product Manager | Specifies which AI decisions require human review, by whom, at what threshold, with what information |
| Manual Prototype Log | Alpha | — | UX Designer / ML Engineer | Documents outcomes of manual (human-as-model) prototype validation sessions |
| Evaluation Rubric | Alpha | Beta, Live | Evaluation Specialist | Defines evaluation dimensions, scoring criteria, weights, and minimum acceptable thresholds |
| Failure Mode Catalogue | Alpha | Beta, Live | ML Engineer | Documents known failure modes, trigger conditions, and mitigations |
| Prompt Version History | Beta | Live | ML Engineer | Changelog of all production prompt changes with rationale and evaluation scores before/after |
| Model Deprecation Plan | Beta | Live | Product Manager | Documents when and how the service will migrate away from each model version it depends on |
| Evaluation Sampling Report | Live | Ongoing | Evaluation Specialist | Periodic report of rubric-based evaluation scores from production sampling |

---

## The AI Delivery Stack

A team delivering an AI agent service needs tooling in these categories:

| Category | What it provides | Examples |
|----------|-----------------|----------|
| Model provider | LLM API access | OpenAI, Anthropic, Google, Azure OpenAI |
| Evaluation harness | Rubric-based scoring, baseline tracking | LLM-as-judge scripts, evaluation datasets |
| Observability | Traces, metrics, cost monitoring | LangSmith, Langfuse, custom dashboards |
| Prompt version control | Prompt changelogs, diff tracking | Git for prompts, dedicated prompt registries |
| Sandboxed testing | Safe environment for model/prompt experiments | Staging environment with production traffic mirror |
| Data pipeline | Data ingestion, transformation, retrieval | Vector databases, ETL pipelines, document stores |

---

## Cross-References

The following [Agent Skills for Context Engineering](https://github.com/ghostmachine-ai/agent-skills-for-context-engineering) skills operationalise the AI delivery process:

| Skill | Delivery Relevance |
|-------|-------------------|
| [ai-delivery-process](https://github.com/ghostmachine-ai/agent-skills-for-context-engineering/tree/main/skills/ai-delivery-process) | Full AI delivery process as agent-loadable context; phase artefacts and exit criteria |
| [agent-observability](https://github.com/ghostmachine-ai/agent-skills-for-context-engineering/tree/main/skills/agent-observability) | Production monitoring, drift detection, prompt versioning — covers Beta and Live requirements |
| [human-ai-collaboration](https://github.com/ghostmachine-ai/agent-skills-for-context-engineering/tree/main/skills/human-ai-collaboration) | HITL Map design, automation spectrum, escalation design — covers Discovery and Alpha requirements |
| [evaluation](https://github.com/ghostmachine-ai/agent-skills-for-context-engineering/tree/main/skills/evaluation) | Evaluation rubric design and production sampling — covers Alpha and Beta requirements |
| [project-development](https://github.com/ghostmachine-ai/agent-skills-for-context-engineering/tree/main/skills/project-development) | Task-model fit analysis, manual prototype validation, pipeline architecture |
