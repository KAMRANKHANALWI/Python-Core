# Python Functions - Essential Guide

## Table of Contents

1. [Basic Functions](#basic-functions)
2. [\*args and \*\*kwargs](#args-and-kwargs)
3. [Closures](#closures)
4. [Recursion](#recursion)
5. [Real-World Patterns](#real-world-patterns)
6. [Best Practices](#best-practices)

---

## Basic Functions

### Function Definition and Call

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
```

### Default Parameters

```python
def create_user(name, age=18, role="user"):
    return {"name": name, "age": age, "role": role}

user1 = create_user("Bob")                    # Uses defaults
user2 = create_user("Charlie", 25, "admin")   # Override defaults
```

### Multiple Return Values

```python
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = get_stats([1, 5, 3, 9, 2])
```

### Keyword Arguments

```python
def process_order(item, quantity=1, priority="normal", discount=0):
    return f"Order: {quantity}x {item}, Priority: {priority}"

# Call with keyword arguments
order = process_order("laptop", quantity=2, priority="high")
```

---

## \*args and \*\*kwargs

### \*args - Variable Positional Arguments

Accept any number of positional arguments:

```python
def calculate_total(*prices):
    """Sum any number of prices."""
    return sum(prices)

total = calculate_total(10.99, 25.50, 7.25, 15.00)
```

### \*\*kwargs - Variable Keyword Arguments

Accept any number of keyword arguments:

```python
def create_profile(**details):
    """Create profile with any details."""
    profile = {"created": "2024", "active": True}
    profile.update(details)
    return profile

user = create_profile(name="Alice", age=25, city="NYC")
```

### Combining Parameter Types

Order matters: positional, \*args, keyword, \*\*kwargs

```python
def flexible_function(required, default="value", *args, **kwargs):
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Extra args: {args}")
    print(f"Keyword args: {kwargs}")

flexible_function("must_have", "custom", "extra1", "extra2",
                 option1="value1", option2="value2")
```

### Unpacking Arguments

Use \* and \*\* to unpack when calling functions:

```python
def calculate_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

# Unpack coordinates
point1 = (0, 0)
point2 = (3, 4)
distance = calculate_distance(*point1, *point2)

# Unpack dictionary
config = {"host": "localhost", "port": 8080, "debug": True}
def connect(**settings):
    return f"Connecting to {settings['host']}:{settings['port']}"

connection = connect(**config)
```

---

## Closures

### Basic Closure

Functions that capture variables from outer scope:

```python
def create_multiplier(factor):
    """Create function that multiplies by factor."""
    def multiply(number):
        return number * factor
    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

### Closure with State

Maintain state between function calls:

```python
def create_counter(start=0):
    """Create counter with persistent state."""
    count = [start]  # Use list for mutability

    def counter():
        count[0] += 1
        return count[0]

    def reset():
        count[0] = start

    counter.reset = reset
    return counter

counter = create_counter(10)
print(counter())  # 11
print(counter())  # 12
counter.reset()
print(counter())  # 11
```

### Configuration Closures

Create specialized functions with preset configurations:

```python
def create_validator(min_length=1, max_length=100):
    """Create validation function with specific rules."""
    def validate(text):
        if len(text) < min_length:
            return False, f"Too short (min: {min_length})"
        if len(text) > max_length:
            return False, f"Too long (max: {max_length})"
        return True, "Valid"
    return validate

username_validator = create_validator(3, 20)
password_validator = create_validator(8, 50)

valid, message = username_validator("bob")
```

---

## Recursion

### Basic Recursion Pattern

```python
def factorial(n):
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)
```

### Fibonacci Sequence

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Generate sequence
fib_sequence = [fibonacci(i) for i in range(8)]
```

### Tree Traversal (Real-World Recursion)

```python
def find_files(directory, extension):
    """Recursively find files with specific extension."""
    files_found = []

    for item in directory:
        if isinstance(item, dict):
            # Subdirectory - recurse
            for subdir, contents in item.items():
                files_found.extend(find_files(contents, extension))
        elif isinstance(item, str) and item.endswith(extension):
            # File with matching extension
            files_found.append(item)

    return files_found
```

### Tail Recursion Pattern

```python
def sum_list(numbers, accumulator=0):
    """Sum using tail recursion pattern."""
    if not numbers:
        return accumulator
    return sum_list(numbers[1:], accumulator + numbers[0])
```

### Recursion Best Practices

- Always define a base case
- Ensure progress toward base case
- Consider iterative alternatives for deep recursion
- Use memoization for overlapping subproblems

---

## Real-World Patterns

### API Handler with Flexible Parameters

```python
def api_request(endpoint, method="GET", *args, **kwargs):
    """Generic API request handler."""
    headers = kwargs.get('headers', {})
    timeout = kwargs.get('timeout', 30)
    data = kwargs.get('data', None)

    # Simulate API call
    return {
        "endpoint": endpoint,
        "method": method,
        "status": "success",
        "args": args,
        "config": kwargs
    }

# Flexible usage
response1 = api_request("/users", method="POST", data={"name": "Alice"})
response2 = api_request("/orders", timeout=60, headers={"Auth": "Bearer token"})
```

### Logger Factory with Closures

```python
def create_logger(service_name):
    """Create logger for specific service."""
    def log(message, level="INFO"):
        timestamp = "2024-01-01 10:00:00"
        print(f"[{timestamp}] {service_name} {level}: {message}")

    # Add convenience methods
    log.info = lambda msg: log(msg, "INFO")
    log.error = lambda msg: log(msg, "ERROR")
    log.warning = lambda msg: log(msg, "WARNING")

    return log

# Create service-specific loggers
auth_logger = create_logger("AUTH")
db_logger = create_logger("DATABASE")

auth_logger.info("User logged in")
db_logger.error("Connection failed")
```

### Memoization with Closures

```python
def memoize(func):
    """Add caching to function using closure."""
    cache = {}

    def memoized(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    memoized.cache = cache
    return memoized

@memoize
def fibonacci_optimized(n):
    if n <= 1:
        return n
    return fibonacci_optimized(n-1) + fibonacci_optimized(n-2)
```

### Configuration Builder

```python
def build_config(**base_config):
    """Build configuration with override capability."""
    def override(**new_config):
        merged = base_config.copy()
        merged.update(new_config)
        return merged

    def get(key, default=None):
        return base_config.get(key, default)

    return type('Config', (), {
        'override': override,
        'get': get,
        'data': base_config
    })()

# Usage
config = build_config(host="localhost", port=8080, debug=True)
prod_config = config.override(host="production.com", debug=False)
```

### Recursive Data Processing

```python
def process_nested_data(data, processor_func):
    """Recursively process nested data structures."""
    if isinstance(data, dict):
        return {k: process_nested_data(v, processor_func) for k, v in data.items()}
    elif isinstance(data, list):
        return [process_nested_data(item, processor_func) for item in data]
    else:
        return processor_func(data)

# Example: convert all strings to uppercase
uppercase_data = process_nested_data(
    {"users": ["alice", "bob"], "settings": {"theme": "dark"}},
    lambda x: x.upper() if isinstance(x, str) else x
)
```

---

## Best Practices

### 1. Use Clear Function Names

```python
# Good: Clear purpose
def calculate_total_with_tax(price, tax_rate=0.1):
    return price * (1 + tax_rate)

# Avoid: Unclear purpose
def calc(p, t=0.1):
    return p * (1 + t)
```

### 2. Keep Functions Focused

```python
# Good: Single responsibility
def validate_email(email):
    return "@" in email and "." in email

def send_email(email, message):
    if validate_email(email):
        # Send logic here
        return True
    return False

# Avoid: Multiple responsibilities
def validate_and_send_email(email, message):
    # Validation + sending in one function
    pass
```

### 3. Use Type Hints (Python 3.5+)

```python
def calculate_discount(price: float, discount_rate: float = 0.1) -> float:
    """Calculate discounted price."""
    return price * (1 - discount_rate)

def process_users(users: list[dict]) -> list[str]:
    """Extract user names."""
    return [user["name"] for user in users]
```

### 4. Handle Errors Gracefully

```python
def safe_divide(a: float, b: float) -> float | None:
    """Safely divide two numbers."""
    if b == 0:
        return None
    return a / b

def parse_config(config_string: str) -> dict:
    """Parse configuration with error handling."""
    try:
        import json
        return json.loads(config_string)
    except json.JSONDecodeError:
        return {}
```

### 5. Use Docstrings

```python
def calculate_compound_interest(principal, rate, time, compound_freq=1):
    """
    Calculate compound interest.

    Args:
        principal: Initial amount
        rate: Annual interest rate (decimal)
        time: Time in years
        compound_freq: Compounding frequency per year

    Returns:
        Final amount after compound interest
    """
    return principal * (1 + rate/compound_freq)**(compound_freq * time)
```

### 6. When to Use Each Pattern

| Pattern        | Use Case               | Example                       |
| -------------- | ---------------------- | ----------------------------- |
| Basic function | Simple operations      | `def add(a, b): return a + b` |
| \*args         | Variable inputs        | `def sum_all(*numbers)`       |
| \*\*kwargs     | Flexible config        | `def api_call(**options)`     |
| Closures       | State preservation     | `def create_counter()`        |
| Recursion      | Tree/nested data       | `def traverse_tree(node)`     |
| Memoization    | Expensive computations | `@memoize def fibonacci(n)`   |

---

## Performance Tips

### 1. Avoid Deep Recursion

```python
# Use iteration for simple cases
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

### 2. Use Generators for Large Data

```python
def process_large_dataset(data):
    """Generator for memory efficiency."""
    for item in data:
        yield process_item(item)
```

### 3. Cache Expensive Operations

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_calculation(n):
    # Expensive operation here
    return result
```

**Key Takeaway**: Functions are the building blocks of clean code. Use the right pattern for each situation, keep functions focused, and leverage closures and recursion for elegant solutions to complex problems.
