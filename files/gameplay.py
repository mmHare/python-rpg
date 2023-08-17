import files.gUtils as gUtils
from files.modPlayer import Player


def play(player: Player):
    gUtils.clrscr()
    print("Welcome", player['name'] + '!')
    return
