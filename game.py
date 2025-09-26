# Our first game snake, water and gun game 
# so rule will be like this 
""" 1 for snake 
    -1 for water 
    0 fir gun"""
import random
computer= random.choice([-1,0,1 ])
youstr=input("enter your choice\n: ")
youDict={"s":1, "w":-1,"g":0}
reverseDict={1:"snake", -1:"water", 0:"gun"}
you=youDict[youstr]

# by now you have two numbers , you and computer
print(f"you chose {reverseDict[you]} and computer chose {reverseDict[computer]}")
if you==computer:
    print("It's a tie")
else:
    if (you==1 and computer==-1):
        print("You win")
    elif (you==0 and computer==-1):
        print("You lose")
    elif (you==-1 and computer==1):
        print("You lose")
    elif (you==-1 and computer==0):
        print("You win")
    elif (you==0 and computer==1):
        print("You win")
    elif (you==1 and computer==0):
        print("You lose")   
    
    else:
        print("Invalid input")
             