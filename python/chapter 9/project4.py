class car:                             #single inheritance
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped..")

class toyota(car):                     #class car
    def __init__(self,name):
        self.name=name

c1=toyota("fortuner") 
c2=toyota("lemborgini")

print(c1.name) 
print(c1.start())
print(c1.stop())