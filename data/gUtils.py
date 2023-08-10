import data.game_lib as game_lib

def clrscr():
    print('\n' * 5)

def createAccount(game_data):
    players = game_lib.load_players()
    name = input("What's your name: ").capitalize()
    if name in players:
        print("(!) Player", name, "already exists.")
        player = {}
    else:
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
                        'weapon': weaponTmp
                        }   
        players[player['name']] = player
        game_lib.save_players(players)
        print("Account created.")
    return player

def deleteAccount(nameToDelete):
    players = game_lib.load_players()
    players.pop(nameToDelete)
    game_lib.save_players(players)