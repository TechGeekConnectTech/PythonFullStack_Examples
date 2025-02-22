class car:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def show_detail(self):
        return f"car name is {self.name}, color {self.color} and price {self.price}"

    def show_detail(self,name):
        return f"car name is {self.name}, color {self.color} and price {self.price}"

class Audi(car):

    def show_Audi(self):
        return f"car name is {self.name}, color {self.color} and price {self.price}"


class Benz(car):
    def __init__(self, segment):
        self.segment = segment


audi=car("Audi S1","Red",5000000)
benz=car("Benz SX","White",6000000)

s1=Audi("Audi S1","Red",5000000)
print(s1.show_Audi())


