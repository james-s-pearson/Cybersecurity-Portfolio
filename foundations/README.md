# Foundations: Python and the Environments I Work In

Python is one of the skills security work leans on most: reading logs,
automating checks, calling web APIs and writing reports. I am a project
manager moving into cybersecurity, and this folder shows how I started
learning it. It has two parts, in the order I did them, and a clean Kali VM for
bug hunting, where I put into practice what I am learning by researching
real-world software failures.

## 1. The coding environment

Before writing any exercises, I built the place to write them. I wanted one
editor where Python, C, Java, web pages, JavaScript and JSON could all run
with a single keypress, so I turned LazyVim (a ready-made Neovim setup) into a
coding playground. It took about a week.

An AI assistant drafted most of the Lua configuration. My part was directing
it, testing every language, catching conflicts and deciding what to keep. The
write-up is honest about what worked and what broke.

The write-ups are here: a
[how-to guide](lazyvim-ide/lazyvim-playground-howto.md) for building the same
setup, and [the story](lazyvim-ide/lazyvim-playground-story.md) of how it came
together. The safe test files I used to check each language are here too:
[lazyvim-testfiles](lazyvim-ide/lazyvim-testfiles/).

## 2. The Python exercises

I then worked through thirteen exercises from a Python course, writing every
one in that environment. Each file keeps the learning visible: my first
attempt, my corrected code, and notes on what was wrong and what I learned.

- [The exercises](python-exercises/)

## Putting it into practice: a clean VM for bug hunting

Python and a good environment only matter if I can point them at real problems.
Bug hunting is how I plan to do that: investigating real-world software bugs,
within each programme's published scope and rules. Before touching any real
target I wanted a separate, tidy place to work from, so that my practice-lab
habits never mix with real-world work. I turned a Kali Linux VM into a clean,
snapshotted hunting machine, set up Burp Suite and a dedicated browser profile,
and kept my notes outside the VM and outside any git repository.

An AI assistant (Claude Code) guided the setup and drafted the guide from the
real session; I ran the steps, reviewed the text and approved it. I then
re-tested the commands on a fresh Kali image, which turned up three corrections
that are now in the guide.

The guide is here:
[clean-hunting-vm](clean-hunting-vm/clean-hunting-vm-guide.md), with a blank
[programme notes template](clean-hunting-vm/programme-notes-template.md).

## How AI was used

- **The environment:** an AI assistant drafted most of the configuration code.
  I directed it and verified the result.
- **The bug hunting VM guide:** an AI assistant (Claude Code) guided the setup
  and drafted the guide; I ran the steps, reviewed it and approved it, and the
  commands were re-tested on a fresh Kali image.
- **The exercises:** I wrote all the code myself. An AI assistant (Claude)
  acted as a tutor: it pointed out problems, gave hints and reviewed my fixes,
  but did not write the solutions.

## Why it matters for security work

The exercises build the habits that security scripts depend on: validating
input before using it, handling errors without crashing, reading structured
data, and calling web APIs with timeouts and retries. The security projects on
the portfolio's roadmap build on the same habits. The bug hunting VM is where I
plan to apply them to real software, always within each programme's published
scope and rules.
