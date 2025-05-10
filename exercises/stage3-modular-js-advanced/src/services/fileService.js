++ exercises/stage3-modular-js-advanced/src/services/fileService.js
const fs = require('fs').promises;

async function readNumbers(filePath) {
  // TODO: implement: read file and parse newline-separated numbers
  throw new Error('Not implemented');
}

async function writeResult(filePath, result) {
  // TODO: implement: write the result to the given filePath
  throw new Error('Not implemented');
}

module.exports = { readNumbers, writeResult };