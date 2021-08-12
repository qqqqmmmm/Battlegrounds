"""
野兽
"""
from minion.minion import Minion, generate_gold_minion


class Alleycat(Minion):
    def __init__(self, source):
        super(Alleycat, self).__init__('Alleycat', 'beast', 1, 1, 1, source,
                                       {'battlecry'})

    def battlecry(self, targets):
        if len(self.board_mine.minions) < 7:
            if self.is_gold:
                self.board_mine.summon_minion(generate_gold_minion(Tabbycat, ''))
            else:
                self.board_mine.summon_minion(Tabbycat(''))


class Tabbycat(Minion):
    # 衍生物
    def __init__(self, source):
        super(Tabbycat, self).__init__('Tabbycat', 'beast', 1, 1, 1, source)


class ScavengingHyena(Minion):
    def __init__(self, source):
        super(ScavengingHyena, self).__init__('Scavenging Hyena', 'beast', 1, 2, 2, source)


class KindlyGrandmother(Minion):
    def __init__(self, source):
        super(KindlyGrandmother, self).__init__('Kindly Grandmother', 'beast', 2, 1, 1, source,
                                                {'deathrattle'})


class BigBadWolf(Minion):
    # 衍生物
    def __init__(self, source):
        super(BigBadWolf, self).__init__('Big Bad Wolf', 'beast', 1, 3, 2, source)


class PackLeader(Minion):
    def __init__(self, source):
        super(PackLeader, self).__init__('Pack Leader', 'none', 2, 3, 4, source)


class RabidSaurolisk(Minion):
    def __init__(self, source):
        super(RabidSaurolisk, self).__init__('Rabid Saurolisk', 'beast', 2, 3, 2, source)


class Houndmaster(Minion):
    def __init__(self, source):
        super(Houndmaster, self).__init__('Houndmaster', 'none', 3, 4, 3, source,
                                          {'battlecry'})

    def battlecry(self, targets):
        attack_buff = 4 if self.is_gold else 2
        health_buff = 4 if self.is_gold else 2
        if len(targets) > 0:
            if targets[0] < len(self.board_mine.minions) - 1:
                if self.board_mine.minions[targets[0]].minion_type in ['beast', 'all']:
                    self.board_mine.minions[targets[0]].buff(attack_buff, health_buff, {'taunt'})
                    return
        # 目标不符合，从左到右依次选择合适目标
        for idx in range(len(self.board_mine.minions) - 1):
            if self.board_mine.minions[idx].minion_type in ['beast', 'all']:
                self.board_mine.minions[idx].buff(attack_buff, health_buff, {'taunt'})
                return


class InfestedWolf(Minion):
    def __init__(self, source):
        super(InfestedWolf, self).__init__('Infested Wolf', 'beast', 3, 3, 3, source,
                                           {'deathrattle'})


class Spider(Minion):
    # 衍生物
    def __init__(self, source):
        super(Spider, self).__init__('Spider', 'beast', 1, 1, 1, source)


class MonstrousMacaw(Minion):
    def __init__(self, source):
        super(MonstrousMacaw, self).__init__('Monstrous Macaw', 'beast', 3, 5, 3, source)


class RatPack(Minion):
    def __init__(self, source):
        super(RatPack, self).__init__('Rat Pack', 'beast', 3, 2, 2, source,
                                      {'deathrattle'})


class Rat(Minion):
    # 衍生物
    def __init__(self, source):
        super(Rat, self).__init__('Rat', 'beast', 1, 1, 1, source)


class CaveHydra(Minion):
    def __init__(self, source):
        super(CaveHydra, self).__init__('Cave Hydra', 'beast', 4, 2, 4, source,
                                        {'battlefury'})


class SavannahHighmane(Minion):
    def __init__(self, source):
        super(SavannahHighmane, self).__init__('Savannah Highmane', 'beast', 4, 6, 5, source,
                                               {'deathrattle'})


class Hyena(Minion):
    # 衍生物
    def __init__(self, source):
        super(Hyena, self).__init__('Hyena', 'beast', 1, 2, 2, source)


class VirmenSensei(Minion):
    def __init__(self, source):
        super(VirmenSensei, self).__init__('Virmen Sensei', 'none', 4, 4, 5, source)

    def battlecry(self, targets):
        attack_buff = 4 if self.is_gold else 2
        health_buff = 4 if self.is_gold else 2
        if len(targets) > 0:
            if targets[0] < len(self.board_mine.minions) - 1:
                if self.board_mine.minions[targets[0]].minion_type in ['beast', 'all']:
                    self.board_mine.minions[targets[0]].buff(attack_buff, health_buff)
                    return
        # 目标不符合，从左到右依次选择合适目标
        for idx in range(len(self.board_mine.minions) - 1):
            if self.board_mine.minions[idx].minion_type in ['beast', 'all']:
                self.board_mine.minions[idx].buff(attack_buff, health_buff)
                return


class IronhideDirehorn(Minion):
    def __init__(self, source):
        super(IronhideDirehorn, self).__init__('Ironhide Direhorn', 'beast', 5, 7, 7, source,
                                               {'overkill'})


class IronhideRunt(Minion):
    # 衍生物
    def __init__(self, source):
        super(IronhideRunt, self).__init__('Ironhide Runt', 'beast', 1, 5, 5, source)


class MamaBear(Minion):
    def __init__(self, source):
        super(MamaBear, self).__init__('Mama Bear', 'beast', 5, 5, 5, source)


class Ghastcoiler(Minion):
    def __init__(self, source):
        super(Ghastcoiler, self).__init__('Ghastcoiler', 'beast', 6, 7, 7, source,
                                          {'deathrattle'})


class GoldrinnTheGreatWolf(Minion):
    def __init__(self, source):
        super(GoldrinnTheGreatWolf, self).__init__('Goldrinn, the Great Wolf', 'beast', 6, 4, 4, source,
                                                   {'deathrattle'})


class Maexxna(Minion):
    def __init__(self, source):
        super(Maexxna, self).__init__('Maexxna', 'beast', 6, 2, 8, source,
                                      {'poisonous'})


name2class_beast = {'Alleycat': Alleycat,
                    'Tabbycat': Tabbycat,
                    'Scavenging Hyena': ScavengingHyena,
                    'Kindly Grandmother': KindlyGrandmother,
                    'Big Bad Wolf': BigBadWolf,
                    'Pack Leader': PackLeader,
                    'Rabid Saurolisk': RabidSaurolisk,
                    'Houndmaster': Houndmaster,
                    'Infested Wolf': InfestedWolf,
                    'Spider': Spider,
                    'Monstrous Macaw': MonstrousMacaw,
                    'Rat Pack': RatPack,
                    'Rat': Rat,
                    'Cave Hydra': CaveHydra,
                    'Savannah Highmane': SavannahHighmane,
                    'Hyena': Hyena,
                    'Virmen Sensei': VirmenSensei,
                    'Ironhide Direhorn': IronhideDirehorn,
                    'Ironhide Runt': IronhideRunt,
                    'Mama Bear': MamaBear,
                    'Ghastcoiler': Ghastcoiler,
                    'Goldrinn, the Great Wolf': GoldrinnTheGreatWolf,
                    'Maexxna': Maexxna}
# 仅包括可购买的随从，不包括衍生物
tier2name_beast = {1: ('Alleycat', 'Scavenging Hyena'),
                   2: ('Kindly Grandmother', 'Pack Leader', 'Rabid Saurolisk'),
                   3: ('Houndmaster', 'Infested Wolf', 'Monstrous Macaw', 'Rat Pack'),
                   4: ('Cave Hydra', 'Savannah Highmane', 'Virmen Sensei'),
                   5: ('Ironhide Direhorn', 'Mama Bear'),
                   6: ('Ghastcoiler', 'Goldrinn, the Great Wolf', 'Maexxna')}
