# Python Threading & Concurrency - Essential Guide

## Table of Contents

1. [Basic Threading](#basic-threading)
2. [Thread Synchronization](#thread-synchronization)
3. [Thread Communication](#thread-communication)
4. [Thread Pool Executor](#thread-pool-executor)
5. [Real-World Patterns](#real-world-patterns)
6. [Best Practices](#best-practices)

---

## Basic Threading

### Creating and Running Threads

```python
import threading
import time

def worker_task(name, duration):
    print(f"Worker {name} starting...")
    time.sleep(duration)
    print(f"Worker {name} completed!")

# Method 1: Manual thread creation
thread1 = threading.Thread(target=worker_task, args=("Thread-1", 2))
thread2 = threading.Thread(target=worker_task, args=("Thread-2", 1))

thread1.start()
thread2.start()

# Wait for completion
thread1.join()
thread2.join()
```

### Multiple Threads Pattern

```python
def run_multiple_tasks(tasks):
    """Run multiple tasks concurrently."""
    threads = []

    for name, duration in tasks:
        thread = threading.Thread(target=worker_task, args=(name, duration))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Usage
tasks = [("Task-A", 1.5), ("Task-B", 1.0), ("Task-C", 2.0)]
run_multiple_tasks(tasks)
```

---

## Thread Synchronization

### Race Conditions Problem

```python
# Dangerous: Race condition
counter = 0

def unsafe_increment():
    global counter
    for _ in range(100000):
        counter += 1  # Not thread-safe!

# This will give inconsistent results
threads = [threading.Thread(target=unsafe_increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Counter: {counter}")  # Often less than 200000
```

### Thread-Safe Solution with Locks

```python
from threading import Lock

counter_safe = 0
lock = Lock()

def safe_increment():
    global counter_safe
    for _ in range(100000):
        with lock:  # Acquire lock automatically
            counter_safe += 1

# This gives consistent results
threads = [threading.Thread(target=safe_increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Safe counter: {counter_safe}")  # Always 200000
```

### Different Lock Types

```python
from threading import Lock, RLock, Semaphore

# Basic Lock - single acquisition
basic_lock = Lock()

# Reentrant Lock - can be acquired multiple times by same thread
reentrant_lock = RLock()

# Semaphore - limit number of concurrent accesses
semaphore = Semaphore(3)  # Max 3 threads can access

def rate_limited_task():
    with semaphore:
        print("Processing...")
        time.sleep(1)
```

---

## Thread Communication

### Producer-Consumer with Queue

```python
import queue

# Thread-safe queue
task_queue = queue.Queue(maxsize=5)

def producer(name, num_items):
    """Produce items for processing."""
    for i in range(num_items):
        item = f"{name}-Item-{i+1}"
        task_queue.put(item)
        print(f"Produced: {item}")
        time.sleep(0.1)

def consumer(name):
    """Consume and process items."""
    while True:
        try:
            item = task_queue.get(timeout=2)
            print(f"Processing: {item}")
            time.sleep(0.2)
            task_queue.task_done()  # Mark as completed
        except queue.Empty:
            break

# Usage
producer_thread = threading.Thread(target=producer, args=("Producer-1", 5))
consumer_thread = threading.Thread(target=consumer, args=("Consumer-1",))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
task_queue.join()  # Wait for all tasks to be processed
```

### Event-Based Communication

```python
from threading import Event

# Coordinate between threads
shutdown_event = Event()

def worker():
    while not shutdown_event.is_set():
        print("Working...")
        time.sleep(1)
    print("Worker stopped")

def controller():
    time.sleep(3)
    print("Sending shutdown signal")
    shutdown_event.set()

# Start worker and controller
threading.Thread(target=worker).start()
threading.Thread(target=controller).start()
```

---

## Thread Pool Executor

### Basic Thread Pool Usage

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_simulation(url):
    """Simulate downloading from URL."""
    print(f"Downloading {url}...")
    time.sleep(1)  # Simulate network delay
    return f"Content from {url}"

urls = ["site1.com", "site2.com", "site3.com", "site4.com"]

# Sequential execution (slow)
start_time = time.time()
results = [download_simulation(url) for url in urls]
sequential_time = time.time() - start_time

# Concurrent execution (faster)
start_time = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:
    concurrent_results = list(executor.map(download_simulation, urls))
concurrent_time = time.time() - start_time

print(f"Sequential: {sequential_time:.2f}s")
print(f"Concurrent: {concurrent_time:.2f}s")
print(f"Speedup: {sequential_time/concurrent_time:.2f}x")
```

### Advanced Thread Pool Patterns

```python
def process_with_results():
    """Handle individual task completion."""

    def task_with_result(task_id):
        duration = task_id * 0.5
        time.sleep(duration)
        return f"Task {task_id} result"

    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks and get futures
        future_to_task = {
            executor.submit(task_with_result, i): i
            for i in range(1, 6)
        }

        # Process results as they complete
        for future in as_completed(future_to_task):
            task_id = future_to_task[future]
            try:
                result = future.result()
                print(f"Completed: {result}")
            except Exception as exc:
                print(f"Task {task_id} failed: {exc}")
```

---

## Real-World Patterns

### Web Scraping with Threading

```python
def fetch_url_data(url):
    """Simulate fetching data from URL."""
    try:
        print(f"Fetching {url}...")
        time.sleep(1)  # Simulate HTTP request
        return {
            "url": url,
            "status": 200,
            "data": f"Content from {url}",
            "success": True
        }
    except Exception as e:
        return {"url": url, "error": str(e), "success": False}

def concurrent_web_scraping(urls):
    """Scrape multiple URLs concurrently."""
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch_url_data, urls))

    successful = [r for r in results if r["success"]]
    failed = [r for r in results if not r["success"]]

    return {"successful": len(successful), "failed": len(failed)}
```

### File Processing Pipeline

```python
def process_file_batch(filenames):
    """Process multiple files concurrently."""

    def process_single_file(filename):
        print(f"Processing {filename}...")
        time.sleep(0.5)  # Simulate processing
        return {
            "filename": filename,
            "lines": len(filename) * 10,  # Mock data
            "status": "processed"
        }

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(process_single_file, filenames))

    return results

# Usage
files = ["data1.csv", "data2.json", "data3.xml", "data4.txt"]
results = process_file_batch(files)
```

### API Rate Limiting with Semaphores

```python
from threading import Semaphore

class RateLimitedAPI:
    """API client with built-in rate limiting."""

    def __init__(self, requests_per_second=2):
        self.semaphore = Semaphore(requests_per_second)
        self.request_count = 0
        self.lock = Lock()

    def make_request(self, endpoint):
        """Make rate-limited API request."""
        with self.semaphore:
            with self.lock:
                self.request_count += 1
                request_id = self.request_count

            print(f"API Request #{request_id}: {endpoint}")
            time.sleep(0.5)  # Simulate API call

            return f"Response from {endpoint}"

# Usage
api = RateLimitedAPI(requests_per_second=3)
endpoints = ["/users", "/products", "/orders", "/reports"]

with ThreadPoolExecutor(max_workers=5) as executor:
    responses = list(executor.map(api.make_request, endpoints))
```

### Background Task Manager

```python
class BackgroundTaskManager:
    """Manage background tasks with worker threads."""

    def __init__(self, num_workers=3):
        self.task_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self.workers = []
        self.shutdown_event = Event()

        # Start worker threads
        for i in range(num_workers):
            worker = threading.Thread(target=self._worker_loop)
            worker.daemon = True
            worker.start()
            self.workers.append(worker)

    def _worker_loop(self):
        """Worker thread main loop."""
        while not self.shutdown_event.is_set():
            try:
                task_func, args, task_id = self.task_queue.get(timeout=1)

                try:
                    result = task_func(*args)
                    self.result_queue.put(("success", task_id, result))
                except Exception as e:
                    self.result_queue.put(("error", task_id, str(e)))

                self.task_queue.task_done()

            except queue.Empty:
                continue

    def add_task(self, func, args, task_id):
        """Add task to processing queue."""
        self.task_queue.put((func, args, task_id))

    def get_results(self):
        """Get completed task results."""
        results = []
        while not self.result_queue.empty():
            results.append(self.result_queue.get())
        return results

    def shutdown(self):
        """Shutdown task manager."""
        self.shutdown_event.set()

# Usage
def email_task(recipient, subject):
    time.sleep(0.5)
    return f"Email sent to {recipient}"

task_manager = BackgroundTaskManager(num_workers=2)
task_manager.add_task(email_task, ("alice@example.com", "Welcome"), "email-1")
task_manager.add_task(email_task, ("bob@example.com", "Newsletter"), "email-2")

# Wait and get results
task_manager.task_queue.join()
results = task_manager.get_results()
task_manager.shutdown()
```

---

## Best Practices

### 1. Choose the Right Tool

```python
# I/O-bound tasks: Use ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(fetch_data, urls)

# CPU-bound tasks: Use ProcessPoolExecutor (not covered here)
from concurrent.futures import ProcessPoolExecutor

# Simple producer-consumer: Use queue.Queue
task_queue = queue.Queue()
```

### 2. Always Use Context Managers for Locks

```python
# Good: Automatic lock release
with lock:
    shared_resource += 1

# Avoid: Manual lock management
lock.acquire()
try:
    shared_resource += 1
finally:
    lock.release()
```

### 3. Handle Thread Exceptions Properly

```python
def safe_worker(task_func, *args):
    """Worker with proper exception handling."""
    try:
        return task_func(*args)
    except Exception as e:
        print(f"Task failed: {e}")
        return None

# Use in thread pool
with ThreadPoolExecutor() as executor:
    futures = [executor.submit(safe_worker, risky_task, arg) for arg in args]
    results = [f.result() for f in futures]
```

### 4. Use Daemon Threads for Background Tasks

```python
# Daemon threads don't prevent program exit
background_thread = threading.Thread(target=background_task)
background_thread.daemon = True
background_thread.start()
```

### 5. Avoid Deadlocks

```python
# Always acquire locks in same order
def transfer_money(from_account, to_account, amount):
    # Order locks by account ID to prevent deadlock
    first_lock = min(from_account.lock, to_account.lock, key=lambda x: id(x))
    second_lock = max(from_account.lock, to_account.lock, key=lambda x: id(x))

    with first_lock:
        with second_lock:
            from_account.balance -= amount
            to_account.balance += amount
```

### 6. Monitor Thread Performance

```python
import time
from threading import current_thread

def monitored_task(task_name):
    """Task with performance monitoring."""
    thread_name = current_thread().name
    start_time = time.time()

    print(f"[{thread_name}] Starting {task_name}")

    # Actual work here
    time.sleep(1)

    end_time = time.time()
    print(f"[{thread_name}] {task_name} completed in {end_time - start_time:.2f}s")
```

---

## Common Patterns Summary

| Pattern                  | Use Case                 | Example                             |
| ------------------------ | ------------------------ | ----------------------------------- |
| **Basic Threading**      | Simple concurrent tasks  | `threading.Thread(target=func)`     |
| **Lock Synchronization** | Protect shared resources | `with lock: shared_data += 1`       |
| **Producer-Consumer**    | Task processing pipeline | `queue.Queue()` with workers        |
| **Thread Pool**          | I/O-bound operations     | `ThreadPoolExecutor(max_workers=5)` |
| **Semaphore**            | Rate limiting            | `Semaphore(max_concurrent=3)`       |
| **Event Coordination**   | Thread communication     | `event.wait()`, `event.set()`       |

## When to Use Threading

### Good for Threading (I/O-bound):

- **Web scraping** and API calls
- **File operations** and database queries
- **Network requests** and downloads
- **User interface** responsiveness

### Not Good for Threading (CPU-bound):

- **Mathematical calculations**
- **Image/video processing**
- **Data analysis** computations
- Use **multiprocessing** instead for CPU-bound tasks

## Performance Tips

### 1. Choose Optimal Thread Count

```python
import os

# For I/O-bound tasks
optimal_threads = min(32, (os.cpu_count() or 1) + 4)

# For network requests
network_threads = min(50, len(urls))

with ThreadPoolExecutor(max_workers=optimal_threads) as executor:
    results = executor.map(io_bound_task, data)
```

### 2. Use Queue Sizes to Control Memory

```python
# Limit queue size to prevent memory issues
bounded_queue = queue.Queue(maxsize=100)

# Producer will block when queue is full
bounded_queue.put(item)  # Blocks if queue full
```

### 3. Batch Operations for Efficiency

```python
def process_batch(items, batch_size=10):
    """Process items in batches to reduce overhead."""
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        with ThreadPoolExecutor(max_workers=3) as executor:
            batch_results = list(executor.map(process_item, batch))
        yield batch_results
```

**Key Takeaway**: Threading is powerful for I/O-bound tasks and building responsive applications. Always use proper synchronization, handle exceptions gracefully, and choose the right concurrency pattern for your specific use case.
