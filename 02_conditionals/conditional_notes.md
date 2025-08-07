# Python Conditionals - Essential Guide

## Table of Contents

1. [Basic Conditional Structures](#basic-conditional-structures)
2. [Operators](#operators)
3. [Advanced Patterns](#advanced-patterns)
4. [Real-World Examples](#real-world-examples)
5. [Best Practices](#best-practices)

---

## Basic Conditional Structures

### if, elif, else

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### Ternary Operator

```python
# Concise conditional assignment
status = "adult" if age >= 18 else "minor"

# Multiple conditions
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
```

---

## Operators

### Comparison Operators

```python
# Basic comparisons
if age == 18:           # Equal
if age != 18:           # Not equal
if age < 18:            # Less than
if age >= 18:           # Greater than or equal

# Chained comparisons
if 18 <= age < 65:      # Between values
if name in ["Alice", "Bob"]:  # Membership
```

### Logical Operators

```python
# AND - both conditions must be true
if age >= 18 and has_license:
    print("Can drive")

# OR - at least one condition must be true
if is_weekend or is_holiday:
    print("Day off")

# NOT - reverses condition
if not is_raining:
    print("Go outside")
```

### Membership and Identity

```python
# Membership testing
if "admin" in user_roles:
    grant_access()

# Identity checking (use with None)
if value is None:
    handle_empty_value()
```

---

## Advanced Patterns

### Guard Clauses

Clean validation with early returns:

```python
def process_user(user):
    # Handle invalid cases first
    if user is None:
        return "No user provided"

    if not user.is_active:
        return "User inactive"

    # Main logic
    return perform_action(user)
```

### Dictionary-Based Conditionals

Replace long if-elif chains:

```python
def get_grade_message(grade):
    messages = {
        "A": "Excellent work!",
        "B": "Good job!",
        "C": "Satisfactory",
        "D": "Needs improvement",
        "F": "Failed"
    }
    return messages.get(grade, "Invalid grade")
```

### Using all() and any()

```python
grades = [85, 90, 78, 92]

# Check if all conditions are met
if all(grade >= 60 for grade in grades):
    print("All subjects passed")

# Check if any condition is met
if any(grade >= 90 for grade in grades):
    print("At least one excellent grade")
```

---

## Real-World Examples

### User Authentication

```python
def authenticate(username, password, attempts=0):
    MAX_ATTEMPTS = 3

    if attempts >= MAX_ATTEMPTS:
        return "Account locked"

    if username == "admin" and password == "secure123":
        return "Login successful"

    return f"Invalid credentials. {MAX_ATTEMPTS - attempts - 1} attempts left"
```

### Shopping Cart with Discounts

```python
def calculate_total(amount, is_member=False, coupon_code=None):
    # Apply member discount
    if is_member:
        amount *= 0.9  # 10% discount

    # Apply coupon
    if coupon_code == "SAVE20" and amount > 100:
        amount *= 0.8  # Additional 20% off

    return round(amount, 2)
```

### Grade Calculator

```python
def assign_grade(score):
    if not 0 <= score <= 100:
        return "Invalid score"

    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"
```

---

## Best Practices

### 1. Keep Conditions Simple

```python
# Good: Clear and readable
is_eligible = age >= 18 and has_license and not is_suspended
if is_eligible:
    allow_driving()

# Avoid: Complex nested conditions
if age >= 18:
    if has_license:
        if not is_suspended:
            allow_driving()
```

### 2. Use Positive Logic

```python
# Good: Positive condition
if user.is_authenticated:
    show_dashboard()

# Avoid: Double negative
if not user.is_not_authenticated:
    show_dashboard()
```

### 3. Handle Edge Cases

```python
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b
```

### 4. Use Constants for Magic Numbers

```python
ADULT_AGE = 18
RETIREMENT_AGE = 65

if ADULT_AGE <= age < RETIREMENT_AGE:
    category = "working_age"
```

### 5. Prefer Early Returns

```python
def process_order(order):
    if not order:
        return "No order"

    if not order.items:
        return "Empty cart"

    if not order.payment_method:
        return "Payment required"

    return "Order processed"
```

---

## Common Patterns Summary

| Pattern           | Use Case               | Example                                |
| ----------------- | ---------------------- | -------------------------------------- |
| Simple if         | Single condition       | `if age >= 18:`                        |
| if-elif-else      | Multiple options       | Grade assignment                       |
| Ternary           | Conditional assignment | `status = "A" if score >= 90 else "B"` |
| Guard clauses     | Input validation       | Early returns for invalid data         |
| Dictionary lookup | Replace long if-elif   | `result = mapping.get(key)`            |
| all()/any()       | Multiple conditions    | `all(grade >= 60 for grade in grades)` |

**Key Takeaway**: Write conditions that are clear, handle edge cases, and use the simplest pattern that solves the problem effectively.
