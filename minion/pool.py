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
from minion.quilboar import *
from minion.general import *

import random


class MinionPool:
    def __init__(self, races):
        self.tier2name = dict()  # 从星级到名字
        self.tier2name_minion_type = dict()  # 从星级到名字，按种族分类
        self.name2number = dict()  # 从名字到剩余随从数量
        self.tier2number = {1: 16, 2: 15, 3: 13, 4: 11, 5: 9, 6: 7}
        self.name2class = dict()
        for tier in range(1, 7):
            self.tier2name[tier] = []
            for name in tier2name_general[tier]:  # 中立随从
                self.tier2name[tier].append(name)
                self.name2number[name] = self.tier2number[tier]
            self.name2class.update(name2class_general)
            if 'beast' in races:
                for name in tier2name_beast[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_beast)
            if 'demon' in races:
                for name in tier2name_demon[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_demon)
            if 'dragon' in races:
                for name in tier2name_dragon[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_dragon)
            if 'elemental' in races:
                for name in tier2name_elemental[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_elemental)
            if 'mech' in races:
                for name in tier2name_mech[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_mech)
            if 'murloc' in races:
                for name in tier2name_murloc[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_murloc)
            if 'pirate' in races:
                for name in tier2name_pirate[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_pirate)
            if 'quilboar' in races:
                for name in tier2name_quilboar[tier]:
                    self.tier2name[tier].append(name)
                    self.name2number[name] = self.tier2number[tier]
                self.name2class.update(name2class_quilboar)

    def sample(self, tier: int):  # 从随从池中获得随从
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

    def sample_tier(self, tier: int):  # 获取特定星级的随从
        minions = self.tier2name[tier]
        nums = []
        for name in minions:
            nums.append(self.name2number[name])
        name = random.choices(minions, nums, k=1)[0]
        self.name2number[name] -= 1
        minion = self.name2class[name]('pool')
        return minion

    def sample_minion_type(self, tier: int, minion_type: str):  # 获取特定种类的随从
        minions = []
        for i in range(1, tier + 1):
            minions.extend(self.tier2name_minion_type[minion_type][i])
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
            # 衍生物直接丢掉
        elif isinstance(minion.source, list):
            for minion in minion.source:
                self.back_to_pool(minion)


if __name__ == '__main__':
    pool = MinionPool(['murloc'])
