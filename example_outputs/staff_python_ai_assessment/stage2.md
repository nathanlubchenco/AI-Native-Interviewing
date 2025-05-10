Stage 2 – Live debugging drill

Example question:
“The file `question2/worker_pool.py` implements a thread-based worker pool, but calling its `shutdown()` method intermittently hangs and never returns.
  1. Analyze the root cause—consider how `Queue.put()`, sentinel tasks, and `Queue.task_done()` interact.
  2. Implement a fix so that `shutdown()` reliably completes.
  3. Describe safety nets you would add for production readiness, including:
     - Timeouts on queue operations.
     - Worker health-check or heartbeat.
     - Graceful cancellation of in-flight tasks on errors.
     - Metrics and alerts for stuck or slow workers.
     - Configuration knobs for max queue size and shutdown grace period.
”