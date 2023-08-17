import json
import os.path
# import getpass
# import random
# import keyring

# from cryptography.fernet import Fernet
import files.confUtils as confUtils
# import gUtils
# from files.player import Player

menuOptions = {
    'play':           {'id': '1', 'keywords': ['play'],                     'visible': False},  # noqa: E501
    'log in':         {'id': '2', 'keywords': ['log in'],                   'visible': True},   # noqa: E501
    'log out':        {'id': '3', 'keywords': ['log out'],                  'visible': False},  # noqa: E501
    'list players':   {'id': '4', 'keywords': ['list', 'list players'],     'visible': True},   # noqa: E501
    'create account': {'id': '5', 'keywords': ['create', 'create account'], 'visible': True},   # noqa: E501
    'delete account': {'id': '6', 'keywords': ['delete', 'delete account'], 'visible': True},   # noqa: E501
    'leave':          {'id': '7', 'keywords': ['leave'],                    'visible': True}    # noqa: E501
}


def check_if_menu_option(inputStr, menuOption):
    if ((inputStr == menuOptions[menuOption]['id'])
            or (inputStr.lower() in menuOptions[menuOption]['keywords'])):
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


class GameData:
    def __init__(self):
        self.data = {
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
        self.load_data()

    def load_data(self):
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
        except FileNotFoundError:
            print('Error loading data')
            exit()
        self.data = game_library


gameDataObj = GameData()

# def save_pass_key(playerId, password):
#     if not os.path.isfile('./data/gen.bin'):
#         key = Fernet.generate_key()

#     with open('./data/gen.bin', 'wb') as file:
#         file.write(key)


# def load_pass_key():
#     if not os.path.isfile('./data/gen.bin'):
#         save_pass_key()
#     with open('./data/gen.bin', 'rb') as file:
#         key = file.read()
#     return key
