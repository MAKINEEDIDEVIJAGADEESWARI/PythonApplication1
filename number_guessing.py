#Number guessing
import random
computer=random.randint(1,50)

for attempt in range(5):
    guess=int(input("enter any number:"))
    if guess == computer:
        print("YOU WIN!!")
    elif guess > computer:
        low=computer-10
        high=computer+10
        print("THINK!! IT'S GREATER NUMBER",low,"and",high)
    elif guess < computer:
        low=computer-10
        high=computer+10
        print("THINK!! IT'S NUMBER",low,"and",high)
    else:
        print("you entered wrong decimal number please check it out")
else:
    print("GAME OVER!!",computer)
input("Press Enter to close...") 




