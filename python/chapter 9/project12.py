class employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showdetails(self):
        print("role=",self.role)
        print("dept=",self.dept) 
        print("salary=",self.salary)

class engineer(employee):
    def __init__(self,name,age):
        self.age=age
        self.name=name
        super().__init__("engineer","IT","75000")

e1=employee("accountat","finanace","600000")  
print(e1.showdetails())       

e2=engineer("parag khapekar",24)
print(e2.showdetails())