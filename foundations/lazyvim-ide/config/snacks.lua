return {
  "folke/snacks.nvim",
  opts = {
    -- Show images inside Neovim (needs a terminal with the kitty graphics protocol, such as Ghostty or Kitty,
    -- and ImageMagick for formats other than PNG)
    image = { enabled = true },
    picker = {
      sources = {
        buffers = {
          -- Configure layout overrides specific to the buffer picker if desired
          layout = {
            -- Adjust preview size depending on the layout box proportions
            -- e.g., passing custom layout options or preset overrides
          },
        },
      },
    },
  },
}
