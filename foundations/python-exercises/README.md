# Python Exercises

Thirteen exercises from a Python course, written in a LazyVim environment I
built ([the story](../lazyvim-ide/lazyvim-playground-story.md)
and [the guide](../lazyvim-ide/lazyvim-playground-howto.md) explain how). The
course's own exercise text and solutions are not included: each exercise is
described in my own words.

## How to read a file

Every file has the same layout:

1. The exercise, described in my own words.
2. My first attempt, commented out.
3. My corrected code. This section starts with notes on what was wrong with
   the first attempt and what I learned, followed by the code that runs.

Reading the notes first makes the code easier to follow.

## Start here

- **Ex13, trivia game:** web requests, JSON, error handling, retries and rate
  limits.
- **Ex12, typing speed:** timing, input validation and a chart.
- **Ex11, color game:** nested loops and input validation.

## All thirteen

1. **Ex01, kilometres to miles:** input validation with `try` and `except`,
   and f-string formatting.
2. **Ex02, initials:** a function that asks until the input is valid, and an
   optional middle name with a confirmation step.
3. **Ex03, lot numbers:** splitting a string, then stripping and validating
   each part.
4. **Ex04, circle area:** `math.pi`, rejecting `nan`, `inf` and overflow, and
   a named constant for the limit.
5. **Ex05, birth month:** parsing DD-MM-YYYY with `split`, range checks, and a
   negative-index bug caught and fixed.
6. **Ex06, guest list:** lists, `append`, `", ".join`, a confirm step, and
   capitalising names without breaking them.
7. **Ex07, dictionary lookup:** `.get` with a default, listing the keys, and
   calculating an age from a date.
8. **Ex08, older or younger:** an age calculated from a birthday inside a
   function, and comparisons.
9. **Ex09, BMI:** a reusable input function, categories, and rounding once so
   the screen and the result agree.
10. **Ex10, random name:** loops, `random.choice`, and one variable
    controlling the whole program.
11. **Ex11, color game:** nested loops and `break`, one place for each
    prompt, and input validation.
12. **Ex12, typing speed:** `time.perf_counter`, counting mistakes, and a
    `matplotlib` chart.
13. **Ex13, trivia game:** web requests with timeouts, JSON, cleaning HTML
    entities, retry and quit, and a countdown that respects rate limits.

## Running them

- Python 3.13: `python3 Ex01_km2miles.py`
- Ex12 needs `matplotlib`. Ex13 needs `requests` and an internet connection.
  Install both with `pip install matplotlib requests`.
- Most programs wait for typed input.

## How these were made

I wrote all the code myself. An AI assistant (Claude) acted as a tutor: it
pointed out problems, gave hints and reviewed my fixes, but did not write the
solutions.
