import importlib
import threading
import time

class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self.lock = threading.Lock()

    def register_task(self, module_name, function_name, *args, **kwargs):
        # Dynamically import plugin and schedule execution
        module = importlib.import_module(module_name)
        func = getattr(module, function_name)
        self.tasks.append((func, args, kwargs))

    def run_all(self, thread_count=4):
        threads = []
        for func, args, kwargs in self.tasks:
            t = threading.Thread(target=self._run_task, args=(func, args, kwargs))
            t.start()
            threads.append(t)
            if len(threads) >= thread_count:
                for thr in threads:
                    thr.join()
                threads = []
        for thr in threads:
            thr.join()

    def _run_task(self, func, args, kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"Task {func.__name__} took {duration:.2f}s and returned {result}")

if __name__ == "__main__":
    sched = TaskScheduler()
    sched.register_task("plugins.example", "process", 42)
    sched.run_all()