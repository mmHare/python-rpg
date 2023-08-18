'''Game menu and data libraries'''
import json
import os.path
from files.confUtils import check_version, PATH_GAME_DATA


class MainMenu:
    '''menu and its handling'''
    def __init__(self):
        self.options = {
            'play':           {'id': '1', 'keywords': ['play'],                     'visible': False},  # noqa: E501
            'log in':         {'id': '2', 'keywords': ['log in'],                   'visible': True},   # noqa: E501
            'log out':        {'id': '3', 'keywords': ['log out'],                  'visible': False},  # noqa: E501
            'list players':   {'id': '4', 'keywords': ['list', 'list players'],     'visible': True},   # noqa: E501
            'create account': {'id': '5', 'keywords': ['create', 'create account'], 'visible': True},   # noqa: E501
            'delete account': {'id': '6', 'keywords': ['delete', 'delete account'], 'visible': True},   # noqa: E501
            'leave':          {'id': '7', 'keywords': ['leave'],                    'visible': True}    # noqa: E501
        }

    def set_tmp_id(self):
        '''for selecting visible options'''
        i = 1
        for optVal in self.options.values():
            if optVal['visible']:
                optVal['tmp_id'] = str(i)
                i += 1
            else:
                optVal['tmp_id'] = str(-1)

    def options_set_visible(self, isPlayerLogged):
        '''visibility cases'''
        if isPlayerLogged:
            self.options['play']['visible'] = True
            self.options['log in']['visible'] = False
            self.options['log out']['visible'] = True
            self.options['list players']['visible'] = True
            self.options['create account']['visible'] = False
            self.options['delete account']['visible'] = False
            self.options['leave']['visible'] = True
        else:
            self.options['play']['visible'] = False
            self.options['log in']['visible'] = True
            self.options['log out']['visible'] = False
            self.options['list players']['visible'] = True
            self.options['create account']['visible'] = True
            self.options['delete account']['visible'] = True
            self.options['leave']['visible'] = True
        self.set_tmp_id()

    def print_options(self):
        for option, val in self.options.items():
            if val['visible']:
                print(str(val['tmp_id']) + ': ' + option)

    def is_option(self, inputStr, menuOption):
        if (((inputStr == self.options[menuOption]['tmp_id'])
                or (inputStr.lower() in self.options[menuOption]['keywords']))
                and (inputStr != '-1')):
            return True
        else:
            return False


class GameData:
    '''game libraries'''
    def __init__(self):
        self.load_data()

    def load_data(self):
        '''loading data from file'''
        check_version()

        if not os.path.isdir('./data/'):
            print('Error loading data: data directory not found')
            exit()

        try:
            with open(PATH_GAME_DATA, encoding="UTF-8") as file:
                game_library = json.load(file)
                for lib_name in game_library:
                    print(lib_name, 'loaded...')
                print('Load success')
                print()
        except FileNotFoundError:
            print('Error loading data')
            exit()
        self.data = game_library


##
# game data objects

mainMenu = MainMenu()
gameDataObj = GameData()
