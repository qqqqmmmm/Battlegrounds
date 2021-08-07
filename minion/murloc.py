"""
鱼人
"""
from minion.minion import Minion, generate_gold_minion


class MurlocTidecaller(Minion):
    def __init__(self, source):
        super(MurlocTidecaller, self).__init__('Murloc Tidecaller', 'murloc', 1, 1, 2, source,
                                               set())


class MurlocTidehunter(Minion):
    def __init__(self, source):
        super(MurlocTidehunter, self).__init__('Murloc Tidehunter', 'murloc', 1, 2, 1, source,
                                               {'battlecry'})

    def battlecry(self, targets):
        if len(self.board_mine.minions) < 7:
            if self.is_gold:
                self.board_mine.summon_minion(generate_gold_minion(MurlocScout, ''))
            else:
                self.board_mine.summon_minion(MurlocScout(''))


class MurlocScout(Minion):
    # 衍生物
    def __init__(self, source):
        super(MurlocScout, self).__init__('Murloc Scout', 'murloc', 1, 1, 1, source)


class RockpoolHunter(Minion):
    def __init__(self, source):
        super(RockpoolHunter, self).__init__('Rockpool Hunter', 'murloc', 1, 2, 3, source,
                                             {'battlecry'})

    def battlecry(self, targets):
        attack_buff = 2 if self.is_gold else 1
        health_buff = 2 if self.is_gold else 1
        if len(targets) > 0:
            if targets[0] < len(self.board_mine.minions) - 1:  # 触发战吼时自己已经进入board，在最右侧，目标不能是自己
                if self.board_mine.minions[targets[0]].minion_type in ['murloc', 'all']:
                    self.board_mine.minions[targets[0]].buff(attack_buff, health_buff)
                    return
        # 目标不符合，从左到右依次选择合适目标
        for idx in range(len(self.board_mine.minions) - 1):
            if self.board_mine.minions[idx].minion_type in ['murloc', 'all']:
                self.board_mine.minions[idx].buff(attack_buff, health_buff)
                return


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
