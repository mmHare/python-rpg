"""
    Main client

"""
import game_lib
import json

players = {}
loggedPlayer = ""

try:
    with open("accounts.json", encoding="UTF-8") as file:
        players = json.load(file)
except FileNotFoundError:
    with open("accounts.json", "w", encoding="UTF-8") as file:
        json.dump(players, file, ensure_ascii=False)

# game_dict.save_dict("weapons")
game_lib.game_data = game_lib.load_data(game_lib.game_data)

##enum menu ?
    
while (True):
    print()
    if loggedPlayer != "":
        print("Player logged:", loggedPlayer)
    print('Main menu:')
    print('1: create account')
    print('2: log in')
    print('3: log out')
    print('4: list players')
    print('5: delete account')
    print('0: leave')
    userInput = input()

#create account
    if userInput == '1' or userInput.lower() == 'create' or userInput.lower() == 'create account':
        name = input("What's your name: ").capitalize()
        if name in players:
            print(">> Player", name, "already exists.")
        else:
            print("Select weapon:")
            for weapon in list(game_lib.game_data["weapons"].keys()):
                print('-', weapon)
            weaponTmp = input().lower()
            while weaponTmp not in game_lib.game_data["weapons"]:
                weaponTmp = input("Weapon not found, try again: ").lower()    

            print("Select class:")
            for playerClass in list(game_lib.game_data["playerClasses"].keys()):
                print('-', playerClass)
            classTmp = input().lower()
            while classTmp not in game_lib.game_data["playerClasses"]:
                classTmp = input("Class not found, try again: ").lower()

            players[name] = {'name': name,
                            'lvl': 1,
                            'class': classTmp,
                            'hp':  game_lib.game_data["playerClasses"][classTmp]['hp'],
                            'atk': game_lib.game_data["playerClasses"][classTmp]['atk'],
                            'def': game_lib.game_data["playerClasses"][classTmp]['def'],
                            'weapon': weaponTmp
                            }            
            with open("accounts.json", "w", encoding="UTF-8") as file:
                json.dump(players, file, ensure_ascii=False)
            print("Account created.")

#log in
    elif userInput == '2' or userInput.lower() == 'log in':
        loggedPlayer = input("Enter name: ").capitalize()
        if loggedPlayer not in players:
            print(">> Player", loggedPlayer, "does not exist.")
            loggedPlayer = ""
        else:
            print("Logged in successfuly")
    
#logout
    elif userInput == '3' or userInput.lower() == 'log out':
        loggedPlayer = ""
        print("Logged out successfuly")

#list players
    elif userInput == '4' or userInput.lower() == 'list' or userInput.lower() == 'list players':        
        with open("accounts.json", encoding="UTF-8") as file:  ##odświeżenie listy (ponowne pobranie)
            players = json.load(file)

        if len(players) == 0:
            print(">> No players")
        else:
            for playerTmp in players:
                print(playerTmp, '\t| lvl:', players[playerTmp]['lvl'], '\t| class:', players[playerTmp]['class'])

#delete account
    elif userInput == '5' or userInput.lower() == 'delete' or userInput.lower() == 'delete account':
        nameToDelete = input("Enter account name to delete: ").capitalize()
        if nameToDelete not in players:
            print("Account", nameToDelete, "does not exist.")
        else:
            print("Are you sure to delete account", nameToDelete + "? (Y/n)")
            confirmed = input()
            if confirmed == 'Y':
                players.pop(nameToDelete)

                with open("accounts.json", "w", encoding="UTF-8") as file:    
                    json.dump(players, file, ensure_ascii=False)
                print(">> Account deleted.")

#exit
    elif userInput == '0' or userInput.lower() == 'leave':
        break

#################
## out of loop
print("See Ya...")



