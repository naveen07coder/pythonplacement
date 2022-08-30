from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print("LAPTOP PROCESS")

class programmer:
    def solving(self, comp):
        print("Solving ")

# c1 = computer()

c2 = laptop()
p1 = programmer()
p1.solving(c2)
c2.process()