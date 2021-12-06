from tkinter import *

t = Tk()

t.title("Welcome to Tkinter app")

# set Label
lbl1 = Label(t, text="Hello World")
btn = Button(t, text="Click Me")

btn.grid(column=1, row=0)

lbl1.grid(column=0, row=0)

# set T Size
t.geometry('350x200')

t.mainloop()