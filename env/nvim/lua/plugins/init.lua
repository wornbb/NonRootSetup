return {

  -- show function signature
  "ray-x/lsp_signature.nvim",
  "antoinemadec/FixCursorHold.nvim", -- This is needed to fix lsp doc highlight

  { import = "lazyvim.plugins.extras.util.project" },
  { import = "lazyvim.plugins.extras.dap.core" },
  { import = "lazyvim.plugins.extras.dap.nlua" },
  { import = "lazyvim.plugins.extras.editor.flash" },
  { import = "lazyvim.plugins.extras.lang.json" },
}
