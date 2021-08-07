"""
元素
"""
from minion.minion import Minion


class RefreshingAnomaly(Minion):
    def __init__(self, source):
        super(RefreshingAnomaly, self).__init__('Refreshing Anomaly', 'elemental', 1, 1, 3, source,
                                                {'battlecry'})

    def battlecry(self, targets):
        if self.is_gold:
            self.board_mine.refresh_free = max(2, self.board_mine.refresh_free)
        else:
            self.board_mine.refresh_free = max(1, self.board_mine.refresh_free)


class Sellemental(Minion):
    def __init__(self, source):
        super(Sellemental, self).__init__('Sellemental', 'elemental', 1, 2, 2, source)

    def sell(self):
        self.board_mine.coin = min(self.board_mine.coin_max, self.board_mine.coin + 1)  # 重写sell函数需要补上这一行
        if self.is_gold:
            for _ in range(min(2, 10 - len(self.board_mine.hand))):
                self.board_mine.minion_enter_hand(WaterDroplet(''))
        else:
            for _ in range(min(1, 10 - len(self.board_mine.hand))):
                self.board_mine.minion_enter_hand(WaterDroplet(''))


class WaterDroplet(Minion):
    # 衍生物
    def __init__(self, source):
        super(WaterDroplet, self).__init__('Water Droplet', 'elemental', 1, 2, 2, source)


name2class_elemental = {'Refreshing Anomaly': RefreshingAnomaly,
                        'Sellemental': Sellemental,
                        'Water Droplet': WaterDroplet}
# 仅包括可购买的随从，不包括衍生物
tier2name_elemental = {1: ('Refreshing Anomaly', 'Sellemental'),
                       2: (),
                       3: (),
                       4: (),
                       5: (),
                       6: ()}
