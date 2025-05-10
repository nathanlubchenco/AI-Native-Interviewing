# Stage 2: Live Debugging Drill

This exercise provides a simple Node.js service with a latent bug.

Getting started:
1. cd exercises/stage2-debugging
2. npm install
3. npm start

The service listens on port 3000. It exposes a POST /order endpoint.

To reproduce the bug, run:
  curl -X POST http://localhost:3000/order \
    -H "Content-Type: application/json" \
    -d '{"orderId":"123"}'

You should see a runtime error or unexpected response.

Task: Over 45 minutes, reproduce the failure, identify the root cause, fix it, and add a test to lock in the desired behavior.
Submit:
- A short decision diary logging hypotheses and any AI prompts used
- The code change and the new test (your safety net)