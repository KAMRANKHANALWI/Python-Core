# Python Functions - Essential Examples
"""
Concise, high-value examples of Python functions.
Covers: basic functions, *args, **kwargs, closures, recursion, and real applications.
"""

print("Python Functions - Essential Patterns")
print("=" * 50)

# ===== BASIC FUNCTIONS =====
print("\n1. BASIC FUNCTIONS")
print("-" * 30)


# Simple function
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))


# Function with default parameters
def create_user(name, age=18, role="user"):
    return {"name": name, "age": age, "role": role}


print(create_user("Bob"))
print(create_user("Charlie", 25, "admin"))


# Multiple return values
def get_name_parts(full_name):
    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[-1] if len(parts) > 1 else ""
    return first_name, last_name


first, last = get_name_parts("John Doe Smith")
print(f"First: {first}, Last: {last}")

# ===== *ARGS AND **KWARGS =====
print("\n2. *ARGS AND **KWARGS")
print("-" * 30)


# *args - variable positional arguments
def calculate_total(*prices):
    """Calculate total of any number of prices."""
    total = sum(prices)
    tax = total * 0.1
    return {"subtotal": total, "tax": tax, "total": total + tax}


result = calculate_total(10.99, 25.50, 7.25)
print(f"Order total: ${result['total']:.2f}")


# **kwargs - variable keyword arguments
def create_profile(**details):
    """Create user profile with any number of details."""
    profile = {"created": "2024", "active": True}
    profile.update(details)
    return profile


user = create_profile(name="Alice", age=25, city="NYC", skill="Python")
print(f"Profile: {user}")


# Combining all parameter types
def flexible_function(required, default="default", *args, **kwargs):
    """Demonstrate all parameter types together."""
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")


flexible_function(
    "must_have", "custom", "extra1", "extra2", option1="value1", option2="value2"
)


# Unpacking arguments
def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# Unpack list/tuple with *
point1 = (0, 0)
point2 = (3, 4)
distance = calculate_distance(*point1, *point2)
print(f"\nDistance: {distance}")

# Unpack dictionary with **
config = {"host": "localhost", "port": 8080, "debug": True}


def connect(**settings):
    return f"Connecting to {settings['host']}:{settings['port']}"


connection = connect(**config)
print(connection)

# ===== CLOSURES =====
print("\n3. CLOSURES")
print("-" * 30)


# Basic closure
def create_multiplier(factor):
    """Create a function that multiplies by factor."""

    def multiply(number):
        return number * factor

    return multiply


double = create_multiplier(2)
triple = create_multiplier(3)

print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")


# Closure with state
def create_counter(start=0):
    """Create a counter function with persistent state."""
    count = [start]  # Use list to make it mutable

    def counter():
        count[0] += 1
        return count[0]

    def reset():
        count[0] = start

    counter.reset = reset  # Attach reset method
    return counter


counter1 = create_counter()
counter2 = create_counter(10)

print(f"Counter1: {counter1()}, {counter1()}, {counter1()}")
print(f"Counter2: {counter2()}, {counter2()}")
counter1.reset()
print(f"Counter1 after reset: {counter1()}")


# Closure for configuration
def create_validator(min_length=1, max_length=100):
    """Create a validation function with specific rules."""

    def validate(text):
        if not isinstance(text, str):
            return False, "Must be a string"
        if len(text) < min_length:
            return False, f"Too short (min: {min_length})"
        if len(text) > max_length:
            return False, f"Too long (max: {max_length})"
        return True, "Valid"

    return validate


# Create different validators
username_validator = create_validator(3, 20)
password_validator = create_validator(8, 50)

print(f"\nUsername 'ab': {username_validator('ab')}")
print(f"Password 'secret123': {password_validator('secret123')}")

# ===== RECURSION =====
print("\n4. RECURSION")
print("-" * 30)


# Classic factorial
def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(f"Factorial of 5: {factorial(5)}")


# Fibonacci sequence
def fibonacci(n):
    """Calculate nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"Fibonacci sequence: {[fibonacci(i) for i in range(8)]}")


# Tree traversal (real-world recursion)
def find_files(directory_structure, extension):
    """Recursively find files with specific extension."""
    files_found = []

    for item in directory_structure:
        if isinstance(item, dict):
            # It's a subdirectory
            for subdir, contents in item.items():
                files_found.extend(find_files(contents, extension))
        elif isinstance(item, str):
            # It's a file
            if item.endswith(extension):
                files_found.append(item)

    return files_found


# Test with mock directory structure
mock_filesystem = [
    "readme.txt",
    "app.py",
    {"src": ["main.py", "utils.py", {"models": ["user.py", "config.json"]}]},
    {"docs": ["guide.md", "api.txt"]},
]

python_files = find_files(mock_filesystem, ".py")
print(f"Python files found: {python_files}")


# Tail recursion optimization pattern
def sum_list_optimized(numbers, accumulator=0):
    """Sum list using tail recursion pattern."""
    if not numbers:
        return accumulator
    return sum_list_optimized(numbers[1:], accumulator + numbers[0])


print(f"Sum of [1,2,3,4,5]: {sum_list_optimized([1,2,3,4,5])}")

# ===== REAL-WORLD APPLICATIONS =====
print("\n5. REAL-WORLD APPLICATIONS")
print("-" * 50)


# Example 1: API Response Handler
def handle_api_response(endpoint, *args, **kwargs):
    """Generic API response handler with flexible parameters."""
    # Simulate API call parameters
    method = kwargs.get("method", "GET")
    headers = kwargs.get("headers", {})
    timeout = kwargs.get("timeout", 30)

    print(f"🌐 API Call: {method} {endpoint}")
    print(f"   Args: {args}")
    print(f"   Headers: {headers}")
    print(f"   Timeout: {timeout}s")

    # Simulate response
    return {"status": "success", "data": f"Response from {endpoint}"}


# Test API handler
response1 = handle_api_response(
    "/users", method="POST", headers={"Auth": "Bearer token"}
)
response2 = handle_api_response("/orders", 123, "details", timeout=60)


# Example 2: Logging System with Closures
def create_logger(service_name, log_level="INFO"):
    """Create a logger function for specific service."""

    def log(message, level="INFO"):
        if level in ["DEBUG", "INFO", "WARNING", "ERROR"]:
            timestamp = "2024-01-01 10:00:00"  # Simplified
            print(f"[{timestamp}] {service_name} {level}: {message}")
        else:
            print(f"Invalid log level: {level}")

    # Add convenience methods
    def debug(message):
        log(message, "DEBUG")

    def info(message):
        log(message, "INFO")

    def warning(message):
        log(message, "WARNING")

    def error(message):
        log(message, "ERROR")

    # Attach methods to main function
    log.debug = debug
    log.info = info
    log.warning = warning
    log.error = error

    return log


# Create different loggers
auth_logger = create_logger("AUTH_SERVICE")
db_logger = create_logger("DATABASE")

print(f"\n📝 Logging Examples:")
auth_logger.info("User login successful")
auth_logger.warning("Failed login attempt")
db_logger.error("Connection timeout")


# Example 3: Configuration Builder
def build_config(**base_config):
    """Build configuration with override capability."""

    def override(**new_config):
        """Override configuration values."""
        merged = base_config.copy()
        merged.update(new_config)
        return merged

    def get(key, default=None):
        """Get configuration value."""
        return base_config.get(key, default)

    def show():
        """Show all configuration."""
        print("Configuration:")
        for key, value in base_config.items():
            print(f"  {key}: {value}")

    # Return object with methods
    return type(
        "Config",
        (),
        {"override": override, "get": get, "show": show, "data": base_config},
    )()


# Test configuration builder
print(f"\n⚙️ Configuration Example:")
base_config = build_config(host="localhost", port=8080, debug=True)
base_config.show()

prod_config = base_config.override(host="production.com", debug=False)
print(f"Production host: {prod_config.data['host']}")


# Example 4: Recursive Data Processing
def process_nested_data(data, processor_func):
    """Recursively process nested data structures."""
    if isinstance(data, dict):
        return {
            key: process_nested_data(value, processor_func)
            for key, value in data.items()
        }
    elif isinstance(data, list):
        return [process_nested_data(item, processor_func) for item in data]
    else:
        return processor_func(data)


# Test with nested data
nested_data = {
    "users": ["alice", "bob", "charlie"],
    "settings": {
        "theme": "dark",
        "notifications": ["email", "sms"],
        "features": {"advanced": True, "beta": False},
    },
}


# Process: convert strings to uppercase
def uppercase_processor(value):
    return value.upper() if isinstance(value, str) else value


processed = process_nested_data(nested_data, uppercase_processor)
print(f"\n🔄 Processed nested data:")
print(f"Users: {processed['users']}")
print(f"Theme: {processed['settings']['theme']}")


# Example 5: Memoization with Closures
def memoize(func):
    """Create a memoized version of a function using closure."""
    cache = {}

    def memoized_func(*args):
        if args in cache:
            print(f"  Cache hit for {args}")
            return cache[args]

        print(f"  Computing for {args}")
        result = func(*args)
        cache[args] = result
        return result

    memoized_func.cache = cache
    memoized_func.clear_cache = lambda: cache.clear()
    return memoized_func


# Apply memoization to expensive function
@memoize
def expensive_fibonacci(n):
    """Fibonacci with memoization."""
    if n <= 1:
        return n
    return expensive_fibonacci(n - 1) + expensive_fibonacci(n - 2)


print(f"\n💾 Memoization Example:")
print(f"Fibonacci(10): {expensive_fibonacci(10)}")
print(f"Fibonacci(10) again: {expensive_fibonacci(10)}")
print(f"Cache size: {len(expensive_fibonacci.cache)}")


# Example 6: Function Factory Pattern
def create_calculator(*operations):
    """Create a calculator with specific operations."""

    def calculator(expression):
        """Evaluate expression with available operations."""
        try:
            # Simple expression evaluator (demo purposes)
            if "+" in expression and "add" in operations:
                parts = expression.split("+")
                return sum(float(part.strip()) for part in parts)
            elif "*" in expression and "multiply" in operations:
                parts = expression.split("*")
                result = 1
                for part in parts:
                    result *= float(part.strip())
                return result
            else:
                return "Operation not supported"
        except:
            return "Invalid expression"

    # Add operation info
    calculator.operations = operations
    return calculator


# Create different calculators
basic_calc = create_calculator("add", "multiply")
advanced_calc = create_calculator("add", "multiply", "divide", "power")

print(f"\n🧮 Calculator Example:")
print(f"Basic calc (2 + 3): {basic_calc('2 + 3')}")
print(f"Basic calc (2 * 3): {basic_calc('2 * 3')}")
print(f"Available operations: {basic_calc.operations}")

# ===== ADVANCED PATTERNS =====
print("\n6. ADVANCED PATTERNS")
print("-" * 40)


# Decorator using closure
def timer(func):
    """Time function execution using closure."""
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper


@timer
def slow_operation():
    """Simulate slow operation."""
    import time

    time.sleep(0.1)
    return "Operation complete"


slow_result = slow_operation()


# Partial application using closures
def create_partial(func, *partial_args, **partial_kwargs):
    """Create a partial function application."""

    def partial_func(*args, **kwargs):
        combined_args = partial_args + args
        combined_kwargs = {**partial_kwargs, **kwargs}
        return func(*combined_args, **combined_kwargs)

    return partial_func


# Example: pre-configured database connection
def connect_to_database(host, port, username, password, database):
    return f"Connected to {database} on {host}:{port} as {username}"


# Create pre-configured connection functions
local_db = create_partial(connect_to_database, "localhost", 5432, "admin")
prod_db = create_partial(connect_to_database, "prod.server.com", 5432, "prod_user")

print(f"\n🔌 Partial Application:")
print(local_db("secret123", "dev_database"))
print(prod_db("prod_pass", "main_database"))


# Higher-order function
def apply_to_list(func_list, value):
    """Apply multiple functions to a value."""
    return [func(value) for func in func_list]


# Test with multiple transformations
transformations = [
    lambda x: x.upper(),
    lambda x: x.replace(" ", "_"),
    lambda x: f"[{x}]",
]

text = "hello world"
results = apply_to_list(transformations, text)
print(f"\nTransformations of '{text}': {results}")

print("\n" + "=" * 50)
print("✅ Essential function patterns demonstrated!")
print("💡 Focus: *args, **kwargs, closures, recursion, real applications")
