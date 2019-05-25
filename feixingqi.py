import random
# 地图初始坐标
Maps = [0] *100    
 
# 玩家A和玩家B的初始坐标
PlayerPos = [0]*2
# 存储玩家姓名
playerNames = [""] *2
 
# 俩个玩家行动的标记
Flags = [True]*2
 
# 封装一个不换行的print
def print_end(num):
    print(num,end="")
 
 
def gameshow():
    """
    飞行棋游戏头
    """
    print('\033[1;31;m')
    print("*"*50)
    print('\033[1;32;m')
    print("*" * 50)
    print('\033[5;33;m')
    print("*" * 15 + "飞行棋爵士版 v1.0" + "*"*20)
    print('\033[1;34;m')
    print("*" * 50)
    print('\033[1;35;m')
    print("*" * 50)
def chushihuamap():
    luckyturn_list = [3,15,33,36,45,71,89,95] # 幸运轮盘 ◎
    for number1 in luckyturn_list:
        Maps[number1] = 1
 
    landmine_list = [7,19,39,67,77,97] # 地雷 ●
    for number2 in landmine_list:
        Maps[number2] = 2
 
    pause_list = [2,5,9,31,37,56,87]  # 暂停 ▲
    for number3 in pause_list:
        Maps[number3] = 3
 
    timeTunnel_list = [1,10,28,60,88,] # 时空隧道 卐
    for number4 in timeTunnel_list:
        Maps[number4] = 4
def drawstringmap(a):
    """
     构造地图
    :param a: 0~99 的地图坐标
    :return: 返回地图坐标所在的 图
    """
    # 玩家A和玩家B在同一坐标用<>表示
    str = ""
    if PlayerPos[0] == PlayerPos[1] and PlayerPos[0] == a:
        str = "<>"
    elif PlayerPos[0] == a:
        str = "Ａ"
    elif PlayerPos[1] == a:
        str = "Ｂ"
    else:
        if Maps[a] == 0:
            print_end('\033[1;32;m')
            str = " □"
 
        elif Maps[a] == 1:
            print_end('\033[1;34;m')
            str = " ◎"
 
        elif Maps[a] == 2:
            print_end('\033[1;31;m')
            str = " ●"
 
        elif Maps[a] == 3:
            print_end('\033[1;35;m')
            str = " ▲"
 
        else:
            print_end('\033[1;33;m')
            str = "卐"
    return str
def drawmap():
    print("玩家A和玩家B在同一位置时用<>表示")
    print("图例：幸运轮盘:◎  地雷:●  暂停:▲  时空隧道:卐")
    # 第一横行
    for a in range(0,30):
        print_end(drawstringmap(a))
    print() # 第一横行结束后应该换行
    # 第一竖行
    for a in range(30,35):
        for b in range(0,29):
            print_end("  ")
        print_end(drawstringmap(a))
        print()
    # 第二横行
    a = 64
    while a >=35:
        print_end(drawstringmap(a))
        a -= 1
    print() # 换行
    # 第二竖行
    for a in range(65,70):
        print(drawstringmap(a))
    # 第三竖行
    for a in range(70,100):
        print_end(drawstringmap(a))
    # 画完最后一行应换行
    print()
def playGame(playnumber):
    """
     玩游戏
    :param playnumber: 玩家坐标
    """
    rNumber = random.randint(1,6)
    input()
    print("玩家{0}按下任意键开始掷骰子".format(playerNames[playnumber]))
    input()
    print("玩家{0}掷出了{1}".format(playerNames[playnumber],rNumber))
    PlayerPos[playnumber] += rNumber
    changePos()
    input()
    print("玩家{0}按任意键开始行动".format(playerNames[playnumber]))
    input()
    print("玩家{0}行动完了".format(playerNames[playnumber]))
    input()
    if Maps[PlayerPos[playnumber]] == 0:
        print("玩家{0}踩到了方块，什么也没发生".format(playerNames[playnumber]))
    elif Maps[PlayerPos[playnumber]] == 1:
        input_num = input("玩家{0}踩到了幸运轮盘，请选择  1.轰炸对方（后退6格） 2.交换位置".format(playerNames[playnumber]))
 
        while True:
            if input_num == "1":
                print("玩家{0}被轰炸，后退6格".format(playerNames[1 - playnumber]))
                PlayerPos[1 - playnumber] -= 6
                changePos()
                input()
                break
            elif input_num == "2":
                print("玩家{0}选择交换位置".format(playerNames[playnumber]))
                PlayerPos[playnumber],PlayerPos[1 - playnumber] = PlayerPos[1 - playnumber],PlayerPos[playnumber]
                input("交换完成，按任意键继续游戏")
                break
            else:
                input_num = input("只能输入 1.轰炸对方（后退6格） 2.交换位置 请重新输入")
 
    elif Maps[PlayerPos[playnumber]] == 2:
        print("玩家{0}踩中了地雷，后退6格".format(playerNames[playnumber]))
        PlayerPos[playnumber] -= 6
        changePos()
        input()
    elif Maps[PlayerPos[playnumber]] == 3:
        print("玩家{0}暂停一回合".format(playerNames[playnumber]))
 
        Flags[playnumber] = False
        input()
    elif Maps[PlayerPos[playnumber]] == 4:
        print("恭喜玩家{0}进入时空隧道，前进10步".format(playerNames[playnumber]))
        PlayerPos[playnumber] += 10
        changePos()
        input()
    changePos()
    # TODO 清屏 。。。。。
    drawmap()
def changePos():
    if PlayerPos[0] < 0:
        PlayerPos[0] = 0
    if PlayerPos[0] >99:
        PlayerPos[0] = 99
    if PlayerPos[1] < 0:
        PlayerPos[1] = 0
    if PlayerPos[1] > 99:
        PlayerPos[1] = 99
def win():
    print('\033[5;33;m')
    print("*" * 80)
    print("                          ■                        ■               ■          ")
    print("        ■■■■■■■■     ■    ■                       ■                 ■         ")
    print("        ■      ■     ■    ■                     ■ ■         ■       ■         ")
    print("        ■      ■     ■■■■■■■■■■               ■   ■         ■       ■         ")
    print("        ■■■■■■■■    ■     ■                    ■■■■■■■■     ■       ■         ")
    print("        ■      ■   ■      ■                      ●■ ●       ■       ■         ")
    print("        ■      ■          ■                     ● ■  ●      ■       ■         ")
    print("        ■      ■     ■■■■■■■■■■■               ●  ■    ●    ■       ■         ")
    print("        ■■■■■■■■          ■                 ●     ■     ●   ■       ■         ")
    print("       ■       ■          ■                       ■         ■       ■         ")
    print("      ■        ■          ■                       ■         ■       ■         ")
    print("     ■         ■          ■                       ■         ■     ■ ■         ")
    print("    ■          ■    ■■■■■■■■■■■■■■                ■                 ■         ")
    print("*" * 80)
def input_names():
    print('\033[1;34;m')
    playerNames[0] = input("请输入玩家A的姓名")
    while playerNames[0] == "":
        playerNames[0] = input("玩家A的名字不能为空，请重新输入")
    playerNames[1] = input("请输入玩家B的姓名")
    while playerNames[1] =="" or playerNames[0] == playerNames[1]:
        if playerNames[1] == "":
            playerNames[1] = input("玩家B的名字不能为空，请重新输入")
        else:
            playerNames[1] = input("玩家A的名字不能和玩家B的名字一样，请重新输入")
def a_and_b_plaing():
    while PlayerPos[0] < 99 and PlayerPos[1] < 99:
        if Flags[0] == True:
            playGame(0)
        else:
            Flags[0] = True
 
        if PlayerPos[0] >= 99:
            print("玩家{0}漂亮的赢了玩家{1}".format(playerNames[0], playerNames[1]))
            break
 
        if Flags[1] == True:
            playGame(1)
        else:
            Flags[1] = True
 
        if PlayerPos[1] >= 99:
            print("玩家{0}无耻的赢了玩家{1}".format(playerNames[1], playerNames[0]))
            break
 
# TODO 怎么清空控制台？
 
# 开始游戏
gameshow()
input_names()
print("玩家{0}的姓名用A表示".format(playerNames[0]))
print("玩家{0}的姓名用B表示".format(playerNames[1]))
chushihuamap()
drawmap()
# 玩家A和玩家B 都没有到达终点
a_and_b_plaing()
drawmap()
win()
