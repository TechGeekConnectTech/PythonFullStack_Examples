class Fruit:
    def __init__(self,name,color,season):
        self.name=name  #Public
        self._color=color  #Procted
        self.__season=season #Private Variable

    def get_season(self):
        return self.__season

class Mango(Fruit):
    def __init__(self,name,color,season,type):
        Fruit.__init__(self,name,color,season)
        self.type=type

    def show_detail(self):
        return f"{self.name},{self._color},{self.get_season()},{self.type}"



f=Mango("Mango","Yello","Summer","Hapus")
print(f.show_detail())


