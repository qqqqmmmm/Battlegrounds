"""
海盗
"""
from minion.minion import MinionWhite


class DeckSwabbie(MinionWhite):
    def __init__(self, source):
        super(DeckSwabbie, self).__init__('Deck Swabbie', 'pirate', 1, 2, 2, source,
                                          {'battlecry'})


class Scallywag(MinionWhite):
    def __init__(self, source):
        super(Scallywag, self).__init__('Scallywag', 'pirate', 1, 2, 1, source,
                                        {'deathrattle'})


# 此处缺少11衍生物运动员


name2class_pirate = {'Deck Swabbie': DeckSwabbie,
                     'Scallywag': Scallywag}
tier2name_pirate = {1: ('Deck Swabbie', 'Scallywag'),
                    2: (),
                    3: (),
                    4: (),
                    5: (),
                    6: ()}
