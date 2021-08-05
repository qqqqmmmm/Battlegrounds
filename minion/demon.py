"""
恶魔
"""
from minion.minion import MinionWhite


class FiendishServant(MinionWhite):
    def __init__(self, source):
        super(FiendishServant, self).__init__('Fiendish Servant', 'demon', 1, 2, 1, source,
                                              {'deathrattle': True})


class VulgarHomunculus(MinionWhite):
    def __init__(self, source):
        super(VulgarHomunculus, self).__init__('Vulgar Homunculus', 'demon', 1, 2, 4, source,
                                               {'taunt': True})


class WrathWeaver(MinionWhite):
    def __init__(self, source):
        super(WrathWeaver, self).__init__('Wrath Weaver', 'none', 1, 1, 3, source,
                                          {})


name2class_demon = {'Fiendish Servant': FiendishServant,
                    'Vulgar Homunculus': VulgarHomunculus,
                    'Wrath Weaver': WrathWeaver}
# 仅包括可购买的随从，不包括衍生物
tier2names_demon = {1: ('Fiendish Servant', 'Vulgar Homunculus', 'Wrath Weaver'),
                    2: (),
                    3: (),
                    4: (),
                    5: (),
                    6: ()}
