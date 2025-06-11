class Car:
    def __init__(self,slug:str , car_name:str, car_model:int, car_color:str, from_date:str,to_date:str,creator_code:str):
        self._slug = slug
        self._car_name = car_name
        self._car_model = car_model
        self._car_color = car_color
        self._from_date = from_date
        self._to_date = to_date
        self._creator_code = creator_code

    @property
    def slug(self):
        return self._slug

    @property
    def car_name(self):
        return self._car_name

    @property
    def car_model(self):
        return self._car_model

    @property
    def car_color(self):
        return self._car_color

    @property
    def from_date(self):
        return self._from_date

    @property
    def to_date(self):
        return self._to_date

    @property
    def creator_code(self):
        return self._creator_code
        
    def __str__(self):
        return f"{self._slug}"