from tkinter import *

t = Tk()

t.title("Welcome to Tkinter app")

t.geometry('350x200')

lbl = Label(t, text="Write Something ")

lbl.grid(column=0, row=0)

txt = Entry(t,width=10)

# Disable the Text Box
# txt = Entry(t,width=10, state='disabled')
# set Focus On Text Box
# txt.focus()

txt.grid(column=1, row=0)

def clicked():

    res = "You Have Entered : " + txt.get()

    lbl.configure(text= res)

btn = Button(t, text="Click Here", command=clicked)

btn.grid(column=2, row=0)

t.geometry('350x200')

t.mainloop()