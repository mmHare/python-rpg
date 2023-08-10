import json
import os.path

menuOptions = {
    'create account': {'id': '1', 'keywords': ['create', 'create account'], 'visible': True},
    'log in':         {'id': '2', 'keywords': ['log in'],                   'visible': True},
    'log out':        {'id': '3', 'keywords': ['log out'],                  'visible': True},
    'list players':   {'id': '4', 'keywords': ['list', 'list players'],     'visible': True},
    'delete account': {'id': '5', 'keywords': ['delete', 'delete account'], 'visible': True},
    'leave':          {'id': '0', 'keywords': ['leave'],                    'visible': True}
}

def check_if_menu_option(inputStr, menuOption):
    if (inputStr == menuOptions[menuOption]['id']) or (inputStr.lower() in menuOptions[menuOption]['keywords']):
        return True
    else:
        return False

game_data = {
            'weapons': 
                    {'sword':  {'dmg': 3},
                    #  'axe':    {'dmg': 5},
                    #  'dagger': {'dmg': 1},
                    #  'bow':    {'dmg': 3},
                     'wand':   {'dmg': 1}
                    },
            'classes': 
                    {'warrior': {'hp': 13, 'atk': 12, 'def': 15},
                    #  'cleric':  {'hp': 15, 'atk': 10, 'def': 12},
                    #  'rogue':   {'hp': 10, 'atk': 15, 'def': 10},
                     'ranger':  {'hp': 12, 'atk': 13, 'def': 13}
                    }
            }

def load_data():
    if not os.path.isdir('./data/'):
        print('Error loading data: data directory not found')
        exit()

    file_path = "./data/data.json"
    try:
        with open(file_path, encoding="UTF-8") as file:
            game_library = json.load(file)
            for lib_name in game_library:
                print(lib_name, 'loaded...')
            print('Load success')
            print()
    except:
        print('Error loading data')
        exit()
    return game_library

def load_players(createNewFile = False):
    players = {}
    try:
        with open("./data/accounts.json", encoding="UTF-8") as file:
            players = json.load(file)
    except FileNotFoundError:
        if createNewFile:
            save_players(players)  
    return players

def save_players(players):
    with open("./data/accounts.json", "w", encoding="UTF-8") as file:
        json.dump(players, file, ensure_ascii=False)