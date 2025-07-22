import json

# Opens fishing_data.json and assigns it to a variable 'fishing_data'
try:
    with open('fishing_data.json', 'r') as file:
        fishing_data = json.load(file)
# Error checks
except FileNotFoundError:
    print("Error: The file 'fishing_game.json' was not found.")
except json.JSONDecodeError:
    print("Error: Invalid JSON format in 'fishing_game.json'.")
except Exception as e:
    print(f"An unexpected error occured: {e}")
    
# Creates Fish class and assigns attributes as parameters
class Fish:
    def __init__(self, name, diet, habitat, size, weight, rarity):
        self.name = name
        self.diet = diet
        self.habitat = habitat
        self.size = size
        self.weight = weight
        self.rarity = rarity

name = fishing_data["fish_species"]
diet = fishing_data["fish_species"]
habitat = fishing_data["fish_species"]
size = fishing_data["fish_species"]
weight = fishing_data["fish_species"]
rarity = fishing_data["fish_species"]


print(fishing_data["fish_species"].keys())
