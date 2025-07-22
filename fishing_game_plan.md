# Fishing Game Development Plan

## Project Overview
A small Tkinter-based fishing game with location-based fishing, probability tables, and inventory management.

## Core Features

### Minimum Viable Game (MVP)
- [ ] Load fish data from JSON file
- [ ] Display fishing location selector (dropdown)
- [ ] "Fish" button that catches random fish based on location probabilities
- [ ] Display caught fish details (name, size, weight)
- [ ] Basic inventory system to store caught fish
- [ ] View inventory functionality

### Nice-to-Have Features (Future Additions)
- [ ] Fish images
- [ ] Multiple fishing locations
- [ ] Rarity system with visual indicators
- [ ] Statistics tracking (total caught, biggest fish, etc.)
- [ ] Save/load game progress
- [ ] Sound effects
- [ ] Fishing animations

## File Structure Plan

```
fishing_game/
├── main.py                 # Main game window and UI
├── fish_game.py           # Game logic classes (Fish, Inventory, etc.)
├── fishing_data.json      # All game data (fish species, locations, probabilities)
├── images/               # Fish pictures (add later)
│   ├── bass.png
│   ├── salmon.png
│   └── default_fish.png
└── README.md             # Project documentation
```

## Development Phases

### Phase 1: Data Foundation
**Goal: Get data loading working**
- [x] Create basic `fishing_data.json` with 2-3 fish species and 1-2 locations
- [x] Design JSON structure (locations with probabilities, fish species with stats)
- [ ] Write Fish class that creates objects from JSON data
- [ ] Test JSON loading and Fish object creation
- [ ] Verify random attribute generation (weight/length within ranges)

**Success Criteria:** Can load JSON, create Fish objects, print their attributes to console

### Phase 2: Basic UI
**Goal: Create functional fishing interface**
- [ ] Set up main Tkinter window
- [ ] Create location selection dropdown (populated from JSON)
- [ ] Add "Go Fishing" button
- [ ] Implement probability-based fish selection
- [ ] Display caught fish information (labels showing name, weight, length)
- [ ] Handle "no location selected" case

**Success Criteria:** Can select location, click button, see random fish based on location probabilities

### Phase 3: Inventory System
**Goal: Store and view caught fish**
- [ ] Create Inventory class to store Fish objects
- [ ] Add caught fish to inventory when fishing
- [ ] Create "View Inventory" button/window
- [ ] Display list of all caught fish
- [ ] Show inventory count/statistics

**Success Criteria:** Fish are saved after catching, can view complete catch history

### Phase 4: Polish & Expansion
**Goal: Improve user experience and add content**
- [ ] Add more fish species and locations to JSON
- [ ] Implement fish images (if desired)
- [ ] Improve UI appearance and layout
- [ ] Add rarity indicators
- [ ] Consider save/load functionality
- [ ] Add error handling and user feedback

## Technical Approach

### Data-Driven Design
Using JSON file to store all game content (fish stats, location probabilities) separate from code logic.

**JSON Structure:**
```json
{
  "locations": {
    "lake_michigan": {
      "display_name": "Lake Michigan",
      "fish_probabilities": {
        "bass": 40,
        "salmon": 30,
        "trout": 25,
        "rare_fish": 5
      }
    }
  },
  "fish_species": {
    "bass": {
      "name": "Largemouth Bass",
      "weight_range": [1.0, 8.0],
      "length_range": [8, 24],
      "rarity": "common"
    }
  }
}
```

### Class Structure Plan
- **Fish Class:** Represents individual caught fish with species-specific attributes
- **Inventory Class:** Manages collection of caught fish
- **Game Class:** Handles main game logic and UI coordination

## First Development Target

**Start Here - Minimal Working Example:**
1. Create simple JSON with 1 fish type
2. Load JSON successfully 
3. Create one Fish object from that data
4. Print fish attributes to console

**Next Steps:** Build UI, then add probability selection, then inventory.

## Notes and Ideas

### Future Location Ideas
- Mountain Stream
- Deep Ocean
- Tropical Lagoon  
- Ice Fishing Hole
- Underground Lake

### Potential Fish Attributes
- Weight (varies within species range)
- Length (varies within species range)  
- Rarity level
- Image file path
- Description text
- Market value (for future trading system?)

### UI Improvements to Consider
- Progress bars for fishing action
- Better visual feedback
- Fish comparison features
- Achievement system

## Development Log
*Use this section to track progress, decisions, and changes*

### [Date] - Project Started
- Initial planning completed
- File structure decided
- Ready to begin Phase 1

---

*This document should be updated as the project evolves. Don't be afraid to modify the plan as you learn what works and what doesn't!*