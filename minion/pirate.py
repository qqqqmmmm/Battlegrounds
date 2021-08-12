"""
海盗
"""
from minion.minion import Minion


class DeckSwabbie(Minion):
    def __init__(self, source):
        super(DeckSwabbie, self).__init__('Deck Swabbie', 'pirate', 1, 2, 2, source,
                                          {'battlecry'})

    def battlecry(self, targets):
        cost_reduce = 2 if self.is_gold else 1
        self.board_mine.upgrade_cost = max(0, self.board_mine.upgrade_cost - cost_reduce)


class Scallywag(Minion):
    def __init__(self, source):
        super(Scallywag, self).__init__('Scallywag', 'pirate', 1, 2, 1, source,
                                        {'deathrattle'})


class SkyPirate(Minion):
    def __init__(self, source):
        super(SkyPirate, self).__init__('Sky Pirate', 'pirate', 1, 1, 1, source)


class RipsnarlCaptain(Minion):
    def __init__(self, source):
        super(RipsnarlCaptain, self).__init__('Ripsnarl Captain', 'pirate', 4, 4, 5, source,
                                              {'when attack'})

    def when_attack(self, minion_attack):
        if minion_attack.minion_type in ['pirate', 'all']:
            if minion_attack is not self:
                attack_buff = 4 if self.is_gold else 2
                health_buff = 4 if self.is_gold else 2
                minion_attack.buff(attack_buff, health_buff, combat=True)


class DreadAdmiralEliza(Minion):
    def __init__(self, source):
        super(DreadAdmiralEliza, self).__init__('Dread Admiral Eliza', 'pirate', 6, 6, 7, source,
                                                {'when attack'})

    def when_attack(self, minion_attack):
        if minion_attack.minion_type in ['pirate', 'all']:
            attack_buff = 4 if self.is_gold else 2
            health_buff = 2 if self.is_gold else 1
            for minion in self.minions_mine:
                minion.buff(attack_buff, health_buff, combat=True)


name2class_pirate = {'Deck Swabbie': DeckSwabbie,
                     'Scallywag': Scallywag,
                     'Sky Pirate': SkyPirate,
                     'Ripsnarl Captain': RipsnarlCaptain,
                     'Dread Admiral Eliza': DreadAdmiralEliza}
# 仅包括可购买的随从，不包括衍生物
tier2name_pirate = {1: ('Deck Swabbie', 'Scallywag'),
                    2: (),
                    3: (),
                    4: ('Ripsnarl Captain',),
                    5: (),
                    6: ('Dread Admiral Eliza',)}
