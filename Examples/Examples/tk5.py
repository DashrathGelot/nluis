# Combobox

from tkinter import *

# for Combobox
from tkinter.ttk import *

t = Tk()

t.title("Welcome to Tkinter app")

t.geometry('350x200')

combo = Combobox(t)

combo['values']= ("Text", 1, 2, 3, 4, 5)

combo.current(2) #set the selected item

combo.grid(column=0, row=0)

t.geometry('350x200')

t.mainloop()