---
title: Live
description: Continuing to improve based on user feedback
---

# Live

## What is Live?

Live begins when the service has reached a point of maturity and all of the main features in the backlog have been built.

## After you go Live

After you move to the Live phase you should keep improving your service based on user feedback, analytics and further user research.

You should:

* continue doing user research
* monitor the status of your service
* maintain uptime and availability
* practice vulnerability and penetration testing
* test your service's performance
* test new features to make sure they're accessible
* maintain quality assurance

## Staffing the Team

Most features will be built at this point, but it's not time to disband the team. Ongoing user research, testing and improvement are essential parts of live and will require a dedicated team.

To reflect the change in workload, reduce the size of the team to a few key roles. Keep a sustainable and multidisciplinary team that can:

* finish building any additional features from the backlog
* manage, maintain and monitor the success of the service
* conduct ongoing user research and testing to update and improve the service

A product manager must continue to be accountable for the service as long as it is live.

**For AI/agent projects**, retain or contract:
- **ML Engineer** (part-time, on-call for incidents): handles model updates, prompt changes, and infrastructure issues
- **AI Safety / Evaluation Lead** (part-time): maintains the ongoing evaluation sampling programme; monitors for drift and bias

## Live Checklist

- [ ] Continuous monitoring active (uptime, latency, error rates)
- [ ] Vulnerability and penetration testing scheduled
- [ ] User research cadence maintained
- [ ] Accessibility re-audited after significant changes
- [ ] Quality assurance processes documented and followed
- [ ] Service support model in operation
- [ ] **AI/agent projects:** model drift detection active
- [ ] **AI/agent projects:** prompt versioning and change management in place
- [ ] **AI/agent projects:** model deprecation plan documented and owned
- [ ] **AI/agent projects:** cost-per-interaction monitored against budget
- [ ] **AI/agent projects:** evaluation sampling programme running at agreed rate
- [ ] **AI/agent projects:** bias and fairness monitoring in place
- [ ] **AI/agent projects:** LLM provider contract and SLA reviewed

## Continuous Improvement

You should repeat the agile development phases (discovery, alpha, beta and live) for smaller pieces of work as your service continues running.

Keep finding things that need improvement, do research to get the best solutions, iterate, then release.

## AI/Agent Live Notes

Live for AI agent systems requires ongoing operational discipline that traditional services do not:

**Model contracts must be versioned**: A model upgrade from your provider is equivalent to a major dependency upgrade. Treat it as one: pin your model version in production, test upgrades in a staging environment against your evaluation rubric, and deploy with staged rollout.

**Model deprecation is an incident response scenario**: Model providers deprecate models on their own schedules. Document your deprecation plan during Beta and review it in Live. When a deprecation notice arrives, you should already know what you will do.

**Cost-per-interaction is a live service metric**: Unlike traditional software where compute costs are relatively stable, AI services have variable per-interaction costs tied to token usage. Monitor cost-per-interaction as a first-class metric alongside latency and error rate. Unexpected spikes are often the first signal of a prompt or usage pattern change.

**Evaluation sampling never stops**: The Live phase evaluation programme is not a one-time audit. Run rubric-based sampling continuously — a small percentage of real interactions evaluated against your Alpha-defined rubric — and alert on score degradation.

> **Cross-reference**: The [agent-observability](https://github.com/ghostmachine-ai/agent-skills-for-context-engineering/tree/main/skills/agent-observability) skill covers the full Live-phase monitoring stack including drift detection and cost monitoring.
