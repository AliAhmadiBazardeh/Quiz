from app.models.car import Car
import app.repositories.queries as q
import os
import psycopg2

class CarRepository:
    def __init__(self):  
        
        # self.conn = psycopg2.connect(
        #     dbname=os.getenv("DB_NAME"),
        #     user=os.getenv("DB_USER"),
        #     password=os.getenv("DB_PASSWORD"),
        #     host=os.getenv("DB_HOST"),
        #     port=os.getenv("DB_PORT"),
        # )
        
        self.conn = psycopg2.connect(
            dbname="car_db",
            user="postgres",
            password="76827633",
            host="localhost",
            port="5433"
        )
     
        self.cursor = self.conn.cursor()

    def insert(self, car: Car):
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

    def get_all(self):
        self.cursor.execute(q.SELECT_ALL_QUERY)
        return [Car(*row) for row in self.cursor.fetchall()]

    def get_by_id(self, slug: str):
        self.cursor.execute(q.SELECT_BY_SLUG_QUERY, (slug,)) 
        row = self.cursor.fetchone()
        return Car(*row) if row else None

    def delete_by_id(self, slug: int):
        self.cursor.execute(q.DELETE_BY_SLUG_QUERY, (slug,))
        self.conn.commit()
