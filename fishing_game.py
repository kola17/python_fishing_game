import json

# Opens fishing_data.json and assigns it to a variable 'fishing_data'
try:
    with open('fishing_data.json', 'r') as file:
        fishing_data = json.load(file)
# Error checks
except FileNotFoundError:
    print("Error: The file 'fishing_data.json' was not found.")
except json.JSONDecodeError:
    print("Error: Invalid JSON format in 'fishing_data.json'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

locations = fishing_data["locations"]
fish_species = fishing_data["fish_species"]

# Defines Fish class
class Fish:
    def __init__(self, data):
        self.data = data
        self.name = data.get("name")
        self.diet = data.get("diet")
        self.habitat = data.get("habitat")
        self.size = data.get("size")
        self.weight = data.get("weight")
        self.rarity = data.get("rarity")
        
# Defines Location class
class Location:
    def __init__(self, data):
        self.data = data
        self.name = data.get("name")
        self.fish_species = data.get("fish_species")
        self.catch_prob = data.get("catch_probabilities")

      
all_fish = []        
common_fish = []
uncommon_fish = []
rare_fish = []

all_locations = []

# Creates fish objects and adds them to the fish list
for fish_key,fish_data in fish_species.items():
    fish_obj = Fish(fish_data)
    fish_obj.id = fish_key
    all_fish.append(fish_obj)

# Creates location objects and adds them to the locations list
for location_key,location_data in locations.items():
    location_obj = Location(location_data)
    location_obj.id = location_key
    all_locations.append(location_obj)

# Create a fish lookup dictionary (do this once during initialization)
fish_lookup = {fish.id: fish for fish in all_fish}

# Gets list of fish for current location "NEEDS STRING ATM"
def get_fish(current_location):
    current_location_fish = []
    current_location_fish.clear()
    for location in all_locations:
        if location.name == current_location:
            for fish_species in location.fish_species:
                if fish_species in fish_lookup:
                    current_location_fish.append(fish_lookup[fish_species])
            break
    return current_location_fish
                
f = get_fish("Salty Stream")
for f in f:
    print(f.name)

