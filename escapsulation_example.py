class Fruit:
    def __init__(self,name,color,season):
        self.name=name #public
        self._color=color  #Protected
        self.__season=season #Private

    def get_season(self):
        return self.__season

f=Fruit("Banana","Yellow","Summer")
print(f.name)
print(f._color)
print(f.get_season())
