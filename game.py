"""
负责酒馆战旗整体游戏进程控制
"""
from minion.pool import MinionPool
from player import Player
from board import Board
from combat import CombatCenter
import random
import sys


class Game:
    def __init__(self, num_player, include_human=False):
        self.num_player = num_player
        self.turn = 0
        self.turn2time = lambda x: min(45 + self.turn * 15, 180)  # 每回合时长
        self.time = 0  # 剩余时长
        self.minion_types = random.sample(['beast', 'demon', 'dragon', 'elemental',
                                           'mech', 'murloc', 'pirate', 'quilboar'], 5)  # 随机挑选种族
        # 初始化英雄池
        self.minion_pool = MinionPool(self.minion_types)  # 初始化随从池
        # 初始化棋盘和玩家
        self.boards = []
        self.players = []
        for idx_player in range(self.num_player):
            self.boards.append(Board(self.minion_types, self.minion_pool))
            self.players.append(Player(idx_player, self.boards[idx_player]))
        if include_human:
            self.players[0].policy = 'human'

    # def get_hero(self, player, minion_types, heroes):
    #     hero = player.choose_hero(minion_types, heroes)
    #     return hero

    def get_observation(self, idx_player):
        pass

    def new_turn(self):
        self.turn += 1
        self.time = self.turn2time(self.turn)
        for idx_player in range(self.num_player):
            self.boards[idx_player].new_turn(self.turn)

    def do_action(self, idx_player, action):
        if action[0] == 'refresh':
            self.boards[idx_player].refresh(False)
        elif action[0] == 'buy' or action[0] == 'recruit':
            self.boards[idx_player].recruit_minion(int(action[1]))
        elif action[0] == 'sell':
            self.boards[idx_player].sell_minion(int(action[1]))
        elif action[0] == 'use':
            self.boards[idx_player].use_card(*list(map(int, action[1:])))
        elif action[0] == 'upgrade':
            self.boards[idx_player].upgrade_tier()
        elif action[0] == 'freeze':
            self.boards[idx_player].freeze()

    def start(self):
        while True:
            self.new_turn()
            action_list = list(range(self.num_player))  # 本回合未结束操作的玩家
            for idx_player in action_list:
                if self.boards[idx_player].health <= 0:  # 判定死亡
                    action_list.remove(idx_player)
            while self.time > 0:
                self.time -= 1
                for idx_player in action_list:
                    if self.players[idx_player].policy == 'human':  # 人类操作输出棋盘
                        self.boards[idx_player].print_board()
                    action = self.players[idx_player].get_action()
                    print(action)
                    if action[0] == 'endgame' or action[0] == 'exit':
                        sys.exit(0)
                    elif action[0] == 'end':
                        action_list.remove(idx_player)
                    else:
                        self.do_action(idx_player, action)


if __name__ == '__main__':
    game = Game(1, True)
    game.start()
