from tkinter import *
from tkinter import ttk

# Creates Tkinter Window
root = Tk()
root.title("Cool Fishing :)")

# Creates Tkinter Frame
frame = ttk.Frame(root, padding=1, borderwidth=5, relief=SUNKEN, width=250, height=250)
frame.grid(column=3, row=3, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Creates Tkinter Buttons
fish_button = ttk.Button(frame, text='Cast!').grid(row=2, column=2)
stop_button = ttk.Button(frame, text='Stop!').grid(row=0, column=0)

# Runs Tkinter Window
root.mainloop()


