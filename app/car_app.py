from car_manager import CarManager
from car import Car
from helper import simple_slugify

class CarApp:   
    def __init__(self):
        self.manager = CarManager()
        self.run()

    def menu(self):
        print("Car Registration System")
        print("1. Register new car")
        print("2. List all cars")
        print("3. Delete car by slug")
        print("4. Exit")    
        
    def register(self):
        try:
            car_name = input("Enter name: ")
            car_model = input("Enter model: ")
            while not car_model.isdigit():  
                print("Only digit for car model is valid!")  
                car_model = input("Enter model: ")  
            car_color = input("Enter color: ")
            from_date = input("From date: ")
            to_date = input("To date: ")
            creation_code = input("Creation code: ")
            
            slug = self.manager.generate_unique_slug(car_name, car_model, car_color)

            # slug = simple_slugify(car_name+" "+car_model+" "+car_color)
            # if self.manager.find_car_by_slug(slug):
            #     print("Car already exists!\n")
            #     return
        

            car = Car(slug, car_name, car_model, car_color, from_date, to_date, creation_code)
            self.manager.add_car(car)
        except ValueError:
            print("Invalid input. Please enter valid data.\n")
            
            
    def run(self):
        while True:
            self.menu()
            choice = input("Choose an option: ")

            if choice == "1":
                self.register()
            elif choice == "2":
                self.manager.list_cars()
            elif choice == "3":               
                slug = input("Enter car slug to delete: ")
                self.manager.delete_car_by_slug(slug)         
            elif choice == "4":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Try again.\n")
                
                
                