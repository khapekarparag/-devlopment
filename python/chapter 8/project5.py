class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks= marks
        print ("name is adding")
    def welcome(self):
        print("welcome students")
    def get_marks(self):
        return self.marks

s1=student("parag",99) 
print(s1.get_marks())
s1.welcome()           