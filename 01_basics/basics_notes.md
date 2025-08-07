# Python Fundamentals - Essential Guide

## Table of Contents

1. [Numbers](#numbers)
2. [Strings](#strings)
3. [Lists](#lists)
4. [Dictionaries](#dictionaries)
5. [Tuples](#tuples)
6. [Data Type Comparison](#data-type-comparison)
7. [Best Practices](#best-practices)

---

## Numbers

### Basic Operations

```python
# Integer operations
a, b = 10, 3
print(a + b)    # Addition: 13
print(a // b)   # Floor division: 3
print(a % b)    # Modulus: 1
print(a ** b)   # Exponentiation: 1000

# Float operations
x = 3.14159
print(round(x, 2))      # 3.14
print(abs(-x))          # 3.14159
```

### Math Functions

```python
import math
print(math.sqrt(16))    # 4.0
print(math.ceil(3.2))   # 4
print(math.floor(3.8))  # 3
```

### Type Conversions

```python
print(int(3.14))        # 3
print(float(42))        # 42.0
print(str(123))         # "123"
```

### Random Numbers

```python
import random
print(random.randint(1, 10))        # Random integer 1-10
print(random.choice([1, 2, 3]))     # Random choice
```

---

## Strings

### Creation and Access

```python
text = "Python"
print(text[0])      # First character: 'P'
print(text[-1])     # Last character: 'n'
print(text[1:4])    # Slice: 'yth'
print(text[::-1])   # Reverse: 'nohtyP'
```

### Essential Methods

```python
text = "  Hello Python World  "
print(text.strip())                 # "Hello Python World"
print(text.lower())                 # "  hello python world  "
print(text.replace("Python", "Java"))  # Replace substring
print(text.strip().split())         # ['Hello', 'Python', 'World']
```

### String Formatting

```python
name, age, score = "Alice", 25, 95.67

# f-strings (preferred)
print(f"Hello {name}, age {age}, score {score:.1f}")

# .format() method
print("Hello {}, age {}, score {:.1f}".format(name, age, score))
```

### String Validation

```python
text = "123"
print(text.isdigit())   # True
print(text.isalpha())   # False
print(text.isalnum())   # True
```

---

## Lists

### Creation and Access

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])        # "apple"
print(fruits[-1])       # "cherry"
print(fruits[1:3])      # ["banana", "cherry"]
```

### Modifying Lists

```python
# Adding elements
fruits.append("date")                   # Add to end
fruits.insert(1, "blueberry")          # Insert at position
fruits.extend(["elderberry", "fig"])   # Add multiple

# Removing elements
fruits.remove("banana")     # Remove first occurrence
last = fruits.pop()         # Remove and return last item
item = fruits.pop(1)        # Remove at index
```

### List Methods

```python
numbers = [3, 1, 4, 1, 5]
print(len(numbers))         # Length: 5
print(numbers.count(1))     # Count occurrences: 2
print(numbers.index(4))     # Find index: 2

numbers.sort()              # Sort in place
numbers.reverse()           # Reverse in place
```

### List Comprehensions

```python
# Basic comprehension
squares = [x**2 for x in range(1, 6)]       # [1, 4, 9, 16, 25]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Processing strings
words = ["hello", "world"]
lengths = [len(word) for word in words]      # [5, 5]
```

---

## Dictionaries

### Creation and Access

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# Access methods
print(student["name"])              # Direct access
print(student.get("age"))           # Safe access
print(student.get("gpa", 0.0))      # With default value
```

### Modifying Dictionaries

```python
# Add/update elements
student["gpa"] = 3.8                # Add new key
student["age"] = 21                 # Update existing

# Update multiple
student.update({"major": "CS", "year": "Junior"})

# Remove elements
gpa = student.pop("gpa")            # Remove and return
last_item = student.popitem()       # Remove last item
```

### Dictionary Methods

```python
print(list(student.keys()))         # All keys
print(list(student.values()))       # All values
print(list(student.items()))        # Key-value pairs

# Iteration
for key, value in student.items():
    print(f"{key}: {value}")
```

### Dictionary Comprehensions

```python
# Basic comprehension
squares = {x: x**2 for x in range(1, 6)}

# From lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
```

---

## Tuples

### Creation and Access

```python
point = (5, 10, 15)
print(point[0])         # First element: 5
print(point[-1])        # Last element: 15

# Single element tuple (note the comma)
single = (42,)
```

### Tuple Methods

```python
data = (1, 2, 3, 2, 4, 2, 5)
print(len(data))        # Length: 7
print(data.count(2))    # Count: 3
print(data.index(4))    # Index: 4
```

### Tuple Unpacking

```python
# Basic unpacking
person = ("Alice", 25, "Engineer")
name, age, profession = person

# Swapping variables
a, b = 10, 20
a, b = b, a     # Swap: a=20, b=10

# Extended unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers  # first=1, middle=[2,3,4], last=5
```

### Named Tuples

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)     # 10 20
print(p[0])         # 10 (also works with index)
```

---

## Data Type Comparison

### Mutability

| Mutable      | Immutable |
| ------------ | --------- |
| Lists        | Numbers   |
| Dictionaries | Strings   |
| Sets         | Tuples    |

### When to Use Each

| Type       | Use Case                 | Example                               |
| ---------- | ------------------------ | ------------------------------------- |
| **List**   | Ordered, changeable data | `shopping_list = ["milk", "bread"]`   |
| **Dict**   | Key-value mapping        | `user = {"name": "Alice", "age": 25}` |
| **Tuple**  | Immutable sequences      | `coordinates = (10, 20)`              |
| **String** | Text processing          | `message = "Hello World"`             |

### Type Conversions

```python
# Between sequential types
data_list = [1, 2, 3]
data_tuple = tuple(data_list)       # List to tuple
back_to_list = list(data_tuple)     # Tuple to list

# String conversions
text = "hello"
char_list = list(text)              # ['h', 'e', 'l', 'l', 'o']
back_to_string = ''.join(char_list) # "hello"
```

---

## Best Practices

### 1. Choose Appropriate Data Types

```python
# Good choices
user_coordinates = (x, y)          # Tuple for fixed pair
shopping_items = []                 # List for changing collection
user_profile = {}                   # Dict for key-value data
user_message = ""                   # String for text
```

### 2. Safe Access Patterns

```python
# Dictionary safe access
def get_user_info(user_dict, key):
    return user_dict.get(key, "Not found")

# List safe access
def get_list_item(data, index):
    if 0 <= index < len(data):
        return data[index]
    return None
```

### 3. Efficient Operations

```python
# Use comprehensions for simple transformations
squares = [x**2 for x in range(10)]

# Use dict.get() instead of key checking
count = word_count.get(word, 0) + 1

# Use join() for string concatenation
result = " ".join(words)  # Better than += in loops
```

### 4. Memory Considerations

```python
# Use generators for large datasets
def process_large_data(data):
    for item in data:
        yield process_item(item)

# Choose appropriate structures
small_lookup = ["a", "b", "c"]      # List for small collections
large_lookup = {"a": 1, "b": 2}     # Dict for fast lookups
```

### 5. Error Handling

```python
def safe_convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

def safe_divide(a, b):
    if b == 0:
        return None
    return a / b
```

---

## Real-World Example: Data Processing

```python
def analyze_student_data(students):
    """Process student data and generate report."""

    # Input: List of dictionaries
    # students = [
    #     {"name": "Alice", "grades": [85, 90, 88]},
    #     {"name": "Bob", "grades": [78, 85, 80]}
    # ]

    results = {}

    for student in students:
        name = student["name"]
        grades = student["grades"]

        # Calculate statistics
        average = sum(grades) / len(grades)
        highest = max(grades)
        lowest = min(grades)

        # Assign letter grade
        if average >= 90:
            letter = "A"
        elif average >= 80:
            letter = "B"
        elif average >= 70:
            letter = "C"
        else:
            letter = "F"

        # Store results
        results[name] = {
            "average": round(average, 1),
            "letter_grade": letter,
            "range": (lowest, highest)
        }

    return results

# Usage
student_data = [
    {"name": "Alice", "grades": [85, 90, 88, 92]},
    {"name": "Bob", "grades": [78, 85, 80, 87]}
]

report = analyze_student_data(student_data)
for name, stats in report.items():
    print(f"{name}: {stats['letter_grade']} (Avg: {stats['average']})")
```

**Key Takeaway**: Master these fundamental data types and their operations. Choose the right type for each situation, use built-in methods efficiently, and handle errors gracefully for robust code.
