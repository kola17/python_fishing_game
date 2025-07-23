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
        self.name = data.get(fishing_data["locations"].values())


       
all_fish = []        
common_fish = []
uncommon_fish = []
rare_fish = []

# Creates fish objects from .json file and assigns them to all_fish
def put_fish_in_list():
    for fish_data in fishing_data["fish_species"].values():
        fish = Fish(fish_data)
        all_fish.append(fish)
# Calls function
put_fish_in_list()

# Creates fish objects from .json file and assigns them to lists based on rarity.
def assign_fish_rarity_lists():
    for fish_data in fishing_data["fish_species"].values():
        fish = Fish(fish_data)
        if fish.rarity == "common" and fish not in common_fish:
            common_fish.append(fish)
        elif fish.rarity == "uncommon" and fish not in uncommon_fish:
            uncommon_fish.append(fish)
        elif fish.rarity == "rare" and fish not in rare_fish:
            rare_fish.append(fish)
        else:
            break    
# Calls function
assign_fish_rarity_lists()

# def get_fish(current_location):
    #for location_data in fishing_data["locations"].values():
        #location = Location(location_data)
    
    #for fish_data in fishing_data["fish_species"].values():
        #fish = Fish(fish_data)
        
        #fish_species = []
        
        #for species in location.fish_species:
            #fish_species.append(species)
            
            #for i,name in enumerate(fish_species):
               # if name == fish.name:
                    #fish_species[i] = fish
                    
def get_fish(current_location):
    # Create fish lookup dictionary once
    fish_lookup = {}
    for fish_data in fishing_data["fish_species"].values():
        fish = Fish(fish_data)
        fish_lookup[fish.name] = fish
    
    # Find matching location and convert names to objects
    for location_data in fishing_data["locations"].values():
        location = Location(location_data)
        if location.name == current_location:
            return [fish_lookup[name] for name in location.fish_species if name in fish_lookup]
    return []

fish_list = get_fish(fishing_data["locations"]["Flatwater Eddy"])

print(fish_list)             
            
            
    
    
    
    
    
    

#fish=Fish(fishing_data["fish_species"]["pike"])

#print(fish.rarity)
