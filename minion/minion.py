"""
随从class
"""


class Minion:
    def __init__(self, name: str, minion_type: str, tier: int, attack: int, health: int,
                 source, characters=tuple()):
        self.name = name
        self.minion_type = minion_type
        self.type = 'minion'
        self.tier = tier
        self.is_gold = False
        # 攻击力
        self.attack_initial = attack  # 初始攻击力
        self.attack_buff = 0  # 招募阶段增加的攻击力
        self.attack = attack  # 总攻击力
        # 血量
        self.health_initial = health  # 初始血量
        self.health_buff = 0  # 招募阶段增加的血量
        self.health = health  # 总生命值
        # 战吼、亡语、圣盾、风怒等character
        self.characters_initial = set(characters)
        self.characters_buff = set()
        self.characters = set(characters)
        self.magnetic_list = []  # 记录贴在随从上的磁力随从

        self.source = source  # 来源
        self.is_frozen = False

        self.board_mine = None  # 自己的board，用于实现战吼
        # 以下两个用于战斗阶段
        self.minions_mine = None  # 自己的minions
        self.minions_opponent = None  # 对手的minions

    def buff(self, attack_buff: int, health_buff: int, characters=tuple(), combat=False, permanent=False):
        if combat:
            self.attack += attack_buff
            self.health += health_buff
            self.characters = self.characters.union(characters)
            if permanent:
                self.attack_buff += attack_buff
                self.health_buff += health_buff
                self.characters_buff = self.characters_buff(characters)
        else:
            self.attack_buff += attack_buff
            self.health_buff += health_buff
            self.characters_buff = self.characters_buff.union(characters)
            self.update_info()

    def update_info(self):
        self.attack = self.attack_initial + self.attack_buff
        self.health = self.health_initial + self.health_buff
        self.characters = self.characters_initial.union(self.characters_buff)

    def sell(self):
        self.board_mine.coin = min(self.board_mine.coin_max, self.board_mine.coin + 1)


def generate_gold_minion(minion_class, sources):
    gold_minion = minion_class(sources)
    gold_minion.name = 'Gold ' + gold_minion.name
    gold_minion.is_gold = True
    gold_minion.attack_initial *= 2
    gold_minion.health_initial *= 2
    for minion in sources:
        gold_minion.attack_buff += minion.attack_buff
        gold_minion.health_buff += minion.health_buff
        gold_minion.characters_buff = gold_minion.characters_buff.union(minion.characters_buff)
        gold_minion.magnetic_list.extend(minion.magnetic_list)
    # 金色随从身材不小于基础身材
    gold_minion.attack_buff = max(0, gold_minion.attack_buff)
    gold_minion.health_buff = max(0, gold_minion.health_buff)
    gold_minion.update_info()
    return gold_minion
