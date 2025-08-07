# Python Async Programming - Essential Guide

## Table of Contents

1. [Basic Async/Await](#basic-asyncawait)
2. [Async HTTP Requests](#async-http-requests)
3. [Async Concurrency Patterns](#async-concurrency-patterns)
4. [Async Context Managers](#async-context-managers)
5. [Real-World Applications](#real-world-applications)
6. [Best Practices](#best-practices)

---

## Basic Async/Await

### Core Concepts

- **`async def`**: Defines an async function (coroutine)
- **`await`**: Pauses execution until awaitable completes
- **`asyncio.run()`**: Runs the main async function
- **`asyncio.gather()`**: Runs multiple coroutines concurrently

### Basic Async Function

```python
import asyncio
import time

async def async_task(name: str, delay: float) -> str:
    """Basic async task with delay."""
    print(f"Starting {name}")
    await asyncio.sleep(delay)  # Non-blocking sleep
    print(f"Completed {name}")
    return f"Result from {name}"

# Sequential execution
async def sequential_example():
    result1 = await async_task("Task-1", 1.0)
    result2 = await async_task("Task-2", 0.5)
    # Total time: ~1.5 seconds

# Concurrent execution
async def concurrent_example():
    results = await asyncio.gather(
        async_task("Task-1", 1.0),
        async_task("Task-2", 0.5),
        async_task("Task-3", 0.8)
    )
    # Total time: ~1.0 seconds (max of all delays)

# Run async code
asyncio.run(concurrent_example())
```

### Key Differences: Async vs Sync

```python
# Synchronous (blocking)
def sync_operation():
    time.sleep(1)  # Blocks entire thread
    return "Done"

# Asynchronous (non-blocking)
async def async_operation():
    await asyncio.sleep(1)  # Allows other tasks to run
    return "Done"
```

---

## Async HTTP Requests

### Basic HTTP Client

```python
import aiohttp
from typing import List, Dict, Any

async def fetch_url(session: aiohttp.ClientSession, url: str) -> Dict[str, Any]:
    """Fetch single URL asynchronously."""
    try:
        async with session.get(url) as response:
            content = await response.text()
            return {
                "url": url,
                "status": response.status,
                "content_length": len(content),
                "success": True
            }
    except Exception as e:
        return {"url": url, "error": str(e), "success": False}

async def fetch_multiple_urls(urls: List[str]) -> List[Dict[str, Any]]:
    """Fetch multiple URLs concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

# Usage
urls = ["http://site1.com", "http://site2.com", "http://site3.com"]
results = asyncio.run(fetch_multiple_urls(urls))
```

### Error Handling in Async HTTP

```python
async def safe_fetch(session: aiohttp.ClientSession, url: str, timeout: int = 5):
    """Fetch with proper error handling."""
    try:
        timeout_obj = aiohttp.ClientTimeout(total=timeout)
        async with session.get(url, timeout=timeout_obj) as response:
            if response.status == 200:
                return await response.json()
            else:
                return {"error": f"HTTP {response.status}"}
    except asyncio.TimeoutError:
        return {"error": "Request timeout"}
    except aiohttp.ClientError as e:
        return {"error": f"Client error: {e}"}
```

---

## Async Concurrency Patterns

### Producer-Consumer with Async Queue

```python
async def producer(name: str, queue: asyncio.Queue, num_items: int):
    """Produce items asynchronously."""
    for i in range(num_items):
        item = f"{name}-Item-{i+1}"
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.1)

async def consumer(name: str, queue: asyncio.Queue):
    """Consume items asynchronously."""
    while True:
        try:
            item = await asyncio.wait_for(queue.get(), timeout=2.0)
            print(f"Processing: {item}")
            await asyncio.sleep(0.2)  # Simulate processing
            queue.task_done()
        except asyncio.TimeoutError:
            break

async def producer_consumer_example():
    """Run producer-consumer pattern."""
    queue = asyncio.Queue(maxsize=5)

    # Start producer and consumers
    await asyncio.gather(
        producer("Producer-1", queue, 10),
        consumer("Consumer-1", queue),
        consumer("Consumer-2", queue),
    )
```

### Rate Limiting with Semaphores

```python
import asyncio

class AsyncRateLimiter:
    """Rate limiter for async operations."""

    def __init__(self, rate: int, per: float = 1.0):
        self.rate = rate
        self.per = per
        self.allowance = rate
        self.last_check = asyncio.get_event_loop().time()

    async def acquire(self):
        """Acquire rate limit permission."""
        now = asyncio.get_event_loop().time()
        time_passed = now - self.last_check
        self.last_check = now
        self.allowance += time_passed * (self.rate / self.per)

        if self.allowance > self.rate:
            self.allowance = self.rate

        if self.allowance < 1.0:
            sleep_time = (1.0 - self.allowance) * (self.per / self.rate)
            await asyncio.sleep(sleep_time)
            self.allowance = 0.0
        else:
            self.allowance -= 1.0

# Usage
rate_limiter = AsyncRateLimiter(rate=5, per=1.0)  # 5 requests per second

async def rate_limited_request(url: str):
    await rate_limiter.acquire()
    # Make your request here
    return f"Request to {url}"
```

### Task Groups (Python 3.11+)

```python
async def task_group_example():
    """Use task groups for structured concurrency."""
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(async_task("Task-1", 1.0))
        task2 = tg.create_task(async_task("Task-2", 0.5))
        task3 = tg.create_task(async_task("Task-3", 0.8))

    # All tasks completed successfully
    results = [task1.result(), task2.result(), task3.result()]
```

---

## Async Context Managers

### Creating Async Context Managers

```python
class AsyncDatabaseConnection:
    """Async database connection context manager."""

    def __init__(self, db_url: str):
        self.db_url = db_url
        self.connection = None

    async def __aenter__(self):
        print(f"Connecting to {self.db_url}")
        await asyncio.sleep(0.1)  # Simulate connection time
        self.connection = f"connection_to_{self.db_url}"
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"Disconnecting from {self.db_url}")
        await asyncio.sleep(0.1)  # Simulate cleanup
        self.connection = None

    async def query(self, sql: str):
        """Execute async query."""
        if not self.connection:
            raise RuntimeError("Not connected")

        await asyncio.sleep(0.2)  # Simulate query time
        return f"Results for: {sql}"

# Usage
async def database_example():
    async with AsyncDatabaseConnection("postgresql://localhost") as db:
        result1 = await db.query("SELECT * FROM users")
        result2 = await db.query("SELECT * FROM orders")
        return [result1, result2]
```

### Async File Operations

```python
import aiofiles

async def async_file_operations():
    """Demonstrate async file operations."""

    # Writing files asynchronously
    async with aiofiles.open('data.txt', 'w') as f:
        await f.write("Hello, async world!")
        await f.write("\nSecond line")

    # Reading files asynchronously
    async with aiofiles.open('data.txt', 'r') as f:
        content = await f.read()
        return content

# Process multiple files concurrently
async def process_files(filenames: List[str]):
    """Process multiple files concurrently."""

    async def read_file(filename: str):
        async with aiofiles.open(filename, 'r') as f:
            content = await f.read()
            return {"filename": filename, "size": len(content)}

    return await asyncio.gather(*[read_file(f) for f in filenames])
```

---

## Real-World Applications

### API Data Aggregator

```python
class AsyncAPIAggregator:
    """Aggregate data from multiple APIs efficiently."""

    def __init__(self, base_timeout: int = 10):
        self.session = None
        self.timeout = aiohttp.ClientTimeout(total=base_timeout)

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(timeout=self.timeout)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def fetch_user_data(self, user_id: int):
        """Fetch user profile data."""
        await asyncio.sleep(0.3)  # Simulate API call
        return {"user_id": user_id, "name": f"User-{user_id}"}

    async def fetch_user_orders(self, user_id: int):
        """Fetch user order history."""
        await asyncio.sleep(0.4)  # Simulate API call
        return [{"order_id": f"ORD-{user_id}-001", "amount": 99.99}]

    async def aggregate_user_data(self, user_id: int):
        """Fetch all user data concurrently."""
        user_data, orders, preferences = await asyncio.gather(
            self.fetch_user_data(user_id),
            self.fetch_user_orders(user_id),
            self.fetch_user_preferences(user_id),
            return_exceptions=True
        )

        return {
            "user": user_data if not isinstance(user_data, Exception) else None,
            "orders": orders if not isinstance(orders, Exception) else [],
            "preferences": preferences if not isinstance(preferences, Exception) else {}
        }

    async def fetch_user_preferences(self, user_id: int):
        """Fetch user preferences."""
        await asyncio.sleep(0.2)  # Simulate API call
        return {"theme": "dark", "notifications": True}

# Usage
async def api_aggregation_example():
    async with AsyncAPIAggregator() as aggregator:
        user_ids = [101, 102, 103, 104]
        results = await asyncio.gather(
            *[aggregator.aggregate_user_data(uid) for uid in user_ids]
        )
        return results
```

### Background Task Processor

```python
class AsyncTaskProcessor:
    """Process background tasks asynchronously."""

    def __init__(self, max_workers: int = 5):
        self.max_workers = max_workers
        self.semaphore = asyncio.Semaphore(max_workers)
        self.tasks = []

    async def add_task(self, coro):
        """Add coroutine to task queue."""
        async with self.semaphore:
            task = asyncio.create_task(coro)
            self.tasks.append(task)
            return task

    async def process_all_tasks(self):
        """Process all queued tasks."""
        if not self.tasks:
            return []

        results = await asyncio.gather(*self.tasks, return_exceptions=True)
        self.tasks.clear()
        return results

# Task functions
async def send_email(recipient: str, subject: str):
    """Simulate sending email."""
    await asyncio.sleep(0.5)
    return f"Email sent to {recipient}: {subject}"

async def generate_report(report_type: str):
    """Simulate generating report."""
    await asyncio.sleep(1.0)
    return f"{report_type} report generated"

async def backup_database(db_name: str):
    """Simulate database backup."""
    await asyncio.sleep(2.0)
    return f"Backup of {db_name} completed"

# Usage example
async def background_tasks_example():
    processor = AsyncTaskProcessor(max_workers=3)

    # Add various background tasks
    await processor.add_task(send_email("alice@example.com", "Welcome"))
    await processor.add_task(generate_report("Daily Sales"))
    await processor.add_task(backup_database("user_db"))
    await processor.add_task(send_email("bob@example.com", "Newsletter"))

    # Process all tasks concurrently
    results = await processor.process_all_tasks()
    return results
```

### Async Web Scraper

```python
class AsyncWebScraper:
    """High-performance web scraper with rate limiting."""

    def __init__(self, requests_per_second: int = 10):
        self.rate_limiter = AsyncRateLimiter(requests_per_second)
        self.session = None
        self.results = []

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def scrape_url(self, url: str) -> Dict[str, Any]:
        """Scrape single URL with rate limiting."""
        await self.rate_limiter.acquire()

        try:
            async with self.session.get(url) as response:
                if response.status == 200:
                    content = await response.text()
                    return {
                        "url": url,
                        "status": response.status,
                        "title": self._extract_title(content),
                        "word_count": len(content.split()),
                        "success": True
                    }
                else:
                    return {"url": url, "status": response.status, "success": False}
        except Exception as e:
            return {"url": url, "error": str(e), "success": False}

    def _extract_title(self, html: str) -> str:
        """Extract title from HTML (simplified)."""
        import re
        match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
        return match.group(1) if match else "No title"

    async def scrape_multiple_urls(self, urls: List[str]) -> List[Dict[str, Any]]:
        """Scrape multiple URLs concurrently."""
        semaphore = asyncio.Semaphore(20)  # Limit concurrent requests

        async def bounded_scrape(url):
            async with semaphore:
                return await self.scrape_url(url)

        results = await asyncio.gather(
            *[bounded_scrape(url) for url in urls],
            return_exceptions=True
        )

        return [r for r in results if not isinstance(r, Exception)]

# Usage
async def web_scraping_example():
    urls = [f"https://example{i}.com" for i in range(1, 21)]

    async with AsyncWebScraper(requests_per_second=5) as scraper:
        results = await scraper.scrape_multiple_urls(urls)

        successful = [r for r in results if r.get("success")]
        failed = [r for r in results if not r.get("success")]

        return {
            "successful": len(successful),
            "failed": len(failed),
            "total_words": sum(r.get("word_count", 0) for r in successful)
        }
```

---

## Best Practices

### 1. Use Session Objects for HTTP

```python
# Good: Reuse session
async with aiohttp.ClientSession() as session:
    for url in urls:
        async with session.get(url) as response:
            data = await response.text()

# Avoid: Creating session for each request
for url in urls:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
```

### 2. Handle Exceptions Properly

```python
async def safe_async_operation():
    """Always handle exceptions in async code."""
    try:
        result = await risky_async_operation()
        return result
    except asyncio.TimeoutError:
        return {"error": "Operation timed out"}
    except Exception as e:
        return {"error": f"Operation failed: {e}"}

# Use gather with return_exceptions
results = await asyncio.gather(
    async_operation1(),
    async_operation2(),
    return_exceptions=True
)

# Process results and exceptions
for result in results:
    if isinstance(result, Exception):
        print(f"Task failed: {result}")
    else:
        print(f"Task succeeded: {result}")
```

### 3. Use Timeouts

```python
async def operation_with_timeout():
    """Always set timeouts for async operations."""
    try:
        result = await asyncio.wait_for(
            slow_async_operation(),
            timeout=5.0
        )
        return result
    except asyncio.TimeoutError:
        return "Operation timed out"

# HTTP client timeouts
timeout = aiohttp.ClientTimeout(total=10, connect=5)
async with aiohttp.ClientSession(timeout=timeout) as session:
    async with session.get(url) as response:
        return await response.text()
```

### 4. Limit Concurrent Operations

```python
async def limited_concurrent_operations(operations, max_concurrent=10):
    """Limit number of concurrent operations."""
    semaphore = asyncio.Semaphore(max_concurrent)

    async def bounded_operation(op):
        async with semaphore:
            return await op

    return await asyncio.gather(
        *[bounded_operation(op) for op in operations]
    )
```

### 5. Use Async Context Managers

```python
class AsyncResource:
    """Proper async resource management."""

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.cleanup()

    async def connect(self):
        # Setup code
        pass

    async def cleanup(self):
        # Cleanup code
        pass

# Usage
async with AsyncResource() as resource:
    await resource.do_work()
```

---

## Performance Comparison

### Async vs Sync I/O

```python
import time

# Synchronous version (blocking)
def sync_io_operations(urls):
    results = []
    start_time = time.time()

    for url in urls:
        time.sleep(0.5)  # Simulate I/O delay
        results.append(f"Result from {url}")

    return results, time.time() - start_time

# Asynchronous version (non-blocking)
async def async_io_operations(urls):
    start_time = time.time()

    async def fetch_url(url):
        await asyncio.sleep(0.5)  # Simulate I/O delay
        return f"Result from {url}"

    results = await asyncio.gather(*[fetch_url(url) for url in urls])
    return results, time.time() - start_time

# Performance comparison
urls = [f"https://site{i}.com" for i in range(5)]

# Sync: ~2.5 seconds (5 * 0.5)
sync_results, sync_time = sync_io_operations(urls)

# Async: ~0.5 seconds (concurrent execution)
async_results, async_time = asyncio.run(async_io_operations(urls))

print(f"Sync time: {sync_time:.2f}s")
print(f"Async time: {async_time:.2f}s")
print(f"Speedup: {sync_time/async_time:.2f}x")
```

## When to Use Async

### Good for Async:

- **I/O-bound operations** (file/network/database)
- **Web scraping** and API calls
- **Concurrent downloads/uploads**
- **Chat applications** and real-time systems
- **Microservices** with many external calls

### Not Good for Async:

- **CPU-intensive tasks** (calculations, image processing)
- **Simple scripts** with minimal I/O
- **Legacy codebases** without async support
- **Operations requiring shared state** (use threading/multiprocessing)

## Common Patterns Summary

| Pattern                   | Use Case                             | Example                                   |
| ------------------------- | ------------------------------------ | ----------------------------------------- |
| **asyncio.gather()**      | Run multiple coroutines concurrently | `await asyncio.gather(*tasks)`            |
| **asyncio.create_task()** | Schedule coroutine for execution     | `task = asyncio.create_task(coro)`        |
| **async with**            | Resource management                  | `async with session.get(url) as resp:`    |
| **asyncio.Queue**         | Producer-consumer pattern            | `queue = asyncio.Queue(maxsize=10)`       |
| **Semaphore**             | Limit concurrent operations          | `async with semaphore:`                   |
| **asyncio.wait_for()**    | Add timeout to operations            | `await asyncio.wait_for(coro, timeout=5)` |

**Key Takeaway**: Async programming excels at I/O-bound operations by allowing concurrent execution without the overhead of threads. Use it for network requests, file operations, and building responsive applications that handle many simultaneous operations.
