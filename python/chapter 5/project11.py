tup=(1,4,9,16,25,36,49,64,81,100)
i=0
app=int(input("enter value:-"))
while i<=len(tup):
 if (app==tup[i]):
  print("char found at",i)
  break
 else:
  print("not found")
  i+=1




