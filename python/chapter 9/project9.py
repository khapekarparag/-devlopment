class student:
    def __init__(self,phy,chem,sci):
        self.phy=phy
        self.chem=chem
        self.sci=sci
    @property
    def percentage(self):
            return str((self.phy+self.chem+self.sci)/3)+"%"  
        
stu1=student(87,89,67)
print(stu1.percentage)


stu1.chem=98
print(stu1.percentage)