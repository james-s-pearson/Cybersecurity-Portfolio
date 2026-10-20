# Foundations: How I Learned Python for Security

Python is one of the skills security work leans on most: reading logs,
automating checks, calling web APIs and writing reports. I am a project
manager moving into cybersecurity, and this folder shows how I started
learning it. It has two parts, in the order I did them.

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

## How AI was used

- **The environment:** an AI assistant drafted most of the configuration code.
  I directed it and verified the result.
- **The exercises:** I wrote all the code myself. An AI assistant (Claude)
  acted as a tutor: it pointed out problems, gave hints and reviewed my fixes,
  but did not write the solutions.

## Why it matters for security work

The exercises build the habits that security scripts depend on: validating
input before using it, handling errors without crashing, reading structured
data, and calling web APIs with timeouts and retries. The security projects on
the portfolio's roadmap build on the same habits.
