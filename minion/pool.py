"""
牌库
"""
from minion.beast import *
from minion.demon import *
from minion.dragon import *
from minion.elemental import *
from minion.mech import *
from minion.murloc import *
from minion.pirate import *
from minion.general import *

import random


class MinionPool:
    def __init__(self, races):
        self.tier2name = dict()  # 从星级到名字
        self.name2number = dict()  # 从名字到剩余随从数量
        self.tier2number = {1: 16, 2: 15, 3: 13, 4: 11, 5: 9, 6: 7}
        self.name2class = dict()
        for tier in range(1, 7):
            self.tier2name[tier] = []
            for name in tier2names_general[tier]:
                self.tier2name[tier].append(name)
                self.name2number[name] = self.tier2number[tier]
            self.name2class.update(name2class_general)
            if 'beast' in races:
                for name in tier2names_beast[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_beast)
            if 'demon' in races:
                for name in tier2names_demon[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_demon)
            if 'dragon' in races:
                for name in tier2names_dragon[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_dragon)
            if 'elemental' in races:
                for name in tier2names_elemental[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_elemental)
            if 'mech' in races:
                for name in tier2names_mech[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_mech)
            if 'murloc' in races:
                for name in tier2names_murloc[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_murloc)
            if 'pirate' in races:
                for name in tier2names_pirate[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_pirate)

    def sample_from_pool(self, tier: int):  # 从随从池中获得随从
        minions = []
        for i in range(1, tier + 1):
            minions.extend(self.tier2name[i])
        nums = []
        for name in minions:
            nums.append(self.name2number[name])
        name = random.choices(minions, nums, k=1)[0]
        self.name2number[name] -= 1
        minion = self.name2class[name]('pool')
        return minion

    def back_to_pool(self, minion):  # 将随从放回随从池
        if isinstance(minion.source, str):
            if minion.source == 'pool':
                self.name2number[minion.name] += 1
        elif isinstance(minion.source, list):
            for minion in minion.source:
                self.back_to_pool(minion)


if __name__ == '__main__':
    pool = MinionPool(['murloc'])
