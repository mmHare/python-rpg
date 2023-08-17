"""
    Main client
"""
from files.game_lib import mainMenu
import files.gUtils as gUtils
import files.gameplay as gameplay
import files.modPlayer as modPlayer

loggedPlayer = None
modPlayer.load_players(True)

########################################
# main loop

while True:
    gUtils.clrscr()
    if loggedPlayer:
        print("Player:", loggedPlayer.name)
    print('Main menu:')

    mainMenu.options_set_visible(loggedPlayer)
    mainMenu.print_options()

    userInput = input().strip()

# create account
    if mainMenu.is_option(userInput, 'create account'):
        gUtils.clrscr()
        loggedPlayer = modPlayer.createAccount()

# log in
    elif mainMenu.is_option(userInput, 'log in'):
        playerTmp = modPlayer.log_in()
        if playerTmp is None:
            print("(!) Log in failed")
            loggedPlayer = None
        else:
            loggedPlayer = playerTmp

# logout
    elif mainMenu.is_option(userInput, 'log out'):
        loggedPlayer = None
        print("Logged out successfuly")

# list players
    elif mainMenu.is_option(userInput, 'list players'):
        players = modPlayer.get_players_list()
        if len(players) == 0:
            print("No players")
        else:
            print('-' * 40)
            for playerTmp, playerVal in players.items():
                print(playerTmp, '\t| lvl:',
                      playerVal['lvl'], '\t| class:',
                      playerVal['playerClass'])
            print('-' * 40)

# delete account
    elif mainMenu.is_option(userInput, 'delete account'):
        players = modPlayer.get_players_list()
        nameToDelete = input("Enter account name to delete: ").capitalize()
        if nameToDelete not in players:
            print("Player", nameToDelete, "does not exist.")
        else:
            print("Are you sure to delete account", nameToDelete + "? (Y/n)")
            confirmed = input()
            if confirmed == 'Y':
                modPlayer.deleteAccount(nameToDelete)
                print(">> Account deleted.")

# play
    elif mainMenu.is_option(userInput, 'play'):
        gameplay.play(loggedPlayer)

# exit
    elif mainMenu.is_option(userInput, 'leave'):
        break

#################
# out of loop
print("See Ya...")
