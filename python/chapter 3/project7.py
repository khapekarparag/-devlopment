list=[]
a=list.append(int(input("enter:")))
s=list.append(int(input("enter:")))
d=list.append(int(input("enter:")))
f=list.append(int(input("enter:")))
g=list.append(int(input("enter:")))
copylist=list.copy()
copylist.reverse()

if(list==copylist):
    print("palindrom")
else:
    print("not")
