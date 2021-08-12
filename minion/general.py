"""
中立
"""
from minion.minion import Minion
import random


class AcolyteOfCThun(Minion):
    def __init__(self, source):
        super(AcolyteOfCThun, self).__init__('Acolyte Of CThun', 'none', 1, 2, 2, source,
                                             {'taunt', 'reborn'})


class TormentedRitualist(Minion):
    def __init__(self, source):
        super(TormentedRitualist, self).__init__('Tormented Ritualist', 'none', 2, 2, 3, source,
                                                 {'taunt', 'when attacked'})

    def when_attacked(self, minion_attacked):
        if minion_attacked is self:
            attack_buff = 2 if self.is_gold else 1
            health_buff = 2 if self.is_gold else 1
            for idx, minion in enumerate(self.minions_mine):
                if minion is self:
                    if idx > 0:
                        self.minions_mine[idx - 1].buff(attack_buff, health_buff, combat=True)
                    if idx < len(self.minions_mine) - 1:
                        self.minions_mine[idx + 1].buff(attack_buff, health_buff, combat=True)


class ArmOfTheEmpire(Minion):
    def __init__(self, source):
        super(ArmOfTheEmpire, self).__init__('Arm of the Empire', 'none', 3, 4, 5, source,
                                             {'when attacked'})

    def when_attacked(self, minion_attacked):
        if 'taunt' in minion_attacked.characters:
            attack_buff = 4 if self.is_gold else 2
            health_buff = 0
            self.buff(attack_buff, health_buff, combat=True, permanent=True)


class ChampionOfYShaarj(Minion):
    def __init__(self, source):
        super(ChampionOfYShaarj, self).__init__('Champion of YShaarj', 'none', 4, 4, 4, source,
                                                {'when attacked'})

    def when_attacked(self, minion_attacked):
        if 'taunt' in minion_attacked.characters:
            attack_buff = 2 if self.is_gold else 1
            health_buff = 2 if self.is_gold else 1
            self.buff(attack_buff, health_buff, combat=True, permanent=True)


class ZappSlywick(Minion):
    def __init__(self, source):
        super(ZappSlywick, self).__init__('Zapp Slywick', 'none', 6, 7, 10, source,
                                          {'windfury', 'choose attack target'})

    def choose_attack_target(self):
        attack = 2147483648  # 此数值为炉石传说最大攻击力-1
        targets = []
        for minion in self.minions_opponent:
            if minion.attack < attack:
                attack = minion.attack
                targets.clear()
                targets.append(minion)
            elif minion.attack == attack:
                targets.append(minion)
        if len(targets) == 1:
            return targets[0]
        return random.choice(targets)


name2class_general = {'Acolyte Of CThun': AcolyteOfCThun,
                      'Tormented Ritualist': TormentedRitualist,
                      'Arm of the Empire': ArmOfTheEmpire,
                      'Champion of YShaarj': ChampionOfYShaarj,
                      'Zapp Slywick': ZappSlywick}
tier2name_general = {1: ('Acolyte Of CThun',),
                     2: ('Tormented Ritualist', ),
                     3: ('Arm of the Empire', ),
                     4: ('Champion of YShaarj', ),
                     5: (),
                     6: ('Zapp Slywick', )}
