tup=(1,4,9,16,25,36,49,64,81,100)
i=0
x=int(input("enter number:-"))
for val in tup :
  if (val==x):
    print("num found at",i) 
  else:
    print("not found")
i+=1