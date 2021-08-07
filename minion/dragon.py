"""
龙
"""
from minion.minion import Minion


class DragonspawnLieutenant(Minion):
    def __init__(self, source):
        super(DragonspawnLieutenant, self).__init__('Dragonspawn Lieutenant', 'dragon', 1, 2, 3, source,
                                                    {'taunt'})


class RedWhelp(Minion):
    def __init__(self, source):
        super(RedWhelp, self).__init__('Red Whelp', 'dragon', 1, 1, 2, source)


name2class_dragon = {'Dragonspawn Lieutenant': DragonspawnLieutenant,
                     'Red Whelp': RedWhelp}
# 仅包括可购买的随从，不包括衍生物
tier2name_dragon = {1: ('Dragonspawn Lieutenant', 'Red Whelp'),
                    2: (),
                    3: (),
                    4: (),
                    5: (),
                    6: ()}
