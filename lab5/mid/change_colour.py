import tkinter as tk
from tkinter import *
from tkinter.ttk import Progressbar
import time

colours = ["white","red","green","blue","orange","black"]
current_colour = 0

root = Tk()
root.title("colour changer")
root.geometry('400x300')

def change_c():
    global current_colour
    colour = colours[current_colour]

    colour_test.config(bg=colour)
    test_label.config(text=f"{colour}")

    current_colour=(current_colour+1)%len(colours)

test_label = Label(root)
test_label.pack(expand=True)

colour_test = Frame(root, width=400, height=200)

start = Button(root, text = "change", command=change_c)

colour_test.pack()
start.pack(expand=True)

root.mainloop()