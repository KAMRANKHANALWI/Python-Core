# Python Loops - Essential Guide

## Table of Contents

1. [For Loops](#for-loops)
2. [While Loops](#while-loops)
3. [Loop Control](#loop-control)
4. [List Comprehensions](#list-comprehensions)
5. [Real-World Patterns](#real-world-patterns)
6. [Best Practices](#best-practices)

---

## For Loops

### Basic Iteration

```python
# Iterate over lists
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Iterate over strings
for char in "Python":
    print(char)
```

### Using enumerate()

Get both index and value:

```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start index from 1
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")
```

### Range Functions

```python
for i in range(5):          # 0, 1, 2, 3, 4
for i in range(2, 8):       # 2, 3, 4, 5, 6, 7
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
for i in range(10, 0, -1):  # 10, 9, 8, ..., 1
```

### Dictionary Iteration

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# Keys only
for key in student:
    print(key)

# Key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

# Values only
for value in student.values():
    print(value)
```

---

## While Loops

### Basic While Loop

```python
count = 5
while count > 0:
    print(f"Count: {count}")
    count -= 1
```

### Input Validation Pattern

```python
def get_valid_input():
    while True:
        user_input = input("Enter a number: ")
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input, try again")
```

### Flag-Controlled Loop

```python
running = True
while running:
    choice = input("Continue? (y/n): ")
    if choice.lower() == 'n':
        running = False
```

---

## Loop Control

### Break Statement

Exit loop early:

```python
# Find first even number
for num in [1, 3, 7, 8, 9]:
    if num % 2 == 0:
        print(f"Found: {num}")
        break
```

### Continue Statement

Skip current iteration:

```python
# Skip odd numbers
for num in range(1, 11):
    if num % 2 == 1:
        continue
    print(num)  # Only prints even numbers
```

### Else Clause

Runs if loop completes normally (no break):

```python
for num in [2, 4, 6]:
    if num % 3 == 0:
        print("Found divisible by 3")
        break
else:
    print("No number divisible by 3 found")
```

---

## List Comprehensions

### Basic Syntax

```python
# Traditional loop
squares = []
for x in range(1, 6):
    squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(1, 6)]
```

### With Conditions

```python
# Even numbers only
evens = [x for x in range(1, 11) if x % 2 == 0]

# Transform strings
words = ["hello", "world"]
upper_words = [word.upper() for word in words]
```

### Nested Comprehensions

```python
# 2D matrix
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [num for sublist in nested for num in sublist]
```

### Dictionary and Set Comprehensions

```python
# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}

# Set comprehension
unique_lengths = {len(word) for word in ["hello", "world", "hi"]}
```

---

## Real-World Patterns

### Data Processing

```python
def process_sales_data(sales):
    total = sum(sales.values())
    best_day = max(sales, key=sales.get)

    for day, amount in sales.items():
        percentage = (amount / total) * 100
        print(f"{day}: ${amount:,.2f} ({percentage:.1f}%)")

    return {"total": total, "best_day": best_day}
```

### Batch Processing

```python
def process_in_batches(data, batch_size=100):
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        yield batch  # Generator for memory efficiency

# Usage
large_dataset = range(1000)
for batch in process_in_batches(large_dataset, 50):
    # Process each batch
    result = sum(batch)
```

### File Processing

```python
def analyze_log_file(filename):
    error_count = 0
    warning_count = 0

    with open(filename, 'r') as file:
        for line_num, line in enumerate(file, 1):
            if 'ERROR' in line:
                error_count += 1
                print(f"Line {line_num}: {line.strip()}")
            elif 'WARNING' in line:
                warning_count += 1

    return {"errors": error_count, "warnings": warning_count}
```

### Search and Filter

```python
def find_users_by_criteria(users, min_age=18, city=None):
    matches = []
    for user in users:
        if user["age"] >= min_age:
            if city is None or user["city"] == city:
                matches.append(user)
    return matches

# List comprehension version
def find_users_comprehension(users, min_age=18, city=None):
    return [user for user in users
            if user["age"] >= min_age and (city is None or user["city"] == city)]
```

---

## Best Practices

### 1. Choose the Right Loop Type

```python
# Use for loops for known iterations
for i in range(10):
    process_item(i)

# Use while loops for unknown iterations
while not condition_met():
    continue_processing()
```

### 2. Use enumerate() Instead of range(len())

```python
# Avoid this
items = ["a", "b", "c"]
for i in range(len(items)):
    print(f"{i}: {items[i]}")

# Prefer this
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

### 3. Use zip() for Parallel Iteration

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

# Good: zip for parallel iteration
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

### 4. Prefer List Comprehensions for Simple Cases

```python
# Simple transformation - use comprehension
squares = [x**2 for x in range(10)]

# Complex logic - use regular loop
results = []
for item in data:
    if complex_condition(item):
        processed = complex_processing(item)
        if processed is not None:
            results.append(processed)
```

### 5. Use Generators for Large Datasets

```python
# Memory efficient for large data
def process_large_file(filename):
    with open(filename) as file:
        for line in file:
            yield process_line(line)

# Use generator expression
large_sum = sum(x**2 for x in range(1000000) if x % 2 == 0)
```

### 6. Avoid Modifying Lists While Iterating

```python
# Wrong: modifying list during iteration
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Dangerous!

# Right: create new list or iterate backwards
numbers = [num for num in numbers if num % 2 != 0]

# Or iterate backwards
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        numbers.pop(i)
```

### 7. Break Early When Possible

```python
# Find first match and exit
def find_user(users, target_id):
    for user in users:
        if user["id"] == target_id:
            return user  # Exit immediately when found
    return None
```

---

## Performance Tips

| Pattern              | Use Case               | Example                            |
| -------------------- | ---------------------- | ---------------------------------- |
| `for` loop           | Known iterations       | `for i in range(10):`              |
| `while` loop         | Condition-based        | `while not done:`                  |
| List comprehension   | Simple transformations | `[x*2 for x in data]`              |
| Generator expression | Large datasets         | `sum(x for x in huge_data)`        |
| `enumerate()`        | Need index + value     | `for i, item in enumerate(items):` |
| `zip()`              | Parallel iteration     | `for a, b in zip(list1, list2):`   |
| `break`              | Early exit             | Exit when condition met            |
| `continue`           | Skip iteration         | Skip invalid items                 |

**Key Takeaway**: Choose the right loop pattern for your specific use case, prioritize readability, and optimize for performance when working with large datasets.
