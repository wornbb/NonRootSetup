-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

-- DAP
vim.api.nvim_set_keymap("n", "<F8>", [[:lua require"dap".toggle_breakpoint()<CR>]], { noremap = true })
vim.api.nvim_set_keymap("n", "<F9>", [[:lua require"dap".continue()<CR>]], { noremap = true })
vim.api.nvim_set_keymap("n", "<F10>", [[:lua require"dap".step_over()<CR>]], { noremap = true })
vim.api.nvim_set_keymap("n", "<S-F10>", [[:lua require"dap".step_into()<CR>]], { noremap = true })
vim.api.nvim_set_keymap("n", "<F12>", [[:lua require"dap.ui.widgets".hover()<CR>]], { noremap = true })
vim.api.nvim_set_keymap("n", "<F5>", [[:lua require"osv".launch({port = 8086})<CR>]], { noremap = true })
