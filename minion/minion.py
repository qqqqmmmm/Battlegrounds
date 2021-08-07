"""
随从class
"""


class Minion:
    def __init__(self, name, minion_type, tier, is_gold, attack, attack_buff, health, health_buff,
                 is_battlecry, is_deathrattle, divine_shield_initial, divine_shield_buff,
                 windfury_initial, windfury_buff, taunt_initial, taunt_buff,
                 poisonous_initial, poisonous_buff, reborn_initial, reborn_buff,
                 frenzy_initial, magnetic_initial, magnetic_list, source):
        self.name = name
        self.minion_type = minion_type
        self.type = 'minion'
        self.tier = tier
        self.is_gold = is_gold
        # 攻击力
        self.attack_initial = attack  # 初始攻击力
        self.attack_buff = attack_buff  # 招募阶段增加的攻击力
        # 血量
        self.health_initial = health  # 初始血量
        self.health_buff = health_buff  # 招募阶段增加的血量
        # 战吼
        self.is_battlecry = is_battlecry
        # 亡语
        self.is_deathrattle = is_deathrattle
        # 圣盾
        self.divine_shield_initial = divine_shield_initial
        self.divine_shield_buff = divine_shield_buff
        # 风怒
        self.windfury_initial = windfury_initial
        self.windfury_buff = windfury_buff
        # 嘲讽
        self.taunt_initial = taunt_initial
        self.taunt_buff = taunt_buff
        # 剧毒
        self.poisonous_initial = poisonous_initial
        self.poisonous_buff = poisonous_buff
        # 复生
        self.reborn_initial = reborn_initial
        self.reborn_buff = reborn_buff
        # 暴怒
        self.frenzy_initial = frenzy_initial
        # 磁力
        self.magnetic_initial = magnetic_initial
        self.magnetic_list = magnetic_list  # 记录贴在随从上的磁力随从

        self.source = source  # 来源
        self.is_frozen = False

        self.info = {'attack': self.attack_initial,
                     'health': self.health_initial,
                     'divine_shield': self.divine_shield_buff,
                     'windfury': self.windfury_initial,
                     'taunt': self.taunt_initial,
                     'poisonous': self.poisonous_initial,
                     'reborn': self.reborn_initial}
        # 以下两个用于实现战吼亡语等功能
        self.board_mine = None  # 自己的board
        self.board_opponent = None  # 对手的board

    def update_info(self):
        self.info['attack'] = self.attack_initial + self.attack_buff
        self.info['health'] = self.health_initial + self.health_buff
        self.info['divine_shield'] = self.divine_shield_initial and self.divine_shield_buff
        self.info['windfury'] = self.windfury_initial and self.windfury_buff
        self.info['taunt'] = self.taunt_initial and self.taunt_buff
        self.info['poisonous'] = self.poisonous_initial and self.poisonous_buff
        self.info['reborn'] = self.reborn_initial and self.reborn_buff

    def sell(self):
        self.board_mine.coin = min(self.board_mine.coin_max, self.board_mine.coin + 1)


class MinionWhite(Minion):
    def __init__(self, name: str, minion_type: str, tier: int, attack: int, health: int,
                 source, characters: set):
        super(MinionWhite, self).__init__(name=name, minion_type=minion_type, tier=tier, is_gold=False,
                                          attack=attack, attack_buff=0, health=health, health_buff=0,
                                          is_battlecry='battlecry' in characters,
                                          is_deathrattle='deathrattle' in characters,
                                          divine_shield_initial='divine_shield' in characters,
                                          divine_shield_buff=False,
                                          windfury_initial='windfury' in characters,
                                          windfury_buff=False,
                                          taunt_initial='taunt' in characters,
                                          taunt_buff=False,
                                          poisonous_initial='poisonous' in characters,
                                          poisonous_buff=False,
                                          reborn_initial='reborn' in characters,
                                          reborn_buff=False,
                                          frenzy_initial='frenzy' in characters,
                                          magnetic_initial='magnetic' in characters,
                                          magnetic_list=[],
                                          source=source)


def generate_gold_minion(minion_class, sources):
    gold_minion = minion_class(sources)
    gold_minion.name = 'Gold ' + gold_minion.name
    gold_minion.is_gold = True
    gold_minion.attack_initial *= 2
    gold_minion.health_initial *= 2
    for minion in sources:
        gold_minion.attack_buff += minion.attack_buff
        gold_minion.health_buff += minion.health_buff
        gold_minion.is_deathrattle |= minion.is_deathrattle
        gold_minion.divine_shield_buff |= minion.divine_shield_buff
        gold_minion.windfury_buff |= minion.windfury_buff
        gold_minion.taunt_buff |= minion.taunt_buff
        gold_minion.poisonous_buff |= minion.taunt_buff
        gold_minion.reborn_buff |= minion.reborn_buff
        gold_minion.magnetic_list.extend(minion.magnetic_list)
    # 金色随从身材不小于基础身材
    gold_minion.attack_buff = max(0, gold_minion.attack_buff)
    gold_minion.health_buff = max(0, gold_minion.health_buff)
    return gold_minion
