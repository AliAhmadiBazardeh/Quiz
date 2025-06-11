from app.car.application.manager import CarManager
from app.car.domain.car import Car

class CarUI:
    def __init__(self, manager: CarManager):
        self.manager = manager

    def show_menu(self):
        print("Car Registration System")
        print("1. Register new car")
        print("2. List all cars")
        print("3. Delete car by slug")
        print("4. Exit")

    def register_car(self):
        name = input("Enter name: ")
        model = input("Enter model: ")
        while not model.isdigit():
            print("Only digits allowed for car model.")
            model = input("Enter model: ")
        color = input("Enter color: ")
        from_date = input("From date: ")
        to_date = input("To date: ")
        code = input("Creation code: ")

        slug = self.manager.generate_unique_slug(name, model, color)
        car = Car(slug, name, model, color, from_date, to_date, code)
        self.manager.add_car(car)
        print(f"{slug} added successfully.\n")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                self.register_car()
            elif choice == "2":
                for car in self.manager.list_cars():
                    print(car)
                print()
            elif choice == "3":
                slug = input("Enter car slug to delete: ")
                self.manager.delete_car_by_slug(slug)
                print(f"{slug} deleted.\n")
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice.\n")
