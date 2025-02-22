class Engine:
    def __init__(self,engine_type):
        self.engine_type=engine_type

    def start_engine(self):
        return f"Starting Engine : {self.engine_type}"

class Body:
    def __init__(self,body):
        self.body=body

    def describe_body(self):
        return f"Body : {self.body}"

class Car(Engine,Body):
    def __init__(self, engine_type,body,brand):
        Engine.__init__(self,engine_type)
        Body.__init__(self,body)
        self.brand=brand

    def describe_car(self):
        return f"Car Brand : {self.brand}, Body : {self.describe_body()}, Engine: {self.engine_type}"

car=Car("V8","SUV","Toyota")
print(car.start_engine())
print(car.describe_body())
print(car.describe_car())