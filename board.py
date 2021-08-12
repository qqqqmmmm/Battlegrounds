"""
一个玩家的棋盘
"""
from collections import Counter
from minion.minion import generate_gold_minion
from spell import TripleReward


class Board:
    def __init__(self, minion_types, minion_pool):
        self.minion_types = minion_types  # 随从种类
        self.minion_pool = minion_pool  # 随从池
        self.turn = 0  # 回合数
        self.hero = 'none'
        self.hero_power = 'none'
        self.hero_power_used = False
        self.health = 40  # 血量
        self.tier = 1  # 酒馆等级
        self.wins = 0  # 连胜场数
        self.triple_cards = 0  # 三连个数
        self.triple_reward = []  # 三连奖励的随从
        self.hand = []  # 手牌
        self.hand_max = 10  # 最大手牌上限
        self.minions = []  # 己方场上的随从
        self.minions_opponent = []  # 上一个对手的随从
        self.minion_counter = Counter()  # 统计随从用于判断三连，不记录金色随从
        self.minion_info = (0, 'none')  # 其他玩家可见的随从信息
        self.tavern = []  # 酒馆中的随从
        self.tavern_is_frozen = False
        self.coin = 0  # 铸币数
        self.coin_max = 10  # 最大铸币数，用于贸易大王
        self.recruit_cost = 3  # 招募消耗
        self.refresh_cost = 1  # 刷新消耗
        self.refresh_free = 0  # 免费刷新次数
        self.tier2upgrade_cost = {1: 6, 2: 7, 3: 8, 4: 9, 5: 10, 6: 0}  # 升级酒馆所需铸币
        self.upgrade_cost = self.tier2upgrade_cost[1]  # 当前升级酒馆所需铸币
        self.tier2refresh_num = {1: 3, 2: 4, 3: 4, 4: 5, 5: 5, 6: 6}
        self.refresh_num = self.tier2refresh_num[self.tier]  # 刷新酒馆时出现的随从数
        self.status = 0  # 0：正常情况，1：选择三连奖励
        # 一些光环
        self.character2minion = dict()
        self.battlecry_num = 1  # 战吼触发次数

    def recruit_minion(self, idx):
        if idx < len(self.tavern) and self.coin >= self.recruit_cost and len(self.hand) < self.hand_max:  # 钱够且手牌未满
            self.coin -= self.recruit_cost
            minion = self.tavern.pop(idx)
            self.minion_enter_hand(minion)

    def minion_enter_hand(self, minion):
        self.hand.append(minion)
        minion.board_mine = self  # 将minion所属board指向自己
        if not minion.is_gold:
            self.minion_counter[minion.name] += 1
            self.check_triple()
    
    def minion_leave_hand(self, minion):
        self.hand.remove(minion)
        if not minion.is_gold:
            self.minion_counter[minion.name] -= 1

    def spell_enter_hand(self, spell):
        self.hand.append(spell)

    def sell_minion(self, idx):
        if idx < len(self.minions):
            minion = self.minions[idx]
            minion.sell()  # 触发出售随从时的效果
            self.minion_leave_ground(minion)
            self.minion_pool.back_to_pool(minion)

    def refresh(self, at_begin: bool):
        if at_begin:  # 回合开始自动刷新
            new_tavern = []
            refresh_num = self.refresh_num
            for minion in self.tavern:
                if minion.is_frozen:
                    refresh_num -= 1
                    minion.is_frozen = False
                    new_tavern.append(minion)
                else:
                    self.minion_pool.back_to_pool(minion)
            self.tavern = new_tavern
            if refresh_num > 0:
                for _ in range(refresh_num):
                    self.tavern.append(self.minion_pool.sample(self.tier))
        else:  # 手动刷新
            if self.refresh_free > 0 or self.coin >= self.refresh_cost:
                if self.refresh_free > 0:  # 免费刷新
                    self.refresh_free -= 1
                else:  # 花钱刷新
                    self.coin -= self.refresh_cost
                for minion in self.tavern:  # 将随从洗入随从池
                    self.minion_pool.back_to_pool(minion)
                self.tavern.clear()
                for _ in range(self.refresh_num):
                    self.tavern.append(self.minion_pool.sample(self.tier))

    def use_card(self, idx, *targets):  # 使用手牌
        if idx < len(self.hand):
            if self.hand[idx].type == 'spell':  # 法术
                pass
            else:  # 随从
                if len(self.minions) < 7:  # 未满场
                    if self.hand[idx].name[:5] == 'Gold ':  # 使用金色随从
                        self.spell_enter_hand(TripleReward(min(self.tier + 1, 6)))
                    minion = self.hand[idx]
                    self.minion_leave_hand(minion)
                    self.minion_enter_ground(minion)
                    if 'battlecry' in minion.characters:
                        for _ in range(self.battlecry_num):
                            minion.battlecry(targets)  # targets可为空，若targets目标不满足条件，则依次选择合适目标

    def minion_enter_ground(self, minion):
        self.minions.append(minion)
        if not minion.is_gold:
            self.minion_counter[minion.name] += 1
        # 此处需加入与熊妈等随从的相关互动
        for character in minion.characters:  # 更新
            self.character2minion[character] = self.character2minion.get(character, set()).union({minion})
    
    def minion_leave_ground(self, minion):
        self.minions.remove(minion)
        if not minion.is_gold:
            self.minion_counter[minion.name] -= 1
        for character in minion.characters:
            self.character2minion[character].remove(minion)

    def summon_minion(self, minion):
        minion.board_mine = self
        self.minion_enter_ground(minion)
        # 此处需加入与卡德加相关互动
        # 需修改三连判定，暂时找回整活的快乐
        self.check_triple()

    def freeze(self):
        self.tavern_is_frozen = not self.tavern_is_frozen
        for minion in self.tavern:
            minion.is_frozen = self.tavern_is_frozen

    def upgrade_tier(self):
        if self.tier < 6:
            if self.coin >= self.upgrade_cost:
                self.coin -= self.upgrade_cost
                self.tier += 1
                self.upgrade_cost = self.tier2upgrade_cost[self.tier]
                self.refresh_num = max(self.tier2refresh_num[self.tier], self.refresh_num)
                # 此处需加入升级酒馆时的判定

    def update_minion_info(self):  # 更新其他人可见的随从种族信息
        minion_types = [minion.minion_type for minion in self.minions]
        count = Counter(minion_types)
        del count['none']
        if len(count) == 0:
            self.minion_info = (0, 'none')
        else:
            num_all = count.get('all', 0)
            del count['all']
            if len(count) == 0:
                self.minion_info = (0, 'mixture')
            else:
                count = count.most_common()
                if len(count) == 1:
                    self.minion_info = (count[0][1] + num_all, count[0][0])
                elif count[0][1] > count[1][1]:
                    self.minion_info = (count[0][1] + num_all, count[0][0])
                else:
                    self.minion_info = (0, 'mixture')

    def show_info(self):
        return self.hero, self.hero_power, self.health, self.tier, self.wins, self.triple_cards, self.minion_info

    def check_triple(self):  # 检查是否三连
        triple_list = []
        count = self.minion_counter.most_common()
        for i in range(len(count)):
            if count[i][1] >= 3:
                triple_list.append(count[i][0])
            else:
                break
        for name in triple_list:
            self.triple(name)

    def triple(self, name):  # 三连
        self.triple_cards += 1
        source_minions = []
        source_hand = []
        for minion in self.minions:
            if minion.name == name:
                source_minions.append(minion)
                if len(source_minions) == 3:
                    break
        for minion in source_minions:
            self.minion_leave_ground(minion)
        else:
            for minion in self.hand:
                if minion.name == name:
                    source_hand.append(minion)
                    if len(source_minions + source_hand) == 3:
                        break
        for minion in source_hand:
            self.minion_leave_hand(minion)
        gold_minion = generate_gold_minion(self.minion_pool.name2class[name], source_minions + source_hand)
        self.minion_enter_hand(gold_minion)

    def new_turn(self, turn):
        self.turn += 1
        self.update_minion_info()  # 更新其他人可见的随从种族信息
        self.refresh(True)  # 回合开始刷新
        self.tavern_is_frozen = False  # 取消冻结
        self.upgrade_cost = max(self.upgrade_cost - 1, 0)
        self.coin = min(turn + 2, 10)  # 重置铸币

    def print_board(self):
        print(f'英雄：{self.hero}', end=' ')
        print(f'英雄技能：{self.hero_power}')
        print(f'本局对战中的随从种类：', *self.minion_types)
        print(f'酒馆等级：{self.tier}', end=' ')
        print(f'升级酒馆所需铸币：{self.upgrade_cost}')
        print(f'血量：{self.health}', end=' ')
        print(f'铸币：{self.coin}')
        print('酒馆中的随从：')
        for idx, minion in enumerate(self.tavern):
            print(idx, end=' ')
            if minion.is_frozen:
                print('frozen', end=' ')
            print(minion.name, minion.tier, minion.attack, minion.health, *minion.characters)
        print('场上的随从：')
        for idx, minion in enumerate(self.minions):
            print(idx, end=' ')
            print(minion.name, minion.tier, minion.attack, minion.health, *minion.characters)
        print('手牌：')
        for idx, card in enumerate(self.hand):
            print(idx, end=' ')
            if card.type == 'minion':
                print(card.name, card.tier, card.attack, card.health, *card.characters)
            elif card.type == 'spell':
                if card.name == 'Triple Reward':
                    print(f'tier {card.tier}', end=' ')
                print(card.name)
        if self.status == 1:
            print('选择三连奖励：')
            for idx, minion in enumerate(self.triple_reward):
                print(minion.name, minion.tier, minion.attack, minion.health)
        print('-' * 30)
