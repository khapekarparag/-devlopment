list=[1,"abc","abc",1]
copylist=list.copy()
copylist.reverse()
if (list==copylist):
    print("palindrom")
else:
    print("not")