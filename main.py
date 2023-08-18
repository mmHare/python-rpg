'''Main client'''

from files.game_lib import mainMenu
from files.gUtils import print_response, prompt_player, clrscr
import files.gameplay as gameplay
import files.managerPlayer as managerPlayer

loggedPlayer = None
managerPlayer.load_players(True)

########################################
# main loop

while True:
    clrscr()
    if loggedPlayer:
        print("Logged player:", loggedPlayer.name)
    print('Main menu:')

    mainMenu.options_set_visible(loggedPlayer)
    mainMenu.print_options()

    userInput = prompt_player()

# create account
    if mainMenu.is_option(userInput, 'create account'):
        loggedPlayer = managerPlayer.createAccount()

# log in
    elif mainMenu.is_option(userInput, 'log in'):
        playerTmp = managerPlayer.log_in()
        if playerTmp is None:
            print_response("Log in failed")
            loggedPlayer = None
        else:
            loggedPlayer = playerTmp

# logout
    elif mainMenu.is_option(userInput, 'log out'):
        loggedPlayer = None
        print_response("Logged out successfuly")

# list players
    elif mainMenu.is_option(userInput, 'list players'):
        players = managerPlayer.load_players()
        if len(players) == 0:
            
            print_response("No players")
        else:
            print('-' * 40)
            for playerTmp, playerVal in players.items():
                print(playerTmp, '\t| lvl:',
                      playerVal['lvl'], '\t| class:',
                      playerVal['playerClass'])
            print('-' * 40)

# delete account
    elif mainMenu.is_option(userInput, 'delete account'):
        players = managerPlayer.load_players()
        nameToDelete = input("Enter account name to delete: ").capitalize()
        if nameToDelete not in players:
            print_response("Player " + nameToDelete + " does not exist.")
        else:
            print()
            confirmed = prompt_player("Are you sure to delete account " + nameToDelete + "? (Y/n)")  # noqa: E501
            if confirmed == 'Y':
                managerPlayer.deleteAccount(nameToDelete)
                print_response("Account deleted.")

# play
    elif mainMenu.is_option(userInput, 'play'):
        gameplay.play(loggedPlayer)

# exit
    elif mainMenu.is_option(userInput, 'leave'):
        break

#################
# out of loop
print("See Ya...")
