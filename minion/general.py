"""
中立
"""
from minion.minion import MinionWhite


class AcolyteOfCThun(MinionWhite):
    def __init__(self, source):
        super(AcolyteOfCThun, self).__init__('Acolyte Of CThun', 'general', 1, 2, 2, source,
                                             {'taunt', 'reborn'})


name2class_general = {'Acolyte Of CThun': AcolyteOfCThun}
tier2name_general = {1: ('Acolyte Of CThun',),
                     2: (),
                     3: (),
                     4: (),
                     5: (),
                     6: ()}
