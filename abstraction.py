from abc import ABC,abstractmethod


class Employee(ABC):
    @abstractmethod
    def name(self):
        pass

    def Address(self):
        pass

class HR(Employee):
    def name(self):
        print("Name of HR Department")


    def Address(self):
        print("Address of HR Department")


class Sale(Employee):
    def name(self):
        print("Name of Sale Department")

    def Address(self):
        print("Address of Sale Department")


hr=HR()
hr.name()
hr.Address()

sale=Sale()
sale.name()
sale.Address()