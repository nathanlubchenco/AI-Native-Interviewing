Stage 1 – Prompt-to-Prototype take-home

Example question:
“Implement a plugin-based, extensible Python CLI tool named `dl_pipeline` that:
  - Ingests data from multiple sources (HTTP endpoints, local files, and S3 buckets).
  - Processes records through dynamically discovered transform plugins (supporting versioned interfaces).
  - Writes outputs to a destination backend (e.g., PostgreSQL or cloud storage).
  - Supports configuration via YAML with schema validation.
  - Provides clear logging, error handling, and metrics emission.

Requirements:
  - Design a clean project structure with a plugin-discovery mechanism.
  - Use `argparse` or `click` for CLI parsing, with subcommands for `run`, `validate-config`, and `list-plugins`.
  - Include a `requirements.txt`, a `README.md` with usage examples, and follow PEP8/flake8.
  - Supply a comprehensive `pytest` suite covering unit, integration (with a local SQLite or moto-simulated S3), and error cases.

Deliverables:
  - Prototype code in a Git repo structure.
  - Tests demonstrating plugin isolation, config validation failures, and streaming for large inputs.
  - Brief explanation of how you’d integrate this into CI (e.g., GitHub Actions) and ensure backwards-compatibility of plugin APIs.