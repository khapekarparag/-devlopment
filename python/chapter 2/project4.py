age = int(input("age of person:-"))
if(age>=18):
    if(age>=80):
        print("Not eligible")
    else:
        print("eligible for voting")
elif(age<18):
    print("Not eligible")
else:
    print("none") 
