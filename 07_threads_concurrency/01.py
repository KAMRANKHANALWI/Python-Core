# Python Threading & Concurrency - Essential Examples
"""
Concise, high-value examples of Python threading and concurrency.
Focus on practical patterns for real applications.
"""

import threading
import time
import queue
import concurrent.futures
from threading import Lock, RLock, Semaphore, Event
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

print("Python Threading & Concurrency - Essential Patterns")
print("=" * 60)

# ===== BASIC THREADING =====
print("\n1. BASIC THREADING")
print("-" * 40)


# Simple thread creation
def worker_task(name, duration):
    """Simple worker task."""
    print(f"🔧 Worker {name} starting...")
    time.sleep(duration)
    print(f"✅ Worker {name} completed!")
    return f"Result from {name}"


# Method 1: Using Thread class
print("Creating threads manually:")
thread1 = threading.Thread(target=worker_task, args=("Thread-1", 2))
thread2 = threading.Thread(target=worker_task, args=("Thread-2", 1))

start_time = time.time()
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()
end_time = time.time()

print(f"⏱️ Total time: {end_time - start_time:.2f} seconds")


# Method 2: Using threading function
def run_concurrent_tasks():
    """Run multiple tasks concurrently."""
    tasks = [("Task-A", 1.5), ("Task-B", 1.0), ("Task-C", 2.0)]

    threads = []
    start_time = time.time()

    for name, duration in tasks:
        thread = threading.Thread(target=worker_task, args=(name, duration))
        thread.start()
        threads.append(thread)

    # Wait for all threads
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"🚀 All tasks completed in {end_time - start_time:.2f} seconds")


print(f"\n📋 Running concurrent tasks:")
run_concurrent_tasks()

# ===== THREAD SYNCHRONIZATION =====
print("\n2. THREAD SYNCHRONIZATION")
print("-" * 40)

# Shared resource without protection (dangerous!)
counter_unsafe = 0


def unsafe_increment():
    """Unsafe counter increment."""
    global counter_unsafe
    for _ in range(100000):
        counter_unsafe += 1


# Demonstrate race condition
print("🚨 Race condition example:")
counter_unsafe = 0
threads = [threading.Thread(target=unsafe_increment) for _ in range(2)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(f"Unsafe counter result: {counter_unsafe} (should be 200000)")

# Thread-safe counter with Lock
counter_safe = 0
counter_lock = Lock()


def safe_increment():
    """Thread-safe counter increment."""
    global counter_safe
    for _ in range(100000):
        with counter_lock:  # Acquire lock automatically
            counter_safe += 1


print(f"\n🔒 Thread-safe example:")
counter_safe = 0
threads = [threading.Thread(target=safe_increment) for _ in range(2)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(f"Safe counter result: {counter_safe}")

# ===== PRODUCER-CONSUMER PATTERN =====
print("\n3. PRODUCER-CONSUMER PATTERN")
print("-" * 40)

# Thread-safe queue for producer-consumer
task_queue = queue.Queue(maxsize=5)
results_queue = queue.Queue()


def producer(name, num_items):
    """Produce items and put them in queue."""
    for i in range(num_items):
        item = f"{name}-Item-{i+1}"
        task_queue.put(item)
        print(f"📦 Producer {name}: Added {item}")
        time.sleep(0.1)

    print(f"✅ Producer {name}: Finished")


def consumer(name):
    """Consume items from queue."""
    while True:
        try:
            # Wait for item with timeout
            item = task_queue.get(timeout=2)
            print(f"🔧 Consumer {name}: Processing {item}")

            # Simulate processing time
            time.sleep(0.2)

            # Mark task as done
            task_queue.task_done()
            results_queue.put(f"Processed-{item}")

        except queue.Empty:
            print(f"🛑 Consumer {name}: No more items, stopping")
            break


print("📋 Producer-Consumer Example:")

# Start producer and consumer threads
producer_thread = threading.Thread(target=producer, args=("Producer-1", 5))
consumer_thread1 = threading.Thread(target=consumer, args=("Consumer-1",))
consumer_thread2 = threading.Thread(target=consumer, args=("Consumer-2",))

producer_thread.start()
consumer_thread1.start()
consumer_thread2.start()

# Wait for producer to finish
producer_thread.join()

# Wait for all tasks to be processed
task_queue.join()

print(f"📊 Results collected: {results_queue.qsize()} items")

# ===== THREAD POOL EXECUTOR =====
print("\n4. THREAD POOL EXECUTOR")
print("-" * 40)


def download_simulation(url, delay):
    """Simulate downloading from URL."""
    print(f"🌐 Downloading from {url}...")
    time.sleep(delay)  # Simulate network delay
    return f"Content from {url} (took {delay}s)"


# Sequential execution (slow)
print("📥 Sequential downloads:")
start_time = time.time()
urls = [("site1.com", 1), ("site2.com", 1.5), ("site3.com", 0.8), ("site4.com", 1.2)]

sequential_results = []
for url, delay in urls:
    result = download_simulation(url, delay)
    sequential_results.append(result)

sequential_time = time.time() - start_time
print(f"⏱️ Sequential time: {sequential_time:.2f} seconds")

# Concurrent execution with ThreadPoolExecutor
print(f"\n🚀 Concurrent downloads:")
start_time = time.time()

with ThreadPoolExecutor(max_workers=4) as executor:
    # Submit all tasks
    future_to_url = {
        executor.submit(download_simulation, url, delay): url for url, delay in urls
    }

    concurrent_results = []
    for future in as_completed(future_to_url):
        url = future_to_url[future]
        try:
            result = future.result()
            concurrent_results.append(result)
            print(f"✅ Completed: {url}")
        except Exception as exc:
            print(f"❌ {url} generated exception: {exc}")

concurrent_time = time.time() - start_time
print(f"⏱️ Concurrent time: {concurrent_time:.2f} seconds")
print(f"🚀 Speedup: {sequential_time/concurrent_time:.2f}x faster")

# ===== REAL-WORLD EXAMPLES =====
print("\n5. REAL-WORLD APPLICATIONS")
print("-" * 50)


# Example 1: Web Scraping with Threading
def fetch_url_info(url):
    """Simulate fetching information from URL."""
    try:
        print(f"🌐 Fetching {url}...")
        # Simulate HTTP request delay
        time.sleep(1)

        # Simulate response
        status_code = 200
        content_length = len(url) * 100  # Mock content length

        return {
            "url": url,
            "status": status_code,
            "content_length": content_length,
            "success": True,
        }
    except Exception as e:
        return {"url": url, "error": str(e), "success": False}


def web_scraping_example():
    """Demonstrate concurrent web scraping."""
    urls = [
        "https://example1.com/api/data",
        "https://example2.com/products",
        "https://example3.com/users",
        "https://example4.com/orders",
        "https://example5.com/analytics",
    ]

    print("🕷️ Web Scraping Example:")
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(fetch_url_info, urls))

    end_time = time.time()

    # Process results
    successful = [r for r in results if r["success"]]
    failed = [r for r in results if not r["success"]]

    print(f"✅ Successfully fetched: {len(successful)} URLs")
    print(f"❌ Failed: {len(failed)} URLs")
    print(f"⏱️ Total time: {end_time - start_time:.2f} seconds")

    for result in successful:
        print(f"   📊 {result['url']}: {result['content_length']} bytes")


web_scraping_example()


# Example 2: File Processing with Threading
def process_file(filename):
    """Simulate file processing."""
    print(f"📄 Processing {filename}...")

    # Simulate different processing times
    processing_time = len(filename) * 0.1
    time.sleep(processing_time)

    # Simulate processing results
    lines_processed = len(filename) * 10
    errors_found = len(filename) % 3

    return {
        "filename": filename,
        "lines_processed": lines_processed,
        "errors_found": errors_found,
        "processing_time": processing_time,
    }


def batch_file_processing():
    """Process multiple files concurrently."""
    files = [
        "data_2024_01.csv",
        "user_logs.txt",
        "sales_report.json",
        "inventory_backup.xml",
        "customer_feedback.csv",
    ]

    print(f"\n📁 Batch File Processing:")

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(process_file, files))

    # Generate summary report
    total_lines = sum(r["lines_processed"] for r in results)
    total_errors = sum(r["errors_found"] for r in results)
    total_time = max(r["processing_time"] for r in results)

    print(f"📊 Processing Summary:")
    print(f"   Total lines processed: {total_lines}")
    print(f"   Total errors found: {total_errors}")
    print(f"   Total processing time: {total_time:.2f} seconds")


batch_file_processing()


# Example 3: API Rate-Limited Requests
class RateLimitedAPI:
    """Simulate API with rate limiting."""

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

            print(f"🌐 API Request #{request_id} to {endpoint}")
            time.sleep(0.5)  # Simulate API call

            return {
                "request_id": request_id,
                "endpoint": endpoint,
                "data": f"Response data from {endpoint}",
                "timestamp": time.time(),
            }


def api_testing_example():
    """Test API with concurrent requests and rate limiting."""
    api = RateLimitedAPI(requests_per_second=3)

    endpoints = [
        "/users",
        "/products",
        "/orders",
        "/analytics",
        "/reports",
        "/settings",
        "/notifications",
    ]

    print(f"\n🔌 Rate-Limited API Testing:")
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(api.make_request, endpoints))

    end_time = time.time()

    print(f"📊 API Test Results:")
    print(f"   Total requests: {len(results)}")
    print(f"   Total time: {end_time - start_time:.2f} seconds")
    print(f"   Average time per request: {(end_time - start_time)/len(results):.2f}s")


api_testing_example()


# Example 4: Background Task Manager
class BackgroundTaskManager:
    """Manage background tasks with threading."""

    def __init__(self):
        self.tasks = queue.Queue()
        self.results = queue.Queue()
        self.workers = []
        self.shutdown_event = Event()

    def start_workers(self, num_workers=3):
        """Start worker threads."""
        for i in range(num_workers):
            worker = threading.Thread(target=self._worker_loop, args=(f"Worker-{i+1}",))
            worker.daemon = True
            worker.start()
            self.workers.append(worker)
        print(f"🔧 Started {num_workers} background workers")

    def _worker_loop(self, worker_name):
        """Worker thread main loop."""
        while not self.shutdown_event.is_set():
            try:
                task_func, args, task_id = self.tasks.get(timeout=1)
                print(f"⚙️ {worker_name}: Processing task {task_id}")

                try:
                    result = task_func(*args)
                    self.results.put(("success", task_id, result))
                except Exception as e:
                    self.results.put(("error", task_id, str(e)))

                self.tasks.task_done()

            except queue.Empty:
                continue

    def add_task(self, func, args, task_id):
        """Add task to queue."""
        self.tasks.put((func, args, task_id))
        print(f"📋 Added task {task_id} to queue")

    def get_results(self):
        """Get completed task results."""
        results = []
        while not self.results.empty():
            results.append(self.results.get())
        return results

    def shutdown(self):
        """Shutdown task manager."""
        self.shutdown_event.set()
        print("🛑 Shutting down task manager...")


def background_task_example():
    """Demonstrate background task management."""

    def data_processing_task(data_size, complexity):
        """Simulate data processing."""
        processing_time = data_size * complexity * 0.1
        time.sleep(processing_time)
        return f"Processed {data_size} items with complexity {complexity}"

    def email_task(recipient, subject):
        """Simulate sending email."""
        time.sleep(0.5)
        return f"Email sent to {recipient}: '{subject}'"

    print(f"\n📋 Background Task Manager:")

    # Create and start task manager
    task_manager = BackgroundTaskManager()
    task_manager.start_workers(3)

    # Add various tasks
    tasks = [
        (data_processing_task, (1000, 2), "data-proc-1"),
        (email_task, ("alice@example.com", "Welcome!"), "email-1"),
        (data_processing_task, (500, 3), "data-proc-2"),
        (email_task, ("bob@example.com", "Newsletter"), "email-2"),
        (data_processing_task, (750, 1), "data-proc-3"),
    ]

    for func, args, task_id in tasks:
        task_manager.add_task(func, args, task_id)

    # Wait for tasks to complete
    print("⏳ Waiting for tasks to complete...")
    task_manager.tasks.join()

    # Get results
    results = task_manager.get_results()
    print(f"📊 Task Results:")
    for status, task_id, result in results:
        if status == "success":
            print(f"   ✅ {task_id}: {result}")
        else:
            print(f"   ❌ {task_id}: {result}")

    # Shutdown
    task_manager.shutdown()


background_task_example()

# ===== ADVANCED PATTERNS =====
print("\n6. ADVANCED THREADING PATTERNS")
print("-" * 40)


# Context manager for thread synchronization
class ThreadSafeResource:
    """Thread-safe resource with context manager."""

    def __init__(self, name):
        self.name = name
        self.lock = RLock()  # Reentrant lock
        self.data = []

    def __enter__(self):
        print(f"🔒 Acquiring lock for {self.name}")
        self.lock.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"🔓 Releasing lock for {self.name}")
        self.lock.release()

    def add_data(self, item):
        """Add data (must be called within context manager)."""
        self.data.append(item)
        print(f"📝 Added '{item}' to {self.name}")

    def get_summary(self):
        """Get data summary."""
        return f"{self.name}: {len(self.data)} items"


def thread_safe_resource_example():
    """Demonstrate thread-safe resource usage."""
    resource = ThreadSafeResource("SharedDatabase")

    def worker_with_resource(worker_id, items):
        """Worker that uses shared resource."""
        with resource:
            for item in items:
                resource.add_data(f"{worker_id}-{item}")
                time.sleep(0.1)

    print(f"\n🛡️ Thread-Safe Resource Example:")

    # Create workers that access shared resource
    workers = [
        threading.Thread(
            target=worker_with_resource, args=("Worker-1", ["A", "B", "C"])
        ),
        threading.Thread(
            target=worker_with_resource, args=("Worker-2", ["X", "Y", "Z"])
        ),
        threading.Thread(
            target=worker_with_resource, args=("Worker-3", ["1", "2", "3"])
        ),
    ]

    for worker in workers:
        worker.start()

    for worker in workers:
        worker.join()

    print(f"📊 Final result: {resource.get_summary()}")


thread_safe_resource_example()

print("\n" + "=" * 60)
print("✅ Essential threading patterns demonstrated!")
print("💡 Focus: Real-world concurrency for scalable applications")
