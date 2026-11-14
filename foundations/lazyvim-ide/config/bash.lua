return {
  -- Bash language server (bash-language-server is already installed through Mason; it also runs shellcheck)
  {
    "neovim/nvim-lspconfig",
    opts = {
      servers = {
        bashls = {},
      },
    },
  },
  -- shfmt formatting for <leader>cf is already set by LazyVim; Mason keeps the tools installed
  {
    "mason-org/mason.nvim",
    opts = { ensure_installed = { "bash-language-server", "shellcheck", "shfmt" } },
  },
}
