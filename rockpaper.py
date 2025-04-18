from tkinter import *
import random

window = Tk()
window.title("ROCK PAPER SCISSORS GAME")
window.geometry("700x700") 


choices = ["Rock", "Paper", "Scissors"]


def check(userchoice):
    choice1 = random.choice(choices)

    if userchoice == choice1:
        result = "It's a Draw!"
    elif (userchoice == "Rock" and choice1 == "Scissors") or \
         (userchoice == "Paper" and choice1 == "Rock") or \
         (userchoice == "Scissors" and choice1 == "Paper"):
        result = "You Win!"
    else:
        result= "You Lose!"

   
result.config(text=result_text)

root =Tk()
root.title("Rock Paper Scissors")
root.geometry("300x300")
root.resizable(False, False)

title = Tk.Label(root, text="Rock Paper Scissors")
title.pack()


title = Tk.Label(root, text="Rock Paper Scissors")
title.pack()


rock_button = Tk.Button(root, text="Rock")
rock_button.pack()

paper_button = Tk.Button(root, text="Paper")
paper_button.pack()

scissors_button = Tk.Button(root, text="Scissors")
scissors_button.pack()

result = Tk.Label(root, text="")
result.pack()

root.mainloop()