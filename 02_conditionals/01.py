# Python Conditionals - Essential Examples
"""
Concise, high-value examples of Python conditional statements.
Focus on practical patterns you'll use in real applications.
"""

print("Python Conditionals - Essential Patterns")
print("=" * 50)

# ===== BASIC CONDITIONALS =====
print("\n1. BASIC PATTERNS")
print("-" * 30)

# Simple if-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Score {score} → Grade {grade}")

# Ternary operator
age = 17
status = "adult" if age >= 18 else "minor"
print(f"Age {age} → Status: {status}")

# Multiple ternary
temperature = 25
clothing = "shorts" if temperature > 25 else "jacket" if temperature < 15 else "t-shirt"
print(f"Temperature {temperature}°C → Wear: {clothing}")

# ===== OPERATORS =====
print("\n2. OPERATORS")
print("-" * 30)

# Logical operators
age = 25
has_license = True
if age >= 18 and has_license:
    print("✅ Can drive")

# Membership
user_roles = ["admin", "editor"]
if "admin" in user_roles:
    print("✅ Admin access granted")

# Chained comparisons
score = 85
if 80 <= score < 90:
    print("✅ Grade B range")

# ===== ADVANCED PATTERNS =====
print("\n3. ADVANCED PATTERNS")
print("-" * 30)


# Guard clauses
def validate_user(user_data):
    if not user_data:
        return "❌ No data provided"

    if "email" not in user_data:
        return "❌ Email required"

    if "@" not in user_data["email"]:
        return "❌ Invalid email format"

    return "✅ User valid"


# Test validation
test_users = [
    {"email": "user@example.com"},
    {"email": "invalid-email"},
    {"name": "John"},  # Missing email
    None,
]

for i, user in enumerate(test_users):
    result = validate_user(user)
    print(f"User {i+1}: {result}")


# Dictionary-based conditionals
def get_day_plan(day):
    plans = {
        "monday": "Team meeting",
        "tuesday": "Code review",
        "wednesday": "Development",
        "thursday": "Testing",
        "friday": "Deployment",
    }
    return plans.get(day.lower(), "Weekend - No work!")


print(f"\nToday's plan: {get_day_plan('friday')}")

# Using all() and any()
grades = [85, 90, 78, 92, 88]
print(f"\nGrades: {grades}")
print(f"All passing (≥60): {all(grade >= 60 for grade in grades)}")
print(f"Any excellent (≥90): {any(grade >= 90 for grade in grades)}")

# ===== REAL-WORLD EXAMPLES =====
print("\n4. REAL-WORLD APPLICATIONS")
print("-" * 30)


# Authentication system
def authenticate(username, password, attempts=0):
    MAX_ATTEMPTS = 3
    VALID_USERS = {"admin": "pass123", "user": "secret"}

    if attempts >= MAX_ATTEMPTS:
        return {"success": False, "message": "🔒 Account locked"}

    if username not in VALID_USERS:
        return {"success": False, "message": "❌ User not found"}

    if VALID_USERS[username] == password:
        return {"success": True, "message": "✅ Login successful"}

    remaining = MAX_ATTEMPTS - attempts - 1
    return {
        "success": False,
        "message": f"❌ Wrong password. {remaining} attempts left",
    }


# Test authentication
auth_tests = [
    ("admin", "pass123", 0),
    ("admin", "wrong", 1),
    ("user", "secret", 0),
    ("nobody", "test", 0),
]

print("\n🔐 Authentication Tests:")
for username, password, attempts in auth_tests:
    result = authenticate(username, password, attempts)
    print(f"{username}/{password}: {result['message']}")


# Shopping cart with discounts
def calculate_total(items, is_member=False, coupon=None):
    total = sum(item["price"] * item["qty"] for item in items)
    original = total

    # Member discount
    if is_member and total > 50:
        total *= 0.9
        print(f"💳 Member discount applied: 10% off")

    # Coupon discount
    if coupon == "SAVE20" and total > 100:
        total *= 0.8
        print(f"🎟️ Coupon SAVE20 applied: 20% off")
    elif coupon == "SAVE10":
        total *= 0.9
        print(f"🎟️ Coupon SAVE10 applied: 10% off")

    savings = original - total
    return {"total": round(total, 2), "savings": round(savings, 2)}


# Test shopping cart
cart = [
    {"name": "Laptop", "price": 999, "qty": 1},
    {"name": "Mouse", "price": 25, "qty": 2},
]

print(f"\n🛒 Shopping Cart:")
for item in cart:
    print(f"- {item['name']}: ${item['price']} x {item['qty']}")

result = calculate_total(cart, is_member=True, coupon="SAVE20")
print(f"💰 Total: ${result['total']} (Saved: ${result['savings']})")


# Grade management
def process_grades(student_grades):
    def letter_grade(score):
        return (
            "A"
            if score >= 90
            else (
                "B"
                if score >= 80
                else "C" if score >= 70 else "D" if score >= 60 else "F"
            )
        )

    def academic_status(gpa):
        if gpa >= 3.7:
            return "Dean's List"
        elif gpa >= 3.0:
            return "Good Standing"
        elif gpa >= 2.0:
            return "Probation"
        else:
            return "Academic Warning"

    results = {}
    for student, grades in student_grades.items():
        avg = sum(grades) / len(grades)
        gpa = avg / 25  # Convert to 4.0 scale (simplified)

        results[student] = {
            "average": round(avg, 1),
            "letter": letter_grade(avg),
            "gpa": round(gpa, 2),
            "status": academic_status(gpa),
        }

    return results


# Test grade processing
students = {
    "Alice": [92, 88, 95, 90],
    "Bob": [78, 82, 75, 80],
    "Charlie": [65, 70, 68, 72],
}

print(f"\n📊 Grade Report:")
grade_results = process_grades(students)
for student, data in grade_results.items():
    print(f"{student}: {data['letter']} (Avg: {data['average']}) - {data['status']}")


# Weather-based recommendations
def recommend_activity(weather, temp):
    if weather == "rainy":
        return "☔ Stay indoors - perfect for coding!"
    elif weather == "sunny":
        if temp > 25:
            return "🏖️ Beach day!"
        elif temp > 15:
            return "🚶 Great for a walk!"
        else:
            return "🧥 Sunny but cold - wear a jacket!"
    elif weather == "snowy":
        return "⛄ Build a snowman!" if temp > -5 else "🏠 Too cold - stay warm inside!"
    else:
        return "🌤️ Check the weather and decide!"


# Test weather recommendations
weather_scenarios = [("sunny", 28), ("rainy", 20), ("snowy", -2), ("cloudy", 18)]

print(f"\n🌤️ Weather Recommendations:")
for weather, temp in weather_scenarios:
    recommendation = recommend_activity(weather, temp)
    print(f"{weather.title()}, {temp}°C: {recommendation}")

print("\n" + "=" * 50)
print("✅ Essential conditional patterns demonstrated!")
print("💡 Focus: Practical patterns for real applications")
