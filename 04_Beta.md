---
title: Beta
description: Developing a minimum viable service and making it available to the public
---

# Beta

## What is Beta?

The goal of Beta is to build a working version of the service that works for a large group of users. The prototypes that were developed and tested during Alpha are used to build a minimum viable product in a live, user-facing environment.

## What do you do in Beta?

In Beta you will work in an agile approach to build quickly and in small segments, taking the time to confirm that each segment of the service is on the right track. Launching a public service is the ultimate usability test, as it collects real data and user feedback. Feedback is used to refine the service, adding and adjusting features until the service is complete.

In Beta:

- make a prioritized list of the user stories that have already been researched
- build a minimum viable product that can be used by the public in a live environment
- continuously test the service with users to collect feedback and discover helpful insights
- test the design for accessibility and use assistive devices like screen readers
- use analytics to track and measure the service against key performance indicators
- resolve any remaining technical or process-related challenges
- update any required policies to support the service

## Staffing the Team

| Role | Commitment | Responsibilities |
|------|-----------|------------------|
| Product Manager | Full-time | Owns delivery roadmap; prioritises backlog; coordinates stakeholders |
| UX Designer | Full-time | Iterates design based on analytics and user feedback |
| Full-Stack Developer | Full-time (2–4) | Builds the MVP and iterates features |
| DevOps / Platform Engineer | Full-time | Manages live environment; CI/CD; infrastructure reliability |
| QA Engineer | Full-time | Accessibility testing; regression testing; quality assurance |
| User Researcher | Part-time | Maintains continuous feedback loops; runs usability sessions |

**For AI/agent projects**, also engage:
- **ML Engineer** (full-time): prompt iteration; model integration; performance tuning; infrastructure for model serving
- **AI Safety / Evaluation Lead** (part-time): monitors model behaviour in production; runs rubric-based sampling; manages evaluation against Alpha baselines; flags regressions

## What do you have at the end of Beta?

By the end of beta, expect to have:

- a fully functional version of the service for public use that adequately meets user needs
- completed the backlog of features for the service
- evidence that your service meets government [accessibility requirements for WCAG AA 2.0](https://www2.gov.bc.ca/gov/content/home/accessibility)

## Beta Checklist

- [ ] MVP live in public-facing environment
- [ ] Analytics instrumented and tracking against KPIs
- [ ] Accessibility audit completed (WCAG AA 2.0)
- [ ] Privacy Impact Assessment completed for production service
- [ ] [Security Threat and Risk Assessment](https://www2.gov.bc.ca/gov/content/governments/services-for-government/information-management-technology/information-security/security-threat-and-risk-assessment) completed
- [ ] Feature backlog completed
- [ ] All remaining technical and process challenges resolved
- [ ] Required policy updates implemented
- [ ] Service support model documented
- [ ] **AI/agent projects:** model monitoring pipeline active in production
- [ ] **AI/agent projects:** prompt versioning and change management in place
- [ ] **AI/agent projects:** hallucination and failure rate tracked against Alpha baseline
- [ ] **AI/agent projects:** bias and fairness review completed
- [ ] **AI/agent projects:** rollback plan documented for model and prompt changes
- [ ] **AI/agent projects:** user trust signals monitored (e.g., correction rate, abandonment)
- [ ] **AI/agent projects:** cost-per-interaction tracked against budget
- [ ] **AI/agent projects:** model deprecation plan documented

## Before going Live

Your service is ready to go Live when you are sure:

- the service meets the user needs you found in your Discovery, Alpha and Beta phases and delivers an end-to-end journey
- you're securing the service's information and data collection
- you've set up your analytics to accurately measure the success of your service
- the service meets government [accessibility requirements](https://www2.gov.bc.ca/gov/content/home/accessibility)
- you've completed a [Privacy Impact Assessment](https://www2.gov.bc.ca/gov/content/governments/services-for-government/information-management-technology/privacy/privacy-impact-assessments?keyword=privacy&keyword=impact&keyword=assessment) for the service
- you've completed a [Security Threat and Risk Assessment](https://www2.gov.bc.ca/gov/content/governments/services-for-government/information-management-technology/information-security/security-threat-and-risk-assessment?keyword=security&keyword=threat&keyword=and&keyword=risk&keyword=assessment) for the service
- you can support the service and you'll be able to keep iterating it and improving it until it's retired

## AI/Agent Delivery Notes

Beta for AI agent systems introduces operational complexity that has no equivalent in traditional software delivery:

**Prompt changes are deployments**: Every change to a system prompt or user-facing prompt must be treated as a deployment — versioned, tested against the evaluation rubric, and documented in a changelog. Untracked prompt changes are the leading cause of unexplained quality regressions in live AI systems.

**Non-determinism requires statistical monitoring**: You cannot alert on a single wrong output. Monitoring requires statistical baselines and drift detection — not binary pass/fail checks. Establish your statistical baseline during Beta and build alerting on deviation from that baseline.

**A/B testing of prompts is a first-class practice**: Prompt changes should be A/B tested in production just as UI changes are. Do not flip an entire user base onto a new prompt without staged rollout and comparative evaluation.

**Model upgrades are silent breaking changes**: When your model provider releases a new version, your prompts and evaluations may break in ways that are not immediately visible. Treat model upgrades like dependency upgrades: test against your rubric before rolling out, and have a rollback plan.

> **Cross-reference**: The [agent-observability](https://github.com/ghostmachine-ai/agent-skills-for-context-engineering/tree/main/skills/agent-observability) skill covers how to set up production monitoring, drift detection, and prompt versioning. The [evaluation](https://github.com/ghostmachine-ai/agent-skills-for-context-engineering/tree/main/skills/evaluation) skill covers rubric-based sampling for production.
