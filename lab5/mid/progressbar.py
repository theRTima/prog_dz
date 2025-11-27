import tkinter
from tkinter import *
from tkinter.ttk import Progressbar
import time

root = Tk()
root.title("progressbar")
root.geometry('400x300')

test_label = Label(root)
test_label.pack(expand=True)

bar = Progressbar(root,length=250)
bar.pack(expand=True)

def start_bar():
    bar["value"] = 0
    root.update()

    for i in range(101):
        bar["value"] = i
        root.update()
        time.sleep(0.04)

start = Button(root, text = "Start",command=start_bar)
start.pack(expand=True)

root.mainloop()