from numpy.random import choice
import json

# Number of options for each item
n_players = 6
AI_diff = 'Hard'
n_frig = 2
n_cap = 2
n_log = 1
n_tac = 2

# Faction info files
factions = {
    'Advent' : 'advent.json',
    'TEC' : 'tec.json',
    'Vasari' : 'vasari.json'
}

# Map & AI Difficulty
with open("maps.json") as f:
    maps = json.load(f)
    size = str(n_players) + ' Players'
    map_choice = choice(maps[size])

# Randomly select faction
faction = (choice(list(factions.keys())))

# Load selected faction's ships and structures
with open(factions[faction]) as f:
    ships_structs = json.load(f)

# Randomly select ships and structures
frigates = choice(ships_structs['frigates'], n_frig, replace=False)
capitals = choice(ships_structs['capitals'], n_cap, replace=False)
logistic = choice(ships_structs['logistic'], n_log, replace=False)
tactical = choice(ships_structs['tactical'], n_tac, replace=False)

# Print selections to terminal
print('Map: {}'.format(map_choice))
print('Faction: {}'.format(faction))
print('Frigates: ' + ', '.join(frigates))
print('Capital Ships: ' + ', '.join(capitals))
print('Logistic Structures: ' + ', '.join(logistic))
print('Tactical Structures: ' + ', '.join(tactical))









