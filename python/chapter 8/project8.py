class car():
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clch=False

    def start(self):
        self.clch=True
        self.acc=True
        print("car stated.....")

car1=car()
car1.start()        