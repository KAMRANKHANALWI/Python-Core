# Python Async Programming - Essential Examples
"""
Concise, high-value examples of Python async/await programming.
Focus on practical patterns for real applications with asyncio.
"""

import asyncio
import aiohttp
import aiofiles
import time
from aiohttp import ClientSession
from typing import List, Dict, Any

print("Python Async Programming - Essential Patterns")
print("=" * 60)

# ===== BASIC ASYNC/AWAIT =====
print("\n1. BASIC ASYNC/AWAIT")
print("-" * 40)


# Basic async function
async def simple_async_task(name: str, delay: float) -> str:
    """Simple async task with delay."""
    print(f"🔧 {name} starting...")
    await asyncio.sleep(delay)  # Non-blocking sleep
    print(f"✅ {name} completed!")
    return f"Result from {name}"


# Running async functions
async def run_basic_example():
    """Demonstrate basic async execution."""
    print("Sequential async execution:")
    start_time = time.time()

    result1 = await simple_async_task("Task-1", 1.0)
    result2 = await simple_async_task("Task-2", 0.5)

    sequential_time = time.time() - start_time
    print(f"⏱️ Sequential time: {sequential_time:.2f} seconds")

    print(f"\nConcurrent async execution:")
    start_time = time.time()

    # Run tasks concurrently
    results = await asyncio.gather(
        simple_async_task("Async-1", 1.0),
        simple_async_task("Async-2", 0.5),
        simple_async_task("Async-3", 0.8),
    )

    concurrent_time = time.time() - start_time
    print(f"⏱️ Concurrent time: {concurrent_time:.2f} seconds")
    print(f"🚀 Speedup: {sequential_time/concurrent_time:.2f}x faster")


# Run the example
asyncio.run(run_basic_example())

# ===== ASYNC HTTP REQUESTS =====
print("\n2. ASYNC HTTP REQUESTS")
print("-" * 40)


async def fetch_url(session: ClientSession, url: str) -> Dict[str, Any]:
    """Fetch data from URL asynchronously."""
    try:
        print(f"🌐 Fetching {url}...")
        async with session.get(url) as response:
            # Simulate different response times
            await asyncio.sleep(0.5)  # Mock network delay

            return {
                "url": url,
                "status": 200,  # Mock status
                "content_length": len(url) * 100,  # Mock content length
                "success": True,
            }
    except Exception as e:
        return {"url": url, "error": str(e), "success": False}


async def fetch_multiple_urls(urls: List[str]) -> List[Dict[str, Any]]:
    """Fetch multiple URLs concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Process results and exceptions
        processed_results = []
        for result in results:
            if isinstance(result, Exception):
                processed_results.append({"error": str(result), "success": False})
            else:
                processed_results.append(result)

        return processed_results


async def web_scraping_example():
    """Demonstrate concurrent web scraping."""
    urls = [
        "https://api.example1.com/data",
        "https://api.example2.com/users",
        "https://api.example3.com/products",
        "https://api.example4.com/orders",
        "https://api.example5.com/analytics",
    ]

    print("🕷️ Async Web Scraping Example:")
    start_time = time.time()

    results = await fetch_multiple_urls(urls)

    end_time = time.time()

    # Analyze results
    successful = [r for r in results if r.get("success", False)]
    failed = [r for r in results if not r.get("success", True)]

    print(f"✅ Successfully fetched: {len(successful)} URLs")
    print(f"❌ Failed: {len(failed)} URLs")
    print(f"⏱️ Total time: {end_time - start_time:.2f} seconds")

    for result in successful:
        print(f"   📊 {result['url']}: {result['content_length']} bytes")


asyncio.run(web_scraping_example())

# ===== ASYNC FILE OPERATIONS =====
print("\n3. ASYNC FILE OPERATIONS")
print("-" * 40)


async def process_file_async(filename: str, content: str) -> Dict[str, Any]:
    """Process file asynchronously."""
    try:
        print(f"📄 Processing {filename}...")

        # Simulate file writing
        await asyncio.sleep(0.2)  # Mock file I/O delay

        # Mock file processing
        word_count = len(content.split())
        char_count = len(content)

        return {
            "filename": filename,
            "word_count": word_count,
            "char_count": char_count,
            "status": "processed",
        }

    except Exception as e:
        return {"filename": filename, "error": str(e), "status": "failed"}


async def batch_file_processing():
    """Process multiple files concurrently."""
    files_data = [
        (
            "report_2024.txt",
            "This is a sample report with multiple words for analysis.",
        ),
        ("user_data.json", "{'users': ['alice', 'bob', 'charlie'], 'count': 3}"),
        ("config.yaml", "database: localhost\nport: 5432\ndebug: true"),
        (
            "logs.txt",
            "INFO: Application started\nERROR: Connection failed\nWARN: Retry attempt",
        ),
        (
            "readme.md",
            "# Project Title\nThis is the project documentation with examples.",
        ),
    ]

    print("📁 Async Batch File Processing:")

    tasks = [process_file_async(filename, content) for filename, content in files_data]

    results = await asyncio.gather(*tasks)

    # Generate summary
    successful = [r for r in results if r["status"] == "processed"]
    total_words = sum(r["word_count"] for r in successful)
    total_chars = sum(r["char_count"] for r in successful)

    print(f"📊 Processing Summary:")
    print(f"   Files processed: {len(successful)}")
    print(f"   Total words: {total_words}")
    print(f"   Total characters: {total_chars}")

    for result in successful:
        print(f"   📄 {result['filename']}: {result['word_count']} words")


asyncio.run(batch_file_processing())

# ===== ASYNC PRODUCERS AND CONSUMERS =====
print("\n4. ASYNC PRODUCERS AND CONSUMERS")
print("-" * 40)


async def producer(name: str, queue: asyncio.Queue, num_items: int):
    """Produce items asynchronously."""
    for i in range(num_items):
        item = f"{name}-Item-{i+1}"
        await queue.put(item)
        print(f"📦 Producer {name}: Added {item}")
        await asyncio.sleep(0.1)  # Simulate production time

    print(f"✅ Producer {name}: Finished producing {num_items} items")


async def consumer(name: str, queue: asyncio.Queue):
    """Consume items asynchronously."""
    processed_items = []

    while True:
        try:
            # Wait for item with timeout
            item = await asyncio.wait_for(queue.get(), timeout=2.0)
            print(f"🔧 Consumer {name}: Processing {item}")

            # Simulate processing time
            await asyncio.sleep(0.2)

            processed_items.append(item)
            queue.task_done()

        except asyncio.TimeoutError:
            print(f"🛑 Consumer {name}: No more items, stopping")
            break

    return processed_items


async def producer_consumer_example():
    """Demonstrate async producer-consumer pattern."""
    print("📋 Async Producer-Consumer Example:")

    # Create queue
    queue = asyncio.Queue(maxsize=5)

    # Create tasks
    producer_task = asyncio.create_task(producer("Producer-1", queue, 8))
    consumer1_task = asyncio.create_task(consumer("Consumer-1", queue))
    consumer2_task = asyncio.create_task(consumer("Consumer-2", queue))

    # Wait for producer to finish
    await producer_task

    # Wait for queue to be empty
    await queue.join()

    # Get consumer results
    results1 = await consumer1_task
    results2 = await consumer2_task

    print(
        f"📊 Results: Consumer-1 processed {len(results1)} items, Consumer-2 processed {len(results2)} items"
    )


asyncio.run(producer_consumer_example())

# ===== ASYNC CONTEXT MANAGERS =====
print("\n5. ASYNC CONTEXT MANAGERS")
print("-" * 40)


class AsyncDatabaseConnection:
    """Mock async database connection context manager."""

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connected = False

    async def __aenter__(self):
        print(f"🔌 Connecting to database: {self.db_name}")
        await asyncio.sleep(0.1)  # Simulate connection time
        self.connected = True
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"🔌 Disconnecting from database: {self.db_name}")
        await asyncio.sleep(0.1)  # Simulate disconnection time
        self.connected = False

    async def query(self, sql: str) -> List[Dict[str, Any]]:
        """Execute query asynchronously."""
        if not self.connected:
            raise RuntimeError("Database not connected")

        print(f"📊 Executing query: {sql}")
        await asyncio.sleep(0.2)  # Simulate query time

        # Mock query results
        return [
            {"id": 1, "name": "Alice", "age": 25},
            {"id": 2, "name": "Bob", "age": 30},
        ]


async def async_context_manager_example():
    """Demonstrate async context managers."""
    print("🗄️ Async Context Manager Example:")

    async with AsyncDatabaseConnection("user_database") as db:
        users = await db.query("SELECT * FROM users")
        print(f"📊 Query result: {len(users)} users found")

        orders = await db.query("SELECT * FROM orders")
        print(f"📊 Query result: {len(orders)} orders found")


asyncio.run(async_context_manager_example())

# ===== REAL-WORLD APPLICATIONS =====
print("\n6. REAL-WORLD APPLICATIONS")
print("-" * 50)


# Example 1: API Data Aggregator
class AsyncAPIAggregator:
    """Aggregate data from multiple APIs asynchronously."""

    def __init__(self):
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def fetch_user_data(self, user_id: int) -> Dict[str, Any]:
        """Fetch user data from API."""
        await asyncio.sleep(0.3)  # Simulate API call
        return {
            "user_id": user_id,
            "name": f"User-{user_id}",
            "email": f"user{user_id}@example.com",
        }

    async def fetch_user_orders(self, user_id: int) -> List[Dict[str, Any]]:
        """Fetch user orders from API."""
        await asyncio.sleep(0.4)  # Simulate API call
        return [
            {"order_id": f"ORD-{user_id}-001", "amount": 99.99},
            {"order_id": f"ORD-{user_id}-002", "amount": 149.50},
        ]

    async def fetch_user_preferences(self, user_id: int) -> Dict[str, Any]:
        """Fetch user preferences from API."""
        await asyncio.sleep(0.2)  # Simulate API call
        return {"theme": "dark", "notifications": True, "language": "en"}

    async def aggregate_user_data(self, user_id: int) -> Dict[str, Any]:
        """Aggregate all user data concurrently."""
        print(f"👤 Aggregating data for User-{user_id}")

        # Fetch all data concurrently
        user_data, orders, preferences = await asyncio.gather(
            self.fetch_user_data(user_id),
            self.fetch_user_orders(user_id),
            self.fetch_user_preferences(user_id),
        )

        return {
            "user": user_data,
            "orders": orders,
            "preferences": preferences,
            "total_order_value": sum(order["amount"] for order in orders),
        }


async def api_aggregator_example():
    """Demonstrate API data aggregation."""
    print("🔄 API Data Aggregator Example:")

    async with AsyncAPIAggregator() as aggregator:
        user_ids = [101, 102, 103, 104]

        # Aggregate data for multiple users concurrently
        start_time = time.time()
        results = await asyncio.gather(
            *[aggregator.aggregate_user_data(user_id) for user_id in user_ids]
        )
        end_time = time.time()

        print(f"📊 Aggregation Results:")
        for result in results:
            user = result["user"]
            total_value = result["total_order_value"]
            print(
                f"   👤 {user['name']}: {len(result['orders'])} orders, ${total_value:.2f} total"
            )

        print(f"⏱️ Total aggregation time: {end_time - start_time:.2f} seconds")


asyncio.run(api_aggregator_example())


# Example 2: Async Task Scheduler
class AsyncTaskScheduler:
    """Schedule and execute tasks asynchronously."""

    def __init__(self):
        self.tasks = []
        self.running = False

    def schedule_task(self, coro, delay: float):
        """Schedule a coroutine to run after delay."""
        self.tasks.append((coro, delay))

    async def run_scheduled_tasks(self):
        """Run all scheduled tasks concurrently."""
        self.running = True

        async def delayed_task(coro, delay):
            await asyncio.sleep(delay)
            return await coro

        # Create delayed tasks
        delayed_tasks = [delayed_task(coro, delay) for coro, delay in self.tasks]

        # Run all tasks concurrently
        results = await asyncio.gather(*delayed_tasks, return_exceptions=True)

        self.running = False
        return results


async def email_task(recipient: str, subject: str) -> str:
    """Simulate sending email."""
    print(f"📧 Sending email to {recipient}: '{subject}'")
    await asyncio.sleep(0.3)  # Simulate sending time
    return f"Email sent to {recipient}"


async def backup_task(database: str) -> str:
    """Simulate database backup."""
    print(f"💾 Starting backup of {database}")
    await asyncio.sleep(0.8)  # Simulate backup time
    return f"Backup of {database} completed"


async def report_task(report_type: str) -> str:
    """Simulate generating report."""
    print(f"📊 Generating {report_type} report")
    await asyncio.sleep(0.5)  # Simulate generation time
    return f"{report_type} report generated"


async def task_scheduler_example():
    """Demonstrate async task scheduling."""
    print("📅 Async Task Scheduler Example:")

    scheduler = AsyncTaskScheduler()

    # Schedule various tasks with different delays
    scheduler.schedule_task(email_task("alice@example.com", "Welcome"), 0.5)
    scheduler.schedule_task(backup_task("user_database"), 1.0)
    scheduler.schedule_task(report_task("Daily Sales"), 0.3)
    scheduler.schedule_task(email_task("bob@example.com", "Newsletter"), 0.7)

    print(f"📋 Scheduled {len(scheduler.tasks)} tasks")

    start_time = time.time()
    results = await scheduler.run_scheduled_tasks()
    end_time = time.time()

    print(f"📊 Task Results:")
    for result in results:
        if isinstance(result, Exception):
            print(f"   ❌ Task failed: {result}")
        else:
            print(f"   ✅ {result}")

    print(f"⏱️ Total execution time: {end_time - start_time:.2f} seconds")


asyncio.run(task_scheduler_example())


# Example 3: Async Rate-Limited Client
class AsyncRateLimitedClient:
    """HTTP client with async rate limiting."""

    def __init__(self, requests_per_second: int = 5):
        self.rate_limit = requests_per_second
        self.request_times = []
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def _wait_for_rate_limit(self):
        """Wait if necessary to respect rate limit."""
        now = time.time()

        # Remove requests older than 1 second
        self.request_times = [t for t in self.request_times if now - t < 1.0]

        # Wait if we've hit the rate limit
        if len(self.request_times) >= self.rate_limit:
            wait_time = 1.0 - (now - self.request_times[0])
            if wait_time > 0:
                print(f"⏳ Rate limit reached, waiting {wait_time:.2f}s")
                await asyncio.sleep(wait_time)
                # Clean up old requests after waiting
                now = time.time()
                self.request_times = [t for t in self.request_times if now - t < 1.0]

        self.request_times.append(now)

    async def make_request(self, endpoint: str) -> Dict[str, Any]:
        """Make rate-limited request."""
        await self._wait_for_rate_limit()

        print(f"🌐 Making request to {endpoint}")
        await asyncio.sleep(0.2)  # Simulate API call

        return {
            "endpoint": endpoint,
            "status": 200,
            "data": f"Response from {endpoint}",
            "timestamp": time.time(),
        }


async def rate_limited_client_example():
    """Demonstrate async rate-limited client."""
    print("🚦 Async Rate-Limited Client Example:")

    endpoints = [
        "/api/users",
        "/api/products",
        "/api/orders",
        "/api/analytics",
        "/api/reports",
        "/api/settings",
        "/api/notifications",
        "/api/logs",
    ]

    async with AsyncRateLimitedClient(requests_per_second=3) as client:
        start_time = time.time()

        # Make all requests concurrently (but rate-limited)
        results = await asyncio.gather(
            *[client.make_request(endpoint) for endpoint in endpoints]
        )

        end_time = time.time()

        print(f"📊 Request Results:")
        print(f"   Total requests: {len(results)}")
        print(f"   Total time: {end_time - start_time:.2f} seconds")
        print(
            f"   Average time per request: {(end_time - start_time)/len(results):.2f}s"
        )


asyncio.run(rate_limited_client_example())

# ===== ASYNC VS SYNC COMPARISON =====
print("\n7. ASYNC VS SYNC PERFORMANCE")
print("-" * 40)


def sync_io_task(task_id: int, delay: float) -> str:
    """Synchronous I/O task."""
    print(f"🐌 Sync Task {task_id} starting")
    time.sleep(delay)
    return f"Sync result {task_id}"


async def async_io_task(task_id: int, delay: float) -> str:
    """Asynchronous I/O task."""
    print(f"⚡ Async Task {task_id} starting")
    await asyncio.sleep(delay)
    return f"Async result {task_id}"


async def performance_comparison():
    """Compare sync vs async performance."""
    tasks_data = [(i, 0.5) for i in range(1, 6)]  # 5 tasks, 0.5s each

    # Synchronous execution
    print("🐌 Synchronous Execution:")
    sync_start = time.time()
    sync_results = [sync_io_task(task_id, delay) for task_id, delay in tasks_data]
    sync_time = time.time() - sync_start
    print(f"⏱️ Sync total time: {sync_time:.2f} seconds")

    # Asynchronous execution
    print(f"\n⚡ Asynchronous Execution:")
    async_start = time.time()
    async_results = await asyncio.gather(
        *[async_io_task(task_id, delay) for task_id, delay in tasks_data]
    )
    async_time = time.time() - async_start
    print(f"⏱️ Async total time: {async_time:.2f} seconds")

    print(f"\n📊 Performance Summary:")
    print(f"   Sync time: {sync_time:.2f}s")
    print(f"   Async time: {async_time:.2f}s")
    print(f"   Speedup: {sync_time/async_time:.2f}x faster with async")
    print(f"   Efficiency: {(1 - async_time/sync_time)*100:.1f}% improvement")


asyncio.run(performance_comparison())

print("\n" + "=" * 60)
print("✅ Essential async patterns demonstrated!")
print("💡 Focus: I/O-bound operations with maximum concurrency")
