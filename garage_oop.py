import json


class Car:

    def __init__(self, brand, model, year, hp):
        self.brand = brand
        self.model = model
        self.year = year
        self.hp = hp

    def show_info(self):
        print(f"{self.brand} {self.model} ({self.year}) - {self.hp} HP")

    def to_dict(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "hp": self.hp
        }
    
class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_all(self):
        for car in self.cars:
            car.show_info()

    def find_car(self, brand):
        for car in self.cars:
            if car.brand == brand:
                return car
        return None

    def delete_car(self, brand):
        for car in self.cars:
            if car.brand == brand:
                self.cars.remove(car)
                return f"{brand} removed from garage"
        return f"{brand} not found"
    
    def save(self):
        data = [car.to_dict() for car in self.cars]
        with open("garage.json", "w") as file:
            json.dump(data, file, indent=2)
        print("Garage saved.")

    def load(self):
        try:
            with open("garage.json", "r") as file:
                content = file.read()
                data = json.loads(content) if content.strip() else []
            self.cars = [Car(d["brand"], d["model"], d["year"], d["hp"]) for d in data]
            print(f"Garage loaded: {len(self.cars)} cars")
        except FileNotFoundError:
            print("No saved garage found. Starting fresh.")

my_garage = Garage()
my_garage.load()

while True:
    print("\n=== GARAGE MENU ===")
    print("1. Add car")
    print("2. Show garage")
    print("3. Search car")
    print("4. Delete car")
    print("5. Exit")

    option = input("\nChoose an option: ")

    if option == "1":
        brand = input("Brand: ")
        model = input("Model: ")
        year = int(input("Year: "))
        hp = int(input("HP: "))
        my_garage.add_car(Car(brand, model, year, hp))
        my_garage.save()
    elif option == "2":
        my_garage.show_all()
    elif option == "3":
        brand = input("Brand to search: ")
        result = my_garage.find_car(brand)
        if result:
            result.show_info()
        else:
            print("Not found")
    elif option == "4":
        brand = input("Brand to delete: ")
        print(my_garage.delete_car(brand))
        my_garage.save()
    elif option == "5":
        print("Bye!")
        break
    else:
        print("Invalid option")

        
 