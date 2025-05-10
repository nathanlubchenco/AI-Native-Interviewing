++ exercises/stage3-modular-js-advanced/src/index.js
const path = require('path');

const cmd = process.argv[2];
const filePath = process.argv[3];

if (!cmd || !filePath) {
  console.error('Usage: node main.js <add|subtract> <inputFile>');
  process.exit(1);
}

try {
  const command = require(`./commands/${cmd}`);
  command(filePath);
} catch (err) {
  console.error(`Failed to execute command '${cmd}':`, err.message);
  process.exit(1);
}