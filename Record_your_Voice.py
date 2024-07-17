#importing neccessary libararies and packages

pip install torch
pip install sounddevice
conda install pytorch torchvision torchaudio -c pytorch
import torch
print(torch.__version__)
import sounddevice as sd
pip install scipy
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo,showwarning
from tkinter.filedialog import askdirectory
import os
from tkinter import Tk, PhotoImage, Label, Entry, Button, messagebox



# Global variable to store the directory path
ad = ""

# Function to ask for the path
def f_path():
    global ad
    ad = askdirectory()
    if not ad:
        showwarning("Path", "No path selected!")
    else:
        showinfo("Path", f"Path selected: {ad}")

# Function to save the file at the given path
def s_file():
    try:
        t = int(s.get())
        add = os.path.join(ad, "voicedemo.wav")
        showinfo(title="Start", message="Recording Started!")
        recording = sd.rec(int(t * 44100), samplerate=44100, channels=2)
        sd.wait()
        write(add, 44100, recording)
        showinfo(title="Stop", message="Recording Ended!")
    except ValueError:
        showwarning(title="Time", message="Time format is wrong!")
    except Exception as e:
        showwarning(title="Error", message=str(e))

# Creating the main window
def mwind():
    global s
    w = Tk()
    w.geometry("600x700")
    w.resizable(False, False)
    w.title("ChiperByte Technologies")
    w.config(bg="orange")

    try:
        pic1 = PhotoImage(file="waves.png")
        l1 = Label(w, image=pic1)
        l1.place(x=60, y=30, height=200, width=500)
    except TclError:
        messagebox.showerror("Error", "waves.png not found")

    s = Entry(w, font=(20))
    s.place(x=175, y=325, height=50, width=250)

    l2 = Label(w, text="Time In Seconds!", font=("Times New Roman", 25), bg="yellow")
    l2.place(x=150, y=250, height=50, width=300)

    b = Button(w, text="Select Location", font=("Times New Roman", 25), command=f_path)
    b.place(x=150, y=400, height=100, width=300)

    try:
        pic2 = PhotoImage(file="recorder1.png")
        start = Button(w, image=pic2, command=s_file)
        start.place(x=250, y=520, height=75, width=75)
    except TclError:
        messagebox.showerror("Error", "recorder.png not found")

    w.mainloop()

mwind()
