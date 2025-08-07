# Python Decorators - Essential Guide

## Table of Contents

1. [What are Decorators?](#what-are-decorators)
2. [Basic Decorator Pattern](#basic-decorator-pattern)
3. [Core Examples](#core-examples)
4. [Parameterized Decorators](#parameterized-decorators)
5. [Real-World Applications](#real-world-applications)
6. [Best Practices](#best-practices)

---

## What are Decorators?

**Definition**: A function that takes another function and extends its behavior without permanently modifying it.

**Key Concept**: Decorators "wrap" functions with additional functionality while preserving the original function.

### Basic Syntax

```python
@decorator_name
def function_name():
    pass

# Equivalent to:
function_name = decorator_name(function_name)
```

### Decorator Pattern

```python
def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Code before function execution
        result = func(*args, **kwargs)
        # Code after function execution
        return result
    return wrapper
```

---

## Basic Decorator Pattern

### Standard Structure

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Pre-processing
        result = func(*args, **kwargs)  # Call original function
        # Post-processing
        return result
    return wrapper
```

### Key Components

- **Outer function**: Accepts the target function
- **Inner wrapper**: Contains enhanced behavior
- **`\*args, **kwargs`\*\*: Ensures function signature compatibility
- **Return wrapper**: Returns the enhanced function

---

## Core Examples

### Timer Decorator

Measure function execution time:

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Completed"
```

### Debug Decorator

Log function calls and returns:

```python
def debug(func):
    def wrapper(*args, **kwargs):
        args_str = ", ".join(str(arg) for arg in args)
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"Calling: {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper

@debug
def add_numbers(a, b):
    return a + b
```

### Cache Decorator

Store results to avoid redundant computations:

```python
def cache(func):
    cache_storage = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(sorted(kwargs.items()))

        if key in cache_storage:
            print(f"Cache hit for {func.__name__}")
            return cache_storage[key]

        result = func(*args, **kwargs)
        cache_storage[key] = result
        print(f"Computing {func.__name__}")
        return result

    wrapper.cache = cache_storage
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

---

## Parameterized Decorators

### Structure

Decorators that accept parameters need an extra function layer:

```python
def decorator_with_params(param1, param2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Use param1, param2 here
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Rate Limiting Example

```python
def rate_limit(max_calls=3, time_window=60):
    def decorator(func):
        calls = []

        def wrapper(*args, **kwargs):
            import time
            now = time.time()

            # Remove expired calls
            calls[:] = [call_time for call_time in calls
                       if now - call_time < time_window]

            if len(calls) >= max_calls:
                return "Rate limit exceeded"

            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=2, time_window=10)
def api_call():
    return "API response"
```

### Retry Logic

```python
def retry(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            import time
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_api_call():
    import random
    if random.random() < 0.7:
        return "Success"
    raise Exception("Service unavailable")
```

---

## Real-World Applications

### Authentication System

```python
def login_required(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_logged_in", False):
            return "Authentication required"
        return func(user, *args, **kwargs)
    return wrapper

def admin_required(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_admin", False):
            return "Admin privileges required"
        return func(user, *args, **kwargs)
    return wrapper

@login_required
@admin_required
def delete_user(user, target_user_id):
    return f"User {target_user_id} deleted"
```

### Input Validation

```python
def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                return "Error: Negative values not allowed"
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(length, width):
    return length * width
```

### Logging System

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Executing {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[{timestamp}] {func.__name__} completed")
        return result
    return wrapper

@log_calls
def process_payment(amount):
    return f"Payment of ${amount} processed"
```

---

## Best Practices

### 1. Use functools.wraps

Preserve original function metadata:

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### 2. Handle Function Signatures Properly

Always use `*args, **kwargs` for compatibility:

```python
def decorator(func):
    def wrapper(*args, **kwargs):  # ✅ Flexible signature
        return func(*args, **kwargs)
    return wrapper
```

### 3. Preserve Return Values

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Process result if needed
        return result  # ✅ Always return the result
    return wrapper
```

### 4. Handle Exceptions Gracefully

```python
def safe_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            raise  # Re-raise for proper error handling
    return wrapper
```

### 5. Stacking Decorators

Multiple decorators are applied bottom to top:

```python
@timer
@debug
@cache
def complex_function(x, y):
    return x ** y

# Execution order: cache -> debug -> timer -> function
```

### 6. Class-Based Decorators

For stateful decorators:

```python
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} called {self.count} times")
        return self.func(*args, **kwargs)

@CallCounter
def greet(name):
    return f"Hello, {name}!"
```

---

## Common Use Cases

| Use Case        | Example                              | Benefits                                    |
| --------------- | ------------------------------------ | ------------------------------------------- |
| **Performance** | `@timer`, `@cache`                   | Monitor execution time, avoid recomputation |
| **Security**    | `@login_required`, `@admin_required` | Control access to functions                 |
| **Reliability** | `@retry`, `@rate_limit`              | Handle failures, prevent abuse              |
| **Debugging**   | `@debug`, `@log_calls`               | Track function behavior                     |
| **Validation**  | `@validate_positive`, `@type_check`  | Ensure input correctness                    |

## Implementation Patterns

### Basic Decorator

```python
def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Enhanced behavior
        return func(*args, **kwargs)
    return wrapper
```

### Parameterized Decorator

```python
def decorator_name(param):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Use param in logic
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Class-Based Decorator

```python
class DecoratorName:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # Enhanced behavior
        return self.func(*args, **kwargs)
```

**Key Takeaway**: Decorators provide a clean way to extend function behavior without modifying the original code. Use them for cross-cutting concerns like logging, authentication, caching, and performance monitoring.
