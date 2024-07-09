pip install torch

import torch
print(torch.__version__)

#importing neccessary packages
from tkinter import *
from tkinter.messagebox import showinfo,showwarning
from tkinter.filedialog import askdirectory
from tkinter import Tk, PhotoImage, Label, Entry, Button, messagebox
from tkinter import simpledialog

import tkinter as tk
#creating window
w=Tk()
w.title("Mastermind")
w.geometry("500x400")
w.resizable(False,False)


# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)


#creating function for correct and misplaced digits
def judgement(confidential, guess ):
        con_list = list(confidential)
        g_list = list(guess)
        correct_dig = sum(c == g for c, g in zip(confidential, guess))
        con_count=len(con_list)
        gue_count=len(g_list)
        m=min(con_count,gue_count)
        avail_dig = sum(min(con_list.count(d), g_list.count(d)) for d in set(g_list))
        return correct_dig, avail_dig-correct_dig

#announcing the winner of Mastermind Game
def winner(p1_t,p2_t):
    if p1_t < p2_t:
        showinfo("Winner", "Player 1 is the Mastermind!")
    elif p1_t > p2_t :
        showinfo("Winner", "Player 2 is the Mastermind!")
    else:
        showinfo("Winner", "It's a tie!")               

#creating function for player to set the confidential no.
def player1_set_con():
    global p1_con
    p1_con = entry.get()
    showinfo("Player 1", f"Player 1 set the confidential number: {p1_con}")
    clear_entry() 
    play_game()


def play_game():
    global p2_tries, correct
    p2_tries = 0
    correct = False
    showinfo(title="player2", message="Player 2: Guess the number: ")
    label.config(text="Player 2: Guess the number:")
    b.config(command=player2_guess)


#creating function for player 2 to guess no.
def player2_guess():
    global p2_tries, p1_con, correct
    guess = entry.get()
    p2_tries += 1
    correct_dig, misplaced_dig = judgement(p1_con, guess)
    if correct_dig == len(p1_con):
        correct = True
        clear_entry()
        showinfo("Result", f"Player 2 guessed correctly in {p2_tries} attempts!")
        showinfo(title="player 2", message=" Player 2: Enter your confidential number: ")
        label.config(text="Player 2: Enter your confidential number:")
        b.config(command=player2_set_con)
    else:
        showinfo("Result", f"Digits in correct place: {correct_dig}, Misplaced digits: {misplaced_dig}")        

#creating function for player 2  to set confidential no.
def player2_set_con():
    global p2_con, p1_tries, correct
    p2_con = entry.get()
    p1_tries = 0
    correct = False
    showinfo("Player 2", f"Player 2 set the confidential number: {p2_con}")
    clear_entry() 
    label.config(text="Player 1: Guess the number:")
    b.config(command=player1_guess)   
    
#creating function for player 1 to guess the no.
def player1_guess():
    global p1_tries, p2_con, correct
    guess = entry.get()
    p1_tries += 1
    correct_dig, misplaced_dig = judgement(p2_con, guess)
    if correct_dig == len(p2_con):
        correct = True
        showinfo("Result", f"Player 1 guessed correctly in {p1_tries} attempts!")
        winner(p1_tries, p2_tries)
    else:
        showinfo("Result", f"Digits in correct place: {correct_dig}, Misplaced digits: {misplaced_dig}")
    

#main mastermind game function
def Mastermind_Game():
        showinfo(title="welcome", message="Welcome to the world of Mastermind")
        
        #player1 set the confidential number
        showinfo(title="player1", message=" Player 1: Enter your confidential number: ")
        label.config(text="Player 1: Enter your confidential number:")
        b.config(command=player1_set_con)

#initializingglobal variable
p1_con = ""
p2_con = ""
p1_tries = 0
p2_tries = 0
correct = False

# Creating top of the mastermind game
topimg=PhotoImage(file="topmaster.png")
Label(w,image=topimg).pack()

# Adding icons and images
img1 = PhotoImage(file="mastericon.png")
w.iconphoto(False, img1)

#adding the gameicon to the top bar
gameicon=PhotoImage(file="mastericon.png")
Label(w, image=gameicon, bg="#32405b").place(x=30,y=15)

#adding heading to the top bar
head=Label(w,text="MASTERMIND GAME", font="arial 20 bold",fg="black")
head.place(x=120,y=20)

#adding the gameicon to the top bar
gameicon1=PhotoImage(file="mastericon.png")
Label(w, image=gameicon1, bg="#32405b").place(x=430,y=15)

#main tasks addition
f=Frame(w,width=700,height=50,bg="white")
f.place(x=0,y=160)

#taking task entry
t=StringVar()
entry=Entry(f,width=18,font="arial 20",bd=0)
entry.place(x=55,y=7)
entry.focus()




#adding button to add the tsk
b=Button(w,text="SUBMIT",font="arial 20 bold",width=8,bg="#32405b",fg="white",bd=0)
b.place(x=155,y=250)

label = tk.Label(w, text="")
label.pack()
    

               


Mastermind_Game()

w.mainloop()
        
