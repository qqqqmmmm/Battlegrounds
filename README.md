# Battlegrounds
## 项目简介
### 终极目标
炉石传说酒馆战棋AI，能够自己玩酒馆战棋，全自动上分
### 总计划
程序主要分为三部分：  
part1：复现酒馆战棋核心内容（包括除图形界面以外所有内容）
part2：深度强化学习AI，用part1完成内容进行自对弈收集数据  
part3：游戏内图像识别，鼠标操作
### 当前进展
基本框架搭好了，随从class(Minion)、随从池class(MinionPool)、棋盘class(Board)基本已经定型，战吼机制已经实现，亡语等机制已有想法如何实现，光环类效果（如铜须、卡德加、熊妈）等还没想好如何优雅地实现，战斗阶段Combat Phase相关内容还没开始写。minion文件夹中八大种族及中立随从，除野兽beast种族的随从1至6星全部写完，其余种族只将1星卡写完。
### 未来规划
先实现战斗阶段Combat Phase基本逻辑（对手选择规则，随从进攻次序，选择目标，造成伤害，受到伤害，死亡判定等）。  
然后在忽略掉许多游戏机制，大部分随从当白板处理，能够进行完整游戏的情况下，尝试写AI看看在简化模式下能不能work，能不能不是人工智障，再决定下一步做什么。
### 游戏操作
目前招募阶段Recruit Phase基本已经实现，程序可以跑起来（python3.8），基本操作如下：  
结束游戏：endgame或exit  
结束回合：end  
招募随从：recruit idx或buy idx  
出售随从：sell idx  
刷新酒馆：refresh  
升级酒馆：upgrade  
使用手牌：use idx idx(战吼目标)
