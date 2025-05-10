++ exercises/stage3-modular-js-advanced/README.md
# Stage 3: Modular JavaScript Advanced Exercise

In this exercise, you're building a simple CLI tool structured with multiple modules. Your task is to implement and wire up services and commands to perform operations on the file system and math functions.

Directory structure:
```
exercises/stage3-modular-js-advanced/
├── package.json
├── main.js
└── src
    ├── index.js
    ├── services
    │   ├── fileService.js
    │   └── mathService.js
    └── commands
        ├── add.js
        └── subtract.js
```

Requirements:
1. In `src/services/fileService.js`, implement:
   - `readNumbers(filePath)`: reads a file containing newline-separated numbers, returns an array of numbers.
   - `writeResult(filePath, result)`: writes the result to the file.
2. In `src/services/mathService.js`, implement:
   - `add(numbers)`: returns sum of array.
   - `subtract(numbers)`: returns result of subtracting all subsequent numbers from first.
3. In `src/commands/add.js` and `subtract.js`, implement command functions that:
   - Read numbers using `fileService`.
   - Compute result using `mathService`.
   - Write the result back to a new file (e.g., `result_add.txt` or `result_subtract.txt`).
4. In `src/index.js`, parse CLI arguments:
   - Usage: `node main.js add input.txt` or `node main.js subtract input.txt`.
   - Load and execute the corresponding command module.
5. In `main.js`, require and invoke `src/index.js`.

You may add helper modules or functions as needed. Ensure proper error handling for file I/O and invalid input.