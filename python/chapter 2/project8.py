A=int(input("enter value A:-"))
B=int(input("enter value B:-"))
C=int(input("enter value C:-"))
D=int(input("enter value D:-"))

if(A>B and A>C and A>D):
        print("A is Largest")
elif(B>C and B>D):
    print("B is largest")
elif(C>D):
    print("C is largest")
else:
    if(A==B==C==D):
        print("All values same")
    else:
      print("D is largest")
