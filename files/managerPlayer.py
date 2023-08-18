'''functions regarding Player'''
import json
import random
import getpass
import requests
from files.confUtils import PATH_ACCOUNTS
from files.gUtils import print_response, prompt_player, check_hashed
from files.game_lib import gameDataObj
from files.modPlayer import Player


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


def check_password(name, tries=1):
    with open(PATH_ACCOUNTS, encoding="UTF-8") as file:
        players = json.load(file)
    passwordTmp = players[name]['password']
    triesCount = 0
    while triesCount < tries:
        passwordIn = getpass.getpass()
        if check_hashed(passwordIn, passwordTmp):
            return True
        else:
            print("(!) Wrong password")
            triesCount += 1
    return False


def log_in():
    playerList = load_players()
    name = input("Enter name: ").capitalize()
    if name not in playerList:
        print("(!) Player", name, "does not exist.")
    else:
        if check_password(name, tries=3):
            print("Logged in successfuly")
            return Player(playerList[name]['playerId'], name).set_data(playerList[name])  # noqa: E501


def createAccount():
    players = load_players()

    name = prompt_player("What's your name (empty to generate random):").capitalize()  # noqa: E501
    if name == "":
        gender = prompt_player("random: male/female/DC?")
        while True:
            if gender == 'male':
                name = api_get_random_name('male')
            elif gender == 'female':
                name = api_get_random_name('female')
            else:
                name = api_get_random_name()
            answer = prompt_player(name + '? (Y/n)').upper()
            if answer == 'Y':
                break
            elif answer == 'N':
                return None
    if name in players:
        print_response("Player " + name + " already exists.")
        player = None
    else:
        playerId = "%05d" % random.randint(0, 99999)
        player = Player(playerId, name)
        player.set_password(getpass.getpass())

        print()
        print("Select class:")
        for playerClass in list(gameDataObj.data["classes"].keys()):
            print('-', playerClass)
        classTmp = prompt_player().lower()
        while classTmp not in gameDataObj.data["classes"]:
            classTmp = prompt_player("Class not found, try again: ").lower()
        player.set_player_class(classTmp)

        print()
        print("Select weapon:")
        for weapon in list(gameDataObj.data["weapons"].keys()):
            print('-', weapon)
        weaponTmp = prompt_player().lower()
        while weaponTmp not in gameDataObj.data["weapons"]:
            weaponTmp = prompt_player("Weapon not found, try again: ").lower()
        player.equip_weapon(weaponTmp)

        players.update(player.get_data_to_save())
        save_players(players)

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
