# LazyVim Test Files

Small, safe files for checking that the one-key runner (F5) in the LazyVim
coding environment described in [Foundations](../../README.md) works for each
language. They are throwaway tests, not examples of my coding. An AI assistant
helped draft them, as it did the setup they test.

I checked every file on macOS (Python 3.13, Node 26, Java 21 and gcc). The
runner should also work on Linux (an earlier partial test on Ubuntu-like Linux
needed one shell fix, described in Step 4 of the [companion
guide](https://github.com/james-s-pearson/Cybersecurity-Portfolio/blob/main/foundations/lazyvim-ide/lazyvim-playground-howto.md)),
but the install steps and these exact files were not verified there. Windows
is not covered.

Every file is self-contained: no input, no network, no personal data. The only
file work is `folder_check.py`, which writes one tiny temporary file next to
itself and deletes it. Open a file in your editor, press F5, and compare the
result with the list below.

## Files that should run cleanly

- `hello.py`: Python through IPython. Open a Python shell first (`<leader>rv`
  or `<leader>rh`). F5 prints a separator line, then
  `--- Python Runner Test Start ---`, a version and timestamp,
  `Math Check: 5 + 10 = 15`, `Logic Check: PASSED`, and an end line.
- `folder_check.py`: Python through IPython (optional). It checks that F5 runs
  your script from the script's own folder. Expect these lines, in order:
  `--- Folder Check Start ---`, `Script folder: ` plus the folder's name,
  `Relative file landed in the script folder: yes`, `Folder Check: PASSED`
  and `--- Folder Check End ---`. It writes `folder_check.tmp` and deletes it
  before it ends. Run with plain `python3` from some other folder, it prints
  `FAILED` instead, which shows the check can fail.
- `hello.c`: C. F5 compiles it with `gcc` and prints `Hello, world!` ten
  times, each followed by a blank line (the string already ends in a newline,
  and `puts` adds another). It leaves `hello.out` behind.
- `Hello.java`: Java. F5 compiles into a temporary folder, runs it and deletes
  the folder. Expect `Java Runner Test: SUCCESS` and `No arguments passed.`
- `hello.js`: JavaScript through Node. F5 prints a start line,
  `Status: Success`, your Node version, `Unicode Check: ✅ 🚀` (if the two
  symbols show as boxes, your terminal font needs fixing), a timestamp, a
  passed logic check and an end line. It has a commented-out error line.
- `valid.json`: JSON. F5 prints `JSON Structure is Valid!`.
- `index.html` and `style.css`: a web page. F5 on `index.html` starts a Live
  Server and opens it in your browser. Edit the heading, save, and the page
  should refresh by itself. Then change the accent colour on line 4 of
  `style.css` (`--accent-color: #00b4d8;`), for example to `#e63946`. Keep the
  `#` and the `;`, change only that line, save, and the heading colour should
  change.
- `notes-a.md` and `notes-b.markdown`: Markdown. F5 saves the file and opens
  a live preview in your browser (a table, a task list, a code block and a
  callout block). Open both files and press F5 in each. Open the second one in
  a split with `:vsplit notes-b.markdown`, or in the same window with
  `:edit notes-b.markdown`: either way each file gets its own browser tab
  (the `:edit` case needs the optional `mkdp_auto_close` line from Step 8 of
  the guide). `<leader>cp` stops every preview at once. The browser preview
  shows a callout block (`> [!NOTE]`) as a plain quote, while the editor
  shows it as a "Note" box. This is a known limit of the preview plugin,
  which I expect to replace later.
- `hello.md`: a fuller Markdown test. F5 opens a live preview with bold and
  italic text, a table, a code block, a task list, emoji, a callout block and
  a footnote. A second Markdown file opened in the same window gets its own
  tab, and `<leader>cp` stops every preview.

## Files that are meant to fail

Each one has a comment saying so. The point is to see how your setup shows an
error, so you know what a real failure looks like. The compiler and
JSON error messages print the file's full path, which includes your username,
so crop it before you share a screenshot.

- `broken.c`: F5 shows a compiler error for the missing semicolon, with the
  file name and line number (`broken.c:6`), and runs nothing. The exact words
  depend on your compiler; on macOS it reads
  `expected ';' after expression`.
- `Broken.java`: F5 shows `Broken.java:5: error: ';' expected` and runs
  nothing. It leaves no files behind.
- `broken.json`: F5 prints `JSON Error:` and a message that starts
  `Expected ',' or '}' after property value in JSON`, with the position (line
  4, column 3).

## Files for trying the formatters

Both are deliberately messy but valid. In this setup, saving does not format
(auto-format on save is off), so they stay messy until you press `<leader>cf`.

- `format_me.py`: formatted by Black. F5 prints `Total: 5` and
  `Config: {'name': 'format_me', 'version': 1}`, before and after formatting.
- `format_me.css`: formatted by Prettier. It is not meant to be run; F5 on a
  `.css` file opens the raw stylesheet in the Live Server, not a page.

## Things to know

- The first time you press F5 on a C, Java, JavaScript or JSON file with no
  shell open, the runner opens a new shell split for you.
- `hello.py` and `hello.js` each have a commented-out error line. Remove the
  comment markers to see how your setup shows a failed run.
- Compiled output is ignored by Git (see `.gitignore`), so running the tests
  does not dirty your clone.
- You need `gcc`, `javac`, `node`, `live-server` and `ipython` installed for
  the matching tests. If a test fails because a tool is missing, install the
  tool; the file is not the problem.
