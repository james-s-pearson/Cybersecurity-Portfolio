-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here
vim.opt.winbar = "%=%m %F"
--
-- LazyVim ignores conform's `format_on_save` and formats on save whenever
-- `vim.g.autoformat` is true (its default). Turn that off; <leader>cf still formats.
vim.g.autoformat = false
--
-- Force Prettier to run even if there is no .prettierrc file in your Git repository
vim.g.lazyvim_prettier_needs_config = false
--
-- markdown-preview.nvim closes a file's preview when its buffer is hidden (for example when you
-- open another file in the same window). Turn that off so F5 on several files keeps every preview.
vim.g.mkdp_auto_close = 0
