class CarNotFoundError(Exception):
    """Raised when a car with the specified slug is not found."""
    def __init__(self, slug: str):
        super().__init__(f"Car with slug '{slug}' not found.")
        self.slug = slug
