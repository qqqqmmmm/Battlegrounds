"""
野猪人
"""
from minion.minion import Minion, generate_gold_minion
from spell import BloodGem


class RazorfenGeomancer(Minion):
    def __init__(self, source):
        super(RazorfenGeomancer, self).__init__('Razorfen Geomancer', 'quilboar', 1, 3, 1, source,
                                                {'battlecry'})

    def battlecry(self, targets):
        if len(self.board_mine.hand) < 10:
            if self.is_gold:
                for _ in range(min(2, 10 - len(self.board_mine.hand))):
                    self.board_mine.spell_enter_hand(BloodGem())
            else:
                for _ in range(min(1, 10 - len(self.board_mine.hand))):
                    self.board_mine.spell_enter_hand(BloodGem())


class SunBaconRelaxer(Minion):
    def __init__(self, source):
        super(SunBaconRelaxer, self).__init__('Sun-Bacon Relaxer', 'quilboar', 1, 1, 2, source)

    def sell(self):
        self.board_mine.coin = min(self.board_mine.coin_max, self.board_mine.coin + 1)
        if len(self.board_mine.hand) < 10:
            if self.is_gold:
                for _ in range(min(4, 10 - len(self.board_mine.hand))):
                    self.board_mine.spell_enter_hand(BloodGem())
            else:
                for _ in range(min(2, 10 - len(self.board_mine.hand))):
                    self.board_mine.spell_enter_hand(BloodGem())


name2class_quilboar = {'Razorfen Geomancer': RazorfenGeomancer,
                       'Sun-Bacon Relaxer': SunBaconRelaxer}
# 仅包括可购买的随从，不包括衍生物
tier2name_quilboar = {1: ('Razorfen Geomancer', 'Sun-Bacon Relaxer'),
                      2: (),
                      3: (),
                      4: (),
                      5: (),
                      6: ()}
