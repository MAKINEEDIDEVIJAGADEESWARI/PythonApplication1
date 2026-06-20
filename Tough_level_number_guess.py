#Number guessing
import random
computer=random.randint(1,100)

for attempt in range(10):
    guess=int(input("enter any number:"))
    if guess == computer:
        print("YOU WIN!!")
    elif guess > computer:
        print("THINK!! IT'S smallest NUMBER")
    elif guess < computer:
        print("THINK!! IT'S greatest NUMBER")
    else:
        print("you entered wrong decimal number please check it out")
else:
    print("GAME OVER!!",computer)
input("Press Enter to close...") 
