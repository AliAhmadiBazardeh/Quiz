class Car:
    def __init__(self,slug:str , car_name:str, car_model:int, car_color:str, from_date:str,to_date:str,creator_code:str):
        self.slug = slug
        self.car_name = car_name
        self.car_model = car_model
        self.car_color = car_color
        self.from_date = from_date
        self.to_date = to_date
        self.creator_code = creator_code
        
    def __str__(self):
        return self.slug