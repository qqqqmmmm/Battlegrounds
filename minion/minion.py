"""
随从class
"""


class Minion:
    def __init__(self, name: str, minion_type: str, tier: int, attack: int, health: int,
                 source: str, characters: dict):
        self.name = name
        self.minion_type = minion_type
        self.type = 'minion'
        self.tier = tier
        # 攻击力
        self.attack_initial = attack  # 初始攻击力
        self.attack_buff = 0  # 招募阶段增加的攻击力
        # 血量
        self.health_initial = health  # 初始血量
        self.health_buff = 0  # 招募阶段增加的血量
        # 战吼
        self.battlecry = characters.get('battlecry', False)
        # 亡语
        self.deathrattle = characters.get('deathrattle', False)
        self.deathrattle_list = [self.name]
        # 圣盾
        self.divine_shield_initial = characters.get('divine_shield', False)
        self.divine_shield_buff = False
        # 风怒
        self.windfury_initial = characters.get('windfury', False)
        self.windfury_buff = False
        # 嘲讽
        self.taunt_initial = characters.get('taunt', False)
        self.taunt_buff = False
        # 剧毒
        self.poisonous_initial = characters.get('poisonous', False)
        self.poisonous_buff = False
        # 复生
        self.reborn_initial = characters.get('reborn', False)
        self.reborn_buff = False
        # 磁力
        self.magnetic_initial = characters.get('magnetic', False)
        self.magnetic_list = []  # 记录贴在随从上的磁力随从

        self.source = source  # 来源
        self.is_frozen = False

        self.info = {'attack': self.attack_initial, 'health': self.health_initial,
                     'divine_shield': self.divine_shield_buff,
                     'windfury': self.windfury_initial,
                     'taunt': self.taunt_initial,
                     'poisonous': self.poisonous_initial,
                     'reborn': self.reborn_initial}

    def update_info(self):
        self.info['attack'] = self.attack_initial + self.attack_buff
        self.info['health'] = self.health_initial + self.health_buff
        self.info['divine_shield'] = self.divine_shield_initial and self.divine_shield_buff
        self.info['windfury'] = self.windfury_initial and self.windfury_buff
        self.info['taunt'] = self.taunt_initial and self.taunt_buff
        self.info['poisonous'] = self.poisonous_initial and self.poisonous_buff
        self.info['reborn'] = self.reborn_initial and self.reborn_buff


class MinionGold:
    def __init__(self, source: list):
        self.source = source
        self.name = 'Gold ' + source[0].name
        self.minion_type = source[0].minion_type
        self.type = 'minion'
        self.tier = source[0].tier
        # 战吼
        self.battlecry = source[0].battlecry
        # 亡语
        self.deathrattle = source[0].deathrattle & source[1].deathrattle & source[2].deathrattle
        self.deathrattle_list = source[0].deathrattle_list + source[1].deathrattle_list + source[2].deathrattle_list
        # 攻击力
        self.attack_initial = source[0].attack_initial * 2
        self.attack_buff = source[0].attack_buff + source[1].attack_buff + source[2].attack_buff
        # 血量
        self.health_initial = source[0].health_initial * 2
        self.health_buff = source[0].health_buff + source[1].health_buff + source[2].health_buff
        # 圣盾
        self.divine_shield_initial = source[0].divine_shield_initial
        self.divine_shield_buff = source[0].divine_shield_buff & source[1].divine_shield_buff & source[2].divine_shield_buff
        # 风怒
        self.windfury_initial = source[0].windfury_initial
        self.windfury_buff = source[0].windfury_buff & source[1].windfury_buff & source[2].windfury_buff
        # 嘲讽
        self.taunt_initial = source[0].taunt_initial
        self.taunt_buff = source[0].taunt_buff & source[1].taunt_buff & source[2].taunt_buff
        # 剧毒
        self.poisonous_initial = source[0].poisonous_initial
        self.poisonous_buff = source[0].poisonous_buff & source[1].poisonous_buff & source[2].poisonous_buff
        # 复生
        self.reborn_initial = source[0].reborn_initial
        self.reborn_buff = source[0].reborn_buff & source[1].reborn_buff & source[2].reborn_buff
        # 磁力
        self.magnetic_initial = source[0].magnetic_initial
        self.magnetic_list = source[0].magnetic_list + source[1].magnetic_list + source[2].magnetic_list

        self.info = {'attack': self.attack_initial + self.attack_buff,
                     'health': self.health_initial + self.health_buff,
                     'divine_shield': self.divine_shield_buff and self.divine_shield_buff,
                     'windfury': self.windfury_initial and self.windfury_buff,
                     'taunt': self.taunt_initial and self.taunt_buff,
                     'poisonous': self.poisonous_initial and self.poisonous_buff,
                     'reborn': self.reborn_initial and self.reborn_buff}

    def update_info(self):
        self.info['attack'] = self.attack_initial + self.attack_buff
        self.info['health'] = self.health_initial + self.health_buff
        self.info['divine_shield'] = self.divine_shield_initial and self.divine_shield_buff
        self.info['windfury'] = self.windfury_initial and self.windfury_buff
        self.info['taunt'] = self.taunt_initial and self.taunt_buff
        self.info['poisonous'] = self.poisonous_initial and self.poisonous_buff
        self.info['reborn'] = self.reborn_initial and self.reborn_buff
