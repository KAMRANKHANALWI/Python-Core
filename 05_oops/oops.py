# Python OOP Code


class Car:
    total_car = 0  # Class variable

    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute (encapsulation)
        self.__model = model  # Private attribute (encapsulation)
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def get_brand(self):
        return self.__brand + "!"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of Transport"

    @property
    def model(self):  # Property getter
        return self.__model

    @model.setter
    def model(self, new_model):  # Property setter with validation
        if new_model and len(new_model) > 0:
            self.__model = new_model
        else:
            raise ValueError("Model cannot be empty")

    @property
    def brand(self):  # Added brand property too
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        if new_brand and len(new_brand) > 0:
            self.__brand = new_brand
        else:
            raise ValueError("Brand cannot be empty")


class ElectricCar(Car):  # Inheritance
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Call parent constructor
        self.battery_size = battery_size

    def fuel_type(self):  # Polymorphism - method overriding
        return "Electric Charge"

    def charging_time(self):  # Additional method for electric cars
        return f"Charging time for {self.battery_size} battery: 8 hours"


class HybridCar(Car):  # Another child class
    def __init__(self, brand, model, battery_size, engine_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        self.engine_size = engine_size

    def fuel_type(self):  # Polymorphism
        return "Hybrid (Electric + Petrol)"


# Multiple Inheritance Classes
class Battery:
    def battery_info(self):
        return "This is Battery"

    def battery_capacity(self):
        return "Battery capacity: 100kWh"


class Engine:
    def engine_info(self):
        return "This is Engine"

    def engine_power(self):
        return "Engine power: 500HP"


class GPS:
    def navigation_info(self):
        return "GPS Navigation enabled"


class SmartElectricCar(Battery, Engine, GPS, Car):  # Multiple inheritance
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
            self.fuel_type(),
        ]


# Demo and Testing Code
if __name__ == "__main__":
    print("=== OOP CONCEPTS DEMONSTRATION ===\n")

    # 1. Basic Class and Object
    print("1. BASIC CLASS AND OBJECT:")
    regular_car = Car("Toyota", "Camry")
    print(f"Car created: {regular_car.full_name()}")
    print(f"Brand: {regular_car.get_brand()}")

    # 2. Class Methods and Self
    print(f"Fuel type: {regular_car.fuel_type()}")
    print()

    # 3. Inheritance
    print("2. INHERITANCE:")
    my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
    print(f"Electric car: {my_tesla.full_name()}")
    print(f"Battery: {my_tesla.battery_size}")
    print(f"Charging: {my_tesla.charging_time()}")
    print()

    # 4. Encapsulation
    print("3. ENCAPSULATION:")
    print(f"Accessing private brand through method: {my_tesla.get_brand()}")
    # print(my_tesla.__brand)  # This would cause an error!
    print("Private attributes protected from direct access")
    print()

    # 5. Polymorphism
    print("4. POLYMORPHISM:")
    cars = [
        Car("Honda", "Civic"),
        ElectricCar("Tesla", "Model 3", "75kWh"),
        HybridCar("Toyota", "Prius", "10kWh", "1.8L"),
    ]

    for car in cars:
        print(f"{car.full_name()}: {car.fuel_type()}")
    print()

    # 6. Class Variables
    print("5. CLASS VARIABLES:")
    print(f"Total cars created: {Car.total_car}")
    another_car = Car("BMW", "X5")
    print(f"After creating BMW: {Car.total_car}")
    print()

    # 7. Static Methods
    print("6. STATIC METHODS:")
    print(f"General description: {Car.general_description()}")
    print("Called without creating instance")
    print()

    # 8. Property Decorators
    print("7. PROPERTY DECORATORS:")
    nexon = Car("Tata", "Nexon")
    print(f"Original model: {nexon.model}")
    nexon.model = "Nexon EV"  # Using setter
    print(f"Updated model: {nexon.model}")  # Using getter

    try:
        nexon.model = ""  # This will raise an error
    except ValueError as e:
        print(f"Validation error: {e}")
    print()

    # 9. isinstance() Function
    print("8. isinstance() FUNCTION:")
    print(f"Is my_tesla a Car? {isinstance(my_tesla, Car)}")
    print(f"Is my_tesla an ElectricCar? {isinstance(my_tesla, ElectricCar)}")
    print(f"Is regular_car an ElectricCar? {isinstance(regular_car, ElectricCar)}")
    print()

    # 10. Multiple Inheritance
    print("9. MULTIPLE INHERITANCE:")
    smart_car = SmartElectricCar("Tesla", "Model X", "100kWh")
    print(f"Smart car: {smart_car.full_name()}")

    features = smart_car.all_features()
    for feature in features:
        print(f"- {feature}")

    print(f"\nMethod Resolution Order (MRO):")
    for i, cls in enumerate(SmartElectricCar.__mro__):
        print(f"{i+1}. {cls.__name__}")
    print()
