return {
  "stevearc/conform.nvim",
  opts = {
    -- Maps languages cleanly to their formatters
    formatters_by_ft = {
      python = { "black" },
      c = { "clang-format" },
      cpp = { "clang-format" },
      java = { "google-java-format" },
      html = { "prettier" },
      css = { "prettier" },
      javascript = { "prettier" },
      typescript = { "prettier" },
      json = { "prettier" },
      markdown = { "prettier" },
      ["markdown.mdx"] = { "prettier" },
    },

    -- Safely overrides CLI flags for Prettier
    formatters = {
      prettier = {
        prepend_args = {
          "--prose-wrap", "always",
          "--print-width", "80",
          "--tab-width", "2",
        },
      },
    },
  },
}
