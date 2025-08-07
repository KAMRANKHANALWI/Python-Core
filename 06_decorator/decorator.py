# Python Decorators: Comprehensive Implementation Guide
"""
A complete collection of decorator patterns demonstrating timing, debugging,
caching, authentication, rate limiting, and other real-world applications.

This module showcases both fundamental decorator concepts and production-ready
implementations for common software engineering challenges.
"""

import time
import functools
from datetime import datetime

print("Python Decorators: Comprehensive Implementation")
print("=" * 60)

# Core Decorator Implementations
print("\nCore Decorator Implementations")


def timer(func):
    """
    Measure and display function execution time.

    Args:
        func: The function to be timed

    Returns:
        Wrapped function that prints execution time
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️  {func.__name__} executed in {end - start:.4f} seconds")
        return result

    return wrapper


def debug(func):
    """
    Log function calls with arguments and return values.

    Args:
        func: The function to be debugged

    Returns:
        Wrapped function that logs call details
    """

    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_value, kwargs_value]))
        print(f"🔍 Calling: {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"🔍 Returned: {result}")
        return result

    return wrapper


def cache(func):
    """
    Cache function results to avoid redundant computations.

    Args:
        func: The function whose results should be cached

    Returns:
        Wrapped function with caching capability
    """
    cache_value = {}

    def wrapper(*args, **kwargs):
        # Create cache key from arguments
        key = str(args) + str(sorted(kwargs.items()))

        if key in cache_value:
            print(f"💾 Cache hit for {func.__name__}")
            return cache_value[key]

        result = func(*args, **kwargs)
        cache_value[key] = result
        print(f"🔄 Computing {func.__name__}")
        return result

    # Expose cache for inspection
    wrapper.cache = cache_value
    return wrapper


print("Testing core implementations:")


@timer
@debug
def example_function(n):
    """Example function that sleeps for n seconds."""
    time.sleep(n)
    return f"Completed after {n} seconds"


@cache
def fibonacci(n):
    """Calculate nth Fibonacci number with caching."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Test core decorators
result = example_function(1)
print(f"Result: {result}")

print(f"\nFibonacci(10) = {fibonacci(10)}")
print(f"Fibonacci(10) cached = {fibonacci(10)}")

print("\n" + "=" * 60)

# Production-Ready Decorator Implementations
print("\nProduction-Ready Decorator Implementations")


def login_required(func):
    """
    Ensure user is authenticated before function execution.

    Args:
        func: Function requiring authentication

    Returns:
        Wrapped function with authentication check
    """

    def wrapper(user, *args, **kwargs):
        if not user.get("is_logged_in", False):
            return "Access denied: Authentication required"
        return func(user, *args, **kwargs)

    return wrapper


def admin_required(func):
    """
    Ensure user has administrative privileges.

    Args:
        func: Function requiring admin access

    Returns:
        Wrapped function with authorization check
    """

    def wrapper(user, *args, **kwargs):
        if not user.get("is_admin", False):
            return "Access denied: Administrative privileges required"
        return func(user, *args, **kwargs)

    return wrapper


def rate_limit(max_calls=3, time_window=60):
    """
    Limit function calls within a specified time window.

    Args:
        max_calls (int): Maximum allowed calls within time window
        time_window (int): Time window in seconds

    Returns:
        Decorator function implementing rate limiting
    """

    def decorator(func):
        calls = []

        def wrapper(*args, **kwargs):
            now = time.time()
            # Remove expired calls
            calls[:] = [
                call_time for call_time in calls if now - call_time < time_window
            ]

            if len(calls) >= max_calls:
                return "Rate limit exceeded: Too many requests"

            calls.append(now)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry(max_attempts=3, delay=1):
    """
    Retry function execution on failure.

    Args:
        max_attempts (int): Maximum retry attempts
        delay (int): Delay between attempts in seconds

    Returns:
        Decorator function implementing retry logic
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        print(f"Failed after {max_attempts} attempts: {e}")
                        raise e
                    print(
                        f"Attempt {attempt + 1} failed: {e}. "
                        f"Retrying in {delay}s..."
                    )
                    time.sleep(delay)

        return wrapper

    return decorator


def log_calls(func):
    """
    Log function calls with timestamps.

    Args:
        func: Function to be logged

    Returns:
        Wrapped function with call logging
    """

    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"📝 [{timestamp}] Executing {func.__name__}")
        result = func(*args, **kwargs)
        print(f"📝 [{timestamp}] {func.__name__} completed")
        return result

    return wrapper


def validate_positive(func):
    """
    Validate that numeric arguments are positive.

    Args:
        func: Function requiring positive numeric inputs

    Returns:
        Wrapped function with input validation
    """

    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                return f"Validation error: Negative values not allowed"
        return func(*args, **kwargs)

    return wrapper


print("Configuring production examples...")

# Production Application Examples


@login_required
@rate_limit(max_calls=2, time_window=10)
@log_calls
@validate_positive
def transfer_money(user, amount, to_account):
    """Transfer money between accounts with security and validation."""
    return f"Transferred ${amount} to account {to_account}"


@admin_required
@log_calls
def view_all_accounts(user):
    """View all system accounts (admin only)."""
    return "Account data: [Account1, Account2, Account3]"


@retry(max_attempts=3, delay=0.5)
@timer
def unreliable_api_call(success_rate=0.3):
    """Simulate unreliable external API call."""
    import random

    if random.random() < success_rate:
        return "API call successful"
    else:
        raise Exception("API temporarily unavailable")


@cache
@timer
@log_calls
def process_large_file(filename, operation="read"):
    """Process large files with caching and timing."""
    time.sleep(1)  # Simulate processing time
    return f"Processed {filename} with {operation} operation"


print("\nTesting Production Scenarios")

# Test user configurations
admin_user = {"name": "Admin", "is_logged_in": True, "is_admin": True}
regular_user = {"name": "Alice", "is_logged_in": True, "is_admin": False}
guest_user = {"name": "Guest", "is_logged_in": False, "is_admin": False}

print("\n1. Financial System Operations:")
print(transfer_money(regular_user, 100, "12345"))
print(transfer_money(regular_user, 50, "67890"))
print(transfer_money(regular_user, 25, "11111"))  # Rate limited

print(transfer_money(guest_user, 100, "12345"))  # Authentication required
print(transfer_money(regular_user, -50, "12345"))  # Validation error

print("\n2. Administrative Operations:")
print(view_all_accounts(admin_user))
print(view_all_accounts(regular_user))  # Authorization required

print("\n3. API Reliability Testing:")
try:
    result = unreliable_api_call(success_rate=0.8)
    print(result)
except Exception as e:
    print(f"Final failure: {e}")

print("\n4. File Processing with Optimization:")
print(process_large_file("data.txt", "read"))
print(process_large_file("data.txt", "read"))  # Cached result
print(process_large_file("config.txt", "write"))

print("\n" + "=" * 60)

# Implementation Patterns Reference
print("\nDecorator Implementation Patterns")
print(
    """
1. Basic Decorator Pattern:
   def decorator_name(func):
       def wrapper(*args, **kwargs):
           # Pre-processing logic
           result = func(*args, **kwargs)
           # Post-processing logic
           return result
       return wrapper

2. Parameterized Decorator Pattern:
   def decorator_name(parameter):
       def decorator(func):
           def wrapper(*args, **kwargs):
               # Use parameter in logic
               return func(*args, **kwargs)
           return wrapper
       return decorator

3. Class-Based Decorator Pattern:
   class DecoratorName:
       def __init__(self, func):
           self.func = func
       def __call__(self, *args, **kwargs):
           return self.func(*args, **kwargs)

4. Decorator Composition:
   @decorator_one
   @decorator_two
   @decorator_three
   def target_function():
       pass
"""
)

print("\nImplementation Summary")
print("=" * 60)
print("✓ Core patterns: timing, debugging, caching")
print("✓ Security: authentication and authorization")
print("✓ Reliability: rate limiting and retry logic")
print("✓ Observability: logging and monitoring")
print("✓ Validation: input checking and error handling")
print("\nDecorator patterns successfully demonstrated.")
