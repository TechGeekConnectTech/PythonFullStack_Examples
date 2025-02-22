from abc import ABC, abstractmethod


class Coaching(ABC):
    @abstractmethod
    def show_class_name(self):
        pass

    @abstractmethod
    def show_class_city(self):
        pass

class TechGeekConnect(Coaching):
    def show_class_name(self):
        print("My class name is TechGeekConnect")

    #def show_class_city(self):
        #print("My City is Pune")


class UpGrad(Coaching):
    def show_class_name(self):
        print("My class name is UpGrade")

    def show_class_city(self):
        print("My City is Banglore")


t=TechGeekConnect()
t.show_class_name()
#t.show_class_city()

u=UpGrad()
u.show_class_name()
u.show_class_city()