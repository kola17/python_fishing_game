from tkinter import *
from tkinter import ttk

# Creates Tkinter Window
root = Tk()
root.title("Cool Fishing :)")

# Creates frame with 3 columns and 3 rows
frame = ttk.Frame(root, padding=1, borderwidth=5, relief=SUNKEN, width=250, height=250)
frame.grid(column=3, row=3, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Creates a dropdown menu for selecting a location


root.mainloop()


