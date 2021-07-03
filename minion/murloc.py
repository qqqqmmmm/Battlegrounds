"""
鱼人
"""
from minion.minion import Minion


class MurlocTidecaller(Minion):
    def __init__(self, source):
        super(MurlocTidecaller, self).__init__('Murloc Tidecaller', 'murloc', 1, 1, 2, source,
                                               {})


class MurlocTidehunter(Minion):
    def __init__(self, source):
        super(MurlocTidehunter, self).__init__('Murloc Tidehunter', 'murloc', 1, 2, 1, source,
                                               {'battlecry': True})


class RockpoolHunter(Minion):
    def __init__(self, source):
        super(RockpoolHunter, self).__init__('Rockpool Hunter', 'murloc', 1, 2, 3, source,
                                             {'battlecry': True})


class MurlocScout(Minion):
    # 衍生物
    def __init__(self, source):
        super(MurlocScout, self).__init__('Murloc Scout', 'murloc', 1, 1, 1, source,
                                          {})


name2class_murloc = {'Murloc Tidecaller': MurlocTidecaller,
                     'Murloc Tidehunter': MurlocTidehunter,
                     'Rockpool Hunter': RockpoolHunter,
                     'Murloc Scout': MurlocScout}
# 仅包括可购买的随从，不包括衍生物
tier2names_murloc = {1: ('Murloc Tidecaller', 'Murloc Tidehunter', 'Rockpool Hunter'),
                     2: (),
                     3: (),
                     4: (),
                     5: (),
                     6: ()}
