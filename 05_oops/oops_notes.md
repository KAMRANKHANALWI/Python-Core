# Python Object-Oriented Programming - Complete Study Guide

## Table of Contents
1. [Introduction to OOP](#introduction-to-oop)
2. [Classes and Objects](#classes-and-objects)
3. [Methods and Instance Variables](#methods-and-instance-variables)
4. [Inheritance](#inheritance)
5. [Encapsulation](#encapsulation)
6. [Polymorphism](#polymorphism)
7. [Class Variables](#class-variables)
8. [Static Methods](#static-methods)
9. [Property Decorators](#property-decorators)
10. [Type Checking with isinstance()](#type-checking-with-isinstance)
11. [Multiple Inheritance](#multiple-inheritance)
12. [Advanced Concepts](#advanced-concepts)
13. [Best Practices](#best-practices)

---

## Introduction to OOP

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code into classes and objects, promoting code reusability, modularity, and maintainability.

### Core OOP Principles
- **Encapsulation**: Bundling data and methods together
- **Inheritance**: Creating new classes based on existing ones
- **Polymorphism**: Same interface, different implementations
- **Abstraction**: Hiding complex implementation details

---

## Classes and Objects

### Definition
- **Class**: A blueprint or template for creating objects
- **Object**: An instance of a class with specific values

### Basic Syntax
```python
class ClassName:
    def __init__(self, parameters):
        self.attribute = parameter
```

### Example: Basic Class Implementation
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand    # Public attribute
        self.model = model    # Public attribute

# Creating objects (instances)
my_car = Car("BMW", "X5")
tesla = Car("Tesla", "Model S")

# Accessing attributes
print(my_car.brand)  # Output: BMW
print(my_car.model)  # Output: X5
```

### Key Components
- **`__init__()`**: Constructor method for object initialization
- **`self`**: Reference to the current instance
- **Attributes**: Data stored in the object
- **Instance creation**: Using the class name with parentheses

---

## Methods and Instance Variables

### Instance Methods
Functions defined within a class that operate on instance data.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        """Return the full name of the car."""
        return f"{self.brand} {self.model}"
    
    def get_brand(self):
        """Return the brand with emphasis."""
        return self.brand + "!"

# Usage
my_car = Car("BMW", "X5")
print(my_car.full_name())   # Output: BMW X5
print(my_car.get_brand())   # Output: BMW!
```

### Method Characteristics
- **First parameter**: Always `self` (refers to the instance)
- **Instance access**: Can access and modify instance variables
- **Return values**: Can return data or modify object state

---

## Inheritance

### Definition
A mechanism where a new class inherits properties and methods from an existing class.

### Basic Inheritance Structure
```python
class ParentClass:
    # Parent class implementation
    pass

class ChildClass(ParentClass):
    # Child class implementation
    pass
```

### Example: Vehicle Inheritance
```python
class Car:
    """Base class for all cars."""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    """Electric car class inheriting from Car."""
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Call parent constructor
        self.battery_size = battery_size
    
    def fuel_type(self):  # Method overriding
        return "Electric Charge"
    
    def charging_time(self):  # Additional method
        return f"Charging time for {self.battery_size}: 8 hours"

# Usage
tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(tesla.full_name())    # Inherited method
print(tesla.fuel_type())    # Overridden method
```

### Inheritance Benefits
- **Code reusability**: Avoid duplicating common functionality
- **Method overriding**: Customize behavior in child classes
- **Extension**: Add new methods to child classes
- **`super()`**: Access parent class methods

---

## Encapsulation

### Problem with Public Attributes
Direct access to attributes can lead to data integrity issues:

```python
my_car = Car("BMW", "X5")
my_car.brand = ""  # Problematic: empty brand value
```

### Private Attributes Solution
Use double underscore prefix to make attributes private:

```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand    # Private attribute
        self.__model = model    # Private attribute
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand + "!"

# Usage
my_car = Car("BMW", "X5")
print(my_car.get_brand())     # Correct: use public method
# print(my_car.__brand)       # Error: cannot access private attribute
```

### Encapsulation Benefits
- **Data protection**: Prevent unauthorized access
- **Controlled access**: Use methods to validate data
- **Implementation hiding**: Internal structure remains hidden
- **Maintainability**: Change internal implementation without affecting external code

### Name Mangling
Python transforms `__attribute` to `_ClassName__attribute` internally:

```python
# Accessible (not recommended):
print(my_car._Car__brand)  # BMW
```

---

## Polymorphism

### Definition
The ability of different classes to provide different implementations of the same method interface.

### Example: Method Overriding
```python
class Car:
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def fuel_type(self):
        return "Electric Charge"

class HybridCar(Car):
    def fuel_type(self):
        return "Hybrid (Electric + Petrol)"

# Polymorphic behavior
vehicles = [
    Car("Honda", "Civic"),
    ElectricCar("Tesla", "Model 3", "75kWh"),
    HybridCar("Toyota", "Prius", "10kWh", "1.8L")
]

for vehicle in vehicles:
    print(f"{vehicle.full_name()}: {vehicle.fuel_type()}")
```

### Benefits
- **Uniform interface**: Same method call, different behaviors
- **Extensibility**: Add new classes without changing existing code
- **Flexibility**: Runtime method resolution

---

## Class Variables

### Definition
Variables shared among all instances of a class.

### Implementation
```python
class Car:
    total_cars = 0  # Class variable
    
    def __init__(self, brand, model):
        self.__brand = brand      # Instance variable
        self.__model = model      # Instance variable
        Car.total_cars += 1       # Increment class variable

# Usage
car1 = Car("BMW", "X5")
car2 = Car("Audi", "A4")
car3 = Car("Tesla", "Model S")

print(Car.total_cars)  # Output: 3
```

### Characteristics
- **Shared state**: Same value across all instances
- **Class-level access**: Access via class name
- **Memory efficiency**: Single copy in memory
- **Common use cases**: Counters, configuration settings

### Class vs Instance Variables
| Type | Scope | Access | Memory |
|------|-------|--------|---------|
| Class Variable | Shared | `ClassName.variable` | Single copy |
| Instance Variable | Per object | `self.variable` | Per instance |

---

## Static Methods

### Definition
Methods that belong to the class but don't require access to instance or class data.

### Implementation
```python
class Car:
    total_cars = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1
    
    @staticmethod
    def general_description():
        """Return general information about cars."""
        return "Cars are means of transport"
    
    @staticmethod
    def validate_model_name(model):
        """Validate model name format."""
        return len(model) > 0 and model.isalnum()

# Usage
print(Car.general_description())  # Call without instance
my_car = Car("BMW", "X5")
print(my_car.general_description())  # Also works with instance
```

### Characteristics
- **No `self` parameter**: Cannot access instance variables
- **No `cls` parameter**: Cannot access class variables
- **Utility functions**: Helper methods related to the class
- **Independent**: Can be called without creating instances

---

## Property Decorators

### Traditional Getter/Setter Approach
```python
class Car:
    def get_model(self):
        return self.__model
    
    def set_model(self, new_model):
        if new_model:
            self.__model = new_model
```

### Modern Property Implementation
```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    
    @property
    def model(self):
        """Getter for model attribute."""
        return self.__model
    
    @model.setter
    def model(self, new_model):
        """Setter for model attribute with validation."""
        if new_model and len(new_model) > 0:
            self.__model = new_model
        else:
            raise ValueError("Model cannot be empty")
    
    @property
    def brand(self):
        """Getter for brand attribute."""
        return self.__brand
    
    @brand.setter
    def brand(self, new_brand):
        """Setter for brand attribute with validation."""
        if new_brand and len(new_brand) > 0:
            self.__brand = new_brand
        else:
            raise ValueError("Brand cannot be empty")

# Usage
car = Car("Toyota", "Camry")
print(car.model)        # Calls getter
car.model = "Corolla"   # Calls setter with validation
print(car.model)        # Output: Corolla

# Error handling
try:
    car.model = ""      # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
```

### Property Benefits
- **Pythonic syntax**: Attribute-like access with method functionality
- **Data validation**: Enforce business rules
- **Backward compatibility**: Add validation without changing interface
- **Read-only properties**: Omit setter for read-only access

---

## Type Checking with isinstance()

### Purpose
Determine the type of an object and its inheritance relationships.

### Basic Usage
```python
regular_car = Car("Toyota", "Camry")
electric_car = ElectricCar("Tesla", "Model S", "85kWh")

# Type checking
print(isinstance(electric_car, Car))         # True (inheritance)
print(isinstance(electric_car, ElectricCar)) # True (direct type)
print(isinstance(regular_car, ElectricCar))  # False
```

### Practical Application
```python
def service_vehicle(vehicle):
    """Provide appropriate service based on vehicle type."""
    if isinstance(vehicle, ElectricCar):
        return "Checking battery and charging system"
    elif isinstance(vehicle, Car):
        return "Checking engine oil and fuel system"
    else:
        return "Unknown vehicle type"

# Usage
print(service_vehicle(regular_car))  # Engine service
print(service_vehicle(electric_car)) # Battery service
```

### Multiple Type Checking
```python
# Check multiple types
def is_eco_friendly(vehicle):
    return isinstance(vehicle, (ElectricCar, HybridCar))
```

---

## Multiple Inheritance

### Definition
A class can inherit from multiple parent classes simultaneously.

### Basic Structure
```python
class ParentA:
    def method_a(self):
        return "From Parent A"

class ParentB:
    def method_b(self):
        return "From Parent B"

class Child(ParentA, ParentB):
    def method_c(self):
        return "From Child"
```

### Example: Vehicle Features
```python
class Battery:
    """Battery functionality for electric vehicles."""
    def battery_info(self):
        return "Battery system available"
    
    def battery_capacity(self):
        return "Battery capacity: 100kWh"

class Engine:
    """Engine functionality for combustion vehicles."""
    def engine_info(self):
        return "Engine system available"
    
    def engine_power(self):
        return "Engine power: 500HP"

class GPS:
    """GPS navigation functionality."""
    def navigation_info(self):
        return "GPS navigation enabled"

class SmartElectricCar(Battery, Engine, GPS, Car):
    """Advanced car with multiple systems."""
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Smart Electric Charge"
    
    def all_features(self):
        """Collect all available features."""
        return [
            self.battery_info(),
            self.engine_info(),
            self.navigation_info(),
            self.fuel_type()
        ]

# Usage
smart_car = SmartElectricCar("Tesla", "Model X", "100kWh")
features = smart_car.all_features()
for feature in features:
    print(f"- {feature}")
```

### Method Resolution Order (MRO)
Python determines method lookup order using the C3 linearization algorithm:

```python
# Display MRO
print("Method Resolution Order:")
for i, cls in enumerate(SmartElectricCar.__mro__):
    print(f"{i+1}. {cls.__name__}")

# Output:
# 1. SmartElectricCar
# 2. Battery
# 3. Engine
# 4. GPS
# 5. Car
# 6. object
```

### Diamond Problem Resolution
When multiple inheritance creates ambiguous method calls, MRO resolves conflicts:

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):  # Diamond inheritance
    pass

d = D()
print(d.method())  # Output: "B" (first in MRO after D)
```

---

## Advanced Concepts

### Class Methods
Methods that receive the class as the first argument:

```python
class Car:
    total_cars = 0
    
    @classmethod
    def get_total_cars(cls):
        return cls.total_cars
    
    @classmethod
    def create_default_car(cls):
        return cls("Default", "Model")
```

### Abstract Base Classes
Define interfaces that subclasses must implement:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
    def stop_engine(self):
        return "Car engine stopped"
```

### Composition vs Inheritance
Sometimes composition is preferred over inheritance:

```python
class Engine:
    def __init__(self, power):
        self.power = power
    
    def start(self):
        return f"Engine with {self.power}HP started"

class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine  # Composition
    
    def start(self):
        return self.engine.start()
```

---

## Best Practices

### 1. Use Meaningful Names
```python
# Good
class ElectricCar:
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity

# Avoid
class EC:
    def __init__(self, b, m, bc):
        self.b = b
        self.m = m
        self.bc = bc
```

### 2. Follow Single Responsibility Principle
Each class should have one reason to change:

```python
# Good: Separate responsibilities
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class CarDatabase:
    def save_car(self, car):
        # Database operations
        pass

# Avoid: Mixed responsibilities
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def save_to_database(self):
        # Car shouldn't handle database operations
        pass
```

### 3. Use Encapsulation Appropriately
```python
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")
```

### 4. Prefer Composition When Appropriate
```python
# Composition for "has-a" relationships
class Car:
    def __init__(self, engine, transmission):
        self.engine = engine          # Car has an engine
        self.transmission = transmission  # Car has a transmission

# Inheritance for "is-a" relationships
class ElectricCar(Car):  # ElectricCar is a Car
    pass
```

### 5. Document Your Classes
```python
class Car:
    """
    Represents a car with basic functionality.
    
    Attributes:
        brand (str): The manufacturer of the car
        model (str): The model name of the car
    """
    
    def __init__(self, brand, model):
        """
        Initialize a new car.
        
        Args:
            brand (str): The manufacturer name
            model (str): The model name
        """
        self.brand = brand
        self.model = model
```

---

## Complete Implementation Example

```python
"""
Complete car management system demonstrating all OOP concepts.
"""

class Car:
    """Base car class with encapsulation and properties."""
    total_cars = 0  # Class variable
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, new_brand):
        if new_brand and len(new_brand) > 0:
            self.__brand = new_brand
        else:
            raise ValueError("Brand cannot be empty")
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_model):
        if new_model and len(new_model) > 0:
            self.__model = new_model
        else:
            raise ValueError("Model cannot be empty")

class ElectricCar(Car):
    """Electric car with inheritance and polymorphism."""
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):  # Polymorphism
        return "Electric Charge"
    
    def charging_time(self):
        return f"Charging time for {self.battery_size}: 8 hours"

class Battery:
    def battery_info(self):
        return "Battery system available"

class Engine:
    def engine_info(self):
        return "Engine system available"

class GPS:
    def navigation_info(self):
        return "GPS navigation enabled"

class SmartElectricCar(Battery, Engine, GPS, Car):
    """Advanced car demonstrating multiple inheritance."""
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Smart Electric Charge"
    
    def all_features(self):
        return [
            self.battery_info(),
            self.engine_info(),
            self.navigation_info(),
            self.fuel_type()
        ]

# Demonstration
if __name__ == "__main__":
    # Basic functionality
    tesla = ElectricCar("Tesla", "Model S", "85kWh")
    print(f"Car: {tesla.full_name()}")
    print(f"Type check: {isinstance(tesla, Car)}")
    print(f"Fuel type: {tesla.fuel_type()}")
    
    # Property usage
    tesla.model = "Model X"
    print(f"Updated model: {tesla.model}")
    
    # Multiple inheritance
    smart_car = SmartElectricCar("Tesla", "Cybertruck", "100kWh")
    features = smart_car.all_features()
    print("Smart car features:")
    for feature in features:
        print(f"- {feature}")
    
    # Class variables
    print(f"Total cars created: {Car.total_cars}")
    
    # Static methods
    print(f"Description: {Car.general_description()}")
```

---

## Summary

Object-Oriented Programming in Python provides powerful tools for creating maintainable, reusable, and organized code. The key concepts work together to create robust software architectures:

- **Classes and Objects** form the foundation
- **Encapsulation** protects data integrity
- **Inheritance** enables code reuse
- **Polymorphism** provides flexible interfaces
- **Properties** offer controlled attribute access
- **Multiple inheritance** allows complex relationships

Understanding these concepts and their proper application is essential for writing professional Python code that scales and maintains well over time.
