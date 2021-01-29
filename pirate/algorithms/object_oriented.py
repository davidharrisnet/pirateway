from abc import ABCMeta, abstractmethod

class Mammal():
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def eat(self):
      """ all mamale eat"""

    @abstractmethod
    def sleep(self):
        """ all mammals sleep"""

    @abstractmethod
    def move(self):
        """ all mammal move"""

    def _name(self):
        return self.name

class Dog(Mammal):
    def __init__(self,name):
       super().__init__(name)

    def eat(self):
        print("chew")

    def sleep(self):
        print("all the time")

    def move(self):
        print("run run run")

    def wag_tail(self):
        print("wag")

    def get_name(self):
        print(super()._name())


m  = Mammal("Animal")
print(m._name())

d = Dog("Spot")

d.get_name()