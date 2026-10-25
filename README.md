# Cybersecurity Portfolio

Original projects and learning work that apply project management and Python
to everyday security work: running security projects, tracking controls,
managing risk, prioritising vulnerabilities and analysing logs. They are built
in stages, tested against safe sample data, and documented with notes on what
went wrong and what I learned.

## About me

I am James Pearson, a PMP-certified project manager and Certified ScrumMaster
with a background in client success, consulting and delivery, moving into
cybersecurity. I am focusing on security project and program management, and
on customer-facing roles at security and GRC (governance, risk and
compliance) software companies. I am studying for the CompTIA Security+. Longer
term I am interested in penetration testing and web application security.

This repository shows both halves of that combination: security work run as a
well-managed project, and security knowledge applied with code.

My hands-on cybersecurity learning includes working through security
fundamentals, practising on TryHackMe and building a coding environment for the
languages and formats that show up throughout security work. [The story of
building it](foundations/lazyvim-ide/lazyvim-playground-story.md) shows how I
test, document and use AI along the way.

I use AI openly, and the scope of its use depends on the deliverable. Where the
code itself is the deliverable, as in my Python exercises and projects, I write
it myself, and an AI assistant (Claude) only gives hints and reviews my work.
Where the project is the deliverable, as with my LazyVim coding environment
and Project Manager in a Box, an AI assistant drafts the code or documents,
and I direct, test and edit them. Each project's README explains how AI was
used.

- LinkedIn: [linkedin.com/in/jamespearson1562](https://www.linkedin.com/in/jamespearson1562)
- GitHub: [james-s-pearson](https://github.com/james-s-pearson)

## TryHackMe

I build hands-on security skills on TryHackMe. Figures as of 15 October 2026.

- Profile: [tryhackme.com/p/JamesPearson](https://tryhackme.com/p/JamesPearson)
- Global ranking: top 2%
- Rooms completed: 121
- Badges earned: 24
- Activity: 1,830 events in the last year
- Learning paths completed: Cyber Security 101 (August 2026) and Pre Security
  (December 2025)

## Projects

Projects are added here as I start them, and each is built in the open: the
commit history shows the work as it happens.

- **[Foundations](foundations/)**: how I learned Python for security. My
  thirteen Python exercises, the write-ups of the coding environment I built
  (a how-to guide and a story) and its safe test files are published, along
  with a guide to setting up a clean Kali VM for investigating real-world
  software bugs.

Project Manager in a Box is the next project.

## Roadmap

Planned work, in order. Each item moves into the Projects section when I start
it.

0. **Project Manager in a Box:** a project management playbook with 22
   templates and a workbook, for hybrid and technical (IT and security)
   projects. I designed and directed it, an AI assistant generated it, and I
   review and edit it.
1. **Security project case study:** a fictional multi-factor authentication
   rollout run as a project (charter, RAID log, status report, lessons
   learned), plus a customer success plan from the vendor's side.
2. **Control evidence tracker (Python):** a status report on security
   controls, using NIST CSF 2.0 style IDs.
3. **Risk register and KRI report (Python):** risk scoring, ranking, overdue
   reviews and key risk indicators.
4. **Vulnerability SLA report (Python):** remediation deadlines by severity
   and a "fix first" list.
5. **Password policy and breach check (Python, web API):** NIST SP 800-63B
   rules and a privacy-preserving breach lookup.
6. **Failed-login detector (Python):** brute-force detection mapped to MITRE
   ATT&CK T1110.
7. **Indicator enrichment (Python, stretch):** threat-intelligence lookups,
   with API keys kept out of Git.

Alongside these:

- **TryHackMe write-ups:** skill summaries from retired rooms, with no flags
  or answers.
- Two short practice exercises (a file integrity checker and a local port
  checker) that support my Security+ study, and a web security and bug bounty
  side track.

## Where each project fits

- **Security project and program management:** Project Manager in a Box, the
  case study, and the control evidence tracker, risk register and
  vulnerability reports, which produce the status reports and risk views a
  security project manager works with.
- **Customer-facing roles at security and GRC vendors:** Project Manager in a
  Box and the case study's customer success plan (running a deployment as a
  project), the control and risk projects (what GRC platforms do for
  customers), and the API projects (hands-on web API work).
- **GRC:** the control evidence tracker, risk register, vulnerability report
  and password policy projects.
- **SOC and threat intelligence:** the vulnerability report, failed-login
  detector and indicator enrichment, plus my TryHackMe work.

Each project's README will also list the Security+ topics it builds.

## What each project will contain

- `README.md`: what it does, why it matters, how it was made (including any AI
  use), its Security+ connection, the stages and the sample data.
- A Python file (or document templates) that starts with the prompt.
- Safe sample input, and for most coding projects an `expected_output.txt` to
  check results against.
- `NOTES.md`: what went wrong, what I learned and the decisions I made.

## Safety and ethics

- Only made-up passwords, fake logs and fictional company data are used.
- Anything that touches the network runs against my own machine, or against
  systems I have written permission to test.
- No secrets, keys or real credentials are ever committed.
- Any bug bounty work will follow each programme's published scope and rules,
  and findings will be reported responsibly.
- TryHackMe write-ups will cover retired rooms only, and will never include
  flags, answers or exam material.

## Requirements

- Python 3.13
- The standard library for most projects
- `matplotlib` for the risk register chart
- `requests` for the projects that call web APIs
- `pytest` for the tests

Each project's README explains how to run it.

## Licence

Released under the [MIT Licence](LICENSE).
