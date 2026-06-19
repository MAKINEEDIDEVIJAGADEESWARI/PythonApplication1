import random

user_score=0
computer_score=0

choices=["rock","paper","scissors"]

user=input("enter rock paper scissors:")

computer=random.choice(choices)

print("your choice:",user)
print("computer choice:",computer)

if user==computer:
    print("it is tie")
elif (user=="rock" and computer=="scissor") or (user=="scissor" and computer=="paper") or (user=="paper" and computer=="rock"):
          print("YOU WIN!!")
          user_score+=1
          print("user score:",user_score)
          
else:
    print("COMPUTER WINS!!")
    computer_score+=1
    print("computer score",computer_score)