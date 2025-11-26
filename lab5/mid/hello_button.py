import tkinter as tk
from tkinter import *

root = Tk()
root.title("Hello Button")
root.geometry('400x300')

test_label = Label(root)
test_label.pack()

h_button = Button(root, text = "Hello")
h_button.pack(expand=True)

root.mainloop()