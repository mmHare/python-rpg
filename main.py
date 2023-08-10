"""
    Main client
"""
import data.game_lib as game_lib
from data.game_lib import game_data
from data.game_lib import menuOptions
from data.game_lib import check_if_menu_option
import data.gUtils as gUtils

##load data
game_data = game_lib.load_data()
players = game_lib.load_players(True)
loggedPlayer = {}

########################################
##main loop    
while (True):
    gUtils.clrscr()
    if loggedPlayer != {}:
        print("Player:", loggedPlayer['name'])
    print('Main menu:')
    
    for menuOption in menuOptions:
        if menuOptions[menuOption]['visible']:
            print(menuOptions[menuOption]['id'] + ': ' + menuOption)

    userInput = input()

#create account
    if check_if_menu_option(userInput, 'create account'):
        gUtils.clrscr()
        loggedPlayer = gUtils.createAccount(game_data)

#log in
    elif check_if_menu_option(userInput, 'log in'):
        name = input("Enter name: ").capitalize()
        if name not in players:
            print("(!) Player", name, "does not exist.")            
        else:
            loggedPlayer = players[name]
            print("Logged in successfuly")
    
#logout
    elif check_if_menu_option(userInput, 'log out'):
        loggedPlayer = ""
        print("Logged out successfuly")

#list players
    elif check_if_menu_option(userInput, 'list players'):     
        players = game_lib.load_players()
        if len(players) == 0:
            print("No players")
        else:
            print('-' * 40)
            for playerTmp in players:
                print(playerTmp, '\t| lvl:', players[playerTmp]['lvl'], '\t| class:', players[playerTmp]['class'])
            print('-' * 40)

#delete account
    elif check_if_menu_option(userInput, 'delete account'):
        nameToDelete = input("Enter account name to delete: ").capitalize()
        if nameToDelete not in players:
            print("Player", nameToDelete, "does not exist.")
        else:
            print("Are you sure to delete account", nameToDelete + "? (Y/n)")
            confirmed = input()
            if confirmed == 'Y':
                gUtils.deleteAccount(nameToDelete)
                print(">> Account deleted.")

#exit
    elif check_if_menu_option(userInput, 'leave'):
        break

#################
## out of loop
print("See Ya...")
