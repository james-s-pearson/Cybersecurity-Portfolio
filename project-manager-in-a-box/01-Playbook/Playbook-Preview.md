# Project Manager in a Box
*A step-by-step playbook for Hybrid and Technical projects*

By James Pearson · Version 0.1 (prototype) · Released October 2026 · CC BY-NC-SA 4.0

**Latest version and all files:** [https://github.com/james-s-pearson/Cybersecurity-Portfolio/tree/main/project-manager-in-a-box](https://github.com/james-s-pearson/Cybersecurity-Portfolio/tree/main/project-manager-in-a-box). Links in this preview open the template files in this folder on GitHub.

## Contents

- **Chapter 1. Initiating**
  - 1.1 Capture the request and build the business case
  - 1.2 Define goals and success criteria
  - 1.3 Identify and analyze stakeholders
  - 1.4 Choose the delivery approach and tailor the playbook
  - 1.5 Draft and approve the project charter
  - 1.6 Hold the initiation gate and kickoff
- **Chapter 2. Planning**
  - 2.1 Elicit and analyze requirements
  - 2.2 Define scope and build the work breakdown structure (WBS)
  - 2.3 Build the schedule and milestones
  - 2.4 Estimate costs and set the budget
  - 2.5 Plan resources, roles and the RACI
  - 2.6 Plan risk management: identify, analyze and plan responses
  - 2.7 Plan communications and stakeholder engagement
  - 2.8 Plan quality and acceptance
  - 2.9 Plan sourcing and procurement
  - 2.10 Integrate the plan and pass the planning gate
- **Chapter 3. Executing**
  - 3.1 Acquire and onboard the team
  - 3.2 Direct the work and run the delivery cadence
  - 3.3 Assure quality
  - 3.4 Engage stakeholders and communicate
  - 3.5 Implement risk responses and resolve issues
  - 3.6 Manage vendors and contracts
  - 3.7 Manage project knowledge and decisions
- **Chapter 4. Monitoring & Controlling**
  - 4.1 Track performance: schedule, cost, scope and quality
  - 4.2 Control changes
  - 4.3 Monitor risks, issues and stakeholder engagement
  - 4.4 Validate scope and accept deliverables
  - 4.5 Report status and escalate
- **Chapter 5. Closing**
  - 5.1 Confirm final acceptance and transition to operations
  - 5.2 Close contracts and finances
  - 5.3 Run the retrospective and capture lessons learned
  - 5.4 Write the closeout and impact report
  - 5.5 Archive, release the team and celebrate
- Appendix A. Template library
- Appendix B. Agile quick reference
- Appendix C. Glossary
- Appendix D. Sources & further reading
- Appendix E. License & credits

## Tracks

**Hybrid track.** For projects that mix plan-driven work (fixed milestones, budgets, procurement, compliance) with iterative work (sprints, backlogs, frequent feedback). It is typical of business, operations, marketing and nonprofit programs, and of any project where some workstreams are predictable and others are not.

**Technical track (IT + Security).** For software, infrastructure, cloud, data and cybersecurity projects. It adds the gates technical work needs: architecture and security review, environments, test strategy, change advisory board (CAB) approval, cut-over and rollback, compliance evidence and handover to operations.

## Tailoring

| Area | Small | Medium | Large |
|---|---|---|---|
| Typical profile | < 3 months, < 5 people, one team, low risk | 3‒9 months, 5–20 people, a few teams or one vendor | > 9 months, multiple teams or vendors, regulated or high risk |
| Charter | One-page charter, approved by email | Full charter, sponsor sign-off | Full charter + business case, steering-committee approval |
| Schedule | Milestone list + task board | WBS + Gantt with dependencies | Integrated master schedule with critical path and baselines |
| Risk | Top-5 risks in the RAID log | Scored RAID log, reviewed bi-weekly | Risk management plan, quantitative analysis, weekly review |
| Change control | PM + sponsor approve by email | Change request form + change log | Formal CCB, impact analysis required |
| Reporting | Weekly email update | Weekly status report + dashboard | Weekly status + monthly steering pack + gate reviews |
| Closing | 30-minute retro + handover note | Retro, closeout report, transition sign-off | Full closeout, impact report, contract closure, audit archive |

## Chapter 1. Initiating
*Decide whether the project should exist, and authorize it.*

Initiating turns an idea or request into an authorized project. The goal is not a detailed plan. It is shared agreement on why the work matters, what success looks like, who is involved and how the work will broadly be delivered. Most failed projects can be traced back to a skipped or rushed Initiating phase: unclear goals, a missing sponsor or stakeholders who never agreed on scope.

**Exit gate:** Initiation gate: the sponsor approves the charter, the PM is named, and funding for planning is released.

### 1.1 Capture the request and build the business case

**What it is.** Turn the incoming request into a short, structured description of the problem, the opportunity, the options and the expected value. This is the business case: the argument that the project is worth doing at all.

**Why it matters.** It stops projects that should never start, and it gives every later decision (scope, budget, trade-offs) something to anchor to. When people argue about scope later, the business case decides.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Request, idea or mandate | Email, intake form, strategy document or leadership meeting | Requester / Sponsor |
| Strategic goals or OKRs | Annual plan, strategy deck, OKR tracker | Sponsor / Leadership |
| Historical data and lessons from similar projects | PMO lessons library, past closeout reports | PMO / PM |
| Rough cost and benefit figures | Finance partner, vendor quotes, operational metrics | Finance Partner |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Intake & Business Case (approved or rejected) | Repository: 01-Initiating | PM (author), Sponsor (approver) |
| Go/no-go decision | Decision Log (workbook) and 00-Admin | Sponsor |

**Templates:** [T01 Project Intake & Business Case](../02-Templates/T01-Project-Intake-Business-Case.docx), [T17 Decision Log](../02-Templates/T17-Decision-Log.xlsx)

**How to do it**

1. Meet the requester and ask the ‘5 Ws’: what, why, who benefits, when and where.
2. Ask three stakeholders from different areas to describe the problem, then combine their answers into one problem statement.
3. Quantify the cost of doing nothing and the expected benefit.
4. Compare at least two options, including doing nothing, and recommend one.
5. Present to the sponsor and record the decision.

> **Hybrid:** Show which parts of the value can be delivered early (e.g., a pilot or MVP) and which require a fixed-date launch. That shapes the hybrid approach in Step 1.4.
>
> **Technical (IT + Security):** Add an early view of the technical options (build, buy, configure, SaaS), the systems affected, data sensitivity (public, internal, confidential, regulated) and any obvious security or compliance triggers.

**Done when:** Problem and benefits are quantified; Options compared; Sponsor decision recorded

### 1.2 Define goals and success criteria

**What it is.** Write measurable goals (SMART goals or OKRs) and the criteria the sponsor will use to judge the project a success, covering both project success (on time, on budget, in scope) and product success (adoption, savings, risk reduced).

**Why it matters.** Measurable goals make trade-offs objective and keep everyone aiming at the same target. Without them, ‘done’ becomes a matter of opinion and closeout becomes a negotiation.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Approved business case | 01-Initiating | Sponsor |
| Organizational OKRs and KPIs | Strategy or OKR tracker | Leadership |
| Baseline metrics (today’s numbers) | Operational reports, analytics, finance | Business owner / BA |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Goals and success criteria | Charter section 2 and the workbook Setup tab | PM (author), Sponsor (approver) |

**Templates:** [T02 Project Charter](../02-Templates/T02-Project-Charter.docx)

**How to do it**

1. Draft 2–4 goals using SMART (Specific, Measurable, Achievable, Relevant, Time-bound).
2. For each goal, record the baseline value, the target value and the data source.
3. Separate project success criteria from product or benefit success criteria.
4. Agree with the sponsor how and when the benefits will be measured. Some benefits arrive after closeout.

> **Hybrid:** Add iteration-level goals (e.g., ‘pilot used by 20 volunteers by week 6’) as well as the end-of-project targets.
>
> **Technical (IT + Security):** Include non-functional targets: availability (e.g., 99.9%), performance, recovery time objective (RTO) and recovery point objective (RPO), and security outcomes (e.g., ‘MFA enforced for 100% of admin accounts’).

**Done when:** Every goal has a baseline, a target and a data source; Sponsor agrees how success will be measured

### 1.3 Identify and analyze stakeholders

**What it is.** List everyone who can affect, or is affected by, the project. Assess their power, their interest and their current versus desired level of support.

**Why it matters.** Stakeholders who are missed become late requirements, blockers or opponents. Early analysis tells you where to spend your relationship time.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Business case and charter draft | 01-Initiating | PM |
| Organization charts | HR system / intranet | Functional managers |
| Sponsor and team knowledge | Interviews | Sponsor / PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Stakeholder Register with power/interest grid | Workbook: Stakeholders tab | PM |

**Templates:** [T03 Stakeholder Register & Power/Interest Grid](../02-Templates/T03-Stakeholder-Register-Power-Interest-Grid.xlsx)

**How to do it**

1. Brainstorm stakeholders with the sponsor and work through each group: users, managers, IT, finance, legal, vendors, regulators and partners.
2. Interview key stakeholders: priorities, concerns, preferred role, preferred communication.
3. Score Power and Interest 1–5 and place each person on the grid.
4. Plan an engagement action for anyone whose current support is below the level you need.

> **Hybrid:** Identify the Product Owner early. In hybrid work that person makes the day-to-day priority calls.
>
> **Technical (IT + Security):** Include the Security, Privacy, Infrastructure and Operations owners, the Change Advisory Board (CAB), and any auditor or compliance contact.

**Done when:** Register complete; Every high-power stakeholder has an engagement action; Product Owner identified

### 1.4 Choose the delivery approach and tailor the playbook

**What it is.** Decide how each workstream will be delivered (predictive, agile or hybrid) and how much of this playbook the project needs (Small, Medium or Large).

**Why it matters.** The approach drives everything that follows: how you plan, report and handle change. Tailoring keeps the process proportionate, because too much process slows small projects down and too little sinks large ones.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Business case and goals | 01-Initiating | PM |
| Organizational standards or PMO methodology | PMO / intranet | PMO |
| Team experience and constraints | Functional managers, Tech Lead | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Approach & Tailoring Worksheet | Repository: 01-Initiating | PM |

**Templates:** [T04 Delivery Approach & Tailoring Worksheet](../02-Templates/T04-Delivery-Approach-Tailoring-Worksheet.xlsx)

**How to do it**

1. Score each workstream on the suitability questions in T04 (requirement stability, feedback availability, cost of change, regulation and so on).
2. Choose an approach per workstream. One project can mix them.
3. Pick the project size using the tailoring table in ‘How to use this playbook’.
4. Record what you will skip or simplify and why.

> **Hybrid:** Typical pattern: plan-driven governance (milestones, budget, gates) wrapped around agile delivery (sprints, backlog). Make the link explicit, for example ‘Milestone M3 = end of Sprint 4’.
>
> **Technical (IT + Security):** Regulated or production-impacting work usually keeps formal gates (architecture review, security review, CAB) even when the build happens in sprints.

**Done when:** Approach chosen for each workstream; Size and tailoring decisions recorded

### 1.5 Draft and approve the project charter

**What it is.** Write the charter: the short document that formally authorizes the project, names the PM and sets the high-level scope, goals, milestones, budget, risks and governance.

**Why it matters.** The charter gives the PM authority and gives everyone a single reference point. Under PMI’s approach it is the formal start of the project.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Business case, goals, stakeholder register, approach worksheet | 01-Initiating | PM |
| High-level budget and funding source | Finance Partner | Finance Partner / Sponsor |
| Known constraints and assumptions | Sponsor, SMEs | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Signed Project Charter | Repository: 00-Admin; summary in the workbook Setup tab | PM (author), Sponsor (approver) |

**Templates:** [T02 Project Charter](../02-Templates/T02-Project-Charter.docx), [T10 RACI Matrix](../02-Templates/T10-RACI-Matrix.xlsx)

**How to do it**

1. Fill in T02 using the earlier outputs. Don’t rewrite what is already approved.
2. Write an explicit out-of-scope list.
3. Name the PM and their decision rights (e.g., can approve changes under 5 days or $5,000).
4. Review the draft with key stakeholders, resolve comments, then get the sponsor’s signature.

> **Hybrid:** Describe scope as outcomes plus a prioritized feature list rather than a fixed specification, and state how the backlog may change within the fixed date and budget.
>
> **Technical (IT + Security):** Add the systems in scope, data classification, the required review gates (architecture, security, CAB) and the target environments.

**Done when:** Charter signed; PM authority stated; Out-of-scope list agreed

### 1.6 Hold the initiation gate and kickoff

**What it is.** Run a short gate review to confirm that Initiating is complete, then hold a kickoff meeting with the core team and key stakeholders to launch Planning.

**Why it matters.** The gate makes sure the project is ready to move on. The kickoff builds shared understanding and momentum, and gives the team a chance to raise concerns early, when changes are still cheap.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Signed charter, stakeholder register | 00-Admin, workbook | PM |
| Team availability | Functional managers | Functional managers |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Gate decision | Decision Log | Sponsor |
| Kickoff notes and action items | 03-Executing/Meetings; actions in the workbook | PM |

**Templates:** [T05 Kickoff Meeting Kit](../02-Templates/T05-Kickoff-Meeting-Kit.docx), [T18 Meeting Agenda & Minutes](../02-Templates/T18-Meeting-Agenda-Minutes.docx), [T17 Decision Log](../02-Templates/T17-Decision-Log.xlsx)

**How to do it**

1. Run the gate checklist: charter signed, sponsor engaged, funding confirmed for Planning.
2. Send the kickoff pre-read 48 hours ahead.
3. At kickoff, cover the why (sponsor), scope, milestones, roles (RACI), ways of working and next steps.
4. Send notes and actions within 24 hours.

> **Hybrid:** Agree the team’s working agreement at kickoff: sprint length, ceremonies and how milestone reporting will draw on sprint data.
>
> **Technical (IT + Security):** Confirm access, tools and environments needed in the first two weeks (repositories, ticketing, cloud accounts, test data).

**Done when:** Gate passed; Kickoff held; Actions logged


## Chapter 2. Planning
*Work out how the work will get done, and set the baselines you will measure against.*

Planning turns the charter into an integrated plan: what will be delivered (scope), when (schedule), for how much (budget), by whom (resources), with what risks, how people will be kept informed and how quality will be assured. The output is a set of baselines, the approved versions of scope, schedule and cost that progress is measured against. In hybrid work, plan the milestones in detail and keep the detailed backlog progressive (rolling-wave planning).

**Exit gate:** Planning gate: the sponsor approves the integrated plan and baselines; the team commits to the schedule.

### 2.1 Elicit and analyze requirements

**What it is.** Find out from stakeholders what the solution must do (functional requirements) and how well it must do it (non-functional requirements). Record them in a register or backlog.

**Why it matters.** Requirements are the bridge between the business goal and the deliverables. Most rework comes from requirements that were missing, vague or never agreed.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Charter, goals, stakeholder register | 00-Admin, workbook | PM |
| Current process documents, user feedback, support tickets | Business owners, service desk | BA / PO |
| Policies and regulations | Legal, Compliance, Security | Compliance / Security Lead |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Requirements Register or Product Backlog | Workbook: Requirements tab (or the team’s backlog tool) | BA / Product Owner |

**Templates:** [T06 Requirements Register / Product Backlog](../02-Templates/T06-Requirements-Register-Product-Backlog.xlsx)

**How to do it**

1. Choose methods: interviews, workshops, observation, surveys, document review, prototyping.
2. Write each requirement as a user story or ‘shall’ statement with acceptance criteria.
3. Prioritize with MoSCoW together with the sponsor and the PO.
4. Trace each requirement to a goal, so anything that doesn’t serve a goal is challenged.

> **Hybrid:** Fully specify the Musts for the first release. Keep later items as epics and refine them before each sprint (backlog refinement).
>
> **Technical (IT + Security):** Capture non-functional requirements explicitly: security, privacy, accessibility (WCAG 2.2 AA), performance, availability, logging, data retention and integration interfaces.

**Done when:** Musts have acceptance criteria; Priorities agreed with the PO and sponsor; NFRs captured

### 2.2 Define scope and build the work breakdown structure (WBS)

**What it is.** Turn the requirements into a scope statement (deliverables, acceptance criteria, exclusions) and break the deliverables down into work packages small enough to estimate and assign.

**Why it matters.** The WBS is the backbone of the plan: the schedule, budget, RACI and risk register all hang off it. If work isn’t in the WBS, it isn’t in scope.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Requirements register | Workbook: Requirements | BA / PO |
| Charter scope and exclusions | 00-Admin | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Scope Statement (scope baseline) | Repository: 02-Planning | PM (author), Sponsor (approver) |
| WBS | Workbook: Schedule tab (WBS IDs) | PM with the team |

**Templates:** [T07 Scope Statement](../02-Templates/T07-Scope-Statement.docx), [T08 WBS & Schedule (Gantt)](../02-Templates/T08-WBS-Schedule-Gantt.xlsx)

**How to do it**

1. Write the scope statement: deliverables, acceptance criteria, exclusions, constraints, assumptions.
2. Run a WBS workshop with the people who will do the work. Decompose deliverables, not activities.
3. Stop decomposing when a work package can be estimated and owned by one person (about 1–10 days).
4. Number the items (1.0, 1.1, 1.1.1) and keep a WBS dictionary for anything unclear.

> **Hybrid:** For agile workstreams, the WBS stops at epic or release level, and the backlog holds the detail.
>
> **Technical (IT + Security):** Include the work people often forget: environments, CI/CD pipeline, data migration, security testing, documentation, runbooks, training, cut-over and hypercare.

**Done when:** Scope statement signed; WBS covers 100% of the scope; Each work package has an owner

### 2.3 Build the schedule and milestones

**What it is.** Sequence the work packages, estimate their durations, assign owners, identify dependencies and the critical path, and set milestone dates.

**Why it matters.** The schedule turns scope into a commitment and shows which tasks have no room to slip (the critical path), so you know where to focus.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| WBS | Workbook: Schedule | PM |
| Resource availability and calendars | Functional managers, team | Functional managers |
| Estimates from the people doing the work | Estimating sessions | Delivery team / Tech Lead |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Project Schedule with milestones (schedule baseline) | Workbook: Schedule tab | PM |

**Templates:** [T08 WBS & Schedule (Gantt)](../02-Templates/T08-WBS-Schedule-Gantt.xlsx)

**How to do it**

1. Ask the people doing the work for estimates. Break large tasks down and question their assumptions.
2. Use three-point estimates for uncertain work: (Optimistic + 4×Most likely + Pessimistic) ÷ 6 (the PERT method).
3. Enter the dependencies, then identify the critical path (the longest chain of dependent tasks).
4. Calculate float, also called slack: the number of days a task can slip without delaying the next task (free float) or the project finish (total float). Tasks on the critical path have no total float, so any slip moves the end date; track them most closely and mention them by name in status updates. Tasks off the path have float you can use when balancing resources. Recheck after every schedule change, because the critical path can move.
5. Add milestones where success can be tested, budget is committed or stakeholders need an update.
6. Add schedule contingency for the top risks and copy the approved dates into the Baseline columns.

> **Hybrid:** Show sprints as recurring blocks on the Gantt and tie each milestone to a sprint review. Report sprint velocity next to milestone status.
>
> **Technical (IT + Security):** Schedule review gates (architecture, security, CAB) and change freeze windows explicitly. They are fixed points that development work has to fit around.

**Done when:** Dependencies entered; Critical path known; Baseline saved; Team commits to the dates

### 2.4 Estimate costs and set the budget

**What it is.** Estimate the cost of every work package (labor, vendors, software, hardware, travel), add reserves and aggregate them into a time-phased budget (cost baseline).

**Why it matters.** Funding approval depends on a credible estimate, and you can’t control costs without a baseline to compare actual spend against.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| WBS and schedule | Workbook | PM |
| Labor rates and cost policies | Finance / HR | Finance Partner |
| Vendor quotes and license prices | Procurement, vendors | Procurement |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Budget and cost baseline | Workbook: Budget tab | PM (owner), Finance Partner (validator) |

**Templates:** [T09 Budget & Cost Tracker](../02-Templates/T09-Budget-Cost-Tracker.xlsx)

**How to do it**

1. Estimate bottom-up from the WBS: hours × rate plus non-labor costs.
2. Add a contingency reserve for identified risks and get management to agree a reserve for unknowns.
3. Phase the spend by month to match the schedule.
4. Have the Finance Partner validate it, then get the sponsor’s approval.

> **Hybrid:** Agile workstreams are often funded by team capacity (team cost per sprint × number of sprints). Show that alongside the fixed-cost items.
>
> **Technical (IT + Security):** Include cloud consumption, license tiers, security tools, penetration testing, extra environments, and ongoing run costs after go-live (total cost of ownership).

**Done when:** Budget validated by Finance; Reserves shown separately; Baseline approved

### 2.5 Plan resources, roles and the RACI

**What it is.** Decide who you need, when and for how much of their time, and make clear who is Responsible, Accountable, Consulted and Informed for each deliverable and decision.

**Why it matters.** Unclear ownership is one of the most common causes of delay. A RACI turns ‘I thought you were doing it’ into an agreed fact.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| WBS and schedule | Workbook | PM |
| Staff availability and skills | Functional managers | Functional managers |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| RACI matrix | Workbook: RACI tab | PM |
| Resource commitments | Email or written agreement in 00-Admin | Functional managers |

**Templates:** [T10 RACI Matrix](../02-Templates/T10-RACI-Matrix.xlsx)

**How to do it**

1. List the roles needed and the percentage of each person’s time, by month.
2. Plan people at about 60 to 80% of their available project time, after subtracting meetings and leave (a common focus factor in agile capacity planning; a rule of thumb, not a standard). Support work and surprises take the rest, and waiting and delays grow sharply as a team nears full load, so a plan that fills everyone’s week leaves no room to recover. If the plan needs more than people can give, change it now: move work, add people or cut scope. Cross-train so that no task depends on one person, and plan around known leave.
3. Get managers to commit those people in writing.
4. Build the RACI with exactly one Accountable per row.
5. Review it with the team and resolve any disputes over who owns what.

> **Hybrid:** Spell out how the PM, PO and Scrum Master/Team Lead roles fit together. Who owns the milestone plan, and who owns the backlog?
>
> **Technical (IT + Security):** Assign named owners for the architecture, security, data, environments, releases and on-call support.

**Done when:** Every deliverable has one A; Resource commitments in writing

### 2.6 Plan risk management: identify, analyze and plan responses

**What it is.** Find the risks to the project, score their probability and impact, and decide a response for each significant one. Record assumptions and dependencies at the same time.

**Why it matters.** Risks you plan for are cheaper than surprises. A visible risk log also builds sponsor confidence and justifies the contingency reserves.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Charter, scope, schedule, budget | Workbook / 02-Planning | PM |
| Lessons from past projects | PMO lessons library | PMO |
| Expert input | Risk workshop with the team and SMEs | Team / SMEs |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| RAID Log | Workbook: RAID tab | PM (owner); each item has a named owner |

**Templates:** [T11 RAID Log (Risks, Assumptions, Issues, Dependencies)](../02-Templates/T11-RAID-Log-Risks-Assumptions-Issues-Dependencies.xlsx)

**How to do it**

1. Run a risk workshop. Go category by category: scope, schedule, cost, people, technology, vendors, compliance, change adoption.
2. Write each risk as ‘Because of <cause>, <event> may occur, leading to <impact>’.
3. Before scoring, agree what the numbers mean on this project. A scale that suits a three-month internal project will mislead a nine-month one. Five levels is a common choice, not a requirement. The example scale below is for a Medium project. Write your own limits in days and money, keep them with the RAID log, and use them every time so everyone scores the same way.
4. Score probability and impact from 1 to 5. Anything scoring 12 or more is Red and 6–11 is Amber.
5. Choose a response (avoid, mitigate, transfer, accept) with an owner and a due date.
6. Copy the assumptions from the scope statement and the external dependencies into the same log.

> **Hybrid:** Review the risks at every sprint review. The demos often reveal new ones.
>
> **Technical (IT + Security):** Run a threat model (e.g., STRIDE) for new systems and record security risks in the RAID log with the Security Lead as owner. Include vendor and third-party risk.

**Done when:** Top risks scored; Every Red/Amber risk has an owner and response; Assumptions logged

**Example risk scale for a Medium project**

| Score | Probability | Impact |
|---|---|---|
| 1 | Would surprise the team | Absorbed within a normal week |
| 2 | Could happen, but not expected | A few days’ slip, or a small cost the team can cover |
| 3 | About as likely as not | About a week’s slip, or a cost the sponsor should hear about |
| 4 | More likely than not | Puts a milestone or the contingency reserve at risk |
| 5 | Expected to happen | Puts the project’s goal or go-live at risk |

### 2.7 Plan communications and stakeholder engagement

**What it is.** Decide who needs what information, when, in what format and from whom. Plan how to move each key stakeholder from their current to their desired level of engagement.

**Why it matters.** Many project failures are communication failures. A plan makes communication routine instead of reactive and builds trust with stakeholders.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Stakeholder register | Workbook: Stakeholders | PM |
| Stakeholder preferences | Stakeholder interviews | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Communication Plan | Workbook: Comms tab | PM |
| Recurring meetings on the calendar | Team calendar | PM |

**Templates:** [T12 Communication Plan](../02-Templates/T12-Communication-Plan.xlsx), [T03 Stakeholder Register & Power/Interest Grid](../02-Templates/T03-Stakeholder-Register-Power-Interest-Grid.xlsx)

**How to do it**

1. Create one row per audience: sponsor, steering committee, team, end users, IT operations and so on.
2. Set the purpose, content, channel, frequency and owner for each.
3. Book recurring meetings now: status, steering and team ceremonies.
4. Add engagement actions for resistant or unaware stakeholders.

> **Hybrid:** Invite stakeholders to sprint reviews. A live demo often does more than a written status report.
>
> **Technical (IT + Security):** Plan release notes, maintenance-window notices, CAB submissions and incident communications.

**Done when:** Every key stakeholder has a communication row; Recurring meetings booked

### 2.8 Plan quality and acceptance

**What it is.** Define the quality standards, the review and test activities, and the criteria and process for accepting each deliverable.

**Why it matters.** Quality is meeting requirements and stakeholder expectations. Agreeing in advance how it will be judged avoids arguments over acceptance at the end.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Requirements and acceptance criteria | Workbook: Requirements | BA / PO |
| Organizational and industry standards | PMO, Compliance, Security | Quality / Compliance |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Quality & Acceptance Plan (incl. Definition of Done and test strategy) | Repository: 02-Planning | PM / Tech Lead |

**Templates:** [T13 Quality & Acceptance Plan](../02-Templates/T13-Quality-Acceptance-Plan.docx)

**How to do it**

1. List the standards that apply.
2. For each deliverable, define how its quality will be checked and who accepts it.
3. Write the Definition of Done with the team.
4. Schedule the quality activities in the plan (reviews, tests, audits).

> **Hybrid:** Use a Definition of Done for sprint work and formal acceptance criteria for milestone deliverables.
>
> **Technical (IT + Security):** Write a test strategy covering unit, integration, system, UAT, performance, accessibility and security testing (SAST/DAST, vulnerability scans, penetration test), plus the entry and exit criteria for each.

**Done when:** Acceptance criteria for every deliverable; Definition of Done agreed; Test strategy approved (Technical track)

### 2.9 Plan sourcing and procurement

**What it is.** Decide what to make versus buy, then plan how vendors will be selected, contracted and managed. Write a statement of work (SOW) for each purchase.

**Why it matters.** Vendor lead times and contract terms often decide the schedule. A clear SOW protects scope, quality and payment.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Scope, WBS, budget | 02-Planning, workbook | PM |
| Procurement policies and approved vendor list | Procurement | Procurement |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Statement(s) of Work | Repository: 02-Planning/Procurement | PM (author), Procurement (owner) |
| Vendor selection decision | Decision Log | Sponsor / Procurement |

**Templates:** [T14 Statement of Work (SOW)](../02-Templates/T14-Statement-of-Work-SOW.docx), [T17 Decision Log](../02-Templates/T17-Decision-Log.xlsx)

**How to do it**

1. Make-or-buy analysis for each major component.
2. Write the SOW: deliverables, acceptance, timeline, payment milestones, security terms.
3. Run the selection (RFQ or RFP), score the vendors against agreed criteria and record the decision.
4. Add vendor milestones and dependencies to the schedule and RAID log.

> **Hybrid:** For vendors working in sprints, contract for capacity plus outcome-based milestones rather than a fixed specification.
>
> **Technical (IT + Security):** Include a vendor security assessment (e.g., SOC 2 Type II report review), data processing agreement, SLAs, data residency and exit/return-of-data terms.

**Done when:** SOW reviewed by Procurement and Legal; Vendor dates in the schedule

### 2.10 Integrate the plan and pass the planning gate

**What it is.** Bring all the plans together into a consistent whole, check that scope, schedule, cost and resources agree with each other, and get approval for the baselines.

**Why it matters.** The parts of a plan can each look fine but contradict each other, for example a schedule that assumes people the budget doesn’t fund. Integration catches this before execution starts.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| All planning outputs (Steps 2.1–2.9) | 02-Planning, workbook | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Approved project management plan and baselines | Repository: 02-Planning; baselines frozen in the workbook | PM (author), Sponsor (approver) |
| Planning gate decision | Decision Log | Sponsor |

**Templates:** [T17 Decision Log](../02-Templates/T17-Decision-Log.xlsx), [T15 Status Report](../02-Templates/T15-Status-Report.docx)

**How to do it**

1. Cross-check: every WBS item has an owner (RACI), dates (schedule) and cost (budget).
2. Confirm the risk reserves cover the top risks.
3. Present the plan to the sponsor or steering committee for approval.
4. Freeze the baselines. From now on, changes go through change control (Step 4.2).

> **Hybrid:** Approve the milestone plan and the release roadmap. The detailed backlog stays flexible within them.
>
> **Technical (IT + Security):** Get architecture and security design approval at this gate, or schedule them as explicit early milestones.

**Done when:** Baselines approved; Gate decision logged; Change control active


## Chapter 3. Executing
*Lead the team and do the work defined in the plan.*

Executing is where most of the time and money goes. The PM’s job shifts from planning to leading: getting resources in place, keeping the team focused, removing blockers, assuring quality, managing vendors and keeping stakeholders engaged. Executing and Monitoring & Controlling run at the same time, so treat Chapter 4 as the control loop around this chapter.

**Exit gate:** No formal gate. Execution moves into Closing when every deliverable has been accepted (Step 4.4).

### 3.1 Acquire and onboard the team

**What it is.** Confirm the people on the project, onboard them (context, access, tools, working agreement) and build the team’s working relationships.

**Why it matters.** A team that understands the goal and has what it needs on day one delivers faster. Missing access and unclear expectations cost weeks.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Resource commitments, RACI | 00-Admin, workbook | PM / Functional managers |
| Onboarding needs (access, tools, training) | Tech Lead, IT | Tech Lead |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Team roster and working agreement | Workbook: Setup tab; 03-Executing | PM |
| Access and tooling confirmed | Ticket references in the RAID log or Decision Log | Tech Lead / IT |

**Templates:** [T05 Kickoff Meeting Kit](../02-Templates/T05-Kickoff-Meeting-Kit.docx), [T10 RACI Matrix](../02-Templates/T10-RACI-Matrix.xlsx)

**How to do it**

1. Hold short one-to-ones: experience, goals, how they like to work, how you can support them.
2. Write a team working agreement: hours, response times, tools, decision rules, escalation path.
3. Request access and equipment in advance and track it as a dependency.
4. Revisit the RACI with the full team.

> **Hybrid:** Set up the sprint ceremonies (planning, daily stand-up, review, retrospective) and how milestone reporting will draw on sprint data.
>
> **Technical (IT + Security):** Grant least-privilege access, set up the repositories, branching strategy, CI/CD and environments, and arrange any security awareness or secure-coding training required.

**Done when:** Everyone has access and tools; Working agreement published

### 3.2 Direct the work and run the delivery cadence

**What it is.** Run the day-to-day rhythm that turns the plan into deliverables: task assignment, stand-ups, sprints or work-package check-ins, removing blockers and keeping the workbook up to date.

**Why it matters.** A steady cadence makes progress visible and surfaces blockers while they are still small.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Schedule / backlog | Workbook: Schedule; backlog tool | PM / PO |
| Approved plan and RACI | 02-Planning | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Deliverables (work products) | Repository: 03-Executing or the team’s tools | Delivery team |
| Updated schedule (% complete, status) | Workbook: Schedule | Task owners (update), PM (check) |

**Templates:** [T08 WBS & Schedule (Gantt)](../02-Templates/T08-WBS-Schedule-Gantt.xlsx), [T18 Meeting Agenda & Minutes](../02-Templates/T18-Meeting-Agenda-Minutes.docx)

**How to do it**

1. Hold a short daily or twice-weekly check-in: progress, plan for the day, blockers.
2. Ask task owners to update the % complete and status in the workbook every week.
3. Clear blockers within 24–48 hours or escalate them.
4. Protect the team from unplanned work. Send new requests through change control.

> **Hybrid:** Sprint planning pulls from the prioritized backlog. Before each sprint, agree a one-sentence sprint goal; plan to 60 to 80% of the team’s available hours, after subtracting meetings and leave; pick backlog items in priority order that fit, each with an owner and any dependency named; confirm the Definition of Done everyone will use (for example reviewed, tested, documented and accepted by the product owner); name the top risks for the sprint and who watches them; and book the sprint review and retrospective. The PM keeps the milestone view current and manages dependencies between agile and plan-driven workstreams. Appendix B has the details.
>
> **Technical (IT + Security):** Use pull requests with peer review, automated builds and tests, and track technical debt explicitly as backlog items.

**Done when:** Cadence running; Workbook updated weekly; Blockers resolved or escalated

### 3.3 Assure quality

**What it is.** Carry out the quality activities in the plan (reviews, tests, audits) and improve the process when defects or rework show up.

**Why it matters.** Finding defects early is far cheaper than finding them at acceptance or in production.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Quality & Acceptance Plan | 02-Planning | PM / Tech Lead |
| Deliverables in progress | 03-Executing | Delivery team |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Review and test results, defect log | 03-Executing/Quality; defects in the RAID log or test tool | Tech Lead / QA |

**Templates:** [T13 Quality & Acceptance Plan](../02-Templates/T13-Quality-Acceptance-Plan.docx), [T11 RAID Log (Risks, Assumptions, Issues, Dependencies)](../02-Templates/T11-RAID-Log-Risks-Assumptions-Issues-Dependencies.xlsx)

**How to do it**

1. Run the planned peer reviews and tests and record the results.
2. Run a short quality audit at least once per phase: are we following our own plan?
3. Look for patterns in defects and fix the cause, not just the defect.
4. Report the quality metrics in the status report (defects open, pass rate).

> **Hybrid:** Check every increment against the Definition of Done at the sprint review. Run a pilot or beta release to test with real users before the full launch.
>
> **Technical (IT + Security):** Run SAST/DAST and dependency scanning in the pipeline, fix critical and high vulnerabilities before release, and keep the test evidence for audit.

**Done when:** Planned quality activities completed; Defect trends reported

### 3.4 Engage stakeholders and communicate

**What it is.** Carry out the communication plan: status updates, steering meetings, demos and engagement actions. Adjust them as stakeholder needs change.

**Why it matters.** Stakeholders who feel informed and heard support the project. Surprises destroy trust faster than bad news does.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Communication plan, stakeholder register | Workbook: Comms, Stakeholders | PM |
| Performance data | Workbook: Dashboard | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Status reports and meeting minutes | 04-Monitoring/Status; 03-Executing/Meetings | PM |
| Updated stakeholder register | Workbook: Stakeholders | PM |

**Templates:** [T15 Status Report](../02-Templates/T15-Status-Report.docx), [T18 Meeting Agenda & Minutes](../02-Templates/T18-Meeting-Agenda-Minutes.docx), [T12 Communication Plan](../02-Templates/T12-Communication-Plan.xlsx)

**How to do it**

1. Send status updates on the agreed day, in the same format every time.
2. Deliver bad news early, with a plan and a request for what you need.
3. Follow up on engagement actions for resistant or unaware stakeholders.
4. Ask key stakeholders every month: ‘Is this update giving you what you need?’

> **Hybrid:** Use sprint reviews and demos as the main way to engage stakeholders. Status reports summarize the trend across sprints.
>
> **Technical (IT + Security):** Publish maintenance and release notices, and coordinate with the service desk so support is ready for user questions.

**Done when:** Communications sent on schedule; Engagement gaps narrowing

### 3.5 Implement risk responses and resolve issues

**What it is.** Carry out the planned risk responses when their triggers occur, and manage issues (problems that have already happened) through to resolution.

**Why it matters.** A risk plan only has value if it is acted on. Issues left open grow and become schedule or budget overruns.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| RAID Log | Workbook: RAID | PM / item owners |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Updated RAID Log (actions, status) | Workbook: RAID | Item owners (update), PM (check) |
| Escalations | Email or steering pack; recorded in the Decision Log | PM |

**Templates:** [T11 RAID Log (Risks, Assumptions, Issues, Dependencies)](../02-Templates/T11-RAID-Log-Risks-Assumptions-Issues-Dependencies.xlsx), [T17 Decision Log](../02-Templates/T17-Decision-Log.xlsx)

**How to do it**

1. Review the Red and Amber items in every status meeting.
2. When a risk occurs, change its type to Issue and start the planned response.
3. Escalate any issue the team can’t resolve within its authority: state the problem, its impact, the options, your recommendation and the decision needed by when.
4. Close items when they are resolved and note what worked.

> **Hybrid:** Raise blockers at the daily stand-up and log them in the RAID log only if they last more than a day or affect a milestone.
>
> **Technical (IT + Security):** Route security incidents through the organization’s incident response process, not just the project RAID log.

**Done when:** No Red item without an active response; Escalations made within agreed thresholds

### 3.6 Manage vendors and contracts

**What it is.** Manage vendor performance against the SOW: progress, quality, invoices, issues and relationships.

**Why it matters.** Vendor slips are among the most common causes of delay. Active management catches them early, and documented performance protects you if disputes arise.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| SOWs and contracts | 02-Planning/Procurement | Procurement |
| Vendor status reports and invoices | Vendor | Vendor / PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Vendor performance notes and accepted deliverables | 03-Executing/Vendors | PM / Procurement |

**Templates:** [T14 Statement of Work (SOW)](../02-Templates/T14-Statement-of-Work-SOW.docx), [T21 Acceptance & Transition Sign-off](../02-Templates/T21-Acceptance-Transition-Sign-off.docx)

**How to do it**

1. Hold regular vendor check-ins linked to the SOW milestones.
2. Approve invoices only against accepted deliverables.
3. Log vendor risks and issues in the RAID log.
4. Escalate contractual issues to Procurement early.

> **Hybrid:** Include vendor staff in the sprint ceremonies so their work stays visible.
>
> **Technical (IT + Security):** Check vendor access is least-privilege and time-limited, and that the security obligations in the contract are being met.

**Done when:** Vendor deliverables accepted before payment; Vendor risks logged

### 3.7 Manage project knowledge and decisions

**What it is.** Record decisions, rationale and know-how as the project goes, so the team and future projects can use them.

**Why it matters.** Decisions that aren’t written down get revisited. Knowledge that isn’t captured leaves with the people who hold it.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Meetings, workshops, conversations | Calendar, notes | PM / Team |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Decision Log | Workbook: Decisions | PM |
| Working lessons learned | Workbook: Lessons | PM / Team |

**Templates:** [T17 Decision Log](../02-Templates/T17-Decision-Log.xlsx), [T19 Retrospective & Lessons Learned Register](../02-Templates/T19-Retrospective-Lessons-Learned-Register.xlsx)

**How to do it**

1. Log every significant decision within 24 hours, including the options considered and why one was chosen.
2. Capture lessons as they happen, not only at the end.
3. Keep documents in the standard repository structure.

> **Hybrid:** Retrospectives produce lessons every sprint. Copy the reusable ones into the Lessons tab.
>
> **Technical (IT + Security):** Keep architecture decision records (ADRs), runbooks and as-built documentation in the code repository or wiki.

**Done when:** Decision Log current; Lessons captured during the project


## Chapter 4. Monitoring & Controlling
*Measure progress against the plan, control change, and keep the project on track.*

Monitoring & Controlling runs alongside Executing from the first day of execution until closing. It compares actual performance with the baselines, forecasts where the project is heading, controls changes and makes sure deliverables are accepted. The Project Workbook dashboard is designed to support this chapter: update the tabs every week and the insights and status numbers update automatically.

**Exit gate:** Ongoing. Phase or release gates use the same data. The project moves to Closing when all deliverables are accepted.

### 4.1 Track performance: schedule, cost, scope and quality

**What it is.** Compare actual progress and spend with the baselines every week, calculate the variances and forecast the finish date and final cost.

**Why it matters.** Small variances caught early are cheap to fix. Forecasts let the sponsor decide while there are still options.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Updated schedule, budget actuals, RAID log | Workbook | Task owners, Finance Partner |
| Baselines | Workbook (baseline columns) | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Performance metrics and RAG status | Workbook: Dashboard | PM |

**Templates:** [T08 WBS & Schedule (Gantt)](../02-Templates/T08-WBS-Schedule-Gantt.xlsx), [T09 Budget & Cost Tracker](../02-Templates/T09-Budget-Cost-Tracker.xlsx)

**How to do it**

1. Every week: tasks updated, actuals entered, RAID log reviewed.
2. Check the dashboard: % complete vs planned, overdue tasks, budget variance, open Red risks.
3. Optional earned value check: Schedule Performance Index (SPI) = EV ÷ PV and Cost Performance Index (CPI) = EV ÷ AC. Values below 0.9 call for action.
4. Agree corrective actions for any variance outside the thresholds (e.g., more than 10% or more than 5 days).

> **Hybrid:** Track sprint velocity and the release burn-up alongside milestone status. A falling velocity is an early warning that a milestone is at risk.
>
> **Technical (IT + Security):** Add delivery metrics where they are useful, such as deployment frequency, change failure rate, open critical vulnerabilities and test pass rate.

**Done when:** Dashboard current every week; Variances explained with an action

### 4.2 Control changes

**What it is.** Assess every proposed change to scope, schedule, budget or quality, decide on it through the agreed authority and update the baselines when a change is approved.

**Why it matters.** Uncontrolled change (scope creep) is one of the main reasons projects miss their targets. Change control doesn’t prevent change. It makes sure each change is deliberate.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Change request | Any stakeholder | Requester |
| Baselines and the PM’s authority limits | Workbook; charter | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Change Log with decisions | Workbook: Changes | PM |
| Updated baselines and plans (if approved) | Workbook; 02-Planning | PM |

**Templates:** [T16 Change Request & Change Log](../02-Templates/T16-Change-Request-Change-Log.xlsx), [T17 Decision Log](../02-Templates/T17-Decision-Log.xlsx)

**How to do it**

1. Log the request and analyze its impact on scope, schedule, cost, risk, quality and resources.
2. Recommend approve, reject or defer, and send it to the right approver (PM, sponsor or CCB).
3. Record the decision. If approved, update the baselines and the affected plans.
4. Tell the affected stakeholders and the team.

> **Hybrid:** Re-prioritizing items within the backlog (swapping items of similar size) is normal agile practice and does not need a change request. Changes to milestones, budget or the overall scope do.
>
> **Technical (IT + Security):** Changes to production also need CAB approval, which is separate from the project’s change control. Include the rollback plan and the risk rating in the CAB request.

**Done when:** No change made without a logged decision; Baselines reflect approved changes

### 4.3 Monitor risks, issues and stakeholder engagement

**What it is.** Check that risk responses are working, identify new risks, track issues and check that stakeholder engagement is moving in the right direction.

**Why it matters.** Risks and stakeholders change throughout a project, so a register that isn’t reviewed soon goes stale.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| RAID log, stakeholder register | Workbook | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Updated RAID log and stakeholder register | Workbook | PM / item owners |

**Templates:** [T11 RAID Log (Risks, Assumptions, Issues, Dependencies)](../02-Templates/T11-RAID-Log-Risks-Assumptions-Issues-Dependencies.xlsx), [T03 Stakeholder Register & Power/Interest Grid](../02-Templates/T03-Stakeholder-Register-Power-Interest-Grid.xlsx)

**How to do it**

1. Review the risks every week (Red and Amber) and the full list every month.
2. Ask at every status meeting: ‘What new risks do we see?’
3. Check whether each response is reducing the score; if not, change the response.
4. Re-score stakeholder engagement each month and adjust the actions.

> **Hybrid:** Use the sprint retrospective and sprint review to spot new risks and stakeholder concerns.
>
> **Technical (IT + Security):** Track vulnerability findings, audit observations and vendor security issues through to closure.

**Done when:** RAID log reviewed every week; Stakeholder engagement re-scored every month

### 4.4 Validate scope and accept deliverables

**What it is.** Get formal acceptance of each completed deliverable from the person named in the RACI, against the acceptance criteria agreed in Planning.

**Why it matters.** Formal acceptance is what lets the project close. Without it, deliverables can be disputed after the team has moved on.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Completed and quality-checked deliverables | 03-Executing | Delivery team |
| Acceptance criteria | Quality & Acceptance Plan; Requirements | PM / PO |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Accepted deliverables and sign-off records | 05-Closing/Acceptance | PM (records), Accepting stakeholder (signs) |

**Templates:** [T21 Acceptance & Transition Sign-off](../02-Templates/T21-Acceptance-Transition-Sign-off.docx), [T06 Requirements Register / Product Backlog](../02-Templates/T06-Requirements-Register-Product-Backlog.xlsx)

**How to do it**

1. Show or test each deliverable against its acceptance criteria.
2. Record acceptance in writing. Email is fine if the charter allows it.
3. Log rejected items with the reasons and a plan to fix them.
4. Update the requirements traceability to ‘Accepted’.

> **Hybrid:** The PO accepts stories at the sprint review. The sponsor accepts milestone deliverables at gate reviews.
>
> **Technical (IT + Security):** Get UAT sign-off, security sign-off (penetration test findings fixed or formally accepted) and operational readiness sign-off.

**Done when:** Every deliverable accepted or has a remediation plan

### 4.5 Report status and escalate

**What it is.** Produce the regular status report and dashboard, run steering meetings and escalate decisions that are above the PM’s authority.

**Why it matters.** Leaders can only support what they can see. Consistent reporting builds trust and gets decisions made quickly.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Dashboard metrics | Workbook: Dashboard | PM |
| RAID log and Decision Log | Workbook | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Weekly status report | 04-Monitoring/Status | PM |
| Steering committee pack (Medium/Large projects) | 04-Monitoring/Steering | PM |

**Templates:** [T15 Status Report](../02-Templates/T15-Status-Report.docx), [T17 Decision Log](../02-Templates/T17-Decision-Log.xlsx)

**How to do it**

1. Update the workbook, then copy the dashboard numbers into the status report.
2. Set the overall RAG: Green = on track; Amber = at risk, recoverable by the team; Red = needs sponsor action.
3. Put decisions and help needed at the top.
4. Escalate using the format: issue, impact, options, recommendation, decision needed by.

> **Hybrid:** Show velocity and the release burn-up next to milestone RAG so stakeholders see both views.
>
> **Technical (IT + Security):** Add a short technical health section covering environments, the release pipeline, open critical vulnerabilities and incidents.

**Done when:** Report sent on schedule; Escalations have decision dates


## Chapter 5. Closing
*Hand over, learn, and formally finish.*

Closing makes sure all the work is finished and accepted, the solution is handed over to the people who will run it, contracts are closed, lessons are captured and the team is released and recognized. Closing applies to each phase or release as well as to the end of the project. Skipping it leaves loose ends: unpaid invoices, unsupported systems, lost knowledge and a team that never got credit.

**Exit gate:** Closure gate: the sponsor confirms the project is complete and approves the closeout report.

### 5.1 Confirm final acceptance and transition to operations

**What it is.** Confirm that every deliverable is accepted, then formally hand the solution over to the business or operations owner with everything they need to run it.

**Why it matters.** A project only creates value when its output is used and supported. Poor handover is a common reason benefits are never realized.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Acceptance records | 05-Closing/Acceptance | PM |
| Operational requirements (support model, training, documentation) | Operations owner | Operations / Support Owner |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Acceptance & Transition Sign-off | 05-Closing | PM (author), Sponsor and Operations owner (sign) |

**Templates:** [T21 Acceptance & Transition Sign-off](../02-Templates/T21-Acceptance-Transition-Sign-off.docx), [T22 Go-Live Readiness & Security Checklist](../02-Templates/T22-Go-Live-Readiness-Security-Checklist.xlsx)

**How to do it**

1. Check that all acceptance records are complete.
2. Hand over the documentation, training, access, support contacts and open defects.
3. Agree a hypercare period and its exit criteria (e.g., two weeks with no Severity 1 incidents).
4. Get the transition signed.

> **Hybrid:** Train end users and run change-adoption activities, then track adoption metrics through hypercare.
>
> **Technical (IT + Security):** Complete the go-live readiness checklist, run the cut-over and hypercare, hand over the runbooks and monitoring, and transfer admin access while removing project-only access.

**Done when:** Transition signed; Hypercare exit criteria met

### 5.2 Close contracts and finances

**What it is.** Confirm that vendors have delivered, settle the final invoices, close the purchase orders and the project cost codes, and release any unused reserve.

**Why it matters.** Open contracts and cost codes create financial and legal exposure, and unused budget sitting in the project can’t be used elsewhere.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Contracts, SOWs, invoices | 02-Planning/Procurement; Finance | Procurement / Finance Partner |
| Accepted vendor deliverables | 03-Executing/Vendors | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Contract closure records and final financials | 05-Closing/Financials; workbook Budget tab | Procurement, Finance Partner |

**Templates:** [T09 Budget & Cost Tracker](../02-Templates/T09-Budget-Cost-Tracker.xlsx)

**How to do it**

1. Confirm all vendor deliverables are accepted.
2. Pay the final invoices and close the purchase orders.
3. Record vendor performance for future sourcing decisions.
4. Reconcile the final budget against the baseline and close the cost codes.

> **Hybrid:** Close capacity-based vendor agreements and reconcile them against the sprints actually delivered.
>
> **Technical (IT + Security):** Make sure vendor access has been revoked, data has been returned or destroyed as the contract requires, and licenses are transferred to the operations owner.

**Done when:** All POs closed; Final cost reconciled; Vendor access removed

### 5.3 Run the retrospective and capture lessons learned

**What it is.** Hold a structured, blame-free review of what to start, stop and continue, and turn the lessons into concrete recommendations for future projects.

**Why it matters.** Lessons not acted on just get repeated. A good retrospective makes the next project cheaper and less risky.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Lessons captured during the project | Workbook: Lessons | PM |
| Performance data (variances, change log, RAID history) | Workbook | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Lessons Learned Register | Workbook: Lessons; shared with the PMO library | PM |

**Templates:** [T19 Retrospective & Lessons Learned Register](../02-Templates/T19-Retrospective-Lessons-Learned-Register.xlsx)

**How to do it**

1. Invite the core team and key stakeholders, and make it a safe space.
2. Walk through the timeline and milestones to refresh memories.
3. Ask: what should we start, stop and continue doing?
4. Turn each lesson into a recommendation with an owner (e.g., update template T08).

> **Hybrid:** Combine the themes from the sprint retrospectives with the end-of-project review.
>
> **Technical (IT + Security):** Include post-incident reviews and deployment metrics, and feed improvements back into engineering standards.

**Done when:** Retrospective held; Each lesson has a recommendation and an owner

### 5.4 Write the closeout and impact report

**What it is.** Summarize what was delivered, how the project performed against its baselines, the benefits achieved, the lessons and the open items. Present the impact to the sponsor and stakeholders.

**Why it matters.** It formally records the project’s results, shows the value delivered and gives future teams a reference.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| Baselines and final actuals | Workbook | PM |
| Success criteria and benefit measures | Charter; business owner | Sponsor / Business owner |
| Lessons Learned Register | Workbook: Lessons | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Closeout & Impact Report | 05-Closing | PM (author), Sponsor (approver) |

**Templates:** [T20 Closeout & Impact Report](../02-Templates/T20-Closeout-Impact-Report.docx)

**How to do it**

1. Compare the final scope, schedule and cost with the baselines and explain the variances.
2. Report results against each success criterion, with data.
3. List open items and their new owners, and the plan for measuring later benefits.
4. Present to the sponsor and get approval to close.

> **Hybrid:** Show the value delivered in increments over the life of the project, not only at the end.
>
> **Technical (IT + Security):** Include final architecture, security posture (residual risks accepted), operational metrics since go-live and the technical debt handed over.

**Done when:** Report approved by the sponsor; Benefit measurement plan handed to the business owner

### 5.5 Archive, release the team and celebrate

**What it is.** Archive the project records, release the people and resources, update the PMO records and recognize the team’s contribution.

**Why it matters.** Archives support audits and future projects, releasing resources quickly helps the rest of the organization, and recognition builds the goodwill your next project will need.

**Inputs**

| Input | Where to get it | Responsible |
|---|---|---|
| All project records | Project repository | PM |

**Outputs**

| Output | Where it is kept | Responsible |
|---|---|---|
| Archived repository (read-only) | Organizational records system | PM / PMO |
| Team release notes and recognition | Email to managers; team event | PM |

**Templates:** [T20 Closeout & Impact Report](../02-Templates/T20-Closeout-Impact-Report.docx)

**How to do it**

1. Clean up and archive the repository using the retention rules.
2. Tell functional managers the release dates and give feedback on each person’s contribution.
3. Celebrate: thank the team publicly, share the impact story and recognize individuals.
4. Close the project in the PMO portfolio.

> **Hybrid:** Celebrate milestones throughout the project as well as at the end.
>
> **Technical (IT + Security):** Archive the repositories, decommission temporary environments and confirm that project service accounts and credentials are revoked.

**Done when:** Archive complete; Team released and recognized; Project closed in the portfolio

## Appendix A. Template library

### T01 Project Intake & Business Case (.docx)
Captures a request in enough detail to decide whether it should become a project.

1. Complete sections 1–4 with the requester in a 30–45 minute conversation.
2. Quantify the problem: cost of doing nothing, volume affected, risk exposure.
3. List at least two options (including ‘do nothing’) and recommend one.
4. Have the Finance Partner check the cost and benefit numbers before the sponsor sees them.
5. Get a go/no-go decision from the sponsor and record it in section 8.

Used in steps: 1.1

[Open the template file](../02-Templates/T01-Project-Intake-Business-Case.docx)

### T02 Project Charter (.docx)
Formally authorizes the project and gives the PM authority to use organizational resources.

1. Copy the problem, goals and benefits from the approved Intake (T01). Do not rewrite them from scratch.
2. Write in-scope and out-of-scope items as a bulleted list. Out-of-scope is the part that prevents scope creep.
3. List high-level milestones only (5–8). The detailed schedule comes in Planning.
4. Name the PM and state their authority level (budget, staffing, change approvals).
5. Circulate for comments, then get a recorded sign-off from the sponsor.

Used in steps: 1.2, 1.5

[Open the template file](../02-Templates/T02-Project-Charter.docx) · [See the filled-in example](../05-Examples/T02-Project-Charter-EXAMPLE-Project-Beacon.docx)

### T03 Stakeholder Register & Power/Interest Grid (.xlsx)
Lists everyone affected by or able to affect the project, and plans how to engage each one.

1. Brainstorm names with the sponsor; ask each stakeholder ‘who else should I talk to?’
2. Score Power and Interest 1–5. The grid quadrant is calculated automatically.
3. Set Current vs Desired engagement (Unaware, Resistant, Neutral, Supportive, Leading).
4. Write one concrete engagement action for every gap between current and desired.
5. Review monthly. People change roles and their attitudes change.

Used in steps: 1.3, 2.7, 4.3

[Open the template file](../02-Templates/T03-Stakeholder-Register-Power-Interest-Grid.xlsx)

### T04 Delivery Approach & Tailoring Worksheet (.xlsx)
Chooses predictive, agile or hybrid delivery for each workstream, and records which playbook steps to scale up or down.

1. Score each workstream on the eight suitability questions (1 = predictive, 5 = agile).
2. An average of 1–2.4 suggests predictive, 2.5–3.4 hybrid and 3.5–5 agile.
3. Pick a size (Small/Medium/Large) using the tailoring table in the playbook.
4. Record every step you will skip or simplify, with the reason, so auditors and successors understand your choices.

Used in steps: 1.4

[Open the template file](../02-Templates/T04-Delivery-Approach-Tailoring-Worksheet.xlsx)

### T05 Kickoff Meeting Kit (.docx)
Agenda, talking points and checklist for the project kickoff meeting.

1. Send the pre-read (charter summary) 48 hours before the meeting.
2. Have the sponsor open the meeting with the ‘why’. It gives the project credibility.
3. Walk through the scope, the milestones, the roles and how the team will work together.
4. Capture questions in the decision log or RAID log and send notes within 24 hours.

Used in steps: 1.6, 3.1

[Open the template file](../02-Templates/T05-Kickoff-Meeting-Kit.docx)

### T06 Requirements Register / Product Backlog (.xlsx)
Captures requirements or user stories with priority, acceptance criteria and traceability.

1. Write each item as ‘As a <user>, I need <capability> so that <benefit>’ or as a ‘shall’ statement.
2. Prioritize with MoSCoW (Must, Should, Could, Won’t this time).
3. Every Must needs testable acceptance criteria before it is built.
4. Link each item to a WBS ID or epic and to its test case for traceability.

Used in steps: 2.1, 4.4

[Open the template file](../02-Templates/T06-Requirements-Register-Product-Backlog.xlsx)

### T07 Scope Statement (.docx)
Defines the deliverables, acceptance criteria, exclusions, constraints and assumptions in detail.

1. Expand the charter scope into specific deliverables with acceptance criteria.
2. List exclusions explicitly, especially ‘nice to have’ items that were turned down.
3. Record constraints (date, budget, technology, regulation) and assumptions; copy the assumptions into the RAID log.
4. Get sign-off from the sponsor and the Product Owner. This becomes the scope baseline.

Used in steps: 2.2

[Open the template file](../02-Templates/T07-Scope-Statement.docx)

### T08 WBS & Schedule (Gantt) (.xlsx)
Breaks the scope into work packages and schedules them with owners, dates, dependencies and progress.

1. Decompose the deliverables (not activities) until each work package fits in 1–10 working days.
2. Enter the start date and duration. The finish date and the Gantt bars are calculated for you.
3. Use the Predecessor column to record dependencies and to find the critical path.
4. Mark milestones with a duration of 0.
5. Once the plan is approved, copy the dates into the Baseline columns and leave them unchanged.

Used in steps: 2.2, 2.3, 3.2, 4.1

[Open the template file](../02-Templates/T08-WBS-Schedule-Gantt.xlsx)

### T09 Budget & Cost Tracker (.xlsx)
Builds the cost estimate and tracks planned vs actual spend by category.

1. Estimate bottom-up from the WBS: labor (hours × rate) plus non-labor items.
2. Add a contingency reserve sized to the risk (typically 5–15%) and show it on its own line.
3. Enter actuals monthly from the finance system. Variance and percent spent are calculated for you.
4. Investigate any line more than 10% over its plan.

Used in steps: 2.4, 4.1, 5.2

[Open the template file](../02-Templates/T09-Budget-Cost-Tracker.xlsx)

### T10 RACI Matrix (.xlsx)
Makes clear who is Responsible, Accountable, Consulted and Informed for each deliverable or decision.

1. List the deliverables or decisions down the rows and the roles or people across the columns.
2. Exactly one A per row. The check column flags rows with no A or more than one.
3. Keep the number of C entries low. Each extra one slows decisions down.
4. Review the matrix with the team at kickoff and get explicit agreement on it.

Used in steps: 1.5, 2.5, 3.1

[Open the template file](../02-Templates/T10-RACI-Matrix.xlsx)

### T11 RAID Log (Risks, Assumptions, Issues, Dependencies) (.xlsx)
One register for everything that could, or already does, get in the way of delivery.

1. A risk is something that might happen. An issue is something that has happened. Move risks to issues when they occur.
2. Score Probability and Impact 1–5. The score (P×I) and RAG rating are calculated for you.
3. Every Red or Amber item needs an owner, a response (avoid, mitigate, transfer, accept) and a due date.
4. Review the top 10 items in every status meeting and close out stale entries.

Used in steps: 2.6, 3.3, 3.5, 4.3

[Open the template file](../02-Templates/T11-RAID-Log-Risks-Assumptions-Issues-Dependencies.xlsx)

### T12 Communication Plan (.xlsx)
Defines who gets what information, how often, in which format and from whom.

1. Build one row per audience, not per message.
2. Ask stakeholders how they prefer to receive updates. Don’t assume.
3. Assign an owner to every communication and put recurring ones on the calendar right away.
4. Review the plan after each gate and whenever stakeholders change.

Used in steps: 2.7, 3.4

[Open the template file](../02-Templates/T12-Communication-Plan.xlsx)

### T13 Quality & Acceptance Plan (.docx)
States quality standards, review and test activities, and how each deliverable will be accepted.

1. List the standards that apply (internal policies, industry or regulatory standards).
2. For each deliverable, define the quality check (peer review, test, audit) and who approves it.
3. Define the Definition of Done for agile work and the acceptance criteria for milestone deliverables.
4. Technical track: attach the test strategy (unit, integration, UAT, performance, security).

Used in steps: 2.8, 3.3

[Open the template file](../02-Templates/T13-Quality-Acceptance-Plan.docx)

### T14 Statement of Work (SOW) (.docx)
Describes the work a vendor will perform, its deliverables, timeline, acceptance and payment terms.

1. Write deliverables as outcomes with acceptance criteria, not as hours of effort.
2. Tie payments to accepted deliverables or milestones wherever possible.
3. Include requirements for security, data handling and confidentiality.
4. Have Procurement and Legal review it before it goes to vendors.

Used in steps: 2.9, 3.6

[Open the template file](../02-Templates/T14-Statement-of-Work-SOW.docx)

### T15 Status Report (.docx)
A one-page weekly update: overall RAG, progress, next steps, top risks and decisions needed.

1. Lead with the overall RAG rating and one sentence explaining why.
2. Report progress against milestones, not activity (‘Design approved’, not ‘worked on design’).
3. List decisions or help needed with an owner and a date. This is the most-read section.
4. Use the same format every week so readers can compare reports at a glance. The workbook dashboard supplies the numbers.

Used in steps: 2.10, 3.4, 4.5

[Open the template file](../02-Templates/T15-Status-Report.docx) · [See the filled-in example](../05-Examples/T15-Status-Report-EXAMPLE-Project-Beacon.docx)

### T16 Change Request & Change Log (.xlsx)
Documents proposed changes to scope, schedule or budget, their impact and the approval decision.

1. Anyone can raise a change. The PM logs it and runs an impact analysis (scope, time, cost, risk, quality).
2. Bring it to the approver named in the charter or the CCB with a recommendation.
3. If approved, update the baselines and tell the affected stakeholders.
4. Rejected changes stay in the log. They show the decision was considered.

Used in steps: 4.2

[Open the template file](../02-Templates/T16-Change-Request-Change-Log.xlsx)

### T17 Decision Log (.xlsx)
Records significant decisions, the options considered, who decided and why.

1. Log any decision that would be expensive to reverse or that someone may question later.
2. Record the options considered and the reasoning, not just the outcome.
3. Link related change requests or RAID items.

Used in steps: 1.1, 1.6, 2.9, 2.10, 3.5, 3.7, 4.2, 4.5

[Open the template file](../02-Templates/T17-Decision-Log.xlsx)

### T18 Meeting Agenda & Minutes (.docx)
A standard agenda and minutes format that turns meetings into decisions and actions.

1. Send the agenda at least 24 hours ahead with the desired outcome of each item.
2. Record decisions, actions (owner and date) and new risks. Skip the play-by-play.
3. Send the minutes within 24 hours and move the actions into the workbook.

Used in steps: 1.6, 3.2, 3.4

[Open the template file](../02-Templates/T18-Meeting-Agenda-Minutes.docx)

### T19 Retrospective & Lessons Learned Register (.xlsx)
Captures what to start, stop and continue, and turns lessons into actions for future projects.

1. Run short retrospectives after each sprint or phase, not only at the end of the project.
2. Use the Start/Stop/Continue framing so the discussion stays safe and constructive.
3. Convert each lesson into a recommendation with an owner (e.g., update a template or standard).
4. Share the register with the PMO or a lessons library.

Used in steps: 3.7, 5.3

[Open the template file](../02-Templates/T19-Retrospective-Lessons-Learned-Register.xlsx)

### T20 Closeout & Impact Report (.docx)
Summarizes what was delivered, performance against baselines, benefits, lessons and open items.

1. Compare the final scope, schedule and cost to the baselines and explain the variances.
2. Report benefits against the success criteria in the charter, with data.
3. List open items and who now owns them.
4. Use the impact section (executive summary, results, what worked, next steps) as the sponsor briefing.

Used in steps: 5.4, 5.5

[Open the template file](../02-Templates/T20-Closeout-Impact-Report.docx) · [See the filled-in example](../05-Examples/T20-Closeout-Impact-Report-EXAMPLE-Project-Beacon.docx)

### T21 Acceptance & Transition Sign-off (.docx)
Records formal acceptance of deliverables and the handover to operations or the business owner.

1. List every deliverable with its acceptance evidence (test results, demo, inspection).
2. Confirm the operations owner has the training, documentation, access and support model they need.
3. Agree a warranty or hypercare period and its exit criteria.
4. Have the sponsor and the receiving owner sign it.

Used in steps: 3.6, 4.4, 5.1

[Open the template file](../02-Templates/T21-Acceptance-Transition-Sign-off.docx) · [See the filled-in example](../05-Examples/T21-Acceptance-Transition-Sign-off-EXAMPLE-Project-Beacon.docx)

### T22 Go-Live Readiness & Security Checklist (.xlsx)
Technical track: confirms that release, security, data, rollback and support criteria are met before production changes.

1. Start the checklist at least two weeks before the planned go-live.
2. Each item needs an owner, a status and evidence (a link or document).
3. Any ‘No’ on a critical item blocks go-live unless the sponsor and Security Lead record an exception.
4. Attach the completed checklist to the CAB request.

Used in steps: 5.1

[Open the template file](../02-Templates/T22-Go-Live-Readiness-Security-Checklist.xlsx)

## Appendix B. Agile quick reference

The Hybrid track runs sprint-based delivery inside a plan with fixed milestones. This appendix covers what a project manager needs to run that combination. It is not a course in Scrum or any other framework; the sources at the end go deeper.

### B.1 The sprint cycle

A sprint is a fixed-length period, usually two to four weeks (Project Beacon uses two), in which the team turns the highest-priority backlog items into finished, usable work. The fixed length gives the team a rhythm, and it gives you a dependable unit for milestone planning. Five regular events keep the cycle running. The time limits below grow with sprint length: the first figure is for a two-week sprint and the second for a four-week sprint. For a three-week sprint, use the middle.

1. Sprint planning. The Product Owner brings the top-priority items. The team decides how much it can finish and agrees a sprint goal: one sentence on why this sprint matters. Output: the sprint goal and the sprint backlog. Time limit: 4 hours (two-week sprint), 8 hours (four-week sprint).
2. Daily stand-up. A 15-minute check where the team compares progress with the sprint goal and names blockers. It is for the team, not a status report to the PM.
3. Backlog refinement. Ongoing work in which the Product Owner and team clarify, split and size upcoming items so they are ready for planning. Common guidance is to keep it to roughly a tenth of team capacity.
4. Sprint review. At the end of the sprint the team shows working results to the Product Owner and stakeholders. The Product Owner accepts or rejects items against the Definition of Done, and feedback goes into the backlog. It doubles as your stakeholder demo and a checkpoint for the milestone plan. Time limit: 2 hours (two-week sprint), 4 hours (four-week sprint).
5. Sprint retrospective. The team looks at how it worked, picks one or two changes to try next sprint, and records any lessons for the Lessons Learned Register (T19). Time limit: 1.5 hours (two-week sprint), 3 hours (four-week sprint).

### B.2 Who does what

Use this rule of thumb: the PM owns when and how much money, the Product Owner owns what, and the team owns how.

- Product Owner: orders the backlog, explains each item, and accepts or rejects finished work.
- Delivery team: decides how many items fit in a sprint and how to build them. Nobody outside the team assigns work inside a sprint.
- Scrum Master or team lead: coaches the way of working and clears blockers. On a small project this may be the PM, but avoid combining the PM and Product Owner roles, because it removes the check between “what we want” and “what we can afford”.
- Project Manager: owns milestones, budget, risks, stakeholders and vendors, and reads sprint results into the milestone plan. The PM does not reorder the backlog or assign sprint work.
- Sponsor: accepts milestone deliverables at the gates.

### B.3 Writing backlog items

Write each item as a short user story: “As a [type of user], I need [capability] so that [benefit].” Add acceptance criteria that say how anyone can tell the item works. Check each story against six qualities, which agile teams remember as INVEST: it can be built Independently, it is open to Negotiation, it delivers Value, the team can Estimate it, it is Small enough for one sprint, and it is Testable.

Large items are called epics. Split an epic into stories before it enters a sprint.

Acceptance criteria and the Definition of Done are different. Acceptance criteria belong to one item (“a volunteer can cancel a shift up to 24 hours before it starts”). The Definition of Done is a checklist that applies to every item (reviewed, tested, documented, accepted). An item is done only when it meets both. The Quality & Acceptance Plan (T13) records the Definition of Done, and the Requirements Register (T06) holds the stories.

### B.4 Story mapping

A story map arranges the backlog as a picture of the user’s journey instead of a flat list.

1. Write the main activities a user performs, left to right, in the order they happen. This row is the backbone.
2. Under each activity, stack the stories that support it, with the most important at the top.
3. Draw horizontal lines across the map to slice it into releases. The top slice is the thinnest version that is still useful to a real user.

A map shows the whole product before the parts, gives the Product Owner and sponsor a shared picture, and makes it easy to explain what waits for a later release. Project Beacon’s volunteer side looks like this:

```
Sign up      Find a shift    Book or cancel   Do the shift   Log hours       Get certificate
-------      ------------    --------------   ------------   ---------       ---------------
Account      Browse open     Book a shift     (offline)      Enter hours     Download PDF
with MFA     shifts          Cancel up to                    after a shift   with total hours
                             24h before
             Coordinators: create recurring shifts with capacity limits
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Release 1 (MVP pilot, Mar 27): everything above this line (Sprints 1 to 3)
                                                                Text reminders
                                                                (deferred)
```

The donor side (recurring gifts, nightly CRM sync) forms a second backbone, planned for Sprints 4 and 5.

### B.5 Planning releases and linking them to milestones

1. Size the backlog. Give each item a relative size (story points or small, medium, large). Relative sizing is quicker and, over many items, about as reliable as hour estimates.
2. Learn the team’s velocity. Velocity is the amount of work a team finishes in one sprint, counted in whatever unit the team estimates in. If the team sizes work in story points, velocity is the story points completed per sprint. Count only items that are fully done and meet the Definition of Done: a nearly finished item adds nothing. Before any sprint has finished, plan with a range and replace it with real numbers after the second or third sprint.
3. Work out what fits. Sprints available multiplied by the velocity range gives the scope the team can deliver by the date. Plan people at about 60 to 80% of their available project time, after subtracting meetings and leave (see the capacity guidance in the planning steps).
4. Place milestones at sprint ends. A milestone tied to a sprint review has real evidence behind it.
5. Re-forecast every sprint. When the date and the budget are fixed, scope is the variable. Use the MoSCoW lines (Must, Should, Could) to decide what moves when the forecast slips.

Use a burn-up chart to show progress. It plots two lines against time: total scope and work completed. The gap between them is the work left. When scope grows, the scope line rises and everyone can see it, which is why a burn-up is better than a burn-down for stakeholder reporting.

Velocity has two good uses. The team’s recent average tells you how much work to plan into coming sprints, and the trend over several sprints shows whether the team is speeding up or is blocked. Treat a change as a prompt to ask why, not as a grade: a rising number can simply mean the estimates are growing. Do not compare velocity across teams, because each team’s estimates are relative to its own work. Do not make it a target either, because pushing it up tends to inflate estimates instead of finishing more. A falling velocity alongside a stable scope line is an early warning that a milestone is at risk.

### B.6 Keeping the plan-driven and agile halves in step

Watch for these common problems.

- Fixing milestone dates before anyone has sized the backlog.
- The PM reordering the backlog, which is the Product Owner’s job.
- Raising a change request for ordinary reprioritization. Swapping items of similar size inside the backlog is normal. Changes to milestones, budget or overall scope go through change control.
- Skipping the retrospective when the schedule is tight. That is when it pays back most.
- Marking items done that do not meet the Definition of Done. Milestone reports then look healthier than the product is.
- Reporting velocity without scope. Show both, as a burn-up.

### B.7 Project Beacon in practice

Sprint 2 (February 23 to March 6, 2026) delivered shift booking. Its goal, in one sentence: “A volunteer can see open shifts and book or cancel one.” The sprint backlog held R-02 (book and cancel) and R-03 (recurring shifts with capacity limits). Late in the sprint the work was about 80% complete, and the sprint review moved from March 6 to March 10. The same sprint carried the spike to test the CRM’s API limits (risk R-002). In that week’s status report, the PM reported the milestone view (the MVP pilot on March 27 on track, go-live still June 1 with one week of float used) and linked the sprint evidence to it, rather than reporting task activity.

### B.8 Where to learn more

These sources are also listed in Appendix D.

- Schwaber, K. and Sutherland, J. (2020). The Scrum Guide. https://scrumguides.org
- Patton, J. (2014). User Story Mapping. O’Reilly Media.
- Wake, B. (2003). INVEST in Good Stories, and SMART Tasks. https://xp123.com/invest-in-good-stories-and-smart-tasks/
- Project Management Institute and Agile Alliance (2017). Agile Practice Guide.
- Beck, K. et al. (2001). Manifesto for Agile Software Development. https://agilemanifesto.org

## Appendix C. Glossary

Short definitions in plain words, listed alphabetically. Each term appears in the playbook, the templates, the example workbook or Appendix B.

- **Acceptance criteria.** The specific conditions an item must meet before the person accepting it agrees it is done.
- **Assumption.** Something believed true for planning purposes but not yet confirmed. Record it in the RAID log so someone checks.
- **Backlog (product backlog).** The ordered list of everything that might be built, kept by the Product Owner. The top is detailed and ready; the bottom is rough.
- **Baseline.** The approved version of the scope, schedule or budget that you measure progress against. It changes only through change control.
- **Benefits realization.** Confirming, after delivery, that the expected benefits actually appeared, with data.
- **Burn-up chart.** A chart of total scope and completed work over time. The gap between the lines is the work remaining.
- **Business case.** The argument for doing a project: the problem, the options, the costs and benefits, and the recommendation.
- **CAB (Change Advisory Board).** The group that approves changes to production systems before they go live.
- **CCB (Change Control Board).** The group that approves changes to a project’s baseline.
- **Change request.** A formal proposal to change the scope, schedule or budget, with its impact analysis and a decision.
- **Charter.** The document that authorizes the project and gives the PM authority to use resources.
- **Contingency reserve.** Money or time set aside for identified risks. Draw on it only through the agreed process.
- **CPI (Cost Performance Index).** Earned value divided by actual cost. Below 1.0 means the work is costing more than planned; above 1.0 means less.
- **Critical path.** The longest chain of dependent tasks. A delay to any task on it delays the finish date.
- **Cut-over.** The moment when users and data move from the old way of working to the new one.
- **DAST (dynamic application security testing).** Testing a running application from the outside for security weaknesses.
- **Definition of Done.** A checklist that every backlog item must meet before the team calls it finished.
- **Deliverable.** Something the project produces that someone can inspect and accept.
- **Dependency.** A relationship in which one task, or an outside event, must happen before another can start or finish.
- **Earned value.** The budgeted value of the work actually completed. Used to compare progress with spending (see CPI and SPI).
- **Epic.** A large backlog item that must be split into stories before the team can build it.
- **Float (slack).** How long a task can slip without delaying the finish date. Tasks on the critical path have none.
- **Gantt chart.** A bar chart of tasks against time, showing start, finish and dependencies.
- **Gate.** A planned decision point where a sponsor or committee decides whether the project may continue to the next stage.
- **Hybrid delivery.** Mixing plan-driven management (fixed milestones, budget, approvals) with iterative delivery (sprints and a backlog).
- **Hypercare.** A short period after go-live when the project team stays close to fix problems quickly before handing over fully.
- **Increment.** The working result of a sprint, usable and meeting the Definition of Done.
- **Issue.** A problem that has already happened and needs action. A risk becomes an issue when it occurs.
- **Lessons learned.** What the team learned that could improve future work, written as recommendations with an owner.
- **MFA (multi-factor authentication).** Signing in with two or more proofs of identity, such as a password and a code from a phone.
- **Milestone.** A significant point in the plan, such as an approval or a delivery. It takes no time itself.
- **MoSCoW.** A priority scheme: Must, Should, Could, Won’t this time.
- **MVP (minimum viable product).** The smallest version of a product that real users can use and give feedback on.
- **OKR (objectives and key results).** A goal-setting method that pairs an ambition with measurable results.
- **PMO (project management office).** A group that sets project standards, supports project managers and often tracks the portfolio.
- **Product Owner.** The person who owns the backlog, decides its order and accepts or rejects finished work.
- **RACI.** A matrix showing who is Responsible, Accountable, Consulted and Informed for each deliverable or decision.
- **RAG (red, amber, green).** A traffic-light rating of status.
- **RAID log.** One register of Risks, Assumptions, Issues and Dependencies.
- **Release.** A set of finished work made available to users.
- **Retrospective.** A team meeting to review how the work went and agree improvements.
- **Risk.** An uncertain event that, if it happens, affects the project. Score it by probability and impact.
- **Rolling-wave planning.** Planning near-term work in detail and later work at a higher level, adding detail as it gets closer.
- **RPO (recovery point objective).** How much recent data, measured in time, an organization can afford to lose after an outage.
- **RTO (recovery time objective).** How long a service can be down before the harm becomes unacceptable.
- **SAST (static application security testing).** Analyzing source code for security weaknesses without running it.
- **Scope creep.** Growth in what the project must deliver without matching changes to time, budget or approval.
- **Scrum Master.** The person who coaches a team in its way of working and removes blockers.
- **SLA (service level agreement).** A written commitment to a level of service, such as response times.
- **SOW (statement of work).** The document describing what a vendor will do, by when, to what standard and for what payment.
- **SPI (Schedule Performance Index).** Earned value divided by planned value. Below 1.0 means behind schedule.
- **Sprint.** A fixed-length period in which a team completes a chosen set of backlog items.
- **Sprint goal.** One sentence that states the purpose of a sprint.
- **SSO (single sign-on).** One login that gives access to several systems.
- **Stakeholder.** Anyone affected by the project or able to affect it.
- **Story map.** A picture of the user’s journey with stories stacked beneath each step, sliced into releases.
- **Technical debt.** The future cost of shortcuts taken in design or code. It is tracked as backlog work.
- **Threat model.** A structured review of how a system could be attacked and which controls address each threat.
- **Traceability.** Links from each requirement to the work and the test that cover it.
- **UAT (user acceptance testing).** Testing by the people who will use the product, to confirm it meets their needs.
- **User story.** A short description of a need from the user’s point of view: who, what and why.
- **Velocity.** The amount of work a team finishes in one sprint, counted in the unit the team estimates in (such as story points), and counting only fully finished items. Teams use their recent average to plan how much to take on, and watch the trend for signs that they are speeding up or are blocked.
- **WBS (work breakdown structure).** A breakdown of the project scope into smaller deliverables and work packages.
- **WCAG (Web Content Accessibility Guidelines).** The W3C standard for making web content usable by people with disabilities.
- **Work package.** The lowest level of the WBS: a piece of work small enough to assign, estimate and track.

## Appendix D. Sources & further reading

These works were consulted for ideas, coverage and background. No affiliation with, or endorsement by, their authors, publishers, PMI or Google is implied. Names are used only to identify the sources.

1. Project Management Institute (2025). The PMBOK® Guide – Eighth Edition. Five focus areas, seven performance domains and 40 processes used for the step structure. https://www.pmi.org/standards/pmbok
2. Project Management Institute. PMI launches the PMBOK® Guide – Eighth Edition (announcement). Used to check the counts of principles, performance domains, focus areas and processes. https://www.projectmanagement.com/articles/1134510/pmi-launches-the-pmbok--guide---eighth-edition
3. PMBOK 8th Edition Process Chart (Andrew Ramdayal, PMP exam prep). Process-to-phase mapping used in each chapter’s ‘Maps to’ line.
4. Ricardo Viana Vargas. PMBOK Guide process-flow charts and infographics. Consulted for how the processes fit together; nothing is reproduced. https://ricardo-vargas.com/
5. Technical Institute of America (TIA). PMP exam-prep course materials. Consulted for coverage; nothing is reproduced. https://www.tiaexams.com/
6. Project Management Institute. PMP Examination Content Outline. Consulted for coverage; nothing is reproduced.
7. PM Study Circle. What is new in the PMBOK Guide 8th Edition (released in 2025; 6 principles, 7 domains, 40 processes). https://pmstudycircle.com/pmbok-guide-8th-edition/
8. Google Project Management Professional Certificate (Coursera): Initiation, Planning, Execution and Closing guiding questions. Used as a reference for good practice only; no course material is reproduced. https://www.coursera.org/professional-certificates/google-project-management
9. Creative Commons. Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). https://creativecommons.org/licenses/by-nc-sa/4.0/
10. W3C. Web Content Accessibility Guidelines (WCAG) 2.2, referenced in non-functional requirements. https://www.w3.org/TR/WCAG22/
11. Microsoft. The STRIDE threat model, referenced in Step 2.6 (Technical track). https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats
12. Project Management Institute. Qualitative risk assessment (PMI Learning Library). Background for the five-level probability and impact scale in Step 2.6. https://www.pmi.org/learning/library/qualitative-risk-assessment-cheaper-faster-3188
13. Scrum Alliance. Capacity planning for a Scrum team. Background for the 60 to 80% capacity guidance in Steps 2.5 and 3.2. https://resources.scrumalliance.org/Article/capacity-planning-scrum-team
14. Tero Parviainen (2016). A Dash of Queueing Theory. Background for the point that waiting grows sharply as utilization nears 100%. https://teropa.info/blog/2016/04/02/a-dash-of-queueing-theory
15. Schwaber, K. and Sutherland, J. (2020). The Scrum Guide. Background for Appendix B (sprint events, roles and the Definition of Done). https://scrumguides.org
16. Patton, J. (2014). User Story Mapping. O’Reilly Media. Background for story mapping in Appendix B.
17. Wake, B. (2003). INVEST in Good Stories, and SMART Tasks. Background for writing backlog items in Appendix B. https://xp123.com/invest-in-good-stories-and-smart-tasks/
18. Project Management Institute and Agile Alliance (2017). Agile Practice Guide. Background for the Hybrid track.
19. Beck, K. et al. (2001). Manifesto for Agile Software Development. https://agilemanifesto.org

## Appendix E. License & credits

© 2026 James Pearson. This playbook, its templates and the Project Workbook are licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (https://creativecommons.org/licenses/by-nc-sa/4.0/).

- **You may** share and adapt the material.
- **Attribution**: you must credit James Pearson, link to the license and say whether you made changes.
- **NonCommercial**: you may not use it for commercial purposes (e.g., selling it or including it in paid training or consulting deliverables) without written permission.
- **ShareAlike**: if you adapt it, you must share your version under the same license.

**Using this at work.** Using the templates and workbook to run your own projects, including at work, is fine. Selling or repackaging them, including them in paid training, or handing them to clients as a product needs my written permission.

**How to credit:** “Project Manager in a Box” by James Pearson, licensed under CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/).

For commercial licensing, contact the author.

**Find me online:** [LinkedIn](https://www.linkedin.com/in/jamespearson1562) · [GitHub](https://github.com/james-s-pearson) · [Portfolio repository](https://github.com/james-s-pearson/Cybersecurity-Portfolio)

**How this was made.** Written and assembled by James Pearson with help from an AI assistant (Anthropic’s Claude). The AI drafted much of the text. I defined the scope and structure, chose what to include, reviewed and edited the content, and tested the templates and workbook. This project is independent and is not affiliated with or endorsed by Anthropic.

**No warranty.** This playbook, its templates and the workbook are a starting point, provided as is and without warranty of any kind. They are not legal, financial, security or professional advice. Check requirements with your own organization before relying on them, especially the Go-Live Readiness & Security Checklist (T22).

PMI, PMBOK and PMP are registered marks of the Project Management Institute, Inc. Project Beacon, Northside Food Collective and all people in the examples are fictional.

---
“Project Manager in a Box” by James Pearson, licensed under CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/).