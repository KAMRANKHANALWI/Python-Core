# Python Loops - Essential Examples
"""
Concise, high-value examples of Python loops.
Focus on practical patterns you'll use in real applications.
"""

print("Python Loops - Essential Patterns")
print("=" * 50)

# ===== FOR LOOPS =====
print("\n1. FOR LOOPS")
print("-" * 30)

# Basic iteration
numbers = [1, 2, 3, 4, 5]
print("Basic iteration:")
for num in numbers:
    print(f"Number: {num}")

# With index using enumerate
print("\nWith index:")
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Range variations
print("\nRange patterns:")
for i in range(5):  # 0 to 4
    print(f"Count: {i}")

for i in range(2, 8):  # 2 to 7
    print(f"Range: {i}")

for i in range(0, 10, 2):  # Even numbers 0-8
    print(f"Even: {i}")

# Dictionary iteration
print("\nDictionary iteration:")
student = {"name": "Alice", "age": 20, "grade": "A"}

for key in student:
    print(f"{key}: {student[key]}")

for key, value in student.items():
    print(f"{key} → {value}")

# ===== WHILE LOOPS =====
print("\n2. WHILE LOOPS")
print("-" * 30)

# Basic while loop
print("Countdown:")
count = 5
while count > 0:
    print(f"T-minus {count}")
    count -= 1
print("🚀 Liftoff!")

# While with user input simulation
print("\nMenu system:")
menu_choice = 0
options = ["Exit", "View Profile", "Settings", "Help"]

while menu_choice != 1:  # Simulate choosing option 1
    menu_choice += 1
    if menu_choice < len(options):
        print(f"Selected: {options[menu_choice]}")

# ===== LOOP CONTROL =====
print("\n3. LOOP CONTROL")
print("-" * 30)

# Break - exit loop early
print("Finding first even number:")
numbers = [1, 3, 7, 8, 9, 12]
for num in numbers:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break
    print(f"Checking {num}...")

# Continue - skip iteration
print("\nSkipping odd numbers:")
for num in range(1, 11):
    if num % 2 == 1:
        continue
    print(f"Even: {num}")

# Else clause (runs if loop completes normally)
print("\nLoop else clause:")
for num in [2, 4, 6, 8]:
    if num % 3 == 0:
        print(f"Found divisible by 3: {num}")
        break
else:
    print("No numbers divisible by 3 found")

# ===== LIST COMPREHENSIONS =====
print("\n4. LIST COMPREHENSIONS")
print("-" * 30)

# Basic comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers: {evens}")

# String processing
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(f"Word lengths: {lengths}")

# Nested comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Multiplication table: {matrix}")

# ===== NESTED LOOPS =====
print("\n5. NESTED LOOPS")
print("-" * 30)

# Basic nested loop
print("Coordinate grid:")
for row in range(3):
    for col in range(3):
        print(f"({row},{col})", end=" ")
    print()  # New line after each row

# Processing 2D data
print("\nGrade table:")
students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "Science", "English"]
grades = [[90, 85, 92], [78, 80, 75], [88, 91, 87]]

for i, student in enumerate(students):
    print(f"\n{student}:")
    for j, subject in enumerate(subjects):
        print(f"  {subject}: {grades[i][j]}")

# ===== REAL-WORLD EXAMPLES =====
print("\n6. REAL-WORLD APPLICATIONS")
print("-" * 50)


# Example 1: Data Processing
def analyze_sales_data(sales):
    """Process sales data and generate report."""
    total_sales = 0
    best_day = ""
    best_amount = 0

    print("📊 Sales Analysis:")
    for day, amount in sales.items():
        total_sales += amount
        if amount > best_amount:
            best_amount = amount
            best_day = day
        print(f"  {day}: ${amount:,.2f}")

    avg_sales = total_sales / len(sales)

    print(f"\n📈 Summary:")
    print(f"  Total Sales: ${total_sales:,.2f}")
    print(f"  Average Daily: ${avg_sales:,.2f}")
    print(f"  Best Day: {best_day} (${best_amount:,.2f})")


# Test sales analysis
weekly_sales = {
    "Monday": 1250.50,
    "Tuesday": 980.75,
    "Wednesday": 1450.25,
    "Thursday": 1100.00,
    "Friday": 1680.80,
}
analyze_sales_data(weekly_sales)


# Example 2: User Input Validation
def get_valid_age():
    """Get valid age input from user with retry logic."""
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        try:
            # Simulate user input
            test_inputs = ["25", "abc", "150", "30"]
            user_input = test_inputs[attempts] if attempts < len(test_inputs) else "25"
            print(f"\nAttempt {attempts + 1}: Input '{user_input}'")

            age = int(user_input)
            if 0 <= age <= 120:
                print(f"✅ Valid age: {age}")
                return age
            else:
                print("❌ Age must be between 0-120")
        except ValueError:
            print("❌ Please enter a valid number")

        attempts += 1

    print("❌ Too many invalid attempts")
    return None


get_valid_age()


# Example 3: Password Generator
def generate_passwords(count=3):
    """Generate multiple secure passwords."""
    import random
    import string

    print(f"\n🔐 Generated {count} passwords:")

    for i in range(count):
        # Create character pool
        chars = string.ascii_letters + string.digits + "!@#$%"
        password = ""

        # Generate 12-character password
        for _ in range(12):
            password += random.choice(chars)

        print(f"  Password {i+1}: {password}")


generate_passwords()


# Example 4: Inventory Management
def process_inventory(items):
    """Process inventory and identify issues."""
    print("\n📦 Inventory Report:")

    low_stock = []
    out_of_stock = []
    total_value = 0

    for item_name, details in items.items():
        stock = details["stock"]
        price = details["price"]
        value = stock * price
        total_value += value

        # Check stock levels
        if stock == 0:
            out_of_stock.append(item_name)
            status = "❌ OUT OF STOCK"
        elif stock < 10:
            low_stock.append(item_name)
            status = "⚠️ LOW STOCK"
        else:
            status = "✅ IN STOCK"

        print(f"  {item_name}: {stock} units @ ${price} = ${value:.2f} {status}")

    print(f"\n📊 Inventory Summary:")
    print(f"  Total Value: ${total_value:,.2f}")

    if out_of_stock:
        print(f"  Out of Stock: {', '.join(out_of_stock)}")

    if low_stock:
        print(f"  Low Stock Alert: {', '.join(low_stock)}")


# Test inventory
inventory = {
    "Laptops": {"stock": 15, "price": 999.99},
    "Mice": {"stock": 5, "price": 25.50},
    "Keyboards": {"stock": 0, "price": 75.00},
    "Monitors": {"stock": 8, "price": 299.99},
}
process_inventory(inventory)


# Example 5: Text Analysis
def analyze_text(text):
    """Analyze text for various metrics."""
    print(f"\n📝 Text Analysis:")
    print(f"Original: '{text}'")

    # Character analysis
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    # Word analysis
    words = text.lower().split()
    word_count = {}
    for word in words:
        # Remove punctuation
        clean_word = "".join(c for c in word if c.isalnum())
        if clean_word:
            word_count[clean_word] = word_count.get(clean_word, 0) + 1

    print(f"\n📊 Results:")
    print(f"  Characters: {len(text)}")
    print(f"  Words: {len(words)}")
    print(f"  Unique words: {len(word_count)}")

    # Most common characters
    print(f"  Most common letters:")
    for char, count in sorted(char_count.items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"    '{char}': {count}")

    # Most common words
    if word_count:
        print(f"  Most common words:")
        for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True)[
            :3
        ]:
            print(f"    '{word}': {count}")


analyze_text("Python is great. Python is powerful. Python makes coding fun!")


# Example 6: Game Score Tracker
def track_game_scores():
    """Track scores for multiple players across rounds."""
    players = ["Alice", "Bob", "Charlie"]
    rounds = 3
    scores = {player: [] for player in players}

    print(f"\n🎮 Game Score Tracking ({rounds} rounds):")

    # Simulate scores for each round
    import random

    for round_num in range(1, rounds + 1):
        print(f"\n  Round {round_num}:")
        round_scores = {}

        for player in players:
            score = random.randint(50, 100)
            scores[player].append(score)
            round_scores[player] = score
            print(f"    {player}: {score}")

        # Find round winner
        round_winner = max(round_scores, key=round_scores.get)
        print(f"    🏆 Round winner: {round_winner}")

    # Calculate final results
    print(f"\n🏆 Final Results:")
    final_scores = {}
    for player in players:
        total = sum(scores[player])
        average = total / len(scores[player])
        final_scores[player] = total
        print(f"  {player}: Total = {total}, Average = {average:.1f}")

    # Game winner
    game_winner = max(final_scores, key=final_scores.get)
    print(f"\n🎉 Game Winner: {game_winner} with {final_scores[game_winner]} points!")


track_game_scores()

# ===== LOOP OPTIMIZATION PATTERNS =====
print("\n7. OPTIMIZATION PATTERNS")
print("-" * 40)

# Using enumerate instead of range(len())
items = ["apple", "banana", "cherry"]

# Good: enumerate
print("Using enumerate:")
for i, item in enumerate(items):
    print(f"  {i}: {item}")

# Using zip for parallel iteration
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

print("\nUsing zip:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name}, {age}, from {city}")

# Generator expressions for memory efficiency
print("\nMemory-efficient processing:")
large_data = range(1000000)  # Simulate large dataset
squares_sum = sum(x**2 for x in large_data if x % 2 == 0)
print(f"  Sum of even squares: {squares_sum}")

print("\n" + "=" * 50)
print("✅ Essential loop patterns demonstrated!")
print("💡 Focus: Practical patterns for real applications")
