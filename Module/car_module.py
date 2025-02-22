from sys import set_coroutine_origin_tracking_depth


class Car:
    def __init__(self,model,price):
        self.model=model
        self.price=price

    def show_model(self):
        return f"Car Model is : {self.model}"

    def show_price(self):
        if self.price >= "30L":
            return f"Car is lunxary car and Price is: {self.price}"
        elif self.price >= "10L" and self.price < "30L":
            return f"Car is SUV car and Price is: {self.price}"