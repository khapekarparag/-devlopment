class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("name is adding")
    def get_avg(self):
        sum=0
        for val in self.marks: 
            sum+=val
        print("hi",self.name,"your avr score is",sum/3)            

s1=student("karan",[97,98,99])
s1.get_avg()

s1.name="parag"
s1.get_ avg()