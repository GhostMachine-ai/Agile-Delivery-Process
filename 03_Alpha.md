---
title: Alpha
description: Developing and testing our hypotheses with users
---

# Alpha

## What is Alpha?

Alpha is about prototyping, testing hypotheses and experimentation. The purpose of Alpha is to determine how to meet the user needs that were identified in Discovery.

## What do you do in Alpha?

The main activity in Alpha is to test hypotheses by building prototypes.

Alpha prototypes are like a proof of concept. They help you to test your understanding of the service. They will show if you have included the most important and meaningful steps the users take when going through the service.

Test with users using paper prototypes first. As you learn from your user research, work up to testing with interactive HTML prototypes.

In Alpha you need to:

- work directly with end users and stakeholders to co-create solutions
- build multiple prototypes of the service
- continuously test prototypes with users
- demonstrate that the service is technically and financially feasible
- estimate how much the service will cost
- identify existing processes or policies that will need to change to support the service

## Staffing the Team

| Role | Commitment | Responsibilities |
|------|-----------|------------------|
| Product Manager | Full-time | Owns scope and prioritisation; manages the Alpha backlog |
| UX Designer / Researcher | Full-time | Creates and iterates prototypes; conducts user testing sessions |
| Full-Stack Developer | Full-time (1–2) | Builds interactive prototypes; validates technical feasibility |
| QA / Test Lead | Part-time | Designs testing methodology; ensures prototype quality |

**For AI/agent projects**, also engage:
- **ML Engineer or Prompt Engineer** (full-time): builds and iterates LLM-backed prototypes; evaluates model options; owns the prompt development cycle
- **Evaluation Specialist** (part-time): designs the evaluation rubric; establishes baseline metrics for AI behaviour; defines what "good enough" means before Beta

## What do you have at the end of Alpha?

At the end of Alpha, the goal is to have defined a minimum viable product that can be built and more broadly tested in Beta. The minimum viable product will be the first working implementation of a service. It is the quickest and simplest version of a service with just enough features to meet basic user needs and provide value.

By the end of Alpha, expect to have:

- thoroughly tested prototypes that demonstrate the design of the service
- a clear vision for the service that will be built in Beta
- a plan and prioritized list of features or user stories to be completed in Beta
- a clear understanding of the technology that will be used to support the service
- an understanding of how to design an accessible service
- set some metrics to measure your service's success

## Alpha Exit Criteria

The service is ready to move to Beta when:

- at least one prototype has been tested with a minimum of 5 representative users per key user group
- the chosen approach is confirmed technically and financially feasible
- a prioritised feature backlog for Beta has been agreed
- accessibility requirements are understood and incorporated in the Beta plan
- **AI/agent projects:** an evaluation rubric has been defined and baseline metrics established
- **AI/agent projects:** at least one LLM-backed prototype has been tested with real users
- **AI/agent projects:** primary failure modes have been catalogued and mitigations identified

## Alpha Checklist

- [ ] Multiple prototypes built (paper first, then interactive)
- [ ] Prototypes tested with representative users (minimum 5 per key user group)
- [ ] Technical feasibility confirmed
- [ ] Financial feasibility confirmed and cost model drafted
- [ ] Prioritised feature backlog created for Beta
- [ ] Technology stack for Beta agreed
- [ ] Accessibility requirements understood and incorporated into Beta plan
- [ ] Existing processes and policies that need to change identified
- [ ] Alpha exit criteria met and documented
- [ ] **AI/agent projects:** evaluation rubric defined before Beta build begins
- [ ] **AI/agent projects:** LLM-backed prototype built and user-tested
- [ ] **AI/agent projects:** multiple model or prompt approaches compared
- [ ] **AI/agent projects:** failure mode catalogue created
- [ ] **AI/agent projects:** Human-in-the-Loop Map tested and validated with users
- [ ] **AI/agent projects:** evaluation harness (testing infrastructure) established

## AI/Agent Delivery Notes

For teams building AI agent systems, Alpha has a critical ordering constraint:

**Define your evaluation rubric before you build**: The single most common AI delivery mistake is building a model or prompt in Beta and then trying to define success after the fact. The evaluation rubric — what dimensions matter, how they are scored, what thresholds must be met — is an Alpha output, not a Beta output.

**Manual prototype validation before automation investment**: Before committing to a complex AI pipeline, build a manual version of the process. A human acting as the "model" — reading inputs and producing outputs that follow the intended pattern — can reveal whether the task is even tractable and whether users accept the output format. This is faster and cheaper than building and testing an actual model integration.

**Test multiple model approaches**: Alpha is the time to compare approaches (different models, different prompt strategies, retrieval-augmented vs. fine-tuned, zero-shot vs. few-shot). Committing to one approach in Alpha without comparison leads to sunk-cost bias in Beta.

**Establish the evaluation harness before the build**: The infrastructure to run evaluation (test datasets, scoring scripts, baseline comparisons) must be in place before Beta begins. Building the harness mid-Beta delays delivery and often gets deprioritised under pressure.

> **Cross-reference**: The [evaluation](https://github.com/ghostmachine-ai/agent-skills-for-context-engineering/tree/main/skills/evaluation) skill covers how to design the evaluation rubric and testing framework. The [project-development](https://github.com/ghostmachine-ai/agent-skills-for-context-engineering/tree/main/skills/project-development) skill describes the manual prototype validation pattern in detail.
