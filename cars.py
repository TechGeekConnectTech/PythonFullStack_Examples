class cars:
    def __init__(self,color, price):
        self.color=color
        self.price=price

    def show(self):
        print(f"Car Color is {self.color} and Price is {self.price}")

audi=cars("Pink",1000000)
benz=cars("white",22000000)

audi.show()
benz.show()