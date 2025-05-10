import threading
from queue import Queue

class WorkerPool:
    def __init__(self, num_workers):
        self.tasks = Queue()
        self.threads = []
        for _ in range(num_workers):
            t = threading.Thread(target=self._worker)
            t.start()
            self.threads.append(t)

    def add_task(self, func, *args):
        self.tasks.put((func, args))

    def _worker(self):
        while True:
            func, args = self.tasks.get()
            if func is None:
                break
            try:
                func(*args)
            finally:
                self.tasks.task_done()

    def shutdown(self):
        # Enqueue sentinel None to signal workers to exit
        for _ in self.threads:
            self.tasks.put((None, ()))
        # Wait until all tasks (including sentinels) are marked done
        self.tasks.join()
        for t in self.threads:
            t.join()

if __name__ == '__main__':
    import time

    def example_task(x):
        time.sleep(0.1)
        print(f"Processed {x}")

    pool = WorkerPool(num_workers=5)
    for i in range(20):
        pool.add_task(example_task, i)
    pool.shutdown()
    print("All tasks completed")