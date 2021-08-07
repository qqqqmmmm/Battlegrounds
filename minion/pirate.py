"""
海盗
"""
from minion.minion import Minion


class DeckSwabbie(Minion):
    def __init__(self, source):
        super(DeckSwabbie, self).__init__('Deck Swabbie', 'pirate', 1, 2, 2, source,
                                          {'battlecry'})

    def battlecry(self, targets):
        if self.is_gold:
            self.board_mine.upgrade_cost = max(0, self.board_mine.upgrade_cost - 2)
        else:
            self.board_mine.upgrade_cost = max(0, self.board_mine.upgrade_cost - 1)


class Scallywag(Minion):
    def __init__(self, source):
        super(Scallywag, self).__init__('Scallywag', 'pirate', 1, 2, 1, source,
                                        {'deathrattle'})


class SkyPirate(Minion):
    def __init__(self, source):
        super(SkyPirate, self).__init__('Sky Pirate', 'pirate', 1, 1, 1, source)


name2class_pirate = {'Deck Swabbie': DeckSwabbie,
                     'Scallywag': Scallywag,
                     'Sky Pirate': SkyPirate}
# 仅包括可购买的随从，不包括衍生物
tier2name_pirate = {1: ('Deck Swabbie', 'Scallywag'),
                    2: (),
                    3: (),
                    4: (),
                    5: (),
                    6: ()}
