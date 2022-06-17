#import the required libraries
#tkinter library to create GUI
#random library because we're randomly selecting numbers
from tkinter import *
import random

background_color = "#0D865D"
#create tkinter instance
root=Tk()
#define geometry
root.geometry("1080x720")
root.title("2D Dice Roller")
#background colour
root.configure(bg=background_color)

#GUI will have two basic components
#1.Button which will trigger the rolling of dice
#2.Dice label
l1=Label(root,font=("Helvetica",330))

def roll():
    #create a number variable in which the list of all the ASCII characters of the string will be stored
    #Use backslash because unicode must have a backslash 
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    #configure the label
    #l1.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    #l1.pack()
    #value of dice numbers
    #unicodes and value of correspondings
    numbers = {'\u2680':1, '\u2681':2,
               '\u2682':3, '\u2683':4,
               '\u2684':5, '\u2685':6}
    
    d1 = random.choice(dice)
    d2 = random.choice(dice)
    
    l1.config(text=f'{random.choice(d1)}{random.choice(d2)}')
    l1.pack()

    
    if d1 in numbers.keys():
        d1_number = numbers[d1]
    
    if d2 in numbers.keys():
        d2_number = numbers[d2]

    
    total_number.config(text=f'You Rolled:{d1_number + d2_number}')
    

b1=Button(root,text="Roll the Dice!",foreground='red',command=roll)
b1.place(x=200,y=100)
b1.pack()

total_number = Label(root,text= '', font=("Helvetica",28))
total_number.pack(pady=10)

root.mainloop()