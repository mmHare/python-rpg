import json
import os.path

game_data = {
            'weapons': 
                    {'sword':  {'dmg': 3},
                    #  'axe':    {'dmg': 5},
                    #  'dagger': {'dmg': 1},
                    #  'bow':    {'dmg': 3},
                     'wand':   {'dmg': 1}
                    },
            'playerClasses': 
                    {'warrior': {'hp': 13, 'atk': 12, 'def': 15},
                    #  'cleric':  {'hp': 15, 'atk': 10, 'def': 12},
                    #  'rogue':   {'hp': 10, 'atk': 15, 'def': 10},
                     'ranger':  {'hp': 12, 'atk': 13, 'def': 13}
                    }
            }

def load_data(game_library):
    #make sure there is 'data' folder
    if not os.path.isdir('./data/'):
        os.mkdir('./data/')
    
    #load data file or create new one
    dict_path = "./data/data.json"
    if os.path.isfile(dict_path):
        with open(dict_path, encoding="UTF-8") as file:
            game_library = json.load(file)
    else:
        with open(dict_path, "w", encoding="UTF-8") as file:
            json.dump(game_library, file, ensure_ascii=False)
    
    return game_library
