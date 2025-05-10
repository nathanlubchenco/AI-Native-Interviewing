Stage 4 – Code-review simulation

Example question:
“Review the code in `question4/task_scheduler.py`. Identify and explain:
  - Design flaws (e.g., dynamic imports on every registration, lack of plugin lifecycle management).
  - Concurrency and performance issues (inefficient thread-join strategy, no timeouts).
  - Fault isolation gaps (exceptions in one plugin can crash the scheduler).
  - Observability shortcomings (no structured logging or metrics).

Suggest concrete improvements, such as:
  - Caching plugin modules and validating interfaces on load.
  - Replacing manual thread management with `concurrent.futures.ThreadPoolExecutor`.
  - Wrapping task execution with try/except and timeouts.
  - Integrating structured logging (e.g., `python-json-logger`) and metrics emission.
”