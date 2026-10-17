const fs = require('fs');
const path = require('path');

console.log("🚀 Node.js Runner Test Initialized Successfully!");

// 1. SMART SCAN: Look through the directory for your configurations
try {
  const currentFolder = __dirname;
  const filesInFolder = fs.readdirSync(currentFolder);
  
  // Find the first JSON file that contains your specific runner configuration structure
  let configData = null;
  let foundFileName = "";

  for (const file of filesInFolder) {
    if (file.endsWith('.json')) {
      const rawText = fs.readFileSync(path.join(currentFolder, file), 'utf8');
      const parsed = JSON.parse(rawText);
      // Double check if this is your runner file by looking for your unique keys
      if (parsed.command === "node" || parsed.env) {
        configData = parsed;
        foundFileName = file;
        break;
      }
    }
  }

  // 2. INJECT ENVIRONMENT VARIABLES IF VALID FILE DETECTED
  if (configData) {
    console.log(`📊 Auto-detected and hooked into config file: "${foundFileName}"`);
    if (configData.env) {
      Object.keys(configData.env).forEach(key => {
        process.env[key] = configData.env[key];
      });
      console.log("📊 Loaded environment variables successfully!");
    }
    if (configData.args) {
      console.log(`📊 Extracted config flags: ${JSON.stringify(configData.args)}`);
    }
  } else {
    console.log("⚠️ Could not locate a valid configuration JSON file in this directory.");
  }

} catch (error) {
  console.log("⚠️ Error reading folder data:", error.message);
}

// Simulate reading arguments passed from command line
const args = process.argv.slice(2);
if (args.length > 0) {
  console.log(`🔹 Arguments received via CLI: ${JSON.stringify(args)}`);
}

// Simulate reading environment variables
const env = process.env.NODE_ENV || "not set";
const port = process.env.PORT || "not set";
console.log(`🔹 Environment: ${env} (Port: ${port})`);

console.log("✅ Execution finished without errors.");
process.exit(0);
