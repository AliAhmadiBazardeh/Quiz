from car import Car
import queries as q
import psycopg2
import helper as helper
import os

class CarManager:
    def __init__(self):     
        # self.conn = psycopg2.connect(
        #     dbname='car_db',
        #     user='postgres',
        #     password='76827633',
        #     host='localhost',
        #     port='5433',        
        # )
        # self.cursor = self.conn.cursor()
        
        
        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432")
        )
        self.cursor = self.conn.cursor()
        
    def add_car(self, car: Car): 
        try:
            self.cursor.execute(
                q.INSERT_QUERY,
                (
                    car.slug,
                    car.car_name,
                    car.car_model,
                    car.car_color,
                    car.from_date,
                    car.to_date,
                    car.creator_code
                 )
            )
            self.conn.commit()
            print(f"{car.slug} added to database.\n")
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error inserting: {e.pgerror}")

    def list_cars(self):
        self.cursor.execute(q.SELECT_ALL_QUERY)
        rows = self.cursor.fetchall()

        if not rows:
            print("\nNo data in database.\n")
            return

        print("\nCars from database:")
        for row in rows:
            car = Car(*row)
            print(car)
        print()
                
                
        
    def find_car_by_slug(self, slug: str):
        self.cursor.execute(q.SELECT_BY_SLUG_QUERY, (slug,))
        row = self.cursor.fetchone()
        if row:
            return Car(*row)
        return None
    
    def delete_car_by_slug(self, slug: int):
        car = self.find_car_by_slug(slug)
        if not car:
            print(f"No car found with slug {slug}\n")
            return

        try:
            self.cursor.execute(q.DELETE_BY_SLUG_QUERY, (slug,))
            self.conn.commit()
            print(f"{slug} deleted successfully.\n")
        except psycopg2.Error as e:
            self.conn.rollback()
            print(f"Error deleting: {e.pgerror}")

    
    def generate_unique_slug(self, car_name, car_model, car_color, max_attempts=10):
        for _ in range(max_attempts):
            slug = helper.simple_slugify(
                f"{car_name} {car_model} {car_color} {helper.random_lower_alphanumeric()}"
            )
            if not self.find_car_by_slug(slug):
                return slug
        raise Exception("Failed to generate unique slug after multiple attempts.")
