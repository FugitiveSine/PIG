import random
import colorama
import tkinter as tk
from tkinter import *
from colorama import Fore


global x
global pT
global playerTotal
pT = 0
x=0
playerTotal = 0

def changeGameText(i, playerTurn):
    nonlocal counter
    counter += 1
    
    if playerTurn % 2 == 0:
            i =1 
            playerTurn = playerTurn + 1
            labelPlayerSelect.configure(text = "Player 1's Turn")
    else:
        i = 2
        playerTurn = playerTurn + 1
        labelPlayerSelect.configure(text = "Player 2's Turn")




def rollDie():
    rand = random.randint(1,6)
    return(rand)

window = tk.Tk()
window.geometry('800x500')
window.configure(background='#262523')
window.title('PIG')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

middle = Frame(window, background='green')
buttonFrame = Frame(window, background="#262523")
#bottom = Frame(window, background='#262523')
#center = Frame(window, background='#262523')

#center.pack(anchor=CENTER)
middle.grid(sticky ='n')
buttonFrame.grid(pady=40)

counter = 0



labelPlayerSelect = tk.Label(window, text="Player Select", font=("Arial", 25))
labelPlayerSelect.grid(in_=middle, row=0, pady=30)

labelGame = tk.Label(window, text="game", font=("Arial", 15))
labelGame.grid(in_=middle, row=1, pady=30)

labelRoundPoints = tk.Label(window, text="Round Points:", font=("Arial", 15))
labelRoundPoints.grid(in_=middle, row=2, pady=30)

labelPlayer1Points = tk.Label(window, text="Player1 Points:", font=("Arial", 15))
labelPlayer1Points.grid(in_=middle, row=3, pady=0)

labelPlayer2Points = tk.Label(window, text="Player2 Points:", font=("Arial", 15))
labelPlayer2Points.grid(in_=middle, row=4, pady=0)

rollButton = tk.Button(window, text="ROLL", font=("Arial", 15), command=lambda: changeGameText(x, pT))
rollButton.grid(row=1, padx=10, pady=0, in_=buttonFrame)
#rollButton.bind('<Button-1>', lambda event, x = x: changeGameText(x))

holdButton = tk.Button(window, text="HOLD", font=("Arial", 15))
holdButton.grid(row=1, column=1, padx=10, pady=0, in_=buttonFrame)




# playerSelect = {1: 0, 2: 0}

# gameOn = True
# tempVar = 0
# playerTurn = 0

# while gameOn:
#     if playerTurn % 2 == 0:
#             i =1 
#             playerTurn = playerTurn + 1
#     else:
#         i = 2
#         playerTurn = playerTurn + 1

#     playerGoing = True
#     while playerGoing:
#         print(f"It is your turn {Fore.YELLOW}player {i}{Fore.WHITE}")

#         rollOrHold = int(input('(1) Roll (2) Hold: '))

#         if rollOrHold == 1:

#             rolledDieNum = rollDie()
#             if rolledDieNum == 1:
#                 tempVar = 0
#                 playerSelect[i] = playerSelect[i] + tempVar
#                 print(f"OH NO you rolled a {Fore.RED}{rolledDieNum}{Fore.WHITE}")
#                 print(f"Your total score is: {Fore.BLUE}{playerSelect[i]}{Fore.WHITE}")
#                 playerGoing = False
#                 break
#             elif rolledDieNum != 1:
#                 tempVar = tempVar + rolledDieNum
#                 print(f"You rolled a {Fore.GREEN}{rolledDieNum}{Fore.WHITE}")
#             else:
#                 pass

#         elif rollOrHold == 2:
#             playerSelect[i] = playerSelect[i] + tempVar
#             #gameOn = False
#             tempVar = 0
#             print(f"Your total score is: {Fore.BLUE}{playerSelect[i]}{Fore.WHITE}")
#             break
#     if playerSelect[i] >= 100:
#         print(f"{Fore.PINK}CONGRATS YOU WON!!{Fore.WHITE}")
#         gameOn = False





window.mainLoop()