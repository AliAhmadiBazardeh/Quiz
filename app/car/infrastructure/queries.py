INSERT_QUERY = "INSERT INTO cars (slug, car_name, car_model, car_color, from_date, to_date, creator_code) VALUES (%s, %s, %s, %s, %s, %s, %s)"
SELECT_ALL_QUERY = "SELECT slug, car_name, car_model, car_color, from_date, to_date, creator_code FROM cars"
SELECT_BY_SLUG_QUERY = "SELECT slug, car_name, car_model, car_color, from_date, to_date, creator_code FROM cars WHERE slug = %s"
EXIST_BY_SLUG_QUERY = "SELECT 1 FROM cars WHERE slug = %s LIMIT 1"
DELETE_BY_SLUG_QUERY = "DELETE FROM cars WHERE slug = %s"
    