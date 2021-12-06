# Radio Button
from tkinter import *

# Radio Button
from tkinter.ttk import *

t = Tk()

t.title("Welcome to Tkinter app")

t.geometry('350x200')

rad1 = Radiobutton(t,text='First', value=1)

rad2 = Radiobutton(t,text='Second', value=2)

rad3 = Radiobutton(t,text='Third', value=3)

rad1.grid(column=0, row=0)

rad2.grid(column=1, row=0)

rad3.grid(column=2, row=0)

t.geometry('350x200')

t.mainloop()