import json
import random
import getpass
import requests
from files.game_lib import gameDataObj
import files.gUtils as gUtils
from files.confUtils import PATH_ACCOUNTS


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

    def load_data(self):
        if (self.playerId == 0) or (self.name == ''):
            return None
        players = load_players()
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

    def save_data(self):
        if (self.playerId == 0) or (self.name == ''):
            return None
        players = load_players()
        if self.name in players:
            players[self.name] = self.get_data_to_save()
        else:
            players.update(self.get_data_to_save())
        save_players(players)


def save_players(players):
    with open(PATH_ACCOUNTS, "w", encoding="UTF-8") as file:
        json.dump(players, file, ensure_ascii=False)


def load_players(tryNewFile=False):
    players = {}
    try:
        with open(PATH_ACCOUNTS, encoding="UTF-8") as file:
            players = json.load(file)
    except FileNotFoundError:
        if tryNewFile:
            save_players(players)
    return players


def get_players_list():
    players = load_players()
    playerList = {}
    for player in players:
        playerList.update({players[player]['name']: {
                'name':        players[player]['name'],
                'playerId':    players[player]['playerId'],
                'lvl':         players[player]['lvl'],
                'playerClass': players[player]['playerClass']}
            })
    return playerList


def check_password(playerId, name, tries=1):
    with open(PATH_ACCOUNTS, encoding="UTF-8") as file:
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
        if check_password(playerList[name]['playerId'], name, tries=3):
            print("Logged in successfuly")
            return Player(playerList[name]['playerId'], name).load_data()  # noqa: E501


def createAccount():
    playerList = get_players_list()

    name = input("What's your name (random to generate): ").capitalize()
    if name == 'Random':
        gender = input("random: male/female/DC? ")
        while True:
            if gender == 'male':
                name = api_get_random_name('male')
            elif gender == 'female':
                name = api_get_random_name('female')
            else:
                name = api_get_random_name()
            answer = input(name + '? (Y/n) ').upper()
            if answer == 'Y':
                break
            elif answer == 'N':
                return None
    if name in playerList:
        print("(!) Player", name, "already exists.")
        player = None
    else:
        playerId = "%05d" % random.randint(0, 99999)
        player = Player(playerId, name)
        player.set_password(getpass.getpass())

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

        player.save_data()

        print("Account created.")
    return player


def deleteAccount(nameToDelete):
    players = load_players()
    players.pop(nameToDelete)
    save_players(players)


def api_get_random_name(gender=""):
    params = {"datatype": "json"}
    if gender in ["male", "female"]:
        params["gender"] = gender

    name = ""
    i = 0
    while i < 30:
        r = requests.get("https://randomuser.me/api/", params, timeout=5)
        result = r.json()

        nameTmp = result['results'][0]['name']['first']
        if nameTmp.isascii():
            name = nameTmp
            break
        i += 1
    return name
