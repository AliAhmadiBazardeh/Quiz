from app.console.app_console import CarUI
from app.services.manager import CarManager
from app.repositories.repository import CarRepository
from app.repositories.db_connection import get_db_connection

if __name__ == "__main__":
    repo = CarRepository(get_db_connection())
    manager = CarManager(repo)
    ui = CarUI(manager)
    ui.run()
