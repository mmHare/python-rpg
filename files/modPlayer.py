'''module with Player class'''
from files.game_lib import gameDataObj
from files.gUtils import hash_text


class Player:
    '''user player data'''
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
        self.password = hash_text(passwordIn)

    def set_data(self, playerData):
        '''setting data from json file'''
        if (self.playerId == 0) or (self.name == ''):
            return None
        self.lvl = playerData['lvl']
        self.playerClass = playerData['playerClass']
        self.hp = playerData['hp']
        self.attack = playerData['attack']
        self.defence = playerData['defence']
        self.weapon = playerData['weapon']
        return self

    def get_data_to_save(self):
        '''returning json file format'''
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
