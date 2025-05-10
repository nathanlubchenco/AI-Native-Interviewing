# Stage 2: Advanced Python Debugging Drill

This exercise provides a simple Flask service with latent bugs.

Getting started:
1. cd exercises/stage2-debugging-python-advanced
2. pip install -r requirements.txt
3. python app.py

The service listens on port 5000 and exposes two POST endpoints:
- `/divide`: expects JSON `{ "x": int, "y": int }`, returns `{ "result": float }`
- `/median`: expects JSON `{ "nums": List[int] }`, returns `{ "median": float }`

To reproduce the bugs, run:
```bash
curl -X POST http://localhost:5000/divide \
     -H "Content-Type: application/json" \
     -d '{"x":7,"y":2}'
``` 
Expected: `{"result": 3.5}`
Actual:   `{"result": 3}`

```bash
curl -X POST http://localhost:5000/median \
     -H "Content-Type: application/json" \
     -d '{"nums":[3,1,2]}'
``` 
Expected: `{"median": 2}`
Actual:   `{"median": 1}`

Task: Over 45 minutes, reproduce the failures, identify the root causes, fix them, and add pytest tests to lock in the desired behavior (including edge cases like division by zero and empty list).
Submit:
- A short decision diary logging your hypotheses and any prompts or strategies used
- The code fixes and the new tests