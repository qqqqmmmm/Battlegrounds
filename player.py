"""
玩家class
"""


class Player:
    def __init__(self, idx):
        self.idx = idx
        self.control = 'ai'

    def choose_hero(self, minion_types, heroes):
        if self.control == 'ai':
            return heroes[0]
        else:
            print(f'本局出现随从的种族为：{minion_types}')
            print('可供选择的英雄：')
            for idx, hero in enumerate(heroes):
                print(idx, hero)
            return heroes[int(input('请选择你的英雄：(输入序号)'))]

    def get_action(self):
        if self.control == 'ai':
            return 'end'
        else:
            return input('请输入你的操作：').split()
