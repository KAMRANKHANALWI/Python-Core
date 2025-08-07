# Python Core - Complete Learning Documentation

> **A comprehensive Python learning repository with practical examples and detailed notes - created during my journey from Python basics to advanced concepts.**

## Overview

This repository contains complete Python learning materials organized from fundamental concepts to advanced programming patterns. Each topic includes executable code examples (`01.py`) and comprehensive study notes (`.md` files) covering theory, best practices, and real-world applications.

## Table of Contents

### Fundamentals
1. [Python Basics](#1-python-basics)
2. [Conditionals](#2-conditionals) 
3. [Loops](#3-loops)
4. [Functions](#4-functions)

### Advanced Concepts
5. [Object-Oriented Programming](#5-object-oriented-programming)
6. [Decorators](#6-decorators)
7. [Threading & Concurrency](#7-threading--concurrency)
8. [Async Programming](#8-async-programming)

---

## 1. Python Basics

**Files:** [`01_basics/01.py`](01_basics/01.py) | [`01_basics/basics_notes.md`](01_basics/basics_notes.md)

### Core Topics
- **Data Types**: Numbers, strings, lists, dictionaries, tuples
- **Operations**: Arithmetic, string manipulation, list operations
- **Type Conversions**: Between different data types
- **Built-in Functions**: `len()`, `type()`, `range()`, etc.

### Key Examples
```python
# String operations
name = "Python"
print(f"Hello {name.upper()}!")  # Hello PYTHON!

# List operations
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]  # [1, 4, 9, 16, 25]

# Dictionary operations
student = {"name": "Alice", "grade": 85}
print(student.get("name", "Unknown"))  # Alice
```

### Learning Outcomes
- Write clean, readable Python code using proper data types
- Transform and manipulate data efficiently with built-in methods
- Build solid foundations for all advanced Python concepts

---

## 2. Conditionals

**Files:** [`02_conditionals/01.py`](02_conditionals/01.py) | [`02_conditionals/conditional_notes.md`](02_conditionals/conditional_notes.md)

### Core Topics
- **Basic Conditionals**: if, elif, else statements
- **Logical Operators**: and, or, not
- **Comparison Operators**: ==, !=, <, >, <=, >=
- **Membership Testing**: in, not in
- **Advanced Patterns**: Ternary operators, guard clauses

### Key Examples
```python
# Grade evaluation
def assign_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B" 
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

# Authentication check
def authenticate(user):
    if not user:
        return "No user provided"
    if not user.get("is_active"):
        return "User inactive"
    return "Access granted"
```

### Learning Outcomes
- Make smart decisions in your code with clean conditional logic
- Handle user input and data validation like a pro
- Write maintainable code that handles edge cases gracefully

---

## 3. Loops

**Files:** [`03_loops/01.py`](03_loops/01.py) | [`03_loops/loops_notes.md`](03_loops/loops_notes.md)

### Core Topics
- **For Loops**: Iteration over sequences, `range()`, `enumerate()`, `zip()`
- **While Loops**: Condition-based iteration
- **Loop Control**: `break`, `continue`, `else` clause
- **Comprehensions**: List, dictionary, and set comprehensions
- **Nested Loops**: Processing 2D data and complex structures

### Key Examples
```python
# Data processing with enumerate
files = ["data1.csv", "data2.json", "data3.xml"]
for index, filename in enumerate(files, 1):
    print(f"Processing file {index}: {filename}")

# List comprehension for filtering and transformation
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]  # [4, 16, 36, 64, 100]

# Producer-consumer pattern
import queue
task_queue = queue.Queue()
for item in ["task1", "task2", "task3"]:
    task_queue.put(item)
```

### Learning Outcomes
- Process large datasets efficiently with the right loop patterns
- Write concise, powerful code using comprehensions
- Build data processing pipelines that scale

---

## 4. Functions

**Files:** [`04_functions/01.py`](04_functions/01.py) | [`04_functions/functions_notes.md`](04_functions/functions_notes.md)

### Core Topics
- **Function Definition**: Parameters, return values, docstrings
- **Variable Arguments**: `*args` and `**kwargs`
- **Closures**: Functions returning functions, state preservation
- **Recursion**: Base cases, recursive patterns, optimization
- **Advanced Patterns**: Decorators, partial application, higher-order functions

### Key Examples
```python
# Simple function
def greet(name):
    return f"Hello, {name}!"

print(greet("Python"))  # Hello, Python!

# Function with default parameters
def calculate_area(length, width=1):
    return length * width

print(calculate_area(5))     # 5 (using default width=1)
print(calculate_area(5, 3))  # 15

# Multiple return values
def get_name_parts(full_name):
    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[-1] if len(parts) > 1 else ""
    return first_name, last_name

first, last = get_name_parts("John Doe")
print(f"First: {first}, Last: {last}")  # First: John, Last: Doe
```

### Learning Outcomes
- Create flexible, reusable functions that adapt to different needs
- Master advanced patterns that make your code incredibly powerful
- Build function libraries that other developers will love to use

---

## 5. Object-Oriented Programming

**Files:** [`05_oops/oops.py`](05_oops/oops.py) | [`05_oops/oops_notes.md`](05_oops/oops_notes.md)

### Core Topics
- **Classes and Objects**: Attributes, methods, `__init__`
- **Encapsulation**: Private attributes, property decorators
- **Inheritance**: Single and multiple inheritance, method overriding
- **Polymorphism**: Method overriding, duck typing
- **Advanced Features**: Class methods, static methods, `__str__`, `__repr__`

### Key Examples
```python
class Car:
    total_cars = 0  # Class variable
    
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.__model = model
        Car.total_cars += 1
    
    @property
    def brand(self):
        return self.__brand
    
    @staticmethod
    def general_description():
        return "Cars are vehicles for transportation"

class ElectricCar(Car):  # Inheritance
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):  # Polymorphism
        return "Electric"
```

### Learning Outcomes
- Design software systems that are easy to extend and maintain
- Create reusable code components using professional OOP patterns
- Build complex applications with confidence and clarity

---

## 6. Decorators

**Files:** [`06_decorator/decorator.py`](06_decorator/decorator.py) | [`06_decorator/decorator_notes.md`](06_decorator/decorator_notes.md)

### Core Topics
- **Basic Decorators**: Function wrappers, `functools.wraps`
- **Parameterized Decorators**: Decorators with arguments
- **Common Patterns**: Timing, logging, caching, authentication
- **Advanced Applications**: Rate limiting, retry logic, validation

### Key Examples
```python
# Simple decorator
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@debug
def add_numbers(a, b):
    return a + b

add_numbers(5, 3)  # Prints: Calling: add_numbers, Result: 8

# Timer decorator  
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done!"
```

### Learning Outcomes
- Add superpowers to your functions without changing their core logic
- Implement professional features like logging, timing, and caching
- Write elegant code that separates concerns beautifully

---

## 7. Threading & Concurrency

**Files:** [`07_threads_concurrency/01.py`](07_threads_concurrency/01.py) | [`07_threads_concurrency/threads_and_concurrency_notes.md`](07_threads_concurrency/threads_and_concurrency_notes.md)

### Core Topics
- **Basic Threading**: `threading.Thread`, `start()`, `join()`
- **Synchronization**: `Lock`, `RLock`, `Semaphore`, `Event`
- **Thread Communication**: `queue.Queue`, producer-consumer pattern
- **Thread Pool**: `ThreadPoolExecutor`, concurrent futures
- **Real-world Patterns**: Background tasks, rate limiting, batch processing

### Key Examples
```python
# Simple threading
import threading
import time

def worker_task(name, duration):
    print(f"Worker {name} starting...")
    time.sleep(duration)
    print(f"Worker {name} completed!")

# Create and start threads
thread1 = threading.Thread(target=worker_task, args=("A", 1))
thread2 = threading.Thread(target=worker_task, args=("B", 1))

thread1.start()
thread2.start()
thread1.join()  # Wait for completion
thread2.join()

# Thread-safe counter
counter = 0
lock = threading.Lock()

def safe_increment():
    global counter
    with lock:  # Thread-safe access
        counter += 1

# Producer-consumer with queue
import queue

task_queue = queue.Queue()

def producer():
    for i in range(3):
        item = f"task-{i}"
        task_queue.put(item)
        print(f"Added: {item}")

def consumer():
    while not task_queue.empty():
        item = task_queue.get()
        print(f"Processing: {item}")
```

### Learning Outcomes
- Make your programs faster by doing multiple things at once
- Handle shared resources safely without breaking your data
- Build responsive applications that don't freeze or hang

---

## 8. Async Programming

**Files:** [`08_async_python/01.py`](08_async_python/01.py) | [`08_async_python/async_concepts_notes.md`](08_async_python/async_concepts_notes.md)

### Core Topics
- **Basic Async**: `async def`, `await`, `asyncio.run()`
- **Concurrency**: `asyncio.gather()`, `asyncio.create_task()`
- **Async I/O**: `aiohttp` for HTTP requests, `aiofiles` for file operations
- **Async Patterns**: Producer-consumer with `asyncio.Queue`
- **Advanced Features**: Context managers, rate limiting, error handling

### Key Examples
```python
# Simple async function
import asyncio

async def fetch_data(name, delay):
    print(f"Fetching {name}...")
    await asyncio.sleep(delay)  # Non-blocking wait
    return f"Data from {name}"

# Sequential execution (slow)
async def sequential():
    result1 = await fetch_data("API-1", 1)
    result2 = await fetch_data("API-2", 1)
    return [result1, result2]  # Takes ~2 seconds

# Concurrent execution (fast)
async def concurrent():
    results = await asyncio.gather(
        fetch_data("API-1", 1),
        fetch_data("API-2", 1)
    )
    return results  # Takes ~1 second

# Run async code
asyncio.run(concurrent())

# Simple async HTTP (conceptual)
async def fetch_url(url):
    # Simulate HTTP request
    await asyncio.sleep(0.5)
    return f"Content from {url}"

async def fetch_multiple():
    urls = ["site1.com", "site2.com", "site3.com"]
    results = await asyncio.gather(*[fetch_url(url) for url in urls])
    return results
```

### Learning Outcomes
- Build lightning-fast applications that handle thousands of operations
- Create web scrapers and API clients that outperform traditional code
- Master the future of Python programming with async/await

---

## Getting Started

### Prerequisites
- Python 3.8+ installed
- Basic command line knowledge

### Quick Start
```bash
git clone https://github.com/KAMRANKHANALWI/Python-Core.git
cd Python-Core

# Start with fundamentals
python 01_basics/01.py               # Python basics
python 02_conditionals/01.py         # Conditionals  
python 03_loops/01.py                # Loops
python 04_functions/01.py            # Functions

# Explore advanced concepts
python 05_oops/oops.py               # Object-oriented programming
python 06_decorator/decorator.py     # Decorators
python 07_threads_concurrency/01.py # Threading
python 08_async_python/01.py         # Async programming
```

### Study Approach
1. **Read the notes first** - Understand concepts before running code
2. **Execute examples** - Run the `.py` files to see output
3. **Experiment** - Modify parameters and observe changes  
4. **Practice** - Implement your own versions of the examples

## Repository Structure

```
Python-Core/
├── 01_basics/
│   ├── 01.py                          # Python basics examples
│   └── basics_notes.md                # Comprehensive basics guide
├── 02_conditionals/
│   ├── 01.py                          # Conditional logic examples
│   └── conditional_notes.md           # Conditionals study guide
├── 03_loops/
│   ├── 01.py                          # Loops and iteration examples
│   └── loops_notes.md                 # Loops comprehensive guide
├── 04_functions/
│   ├── 01.py                          # Functions examples
│   └── functions_notes.md             # Functions detailed guide
├── 05_oops/
│   ├── oops.py                        # OOP implementation
│   └── oops_notes.md                  # OOP complete guide
├── 06_decorator/
│   ├── 01_decorator.py                # Simple decorator examples
│   ├── 02_decorator.py                # Advanced decorator patterns
│   ├── 03_decorator.py                # Real-world decorator applications
│   ├── decorator.py                   # Comprehensive decorator examples
│   └── decorator_notes.md             # Decorators study guide
├── 07_threads_concurrency/
│   ├── 01.py                          # Threading examples
│   └── threads_and_concurrency_notes.md  # Threading guide
├── 08_async_python/
│   ├── 01.py                          # Async programming examples
│   └── async_concepts_notes.md        # Async programming guide
└── README.md                          # This file
```

## Why Programming Changes Everything

> *"Programming is not about what you know; it's about what you can figure out."* - Chris Pine

### 🚀 **From Idea to Reality**
Programming is the closest thing to having superpowers in the real world. You can:
- **Automate boring tasks** - Never do repetitive work again
- **Solve real problems** - Build tools that help millions of people
- **Create from nothing** - Turn your wildest ideas into working software
- **Work from anywhere** - Your office is wherever you have a laptop

### 💡 **The Problem-Solving Mindset**
Learning Python teaches you to think differently:
- Break big challenges into smaller, manageable pieces
- Find patterns and create reusable solutions
- Think logically while staying creative

---

**Created during my Python learning journey - from basics to advanced concepts with practical, production-ready examples.**
