import random
import colorama
import tkinter as tk
from tkinter import *
from colorama import Fore


playerTurn=0
playerSelect = {1: 0, 2: 0}
tempVar = 0
i = 0
playerSelecti = NONE
checkRollBtnClickedFirst = False

def rollButton():
    global playerTurn
    global playerSelect
    global tempVar
    global i
    global playerSelecti
    global checkRollBtnClickedFirst
    checkRollBtnClickedFirst = True
   
    if playerTurn % 2 == 0:
            i = 1 
            labelPlayerSelect.configure(text = "Player 1's Turn", fg='white', bg='#262523')
            playerSelecti = labelPlayer1Points
    else:
        i = 2
        labelPlayerSelect.configure(text = "Player 2's Turn", fg='white', bg='#262523')
        playerSelecti = labelPlayer2Points
         

    rolledNum = rollDie()

    if rolledNum == 1:
        #playerSelect[i] = playerSelect[i] + tempVar
        labelGame.configure(text = f"OH NO you rolled a {rolledNum}", fg = 'red', bg='#262523')
        labelRoundPoints.configure(text = f"Your round score is: {tempVar}", fg ='blue', bg='#262523')
        playerTurn = playerTurn + 1
        tempVar = 0
    elif rolledNum != 1:
        tempVar = tempVar + rolledNum
        labelGame.configure(text = f"You rolled a {rolledNum}", fg = 'green', bg='#262523')
        labelRoundPoints.configure(text = f"Your round score is: {tempVar}", fg ='blue', bg='#262523')
    else:
        pass
    checkWinner()



def holdButton():
     global i, tempVar, playerSelect, playerTurn, playerSelecti, checkRollBtnClickedFirst
     if checkRollBtnClickedFirst == True:
        playerSelect[i] = playerSelect[i] + tempVar
        tempVar = 0
        playerTurn = playerTurn + 1
        playerSelecti.configure(text=f"Player {i}'s score is: {playerSelect[i]}", fg='pink', bg='#262523')
        if i == 2:
            labelPlayerSelect.configure(text = "Player 1's Turn", fg='white', bg='#262523')
        elif i == 1: 
            labelPlayerSelect.configure(text = "Player 2's Turn", fg='white', bg='#262523')
        else:
            pass
        checkWinner()
     else:
        labelGame.configure(text = f"***PLEASE CLICK ROLL FIRST****", fg = 'green', bg='#262523')

def rollDie():
    rand = random.randint(1,6)
    return(rand)

def checkWinner():
    global i, tempVar, playerSelect, playerTurn, playerSelecti
    if playerSelect[i] >= 100:
        newWindow = Toplevel(window)
        newWindow.geometry('400x300')
        newWindow.configure(background='#262523')
        newWindow.title(f"Player {i} Won")
        labelWinnerText = tk.Label(newWindow, text=f"Congradulations on your VICTORY Player {i}!!", fg='yellow', background='#262523', font=("Arial",) )
        labelWinnerText.grid()
        middle.destroy()
        buttonFrame.destroy()


window = tk.Tk()
window.geometry('800x500')
window.configure(background='#262523')
window.title('PIG')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

middle = Frame(window, background='#262523')
buttonFrame = Frame(window, background="#262523")

middle.grid(sticky ='n')
buttonFrame.grid(pady=40)

counter = 0



labelPlayerSelect = tk.Label(window, text="Player Select", font=("Arial", 25), fg='white', bg='#262523')
labelPlayerSelect.grid(in_=middle, row=0, pady=30)

labelGame = tk.Label(window, text="game", font=("Arial", 15), fg = 'green', bg='#262523')
labelGame.grid(in_=middle, row=1, pady=30)

labelRoundPoints = tk.Label(window, text="Round Points:", font=("Arial", 15), fg ='blue', bg='#262523')
labelRoundPoints.grid(in_=middle, row=2, pady=30)

labelPlayer1Points = tk.Label(window, text="Player1 Points:", font=("Arial", 15), fg='pink', bg='#262523')
labelPlayer1Points.grid(in_=middle, row=3, pady=0)

labelPlayer2Points = tk.Label(window, text="Player2 Points:", font=("Arial", 15), fg='pink', bg='#262523')
labelPlayer2Points.grid(in_=middle, row=4, pady=0)

rollButton = tk.Button(window, text="ROLL", font=("Arial", 15), command=rollButton)
rollButton.grid(row=1, padx=10, pady=0, in_=buttonFrame)

holdButton = tk.Button(window, text="HOLD", font=("Arial", 15), command=holdButton)
holdButton.grid(row=1, column=1, padx=10, pady=0, in_=buttonFrame)



#**********CODE FOR TEXT BASED************
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





window.mainloop()