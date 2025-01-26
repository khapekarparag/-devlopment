class car:                             #multilevel inheritance
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped..")

class toyota(car):                     
    def __init__(self,name):
        self.name=name

class fortuner(toyota):
    def __init__(self,type):
        self.type=type


c1=fortuner("disel")
c2=fortuner("petrol")

print(c1.type)
print(c1.start())
