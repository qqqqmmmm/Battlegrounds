"""
元素
"""
from minion.minion import MinionWhite


class RefreshingAnomaly(MinionWhite):
    def __init__(self, source):
        super(RefreshingAnomaly, self).__init__('Refreshing Anomaly', 'elemental', 1, 1, 3, source,
                                                {'battlecry'})

    def battlecry(self, targets):
        self.board_mine.refresh_free = 1


class Sellemental(MinionWhite):
    def __init__(self, source):
        super(Sellemental, self).__init__('Sellemental', 'elemental', 1, 2, 2, source,
                                          set())


# 此处缺22衍生物


name2class_elemental = {'Refreshing Anomaly': RefreshingAnomaly,
                        'Sellemental': Sellemental}
# 仅包括可购买的随从，不包括衍生物
tier2name_elemental = {1: ('Refreshing Anomaly', 'Sellemental'),
                       2: (),
                       3: (),
                       4: (),
                       5: (),
                       6: ()}
