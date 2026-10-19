return {
  {
    "jpalardy/vim-slime",
    init = function()
      vim.g.slime_target = "neovim"
      vim.g.slime_bracketed_paste = 1
      vim.g.slime_dont_ask_default = 1
    end,
    config = function()
      -- Terminal buffer names end in //PID:command, so this returns the command a terminal was started with
      local function terminal_cmd(buf)
        return vim.api.nvim_buf_get_name(buf):match("//%d+:(.*)$") or ""
      end

      local function is_tool_terminal(cmd)
        return cmd:find("ipython", 1, true) or cmd:find("lazygit", 1, true) or cmd:find("live-server", 1, true)
      end

      -- A hidden terminal (for example the Ctrl+/ one after a second Ctrl+/) is alive but has no window
      local function is_visible(buf)
        return vim.fn.bufwinid(buf) ~= -1
      end

      -- Find an active terminal channel (Split OR Float).
      -- kind "python" only accepts a visible IPython terminal (nil if none, so F5 prints its error message).
      -- kind "shell" only accepts a visible terminal that is not IPython, LazyGit or live-server (nil if none, so
      -- the caller opens a new zsh split). With no kind, the first terminal found is used (the old behaviour).
      local function get_active_terminal_job_id(kind)
        local fallback
        for _, buf in ipairs(vim.api.nvim_list_bufs()) do
          local chan = vim.bo[buf].buftype == "terminal" and vim.b[buf].terminal_job_id
          if chan then
            local cmd = terminal_cmd(buf)
            if kind == "python" and cmd:find("ipython", 1, true) and is_visible(buf) then
              return chan
            end
            if kind == "shell" and not is_tool_terminal(cmd) and is_visible(buf) then
              return chan
            end
            if kind == nil then
              fallback = fallback or chan
            end
          end
        end
        return fallback
      end

      -- 1. Open Python Shell: VERTICAL Split (Space + r + v)
      vim.keymap.set("n", "<leader>rv", function()
        vim.cmd("vsplit | terminal ipython --no-autoindent")
        local term_buf = vim.api.nvim_get_current_buf()
        local term_chan = vim.b[term_buf].terminal_job_id
        vim.cmd("wincmd p")
        vim.b.slime_config = { jobid = term_chan }
      end, { desc = "Python Shell: Vertical Split" })

      -- 2. Open Python Shell: HORIZONTAL Split (Space + r + h)
      vim.keymap.set("n", "<leader>rh", function()
        vim.cmd("split | terminal ipython --no-autoindent")
        local term_buf = vim.api.nvim_get_current_buf()
        local term_chan = vim.b[term_buf].terminal_job_id
        vim.cmd("wincmd p")
        vim.b.slime_config = { jobid = term_chan }
      end, { desc = "Python Shell: Horizontal Split" })

      -- 3. SMART MULTI-LANGUAGE F5 KEYMAP (Python, C, Java, HTML, JS, JSON, & Markdown)
      vim.keymap.set("n", "<F5>", function()
        vim.cmd("w") -- Save the current file

        local file_ext = vim.fn.expand("%:e") -- Get file extension
        local filepath = vim.fn.expand("%:p") -- Get full absolute path
        local filedir = vim.fn.expand("%:p:h") -- Get the folder containing the file
        local filename = vim.fn.expand("%:t:r") -- Get file name without extension
        local filetail = vim.fn.expand("%:t") -- Get full file name with extension

        -- PYTHON WORKFLOW
        if file_ext == "py" then
          local target_chan = get_active_terminal_job_id("python")
          if target_chan then
            vim.b.slime_config = { jobid = target_chan }
            -- A separator line (file name and time) replaces the old %clear, so earlier runs stay in the scrollback
            -- FIXED: %cd forces IPython to match the script's exact folder before running %run
            vim.fn["slime#send"](
              string.format(
                "print('\\n──── %s · %s ────')\n%%cd '%s'\n%%run '%s'\n",
                filetail,
                os.date("%H:%M:%S"),
                filedir,
                filepath
              )
            )
          else
            print("Error: No active Python terminal. Open one with <leader>rv or <leader>rh")
          end

          -- C WORKFLOW (Compile and Run)
        elseif file_ext == "c" then
          local compile_and_run_cmd = string.format(
            "cd '%s' && gcc '%s' -o '%s.out' && clear && ./'%s.out'\n",
            filedir,
            filepath,
            filename,
            filename
          )
          local target_chan = get_active_terminal_job_id("shell")
          if target_chan then
            vim.b.slime_config = { jobid = target_chan }
            vim.fn["slime#send"](compile_and_run_cmd)
          else
            vim.cmd("vsplit | terminal zsh")
            local term_buf = vim.api.nvim_get_current_buf()
            local term_chan = vim.b[term_buf].terminal_job_id
            vim.cmd("wincmd p")
            vim.b.slime_config = { jobid = term_chan }
            vim.fn["slime#send"](compile_and_run_cmd)
          end

          -- JAVA WORKFLOW (Self-Cleaning Compiled Loop)
        elseif file_ext == "java" then
          -- Compile into a temporary folder so nothing is written to, or deleted from, the project folder
          local java_compile_run_clean = string.format(
            "cd '%s' && jtmp=$(mktemp -d) && javac -d \"$jtmp\" '%s' && clear && java -cp \"$jtmp:.\" '%s'; rm -rf \"$jtmp\"\n",
            filedir,
            filepath,
            filename
          )
          local target_chan = get_active_terminal_job_id("shell")
          if target_chan then
            vim.b.slime_config = { jobid = target_chan }
            vim.fn["slime#send"](java_compile_run_clean)
          else
            vim.cmd("vsplit | terminal zsh")
            local term_buf = vim.api.nvim_get_current_buf()
            local term_chan = vim.b[term_buf].terminal_job_id
            vim.cmd("wincmd p")
            vim.b.slime_config = { jobid = term_chan }
            vim.fn["slime#send"](java_compile_run_clean)
          end

          -- HTML WORKFLOW (Live Server Launch)
        elseif file_ext == "html" or file_ext == "css" then
          -- A live-server started for this file's folder counts as running, visible or hidden (it keeps serving)
          local server_running = false
          for _, buf in ipairs(vim.api.nvim_list_bufs()) do
            if vim.bo[buf].buftype == "terminal" then
              local cmd = terminal_cmd(buf)
              if cmd:find("live-server", 1, true) and cmd:find("cd '" .. filedir .. "'", 1, true) then
                server_running = true
                break
              end
            end
          end
          if server_running then
            print("Live Server running. Modifications saved will auto-refresh the browser!")
          else
            local launch_cmd = string.format("split | terminal cd '%s' && live-server --open='%s'", filedir, filetail)
            vim.cmd(launch_cmd)
            vim.cmd("wincmd p")
            print("Launching web preview live server...")
          end

          -- JAVASCRIPT WORKFLOW (Execute via Node.js natively)
        elseif file_ext == "js" then
          local js_run_cmd = string.format("cd '%s' && clear && node '%s'\n", filedir, filetail)
          local target_chan = get_active_terminal_job_id("shell")
          if target_chan then
            vim.b.slime_config = { jobid = target_chan }
            vim.fn["slime#send"](js_run_cmd)
          else
            vim.cmd("vsplit | terminal zsh")
            local term_buf = vim.api.nvim_get_current_buf()
            local term_chan = vim.b[term_buf].terminal_job_id
            vim.cmd("wincmd p")
            vim.b.slime_config = { jobid = term_chan }
            vim.fn["slime#send"](js_run_cmd)
          end

          -- MARKDOWN WORKFLOW (Open a browser preview; each Markdown file gets its own page)
        elseif file_ext == "md" or file_ext == "markdown" then
          -- Open only, never toggle: toggling one file stops the server and closes every preview
          vim.cmd("MarkdownPreview")
          print("Markdown preview opened. Stop all previews with <leader>cp.")

          -- JSON WORKFLOW (Validate syntax)
        elseif file_ext == "json" then
          local json_test_cmd = string.format(
            "clear && node -e \"try { require('%s'); console.log('✅ JSON Structure is Valid!'); } catch(e) { console.error('❌ JSON Error:\\n', e.message); }\"\n",
            filepath
          )
          local target_chan = get_active_terminal_job_id("shell")
          if target_chan then
            vim.b.slime_config = { jobid = target_chan }
            vim.fn["slime#send"](json_test_cmd)
          else
            vim.cmd("vsplit | terminal zsh")
            local term_buf = vim.api.nvim_get_current_buf()
            local term_chan = vim.b[term_buf].terminal_job_id
            vim.cmd("wincmd p")
            vim.b.slime_config = { jobid = term_chan }
            vim.fn["slime#send"](json_test_cmd)
          end
        else
          print("F5 is not configured for ." .. file_ext .. " files yet!")
        end
      end, { desc = "Smart F5: Run current file" })

      -- 4. NEW: ONE-KEY TERMINAL CLOSE SHORTCUT (F6)
      -- Closes the terminal you are in; otherwise the newest visible terminal that is not LazyGit
      local function close_active_terminal()
        local current = vim.api.nvim_get_current_buf()
        if vim.bo[current].buftype == "terminal" then
          vim.cmd("bdelete! " .. current)
          return
        end
        local target
        for _, buf in ipairs(vim.api.nvim_list_bufs()) do
          if
            vim.bo[buf].buftype == "terminal"
            and is_visible(buf)
            and not terminal_cmd(buf):find("lazygit", 1, true)
          then
            target = buf
          end
        end
        if target then
          vim.cmd("bdelete! " .. target)
        else
          print("No open terminal window to close.")
        end
      end
      vim.keymap.set("n", "<F6>", close_active_terminal, { desc = "Close open runner split" })
      vim.keymap.set("t", "<F6>", close_active_terminal, { desc = "Terminal: Close open runner split" })

      -- 5. Force-Kill Keymap for Terminal Mode (Ctrl + c)
      vim.keymap.set("t", "<C-c>", [[<C-\><C-n>i<C-c>]], { desc = "Force-kill frozen script" })

      -- 6. Quick Window Switching (Normal Mode)
      vim.keymap.set("n", "<C-h>", "<C-w>h", { desc = "Go to Left Window" })
      vim.keymap.set("n", "<C-j>", "<C-w>j", { desc = "Go to Bottom Window" })
      vim.keymap.set("n", "<C-k>", "<C-w>k", { desc = "Go to Top Window" })
      vim.keymap.set("n", "<C-l>", "<C-w>l", { desc = "Go to Right Window" })

      -- 7. Quick Window Switching (Terminal Mode)
      -- Trade-off: in a terminal these four keys no longer reach the shell, so Ctrl+l (clear screen),
      -- Ctrl+k (delete to end of line), Ctrl+j (Enter) and Ctrl+h (backspace) are taken.
      vim.keymap.set("t", "<C-h>", [[<C-\><C-n><C-w>h]], { desc = "Terminal: Go Left" })
      vim.keymap.set("t", "<C-j>", [[<C-\><C-n><C-w>j]], { desc = "Terminal: Go Bottom" })
      vim.keymap.set("t", "<C-k>", [[<C-\><C-n><C-w>k]], { desc = "Terminal: Go Top" })
      vim.keymap.set("t", "<C-l>", [[<C-\><C-n><C-w>l]], { desc = "Terminal: Go Right" })

      -- Ctrl+k is taken above, so Ctrl+o sends it to the shell instead (delete from the cursor to end of line)
      vim.keymap.set("t", "<C-o>", function()
        vim.api.nvim_chan_send(vim.b.terminal_job_id, "\11")
      end, { desc = "Terminal: Delete to end of line (sends Ctrl+k)" })

      -- 8. Keep Ctrl+c Ctrl+c in Normal Mode for sending single lines
      vim.keymap.set("n", "<C-c><C-c>", ":SlimeSend<CR>", { silent = true, desc = "Send line to REPL" })
    end,
  },
}
