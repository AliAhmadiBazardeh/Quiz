class CarNotFoundError(Exception):
    def __init__(self, slug: str):
        self.slug = slug
        self.message = f"Car with slug '{slug}' not found."
        super().__init__(self.message)
