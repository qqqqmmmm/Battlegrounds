"""
随从class
"""


class Minion:
    def __init__(self, name, minion_type, tier, is_gold, attack, attack_buff, health, health_buff,
                 is_battlecry, is_deathrattle, divine_shield_initial, divine_shield_buff,
                 windfury_initial, windfury_buff, taunt_initial, taunt_buff,
                 poisonous_initial, poisonous_buff, reborn_initial, reborn_buff,
                 magnetic_initial, magnetic_list, source):
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


class MinionWhite(Minion):
    def __init__(self, name: str, minion_type: str, tier: int, attack: int, health: int,
                 source, characters: dict):
        super(MinionWhite, self).__init__(name=name, minion_type=minion_type, tier=tier, is_gold=False,
                                          attack=attack, attack_buff=0, health=health, health_buff=0,
                                          is_battlecry=characters.get('battlecry', False),
                                          is_deathrattle=characters.get('deathrattle', False),
                                          divine_shield_initial=characters.get('divine_shield', False),
                                          divine_shield_buff=False,
                                          windfury_initial=characters.get('windfury', False),
                                          windfury_buff=False,
                                          taunt_initial=characters.get('taunt', False),
                                          taunt_buff=False,
                                          poisonous_initial=characters.get('poisonous', False),
                                          poisonous_buff=False,
                                          reborn_initial=characters.get('reborn', False),
                                          reborn_buff=False,
                                          magnetic_initial=characters.get('magnetic', False),
                                          magnetic_list=[],
                                          source=source)


class MinionGold(Minion):
    def __init__(self, sources: list):
        super(MinionGold, self).__init__(name='Gold '+sources[0].name, minion_type=sources[0].minion_type,
                                         tier=sources[0].tier, is_gold=True,
                                         attack=sources[0].attack_initial * 2,
                                         attack_buff=max(0, sources[0].attack_buff +
                                                         sources[1].attack_buff + sources[2].attack_buff),
                                         health=sources[0].health_initial * 2,
                                         health_buff=max(0, sources[0].health_buff +
                                                         sources[1].health_buff + sources[2].health_buff),
                                         is_battlecry=sources[0].is_battlecry,
                                         is_deathrattle=sources[0].is_deathrattle and sources[1].is_deathrattle and sources[2].is_deathrattle,
                                         divine_shield_initial=sources[0].divine_shield_initial,
                                         divine_shield_buff=sources[0].divine_shield_buff & sources[1].divine_shield_buff & sources[2].divine_shield_buff,
                                         windfury_initial=sources[0].windfury_initial,
                                         windfury_buff=sources[0].windfury_buff & sources[1].windfury_buff & sources[2].windfury_buff,
                                         taunt_initial=sources[0].taunt_initial,
                                         taunt_buff=sources[0].taunt_buff & sources[1].taunt_buff & sources[2].taunt_buff,
                                         poisonous_initial=sources[0].poisonous_initial,
                                         poisonous_buff=sources[0].poisonous_buff & sources[1].poisonous_buff & sources[2].poisonous_buff,
                                         reborn_initial=sources[0].reborn_initial,
                                         reborn_buff=sources[0].reborn_buff & sources[1].reborn_buff & sources[2].reborn_buff,
                                         magnetic_initial=sources[0].magnetic_initial,
                                         magnetic_list=sources[0].magnetic_list + sources[1].magnetic_list + sources[2].magnetic_list,
                                         source=sources)
