# Python Basics

print("🐍 Python Basics Made Simple")
print("=" * 40)

# ===== 1. NUMBERS =====
print("\n📊 NUMBERS")
print("-" * 20)

# Basic math
a = 10
b = 3
print(f"{a} + {b} = {a + b}")  # Addition
print(f"{a} - {b} = {a - b}")  # Subtraction
print(f"{a} * {b} = {a * b}")  # Multiplication
print(f"{a} / {b} = {a / b}")  # Division

# Useful number functions
price = 19.99
print(f"Rounded price: ${round(price)}")
print(f"Absolute value of -5: {abs(-5)}")

# ===== 2. STRINGS =====
print("\n📝 STRINGS")
print("-" * 20)

name = "Alice"
age = 25

# String basics
print(f"Hello, my name is {name}")  # Simple text
print(f"First letter: {name[0]}")  # Get first character
print(f"Last letter: {name[-1]}")  # Get last character
print(f"Uppercase: {name.upper()}")  # Make uppercase
print(f"Length: {len(name)} characters")  # Count characters

# Combining strings
greeting = f"Hi {name}, you are {age} years old"
print(greeting)

# ===== 3. LISTS =====
print("\n📋 LISTS")
print("-" * 20)

# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]

print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")  # Get first item
print(f"Last fruit: {fruits[-1]}")  # Get last item

# Adding to lists
fruits.append("grape")  # Add to end
print(f"After adding grape: {fruits}")

# Removing from lists
fruits.remove("banana")  # Remove specific item
print(f"After removing banana: {fruits}")

# List operations
print(f"Number of fruits: {len(fruits)}")
print(f"Sorted fruits: {sorted(fruits)}")

# ===== 4. DICTIONARIES =====
print("\n📚 DICTIONARIES")
print("-" * 20)

# Creating dictionaries (like a phone book)
person = {"name": "Bob", "age": 30, "city": "New York"}

print(f"Person info: {person}")
print(f"Name: {person['name']}")  # Get value by key
print(f"Age: {person['age']}")

# Adding new information
person["job"] = "Teacher"  # Add new key-value pair
print(f"Updated person: {person}")

# Getting all keys and values
print(f"All keys: {list(person.keys())}")
print(f"All values: {list(person.values())}")

# ===== 5. TUPLES =====
print("\n📍 TUPLES")
print("-" * 20)

# Tuples are like lists but can't be changed
coordinates = (10, 20)
colors = ("red", "green", "blue")

print(f"Point location: {coordinates}")
print(f"X coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")
print(f"Available colors: {colors}")

# Unpacking tuples
x, y = coordinates
print(f"x = {x}, y = {y}")

# ===== SIMPLE EXAMPLES =====
print("\n🌟 PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Shopping list
print("📝 Shopping List Manager:")
shopping_list = []
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")

print(f"Need to buy: {shopping_list}")
print(f"Total items: {len(shopping_list)}")

# Example 2: Simple grade calculator
print("\n📊 Grade Calculator:")
grades = [85, 92, 78, 96, 88]
average = sum(grades) / len(grades)
print(f"Grades: {grades}")
print(f"Average: {average:.1f}")
print(f"Highest: {max(grades)}")
print(f"Lowest: {min(grades)}")

# Example 3: Contact book
print("\n📞 Contact Book:")
contacts = {"Mom": "555-0123", "Dad": "555-0124", "Best Friend": "555-0125"}

print("My contacts:")
for name, phone in contacts.items():
    print(f"  {name}: {phone}")

# Example 4: Word counter
print("\n🔢 Word Counter:")
sentence = "Python is fun and Python is easy"
words = sentence.split()
word_count = len(words)
print(f"Sentence: '{sentence}'")
print(f"Number of words: {word_count}")

# Count specific word
python_count = words.count("Python")
print(f"'Python' appears {python_count} times")

print("\n" + "=" * 40)
print("✅ That's it! You now know Python basics!")
print("💡 Practice with these examples to get better!")

# ===== QUICK REFERENCE =====
print("\n📋 QUICK REFERENCE")
print("-" * 25)
print("Numbers: 42, 3.14")
print("Strings: 'hello', \"world\"")
print("Lists: [1, 2, 3] - can change")
print("Tuples: (1, 2, 3) - cannot change")
print("Dictionaries: {'key': 'value'}")
print("\nRemember:")
print("• Use square brackets [] for lists")
print("• Use curly braces {} for dictionaries")
print("• Use parentheses () for tuples")
print("• Use quotes '' or \"\" for strings")
