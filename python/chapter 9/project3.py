class person:
    __name="anonymous"

    def __hello(self):
        print("hello user")

    def welcome(self):
        self.__hello()   

p1=person()
print(p1.welcome())