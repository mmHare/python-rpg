import json
import random
import getpass
# import files.game_lib as game_lib
from files.game_lib import gameDataObj
import files.gUtils as gUtils


class Player:
    def __init__(self, playerId=0, name='') -> None:
        self.playerId = playerId
        self.name = name
        self.lvl = 1
        self.playerClass = ''
        self.hp = 10
        self.attack = 10
        self.defence = 10
        self.weapon = ''
        self.password = ''

    def set_player_class(self, playerClass):
        self.playerClass = playerClass
        self.hp = gameDataObj.data["classes"][playerClass]['hp']
        self.attack = gameDataObj.data["classes"][playerClass]['atk']
        self.defence = gameDataObj.data["classes"][playerClass]['def']

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def set_password(self, passwordIn):
        self.password = gUtils.hash_text(passwordIn)

    def load_player_data(self):
        if (self.playerId == 0) or (self.name == ''):
            return None
        with open("./data/accounts.json", encoding="UTF-8") as file:
            players = json.load(file)
        self.lvl = players[self.name]['lvl']
        self.playerClass = players[self.name]['playerClass']
        self.hp = players[self.name]['hp']
        self.attack = players[self.name]['attack']
        self.defence = players[self.name]['defence']
        self.weapon = players[self.name]['weapon']
        return self

    def get_data_to_save(self):
        playerData = {self.name: {'playerId': self.playerId,
                                  'name': self.name,
                                  'lvl': self.lvl,
                                  'playerClass': self.playerClass,
                                  'hp':  self.hp,
                                  'attack': self.attack,
                                  'defence': self.defence,
                                  'weapon': self.weapon,
                                  'password': self.password
                                  }
                      }
        return playerData


def save_players(players):
    with open("./data/accounts.json", "w", encoding="UTF-8") as file:
        json.dump(players, file, ensure_ascii=False)


def player_save(player: Player):
    playerToSave = player.get_data_to_save()
    players = {}

    with open("./data/accounts.json", encoding="UTF-8") as file:
        players = json.load(file)
    if player.name in players:
        players[player.name] = playerToSave
    else:
        players.update(playerToSave)
    save_players(players)


def get_players_list():
    players = load_players()
    playerList = {}
    for player in players:
        playerList.update({players[player]['name']: {
            'name': players[player]['name'],
            'playerId': players[player]['playerId'],
            'lvl': players[player]['lvl'],
            'playerClass': players[player]['playerClass']
        }})
    return playerList


def load_players(tryNewFile=False):
    players = {}
    try:
        with open("./data/accounts.json", encoding="UTF-8") as file:
            players = json.load(file)
    except FileNotFoundError:
        if tryNewFile:
            save_players(players)
    return players


def check_password(playerId, name, tries=1):
    with open("./data/accounts.json", encoding="UTF-8") as file:
        players = json.load(file)
    passwordTmp = players[name]['password']
    triesCount = 0
    while triesCount < tries:
        passwordIn = getpass.getpass()
        if gUtils.check_hashed(passwordIn, passwordTmp):
            return True
        else:
            print("(!) Wrong password")
            triesCount += 1
    return False


def log_in():
    playerList = get_players_list()
    name = input("Enter name: ").capitalize()
    if name not in playerList:
        print("(!) Player", name, "does not exist.")
    else:
        if check_password(playerList[name]['playerId'], name):
            print("Logged in successfuly")
            return Player(playerList[name]['playerId'], name).load_player_data()  # noqa: E501


def createAccount():
    playerList = get_players_list()

    name = input("What's your name: ").capitalize()
    if name in playerList:
        print("(!) Player", name, "already exists.")
        player = {}
    else:
        playerId = "%05d" % random.randint(0, 99999)
        player = Player(playerId, name)
        playerPassword = getpass.getpass()
        player.set_password(playerPassword)

        # game_data = game_lib.load_data()

        print("Select class:")
        for playerClass in list(gameDataObj.data["classes"].keys()):
            print('-', playerClass)
        classTmp = input().lower()
        while classTmp not in gameDataObj.data["classes"]:
            classTmp = input("Class not found, try again: ").lower()
        player.set_player_class(classTmp)

        print("Select weapon:")
        for weapon in list(gameDataObj.data["weapons"].keys()):
            print('-', weapon)
        weaponTmp = input().lower()
        while weaponTmp not in gameDataObj.data["weapons"]:
            weaponTmp = input("Weapon not found, try again: ").lower()
        player.equip_weapon(weaponTmp)

        # player = {'id': id,
        #           'name': name,
        #           'lvl': 1,
        #           'class': classTmp,
        #           'hp':  game_data["classes"][classTmp]['hp'],
        #           'atk': game_data["classes"][classTmp]['atk'],
        #           'def': game_data["classes"][classTmp]['def'],
        #           'weapon': weaponTmp,
        #           'magic': magic,
        #           'password': playerPasswordSec
        #           }
        # players[name] = player

        # players.update(player)

        player_save(player)
        # save_players(players)
        print("Account created.")
    return player


def deleteAccount(nameToDelete):
    players = load_players()
    players.pop(nameToDelete)
    save_players(players)
