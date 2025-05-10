 # Senior Python Engineer Technical Assessment

 This document contains a set of test questions designed to evaluate the skills of a senior Python engineer across system design, concurrency, performance, security, testing, and deployment.

 ## 1. System Architecture Design
 **Scenario**: Design a high-throughput JSON event ingestion microservice in Python that reads events from HTTP POST requests, processes them (validates and enriches), and publishes to a Kafka topic.
 **Task**: Outline the key components, libraries/frameworks you would use, and describe how you would ensure reliability, scalability, and fault tolerance.

 ## 2. Concurrency and Thread Safety
 **Scenario**: You need an in-memory cache with TTL eviction that can be accessed by multiple threads.
 **Task**: Implement a thread-safe Python class `TTLCache` with methods `get(key)`, `set(key, value, ttl_seconds)`, and automatic eviction. You may use `threading` primitives.

 ## 3. Performance Optimization
 **Scenario**: A data pipeline reads 50 million rows from CSV files, transforms each row, and writes results to a database. The current implementation in pure Python takes hours to complete.
 **Task**: Identify performance bottlenecks and propose concrete code-level optimizations or alternative libraries/tools to reduce runtime.

 ## 4. Debugging and Root Cause Analysis
 **Scenario**: A multithreaded Python application intermittently deadlocks. You are given a simplified code snippet.
 ```python
 import threading

 lock_a = threading.Lock()
 lock_b = threading.Lock()

 def task1():
     with lock_a:
         do_work()
         with lock_b:
             do_more_work()

 def task2():
     with lock_b:
         do_other_work()
         with lock_a:
             do_even_more_work()

 threads = [
     threading.Thread(target=task1),
     threading.Thread(target=task2),
 ]
 for t in threads:
     t.start()
 ```
 **Task**: Explain why deadlocks occur and propose a fix.

 ## 5. Security and Code Review
 **Scenario**: Review the following code that builds SQL queries from user input:
 ```python
 def get_user_orders(user_id):
     query = f"SELECT * FROM orders WHERE user_id = {user_id}"
     cursor.execute(query)
     return cursor.fetchall()
 ```
 **Task**: Identify security vulnerabilities and rewrite the function to eliminate these issues.

 ## 6. Automated Testing with pytest
 **Scenario**: You have a function `compute_statistics(data: List[float]) -> Dict[str, float]` that returns mean, median, and mode.
 **Task**: Write comprehensive `pytest` test cases covering normal cases, edge cases, and invalid inputs.

 ## 7. Deployment and CI/CD
 **Scenario**: You need to deploy a Python AWS Lambda function that processes S3 events and writes to DynamoDB.
 **Task**: Describe how you would set up a CI/CD pipeline (e.g., GitHub Actions) to build, test, and deploy this Lambda function, including handling environment-specific configurations and secrets.