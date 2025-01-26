import random
target=random.randint(1,100)

while True:
    userChoice=input("guess the number or quit:")
    if(userChoice=='quit'):
        break
    userChoice=int(userChoice)
    if(userChoice == target):
        print("congratulation you guess correct!!")
        break
    elif(userChoice<target):
        print("you choose to less number, please guess bigger number")
    else:
        print("you choose to big number, please guess lesser number")
    print("game over")