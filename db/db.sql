CREATE TABLE IF NOT EXISTS cars (
    slug VARCHAR(100) UNIQUE NOT NULL,
    car_name VARCHAR(50) NOT NULL,
    car_model VARCHAR(20) NOT NULL,
    car_color VARCHAR(20) NOT NULL,
    from_date VARCHAR(50),
    to_date VARCHAR(50),
    creator_code VARCHAR(20) NOT NULL
);
