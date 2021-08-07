"""
机械
"""
from minion.minion import Minion


class MicroMachine(Minion):
    def __init__(self, source):
        super(MicroMachine, self).__init__('Micro Machine', 'mech', 1, 1, 2, source)


class MicroMummy(Minion):
    def __init__(self, source):
        super(MicroMummy, self).__init__('Micro Mummy', 'mech', 1, 1, 2, source,
                                         {'reborn'})


name2class_mech = {'Micro Machine': MicroMachine,
                   'Micro Mummy': MicroMummy}
# 仅包括可购买的随从，不包括衍生物
tier2name_mech = {1: ('Micro Machine', 'Micro Mummy'),
                  2: (),
                  3: (),
                  4: (),
                  5: (),
                  6: ()}
