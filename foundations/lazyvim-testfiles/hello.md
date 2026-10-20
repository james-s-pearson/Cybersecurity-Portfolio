<!--
  Test file for the Markdown preview. Safe, self-contained, no network.
  Open it in Neovim and press F5: the page below should open in your browser.
-->

# Markdown Preview Test

If you can read this heading in your browser, F5 started the preview. Edit
this sentence in Neovim, and the page should update as you type.

## Text styles

This line has **bold**, *italic*, ~~strikethrough~~ and `inline code`. Here is
a [link to a local file](hello.py) and a
[link to a website](https://example.com).

## A table

| Runner   | Opens in | Needs a terminal |
| -------- | -------- | ---------------- |
| Python   | IPython  | yes              |
| C        | shell    | yes              |
| Markdown | browser  | no               |

## A code block

```python
def greet(name):
    return f"Hello, {name}!"


print(greet("preview"))
```

## A task list

- [x] Press F5 on a Markdown file
- [x] See this page in the browser
- [ ] Open a second Markdown file and press F5 again

## Emoji

Shortcode: :tada: and typed: ✅ 🚀

## An alert

> [!NOTE]
> GitHub draws this as a coloured "Note" box. The browser preview shows it as
> a plain quote that starts with `[!NOTE]`. That is expected.

## Footnote

The preview handles footnotes too[^1].

[^1]: This line appears at the bottom of the page.

## What to check

- F5 on this file opens a browser tab with this page.
- A `.markdown` copy of this file behaves the same way.
- Open a second Markdown file in the same window and press F5. Both previews
  stay open. Close them with `<leader>cp`, which stops every preview.
