"""
    Main client
"""
import files.game_lib as game_lib
from files.game_lib import game_data, menuOptions, check_if_menu_option
import files.gUtils as gUtils
import files.gameplay as gameplay

##load data
game_data = game_lib.load_data()
players = game_lib.load_players(True)
loggedPlayer = {}
visibleMenuOptions = []

# [strOut, key] = gUtils.encrypt_text('oleole')
# print(strOut)
# print(key)
# print(gUtils.decrypt_text(strOut, key))

########################################
##main loop    
while (True):
    gUtils.clrscr()
    if loggedPlayer != {}:
        print("Player:", loggedPlayer['name'])
    print('Main menu:')
    
    menuOptions = game_lib.menu_options_set_visible(menuOptions, (loggedPlayer != {}))
    visibleMenuOptions = []
    i = 1
    for menuOption in menuOptions:                
        if menuOptions[menuOption]['visible']:
            visibleMenuOptions.append((i, menuOptions[menuOption]['id']))
            print(str(visibleMenuOptions[i-1][0]) + ': ' + menuOption)
            i += 1

    userInput = input()

    if userInput.isnumeric():
        for pos, id in visibleMenuOptions:
            if int(userInput) == pos:
                userInput = str(id)
                break

#create account
    if check_if_menu_option(userInput, 'create account'):
        gUtils.clrscr()
        loggedPlayer = gUtils.createAccount(game_data)

#log in
    elif check_if_menu_option(userInput, 'log in'):
        playerTmp = game_lib.log_in()
        if playerTmp == None:
            print("(!) Log in failed")
            loggedPlayer = {}
        else:
            loggedPlayer = playerTmp
    
#logout
    elif check_if_menu_option(userInput, 'log out'):
        loggedPlayer = {}
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

#play
    elif check_if_menu_option(userInput, 'play'):
        gameplay.play(loggedPlayer)

#exit
    elif check_if_menu_option(userInput, 'leave'):
        break

#################
## out of loop
print("See Ya...")
