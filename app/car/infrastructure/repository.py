from app.car.domain.car import Car
import app.car.infrastructure.queries as q
from typing import List, Optional

class CarRepository:
    def __init__(self, connection):
        self.conn = connection
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

    def get_all(self) -> List[Car]:
        self.cursor.execute(q.SELECT_ALL_QUERY)
        return [Car(*row) for row in self.cursor.fetchall()]

    def get_by_slug(self, slug: str) -> Optional[Car]:
        self.cursor.execute(q.SELECT_BY_SLUG_QUERY, (slug,))
        row = self.cursor.fetchone()
        return Car(*row) if row else None

    def delete_by_slug(self, slug: str):
        self.cursor.execute(q.DELETE_BY_SLUG_QUERY, (slug,))
        self.conn.commit()
