"""
中立
"""
from minion.minion import Minion


class AcolyteOfCThun(Minion):
    def __init__(self, source):
        super(AcolyteOfCThun, self).__init__('Acolyte Of CThun', 'none', 1, 2, 2, source,
                                             {'taunt': True, 'reborn': True})


name2class_neutral = {'Acolyte Of CThun': AcolyteOfCThun}
tier2names_neutral = {1: ('Acolyte Of CThun',),
                      2: (),
                      3: (),
                      4: (),
                      5: (),
                      6: ()}
