from tkinter import *
from tkinter import ttk
import json

# Loads game data from .json file
with open('fishing_data.json', 'r') as f:
    game_data = json.load(f)

# Location data Variable
location = game_data["locations"]

# Fish Species Variable
fish_species = game_data["fish_species"]

# Creates Tkinter Window
root = Tk()
root.title("Cool Fishing :)")

# Creates frame with 3 columns and 3 rows
frame = ttk.Frame(root, padding=1, borderwidth=5, relief=SUNKEN, width=250, height=250)
frame.grid(column=3, row=3, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Creates a dropdown menu for selecting a location


root.mainloop()

print(location.items())
print(fish_species.items())
