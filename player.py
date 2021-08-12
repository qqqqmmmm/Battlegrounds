"""
玩家class
"""


class Player:
    def __init__(self, idx, board):
        self.idx = idx
        self.board = board
        self.policy = 'default'
        # 以下为default policy
        self.policy_default = {1: iter(['buy 0', 'use 0', 'end']),
                               2: iter(['upgrade', 'end']),
                               3: iter(['sell 0', 'buy 0', 'buy 0', 'use 0', 'use 0', 'end'])}

    def choose_hero(self, minion_types, heroes):
        if self.policy == 'default':
            return heroes[0]
        else:
            print(f'本局出现随从的种族为：{minion_types}')
            print('可供选择的英雄：')
            for idx, hero in enumerate(heroes):
                print(idx, hero)
            return heroes[int(input('请选择你的英雄：(输入序号)'))]

    def get_action(self):
        if self.policy == 'default':
            return next(self.policy_default[self.board.turn]).split()
        else:
            return input('请输入你的操作：').split()
