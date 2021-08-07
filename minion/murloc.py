"""
鱼人
"""
from minion.minion import MinionWhite, generate_gold_minion


class MurlocTidecaller(MinionWhite):
    def __init__(self, source):
        super(MurlocTidecaller, self).__init__('Murloc Tidecaller', 'murloc', 1, 1, 2, source,
                                               set())


class MurlocTidehunter(MinionWhite):
    def __init__(self, source):
        super(MurlocTidehunter, self).__init__('Murloc Tidehunter', 'murloc', 1, 2, 1, source,
                                               {'battlecry'})

    def battlecry(self, targets):
        if len(self.board_mine.minions) < 7:
            if self.is_gold:
                self.board_mine.summon_minion(generate_gold_minion(MurlocScout, ''))
            else:
                self.board_mine.summon_minion(MurlocScout(''))


class MurlocScout(MinionWhite):
    # 衍生物
    def __init__(self, source):
        super(MurlocScout, self).__init__('Murloc Scout', 'murloc', 1, 1, 1, source,
                                          set())


class RockpoolHunter(MinionWhite):
    def __init__(self, source):
        super(RockpoolHunter, self).__init__('Rockpool Hunter', 'murloc', 1, 2, 3, source,
                                             {'battlecry'})


name2class_murloc = {'Murloc Tidecaller': MurlocTidecaller,
                     'Murloc Tidehunter': MurlocTidehunter,
                     'Murloc Scout': MurlocScout,
                     'Rockpool Hunter': RockpoolHunter}
# 仅包括可购买的随从，不包括衍生物
tier2name_murloc = {1: ('Murloc Tidecaller', 'Murloc Tidehunter', 'Rockpool Hunter'),
                    2: (),
                    3: (),
                    4: (),
                    5: (),
                    6: ()}
