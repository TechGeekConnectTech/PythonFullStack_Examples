from abc import abstractmethod,ABC

class Car(ABC):
    @abstractmethod
    def start(self):
        pass

    def engine(self):
        print("Starting Engine")

class ElectricVehical(Car):
    def start(self):
        print("Starting Electric Vehicle")


    '''def engine(self):
        print("Starting Engine from Elctric Vehicle class")
'''

elctric=ElectricVehical()
#elctric.engine()
elctric.start()