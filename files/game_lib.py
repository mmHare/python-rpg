import json
import os.path
import getpass
import files.confUtils as confUtils

menuOptions = {    
    'play':           {'id': '1', 'keywords': ['play'],                     'visible': False},
    'log in':         {'id': '2', 'keywords': ['log in'],                   'visible': True},
    'log out':        {'id': '3', 'keywords': ['log out'],                  'visible': False},    
    'list players':   {'id': '4', 'keywords': ['list', 'list players'],     'visible': True},
    'create account': {'id': '5', 'keywords': ['create', 'create account'], 'visible': True},
    'delete account': {'id': '6', 'keywords': ['delete', 'delete account'], 'visible': True},
    'leave':          {'id': '7', 'keywords': ['leave'],                    'visible': True}
}

def check_if_menu_option(inputStr, menuOption):
    if (inputStr == menuOptions[menuOption]['id']) or (inputStr.lower() in menuOptions[menuOption]['keywords']):
        return True
    else:
        return False
    
def menu_options_set_visible(menuItems, isPlayerLogged):
    if isPlayerLogged:
        menuItems['play']['visible'] = True
        menuItems['log in']['visible'] = False
        menuItems['log out']['visible'] = True
        menuItems['list players']['visible'] = True
        menuItems['create account']['visible'] = False
        menuItems['delete account']['visible'] = False
        menuItems['leave']['visible'] = True
    else:
        menuItems['play']['visible'] = False
        menuItems['log in']['visible'] = True
        menuItems['log out']['visible'] = False
        menuItems['list players']['visible'] = True
        menuItems['create account']['visible'] = True
        menuItems['delete account']['visible'] = True
        menuItems['leave']['visible'] = True
    return menuItems


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
    confUtils.check_version()

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

def log_in():
    players = load_players()
            
    name = input("Enter name: ").capitalize()
    if name not in players:
        print("(!) Player", name, "does not exist.")            
    else:             
        triesCount = 0
        while triesCount < 3:
            passwordTmp = getpass.getpass()
            if passwordTmp == players[name]['password']:                      
                print("Logged in successfuly")
                return players[name]
            else:
                print("(!) Wrong password")
                triesCount += 1
        return None
    
def createAccount(game_data):
    players = load_players()
    name = input("What's your name: ").capitalize()
    if name in players:
        print("(!) Player", name, "already exists.")
        player = {}
    else:       
        playerPassword = getpass.getpass() 

        print("Select weapon:")
        for weapon in list(game_data["weapons"].keys()):
            print('-', weapon)
        weaponTmp = input().lower()
        while weaponTmp not in game_data["weapons"]:
            weaponTmp = input("Weapon not found, try again: ").lower()    

        print("Select class:")
        for playerClass in list(game_data["classes"].keys()):
            print('-', playerClass)
        classTmp = input().lower()
        while classTmp not in game_data["classes"]:
            classTmp = input("Class not found, try again: ").lower()

        player = {'name': name,
                        'lvl': 1,
                        'class': classTmp,
                        'hp':  game_data["classes"][classTmp]['hp'],
                        'atk': game_data["classes"][classTmp]['atk'],
                        'def': game_data["classes"][classTmp]['def'],
                        'weapon': weaponTmp,
                        'password': playerPassword
                        }   
        players[player['name']] = player
        save_players(players)
        print("Account created.")
    return player

def deleteAccount(nameToDelete):
    players = load_players()
    players.pop(nameToDelete)
    save_players(players)