from os import system, name 
import random 

def clear(): 
  

    if name == 'nt': 
        _ = system('cls') 

    else: 
        _ = system('clear') 


print("...Rock...\n...Razors...\n...Scizzors...")
clear()
player1 = input("Insert Player 1 Choice : ")
computer = random.randint(0,2)

print("SHOOT")
if player1[0] == computer:
    for char in range(1,10):
       print("DRAW GAME")
elif (player1[0]=="r" or player1[0]=="R")  and not(computer==0) :
    for char in range(1,10):
        print("Player 1 WON")
elif (player1[0]=="P" or player1[0]=="p")  and not(computer==1):
    for char in range(1,10):
        print("Player 1 WON")
elif (player1[0]=="S" or player1[0]=="s")  and not(computer==2):
    for char in range(1,10):
        print("Player 1 WON")   
else:
    for char in range(1,10):
        print("Computer WON")