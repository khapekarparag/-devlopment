
#single line statement
food=input("food:-")
print("sweet")if food=="mango" or food=="banana" else print("not acceptable")


#clever if
age=int(input("age:-"))
vote=("no","yes")[age>=18]
print(vote)

sal=int(input("salary:"))
tax=sal*(0.1,0.2)[sal>50000]
print(tax)