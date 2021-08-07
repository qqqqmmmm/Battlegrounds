"""
野兽
"""
from minion.minion import MinionWhite, generate_gold_minion


class Alleycat(MinionWhite):
    def __init__(self, source):
        super(Alleycat, self).__init__('Alleycat', 'beast', 1, 1, 1, source,
                                       {'battlecry'})

    def battlecry(self, targets):
        if len(self.board_mine.minions) < 7:
            if self.is_gold:
                self.board_mine.summon_minion(generate_gold_minion(Tabbycat, ''))
            else:
                self.board_mine.summon_minion(Tabbycat(''))


class Tabbycat(MinionWhite):
    # 衍生物
    def __init__(self, source):
        super(Tabbycat, self).__init__('Tabbycat', 'beast', 1, 1, 1, source,
                                       set())


class ScavengingHyena(MinionWhite):
    def __init__(self, source):
        super(ScavengingHyena, self).__init__('Scavenging Hyena', 'beast', 1, 2, 2, source,
                                              set())


name2class_beast = {'Alleycat': Alleycat,
                    'Tabbycat': Tabbycat,
                    'Scavenging Hyena': ScavengingHyena}
# 仅包括可购买的随从，不包括衍生物
tier2name_beast = {1: ('Alleycat', 'Scavenging Hyena'),
                   2: (),
                   3: (),
                   4: (),
                   5: (),
                   6: ()}
