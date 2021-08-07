"""
法术
"""


class GoldCoin:
    def __init__(self):
        self.name = 'Gold Coin'
        self.type = 'spell'


class TripleReward:
    def __init__(self, tier):
        self.name = 'Triple Reward'
        self.type = 'spell'
        self.tier = tier  # 发现此等级的随从
