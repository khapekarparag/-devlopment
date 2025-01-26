list=[1,2,3,4,5]

copylist1=list.copy()
copylist1.reverse()
print(copylist1)


if(copylist1==list):
    print("palindrom")
else:
    print("not")