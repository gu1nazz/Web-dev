class Vehicle:
    def __init__(self, brand, year, vehicle_type):
        self.brand = brand
        self.year = year
        self.vehicle_type = vehicle_type

    def move(self):
        return f"{self.brand} is moving.."
    
    def get_info(self):
        return f"{self.brand} is a {self.year} {self.vehicle_type}."
    
    def __str__(self):
        return f"Vehicle Object: {self.brand}"


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year, "Car")
        self.model = model

    def move(self):
        return f"Car {self.brand} {self.model} is driving.."
    
    def signal(self):
        return "Beep beep!"
    

class Bike(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year, "Bike")

    def move(self):
        return f"{self.brand} bike is moving on the road"

    def signal(self):
        return "Ring ring!"