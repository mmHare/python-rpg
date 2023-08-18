'''constants and configuration stuff'''

import os.path
import fileinput
from datetime import datetime

GAME_NAME = "python-rpg"
GAME_VERSION = "1.0.0.3"

# PATHS TO FILES
PATH_GAME_DATA = "./data/data.json"
PATH_ACCOUNTS = "./data/accounts.json"


def save_config_value(keyName, keyVal):
    lineToSave = keyName + '=' + keyVal
    now = datetime.now()
    modificationTime = now.strftime("%d/%m/%Y %H:%M:%S")

    with open("config.conf", "r", encoding="UTF-8") as file:
        lines = file.read().splitlines()

    keyFound = False
    keyValModified = False
    for i in range(0, len(lines)):
        if lines[i].startswith(keyName):
            if (lines[i] != lineToSave):
                keyValModified = True
                lines[i] = lineToSave
            keyFound = True
            break

    if not keyFound:
        lines.append(lineToSave)
        keyValModified = True

    if keyValModified:
        lines[2] = "#Modified at:" + modificationTime
        with open("config.conf", "w", encoding="UTF-8") as file:
            file.writelines(line + '\n' for line in lines)


def get_config_val(keyName):
    if not os.path.isfile("config.conf"):
        print("Config file not found")
        return None

    keyName = keyName + '='
    with fileinput.input("config.conf", encoding="UTF-8") as f:
        for line in f:
            if line.startswith(keyName):
                return line[len(keyName):].strip()
        print("Value", keyName, "not found")


def check_version():
    print(GAME_NAME, 'v', GAME_VERSION)

    if not os.path.isfile("config.conf"):
        # create new conf file
        with open("config.conf", "w", encoding="UTF-8") as file:
            now = datetime.now()
            modificationTime = now.strftime("%d/%m/%Y %H:%M:%S")
            file.write("#" + GAME_NAME + ' configuration\n')
            file.write("#Created at:" + modificationTime + '\n')
            file.write("#Modified at:" + modificationTime + '\n')
        save_config_value("version", GAME_VERSION)

    if get_config_val("version") == GAME_VERSION:
        print("Version up to date")
    else:
        print("Update available")
        updateVersion()


def updateVersion():
    # update stuff in future
    save_config_value("version", GAME_VERSION)
    print("Update successful")
