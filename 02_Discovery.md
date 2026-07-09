---
title: Discovery
description: Conducting user research to understand people's needs
---

# Discovery

## What is Discovery?
Discovery is about conducting user research to understand people's needs. Discovery helps define a service's potential users and how their needs can be met. You shouldn't start building your service in Discovery.

## What do you do in Discovery?

In Discovery you will:

- conduct user research
- learn about the people who will use the service
- understand what users need in a service
- check if there are existing or non-governmental services that meet user needs
- identify policies and other barriers that will make meeting user needs difficult
- conduct a policy review using the [Gender-Based Analysis Plus (GBA+)](https://cfc-swc.gc.ca/gba-acs/course-cours-en.html) framework to assess how diverse groups of women, men and non-binary people along with other identity factors such as race, ethnicity, religion, age, and mental or physical disability may experience or be impacted by your service differently
- identify how impairments might affect your users — for example, visual, hearing, motor and cognitive (memory and thinking) impairments
- document the research and findings through artefacts such as journey maps, service blueprints and personas

## Staffing the Team

| Role | Commitment | Responsibilities |
|------|-----------|------------------|
| User Researcher | Full-time (1–2) | Primary research lead; designs and conducts interviews, observations, and usability tests |
| Service Designer | Full-time | Journey mapping, service blueprinting, synthesis of research findings |
| Product Manager | Full-time | Backlog and prioritisation; translates research insights into user stories |
| Subject Matter Expert | Part-time | Provides domain context; validates research interpretation |
| Technical Lead | Part-time | Assesses technical feasibility of candidate solutions; identifies constraints |

**For AI/agent projects**, also engage:
- **Data Analyst or ML Engineer** (part-time): audits existing data assets; produces the Data Availability Matrix; performs preliminary task-model fit assessment for candidate AI features

## What do you have at the end of Discovery?

By the end of Discovery, expect to have:

- a clear understanding of the problems that the service will address
- a documented set of user needs and stories
- a plan for what will be prototyped and tested in Alpha
- a team of people and list of what resources you need to support work in Alpha
- current benchmarks of service performance
- how you will measure improvements to the service

## Discovery Artefacts

| Artefact | Description | Owner |
|----------|-------------|-------|
| Journey Map | End-to-end map of the user's experience of the current service | Service Designer |
| Service Blueprint | Cross-functional map linking user actions to backstage processes | Service Designer |
| User Personas | Synthesised representations of key user groups | User Researcher |
| Research Synthesis | Documented findings, patterns, and insights from research | User Researcher |
| Problem Statement | Clear articulation of the core problem to be solved | Product Manager |
| User Stories | Structured descriptions of user needs in "As a / I want / So that" format | Product Manager |
| Data Availability Matrix | *(AI projects)* Inventory of data available to support AI features | Data Analyst / ML Engineer |
| Task-Model Fit Assessment | *(AI projects)* Preliminary evaluation of which candidate tasks are well-suited to LLM/agent processing | ML Engineer |
| Human-in-the-Loop Map (draft) | *(AI projects)* Initial mapping of which AI decisions require human review | Product Manager |

## Discovery Checklist

- [ ] Primary and secondary research completed
- [ ] Journey map created and validated with users
- [ ] Service blueprint drafted
- [ ] User needs documented as user stories
- [ ] Policy review (including GBA+) completed
- [ ] Accessibility barriers and impairments identified
- [ ] Benchmarks of current service performance documented
- [ ] Plan for Alpha (what to prototype and test) agreed
- [ ] Alpha team composition and resource needs confirmed
- [ ] **AI/agent projects:** candidate AI features identified and listed
- [ ] **AI/agent projects:** Data Availability Matrix completed
- [ ] **AI/agent projects:** preliminary task-model fit assessment completed
- [ ] **AI/agent projects:** draft Human-in-the-Loop Map created
- [ ] **AI/agent projects:** data access agreements initiated for required datasets

## AI/Agent Delivery Notes

For teams building AI agent systems, Discovery has additional responsibilities:

**Candidate task identification**: As you research user needs, identify which tasks are candidates for LLM/agent automation. For each candidate, ask: Is the task well-defined? Is high-quality data available? What does failure look like, and who is harmed?

**Data in a data vacuum**: Do not design AI features without first understanding what data exists to support them. Discovering in Alpha that required training data does not exist is a major setback. The Data Availability Matrix is a Discovery output, not an Alpha assumption.

**Human-in-the-loop design starts in Discovery**: The question "which decisions must a human make?" is a user research question, not an engineering question. Research with users to understand trust, comfort, and the stakes of incorrect AI outputs. Draft the Human-in-the-Loop Map in Discovery; test it as a hypothesis in Alpha.

**Non-determinism is a user need**: If your service involves AI-generated outputs, research how users respond to outputs that vary. Some user groups require deterministic, auditable decisions — an LLM-based approach may be incompatible regardless of accuracy.

> **Cross-reference**: The [human-ai-collaboration](https://github.com/ghostmachine-ai/agent-skills-for-context-engineering/tree/main/skills/human-ai-collaboration) skill covers how to design the Human-in-the-Loop Map. The [ai-delivery-process](https://github.com/ghostmachine-ai/agent-skills-for-context-engineering/tree/main/skills/ai-delivery-process) skill provides the full Discovery-phase artefact specifications for AI projects.
