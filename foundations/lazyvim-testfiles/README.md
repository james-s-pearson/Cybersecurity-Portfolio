# LazyVim Test Files

Small, safe files for checking that the one-key runner (F5) in the LazyVim
coding environment described in [Foundations](../README.md) works for each
language. They are throwaway tests, not examples of my coding. An AI assistant
helped draft them, as it did the setup they test.

Every file is self-contained: no input, no network, no personal data. The only
file work is `folder_check.py`, which writes one tiny temporary file next to
itself and deletes it. Open a file in your editor, press F5, and compare the
result with the list below.

## What to expect

- `hello.py`: Python through IPython. Open a Python shell first (`<leader>rv`,
  `<leader>rh` or `Ctrl+/`). F5 prints a separator line, then
  `--- Python Runner Test Start ---`, a version and timestamp,
  `Math Check: 5 + 10 = 15`, `Logic Check: PASSED`, and an end line.
- `folder_check.py`: Python through IPython (optional). It checks that F5 runs
  your script from the script's own folder. Expect these lines, in order:
  `--- Folder Check Start ---`, `Script folder: ` plus the folder's name,
  `Relative file landed in the script folder: yes`, `Folder Check: PASSED`
  and `--- Folder Check End ---`. It writes `folder_check.tmp` and deletes it
  before it ends. Run with plain `python3` from some other folder, it prints
  `FAILED` instead, which shows the check can fail.
- `firstprog.c`: C. F5 compiles it with `gcc` and prints `Hello, world!` ten
  times, each followed by a blank line (the string already ends in a newline,
  and `puts` adds another). It leaves `firstprog.out` behind.
- `Main.java`: Java. F5 compiles into a temporary folder, runs it and deletes
  the folder. Expect `Java Runner Test: SUCCESS` and `No arguments passed.`
- `firstjs.js` and `lvtext.js`: JavaScript through Node. F5 prints a start
  line, `Status: Success`, a timestamp and a passed logic check (`firstjs.js`),
  or a numbered list of plugin names (`lvtext.js`).
- `index.js`: Node again. It reads the JSON files in its own folder and
  reports the settings it finds in `runner-config.json`: environment
  `development`, port `3000`, and no errors.
- `index.html`: a web page. F5 starts a Live Server and opens it in your
  browser. Edit the heading, save, and the page should refresh by itself.
- `runner-config.json` and `simplesafe.json`: JSON. F5 prints
  `JSON Structure is Valid!`. Break a comma on purpose to see a
  `JSON Error` message. `index.js` reads `runner-config.json`, so keep the two
  together.

## Things to know

- The first time you press F5 on `firstprog.c`, `Main.java` or a JavaScript
  file with no shell open, the runner opens a new shell split for you.
- `lvtext.js` and `hello.py` each have a commented-out error line. Remove the
  comment markers to see how your setup shows a failed run.
- Compiled output is ignored by Git (see `.gitignore`), so running the tests
  does not dirty your clone.
- You need `gcc`, `javac`, `node`, `live-server` and `ipython` installed for
  the matching tests. If a test fails because a tool is missing, install the
  tool; the file is not the problem.
