/**
 * LazyVim Node.js Runner Test
 * Safe script to test buffer execution, error catching, and environment.
 */

console.log("🚀 [LazyVim Node Test] Starter triggered successfully.");

// 1. Check Node Environment
console.log(`Node Version : ${process.version}`);
console.log(`Current File : ${__filename}`);

// 2. Test Array Methods & Logic
const plugins = ["Lazy.nvim", "Mason", "Treesitter", "Telescope"];
console.log(`Testing list mapping...`);
plugins.forEach((plugin, index) => {
    console.log(`  [${index + 1}] Loaded: ${plugin}`);
});

// 3. Test Error Handling (Uncomment the line below to test how your runner displays errors)
// throw new Error("Intentional test error to check LazyVim diagnostic/loclist window");

console.log("✅ [LazyVim Node Test] Finished cleanly.");

