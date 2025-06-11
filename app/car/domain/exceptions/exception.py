class CarNotFoundError(Exception):
    def __init__(self, slug: str):
        self.message = f"Car with slug '{slug}' not found."
        self.slug = slug
        super().__init__(self.message)
        
class ErrorMessages:
    CAR_NOT_FOUND = "Car with slug '{slug}' not found."