import random
from tkinter import *
import tkinter as tk


root = tk.Tk()
root.geometry("400x450")
root.title="Roll the Dice:"
l1 = Label(root, text='', font = ("Times New Roman", 200))


def roll():
    number = ['\u2680', '\u2861', '\u2862', '\u2863', '\u2864', '\u2865']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()


button = tk.Button(root, text="Press to roll..", command=roll)
button.place(x=330, y=10)

root.mainloop
