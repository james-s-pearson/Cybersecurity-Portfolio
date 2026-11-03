# Project Manager in a Box (v0.2 prototype)

**Version 0.2 · released November 2026.** This folder is always the latest version. To check you have it, compare the version line on the first page of the playbook with the one here. Older versions stay available through this repository’s tags (for example `pm-in-a-box-v0.1`): open the repository on GitHub, choose **Releases** or the branch/tag menu, and pick a tag.

A step-by-step project management playbook for **Hybrid** and **Technical (IT + Security)** projects, with 30 templates and a fill-in-ready Excel workbook that has a live dashboard.
By James Pearson · CC BY-NC-SA 4.0 (see `LICENSE.md`).

## How this was made

Written and assembled by James Pearson with help from an AI assistant (Anthropic’s Claude). The AI drafted much of the text. I defined the scope and structure, chose what to include, reviewed and edited the content, and tested the templates and workbook. This project is independent and is not affiliated with or endorsed by Anthropic.

## Status and support

This is a **v0.2 prototype**, released as is and without warranty of any kind. It is not legal, financial, security or professional advice. Check anything you rely on, especially the Go-Live Readiness & Security Checklist (T22), against your own organization's rules. I may not be able to answer every question.

## Using this at work

Using the templates and workbook to run your own projects, including at work, is fine. Selling or repackaging them, including them in paid training, or handing them to clients as a product needs my written permission. You can reach me through the links at the bottom of this page.

## Start here

1. **Read the playbook.** On GitHub, open `01-Playbook/Playbook-Preview.md`, or download `01-Playbook/Project-Manager-in-a-Box.pdf` for clickable links. For the full web book, download **`Project-Manager-in-a-Box.html`** and open it in your browser: a sidebar table of contents, a track switch (Both / Hybrid / Technical) and download buttons for every template.
2. Open **`05-Examples/Project-Workbook-EXAMPLE-Project-Beacon.xlsx`** to see a finished project (the fictional Project Beacon), then use **`03-Project-Workbook/Project-Workbook.xlsx`** for your own. The same folder holds five filled-in Word examples: a charter, a final status report, a closeout report, an acceptance sign-off and a change request form.

## What's in the folder

| Folder / file | Contents |
|---|---|
| `Project-Manager-in-a-Box.html` | Web book (5 chapters, 33 steps, template library, recovery plays, license) |
| `01-Playbook/Project-Manager-in-a-Box.pdf` | Print/PDF edition with a clickable contents page and PDF bookmarks. For clickable links, download the PDF instead of viewing it on GitHub. |
| `01-Playbook/Playbook-Preview.md` | Markdown preview of the full text, for review and editing |
| `02-Templates/` | T01–T30: 11 Word templates and 19 Excel templates, each with a built-in usage guide |
| `03-Project-Workbook/` | Blank Project Workbook (22 tabs) with a live dashboard |
| `05-Examples/` | Worked examples from the fictional Project Beacon: the finished workbook, plus a filled-in charter (T02), final status report (T15), closeout report (T20), acceptance sign-off (T21) and change request form (T24) |
| `04-Claude-Skill/` | `project-manager-in-a-box` skill so Claude can run projects using this playbook |
| `LICENSE.md` | CC BY-NC-SA 4.0 terms and how to credit |

## What changed

- **v0.2 (November 2026):**
  - Eight new templates, each also a tab in the workbook (now 22 tabs), apart from the Word form: Acceptance Log (T23), Change Request Form (T24, Word), Backlog (T25), Sprint Backlog (T26), Sprint Log (T27), Environment Log (T28), WBS Dictionary (T29) and Activity List (T30).
  - Plan-driven work can be broken into activities in the Activity List (T30), which calculates each work package's % complete.
  - T06 is now the Requirements Register, and its file is renamed from `T06-Requirements-Register-Product-Backlog.xlsx` to `T06-Requirements-Register.xlsx`. Each requirement names one approver and one acceptor and gets a calculated status. The work that delivers it is tracked as backlog items in T25.
  - Acceptance is recorded in one log for sprint items, work packages and requirements, linked by requirement and WBS IDs, so plan-driven and sprint work are tracked in the same place.
  - The change log analyzes impact in six areas (scope, schedule, cost, risk, quality, resources), and the new form is for projects with a change board or other approval process.
  - Changes to the Definition of Done are recorded in the Decision Log.
  - The Dashboard adds velocity and burn-up charts from the Sprint Log.
  - New Appendix E, "Recovery plays by cause". License & credits moves to Appendix F.
  - A filled-in Project Beacon example of the Change Request Form.
- **v0.1 (October 2026):** first public release. Playbook (5 chapters, 33 steps), 22 templates, Project Workbook, Claude skill, and the Project Beacon examples.

Every file also carries a link back to this folder, so a copy you saved earlier can find the latest version.

Questions or improvements? I'd love to hear how it goes.

**Find me online:** [LinkedIn](https://www.linkedin.com/in/jamespearson1562) · [GitHub](https://github.com/james-s-pearson) · [Portfolio repository](https://github.com/james-s-pearson/Cybersecurity-Portfolio)
