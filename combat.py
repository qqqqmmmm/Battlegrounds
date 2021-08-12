"""
负责处理两个玩家的战斗
"""


import random


class CombatCenter:
    def __init__(self, minion_types):
        self.minion_types = minion_types
        self.boards = []
        self.minions = []
        self.character2minion = []
        self.turn = 0  # 回合数，任意一方攻击一次+1，无论主动被动
        self.turn_max = 1000  # turn达到turn_max后视为平局，避免无限
        self.role = 0  # 0/1，轮到谁攻击
        self.attack_list = []

    def combat(self, board0, board1):
        self.before_combat(board0, board1)
        while True:
            is_end, winner, damage = self.is_end()
            if is_end:
                return winner, damage
            minion_attack = self.attack_list[self.role].pop(0)
            if 'choose attack target' in minion_attack.characters:
                minion_attacked = minion_attack.choose_attack_target()
            else:
                minion_attacked = self.get_minion_attacked()
            for minion in self.character2minion[self.role].get('when attack', []):  # 触发所有随从攻击前的效果
                minion.when_attack(minion_attack)
            for minion in self.character2minion[self.role].get('when attacked', []):  # 触发所有随从被攻击前的效果
                minion.when_attacked(minion_attacked)
            # 此处下一步编写造成伤害

    def before_combat(self, board0, board1):  # 战斗阶段开始前
        self.boards.clear()
        self.boards.extend([board0, board1])
        self.minions.clear()
        self.minions.extend([board0.minions.copy(), board1.minions.copy()])
        self.character2minion.clear()
        self.character2minion.extend([board0.character2minion.copy(), board1.character2minion.copy()])
        self.start_of_combat()  # 触发战斗阶段开始时的效果
        self.attack_list.clear()
        self.attack_list.extend([self.minions[0].copy(), self.minions[1].copy()])
        for idx in range(2):
            for minion in self.minions[idx]:
                minion.minions_mine = self.minions[idx]
                minion.minions_opponent = self.boards[1 - idx]

    def start_of_combat(self):  # 战斗阶段开始时
        for idx in range(2):
            if self.boards[idx].hero_power == 'Embrace Your Rage':
                if self.boards[idx].hero_power_used:
                    minion = self.boards[idx].minion_pool.sample_tier(self.boards[idx].tier)
                    self.boards[idx].minion_enter_hand(minion)
                    self.minions[idx].append(minion)
            # elif self.boards[idx].hero_power == 'Wingmen':
            #     self.role = 1 - idx

    # def minions_enter_ground(self, minions):


    def get_minion_attacked(self):
        minions_taunt = self.character2minion[1 - self.role].get('taunt', [])
        if minions_taunt:
            return random.choice(minions_taunt)
        return random.choice(self.minions[1 - self.role])

    def is_end(self):
        if self.turn > self.turn_max:
            return True, 2, 0  # 2代表平局，0填充位置
        elif len(self.minions[0]) == 0:
            if len(self.minions[1]) == 0:
                return True, 2, 0
            else:  # 1胜利
                damage = self.boards[1].tier
                for minion in self.minions[1]:
                    damage += minion.tier
                return True, 1, damage
        elif len(self.minions[1]) == 0:  # 0胜利
            damage = self.boards[0].tier
            for minion in self.minions[0]:
                damage += minion.tier
            return True, 0, damage
        else:
            return False, 2, 0  # 2填充位置，0填充位置
