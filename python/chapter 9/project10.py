class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img + self.img
        return  complex(newReal, newImg)

num1=complex(1,3)
print(num1.showNumber())        

num2=complex(4,6)
print(num2.showNumber())        

num3=num1+num2
print(num3.showNumber())