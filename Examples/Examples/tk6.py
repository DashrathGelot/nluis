# Checkbutton widget (Tkinter checkbox)

from tkinter import *

# for Checkbutton
from tkinter.ttk import *

t = Tk()

t.title("Welcome to Tkinter app")

t.geometry('350x200')

chk_state = BooleanVar()
chk_state.set(True) #set check state check
# chk_state.set(False) #set check state uncheck

# chk_state = IntVar()
# chk_state.set(0) #uncheck
# chk_state.set(1) #check

chk = Checkbutton(t, text='Choose', var=chk_state)

chk.grid(column=0, row=0)

t.geometry('350x200')

t.mainloop()