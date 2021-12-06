# Radio Button
from tkinter import *

# Radio Button
from tkinter.ttk import *

t = Tk()

t.title("Welcome to Tkinter app")

selected = IntVar()

rad1 = Radiobutton(t,text='First', value=1, variable=selected)

rad2 = Radiobutton(t,text='Second', value=2, variable=selected)

rad3 = Radiobutton(t,text='Third', value=3, variable=selected)

lbl = Label(t, text="Select Something ")


def clicked():

   print(selected.get())
   res = "You Have Selected : " + str(selected.get())
   lbl.configure(text= res)
   

btn = Button(t, text="Click Me", command=clicked)

rad1.grid(column=0, row=0)

rad2.grid(column=1, row=0)

rad3.grid(column=2, row=0)

btn.grid(column=3, row=0)

lbl.grid(column=0, row=2)

t.geometry('350x200')

t.mainloop()