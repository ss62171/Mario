"""main file"""
import os
import time
from colorama import Fore
import NonBlockingInput as keyb
import variables
from board import drawboard, getnewboard
from classes import *

kb = keyb.KBHit()
#os.system('aplay -q main_theme.wav&')


def collision_check_d():
    """checking collision forward"""

    if BOARD[variables.MARIO_X][variables.MARIO_Y + 1] == "| |" or BOARD[variables.MARIO_X][variables.MARIO_Y + 1] == "!$!" or BOARD[variables.MARIO_X][variables.MARIO_Y + 1] == "---" or BOARD[variables.MARIO_X][variables.MARIO_Y + 1] == "===" or BOARD[variables.MARIO_X][variables.MARIO_Y + 1] == " T ":
        variables.FLAG_D = 0
    else:
        variables.FLAG_D = 1


def collision_check_a():
    """checking collision backward"""
    if BOARD[variables.MARIO_X][variables.MARIO_Y - 1] == "| |" or BOARD[variables.MARIO_X][variables.MARIO_Y - 1] == "---" or BOARD[variables.MARIO_X][variables.MARIO_Y - 1] == "!$!" or BOARD[variables.MARIO_X][variables.MARIO_Y - 1] == "===" or BOARD[variables.MARIO_X][variables.MARIO_Y - 1] == " T ":
        variables.FLAG_A = 0
    else:
        variables.FLAG_A = 1


def getinput():
    """checking users input"""
    if kb.kbhit():
        variables.CHAR = kb.getch()
    else:
        variables.CHAR = "{"

    if variables.CHAR == "q":
        exit()
    if variables.CHAR == "d" and variables.FLAG_D == 1:
        if variables.BOSS_COME == 1:
            if variables.MARIO_Y >= 159:
                variables.MARIO_Y = 159
            else:
                variables.MARIO_Y = variables.MARIO_Y + 1
        else:
            variables.MARIO_Y = variables.MARIO_Y + 1
        if (variables.MARIO_Y > (variables.SCENERY_BEGIN + variables.SCENERY_END) / 2 and variables.BOSS_COME == 0):
            variables.SCENERY_BEGIN = variables.SCENERY_BEGIN + 1
            variables.SCENERY_END = variables.SCENERY_END + 1

    if variables.CHAR == "a" and variables.FLAG_A == 1:
        if variables.MARIO_Y > 0 and variables.SCENERY_BEGIN < variables.MARIO_Y:
            variables.MARIO_Y = variables.MARIO_Y - 1
        else:
            pass

    if variables.CHAR == "w" and variables.LAST == "rest" and variables.MARIO_X < 19:
        variables.JUMP = True
        variables.LAST = "motion"
#        os.system('aplay -q smb_jump-small.wav&')


def stand():
    """checking standing condition"""
    if(BOARD[variables.MARIO_X - 1][variables.MARIO_Y] == " $ " or BOARD[variables.MARIO_X - 1][variables.MARIO_Y] == "POP" or BOARD[variables.MARIO_X - 1][variables.MARIO_Y] == "  (" or BOARD[variables.MARIO_X - 1][variables.MARIO_Y] == "(_ "):
        pass
    elif BOARD[variables.MARIO_X - 1][variables.MARIO_Y] != "   ":
        #            os.system('aplay -q smb_bump.wav&')
        variables.JUMP = False
        if BOARD[variables.MARIO_X - 1][variables.MARIO_Y] == "???":
            time.sleep(0.1)
            variables.GIFT.remove([variables.MARIO_X - 1, variables.MARIO_Y])
            variables.POWERUP.append([variables.MARIO_X - 2, variables.MARIO_Y])


def land():
    """checking landing condition"""
    if(variables.JUMP is False and BOARD[variables.MARIO_X + 1][variables.MARIO_Y] == " T "):
        variables.HEIGHT = 0
        variables.LAST = "rest"
        variables.JUMP = True
        variables.SPRING = 1
        BOARD[17][0] = "   "
#        os.system('aplay -q smb_jump-super.wav&')
    elif(variables.JUMP is False and BOARD[variables.MARIO_X + 1][variables.MARIO_Y] == "!$!"):
        variables.HEIGHT = 0
        variables.LAST = "rest"
        variables.BOSS_FLAG = 1
    elif(variables.JUMP is False and BOARD[variables.MARIO_X + 1][variables.MARIO_Y] != "   "):
        variables.HEIGHT = 0
        variables.LAST = "rest"


def coins():
    """checking collision coins"""
    if BOARD[variables.MARIO_X][variables.MARIO_Y] == " $ ":
        #        os.system('aplay -q smb_coin.wav&')
        variables.COIN.remove([variables.MARIO_X, variables.MARIO_Y])
        variables.SCORE += 10


def MARIO():
    """define mario string"""
    if BOARD[variables.MARIO_X][variables.MARIO_Y] == "POP":
        variables.MARIO_STR = "|O|"
        variables.POWERUP.clear()


def akhil():
    """checking jumping condition"""
    if (variables.JUMP is False and (BOARD[variables.MARIO_X + 1][variables.MARIO_Y] == "   " or BOARD[variables.MARIO_X + 1][variables.MARIO_Y] == "POP" or BOARD[variables.MARIO_X + 1][variables.MARIO_Y] == " $ " or BOARD[variables.MARIO_X + 1][variables.MARIO_Y] == " O " or BOARD[variables.MARIO_X + 1][variables.MARIO_Y] == "{ }") and (variables.MARIO_X != 18 or variables.MARIO_X != 19)):

        variables.HEIGHT = 1


def jumping():
    """checking jumping constraints"""
    stand()
    land()
    akhil()
    if variables.JUMP:
        variables.HEIGHT = variables.HEIGHT + 1
        variables.MARIO_X = variables.MARIO_X - 1

    if(variables.HEIGHT == 6 and variables.SPRING == 0):
        variables.JUMP = False
    if(variables.HEIGHT == 14 and variables.SPRING == 1):
        variables.JUMP = False
        variables.SPRING = 0

    if(variables.JUMP is False and variables.HEIGHT > 0):
        variables.HEIGHT = variables.HEIGHT - 1
        variables.MARIO_X = variables.MARIO_X + 1
        if(BOARD[variables.MARIO_X + 1][variables.MARIO_Y] == "POP" or BOARD[variables.MARIO_X + 1][variables.MARIO_Y] == " $ " or BOARD[variables.MARIO_X + 1][variables.MARIO_Y] == " O " or BOARD[variables.MARIO_X + 1][variables.MARIO_Y] == "{ }"):
            variables.HEIGHT = variables.HEIGHT - 1
            variables.MARIO_X = variables.MARIO_X + 1


def gameover():
    """checking gameover condition"""
    if(variables.CHANCES > 0 and (variables.DEAD_FLAG == 1 or variables.DEAD_FLAG_TIME == 1)):
        print(Fore.WHITE + "press 'q' for exit and press Enter")
        print(Fore.WHITE + "press 'c' to continue and press Enter")
        ans = input()
        if ans == "q":
            exit()
        if(ans == "c" and variables.DEAD_FLAG == 1):
            variables.CHANCES = variables.CHANCES - 1
            variables.CHAR = "]"
            if variables.MARIO_Y in range(0, 28):
                variables.MARIO_Y = 2
            elif variables.MARIO_Y in range(28, 38):
                variables.MARIO_Y = 28
            elif variables.MARIO_Y in range(38, 59):
                variables.MARIO_Y = 28
            elif variables.MARIO_Y in range(59, 102):
                variables.MARIO_Y = 59
            elif variables.MARIO_Y in range(102, 128):
                variables.MARIO_Y = 103
            elif variables.MARIO_Y in range(128, 165):
                variables.MARIO_Y = 128
            variables.MARIO_X = 18
            variables.FLAG_D = 1
            variables.HEIGHT = 0
            variables.LAST = "rest"
            variables.SCENERY_BEGIN = variables.MARIO_Y - 2
            variables.SCENERY_END = variables.MARIO_Y - 2 + 30
            variables.DEAD_FLAG = 0
            variables.JUMP = False
            variables.MARIO_STR = "/o\\"
        if(ans == "c" and variables.DEAD_FLAG_TIME == 1):
            variables.CHAR = "]"
            variables.MARIO_Y = 0
            variables.MARIO_X = 18
            variables.FLAG_D = 1
            variables.HEIGHT = 0
            variables.LAST = "rest"
            variables.SCENERY_BEGIN = 0
            variables.SCENERY_END = 30
            variables.DEAD_FLAG_TIME = 0
            variables.JUMP = False
            variables.MARIO_STR = "/o\\"
            variables.START_TIME = time.time()

        else:
            print(Fore.WHITE + "Mistyped")
            gameover()
    if variables.CHANCES == 0:
        print(Fore.WHITE + "GAME OVER")
#        os.system('aplay -q smb_gameover.wav&')
#        os.system('killall aplay')
        exit()


GAMEBOARD = getnewboard()
mario = Some(variables.MARIO_X, variables.MARIO_Y, variables.MARIO_STR)
for i in range(500):
    BOARD[19][i] = "==="
    BOARD[20][i] = "==="

from hardcode import *


for i in variables.LIS:
    e = Enemy(i[0], i[1], "{ }", " O ")
    variables.EN.append(e)


def enemy_touch():
    """checking enemy collision"""
    variables.TOUCH = 0
    for i in variables.EN:
        if(variables.MARIO_X == i.pos_x and variables.MARIO_Y == i.pos_y):
            variables.TOUCH = 1
        if variables.TOUCH == 1:
            if variables.MARIO_STR == "|O|":
                variables.MARIO_STR = "/o\\"
                i.speed *= -1
                variables.TEMP_FLAG = 1
                variables.TOUCH = 0
                break

            elif(variables.MARIO_STR == "/o\\" and variables.TEMP_FLAG == 0):
                variables.DEAD_FLAG = 1
                i.speed *= -1
                variables.TOUCH = 0
                break
    gameover()


def collision_enemy():
    """killing enemy"""
    for i in variables.EN:
        if(variables.MARIO_X + 1 == i.pos_x and variables.MARIO_Y == i.pos_y):
            i.flag = 1
            variables.SCORE += 20


for i in range(5, 18):
    BOARD[i][165] = " ||"


def mario_stair():
    """stair function"""
    for i in variables.STAIR:
        if(variables.MARIO_X == i[0] - 1 and variables.MARIO_Y == i[1]):
            return 1


def move_stair():
    """moving stair function"""
    for i in variables.STAIR:
        i[0] -= 1
        if i[0] == -1:
            i[0] = 19


def boss(y):
    """boss enemy function"""
    BOARD[17][y] = "WWW"
    BOARD[16][y] = "MMM"
    BOARD[17][y + 2] = "WWW"
    BOARD[16][y + 2] = "MMM"
    BOARD[15][y + 1] = "!$!"
    if len(variables.EN) <= 11:
        if(variables.CONTROL % 10 == 0 and variables.MARIO_Y >= 135 and variables.BOSS_KILL < 10):
            if variables.CONTROL_FLAG == 1:
                variables.EN.append(Enemy(18, y, "{ }", " O "))
                variables.CONTROL_FLAG = 0
    if variables.BOSS_FLAG == 1:
        BOARD[17][y] = "   "
        BOARD[16][y] = "   "
        BOARD[17][y + 2] = "   "
        BOARD[16][y + 2] = "   "
        BOARD[15][y + 1] = "   "
        variables.BOSS_KILL += 1
        if variables.BOSS_KILL == 1:
            variables.GENERATE = 143
            variables.BOSS_FLAG = 0
        elif variables.BOSS_KILL == 2:
            variables.GENERATE = 149
            variables.BOSS_FLAG = 0
        elif variables.BOSS_KILL == 3:
            variables.SCORE += 1000
            variables.BOSS_KILL = 10


BOARD[variables.FLAG_POSITION][166] = " > "
BOARD[18][0] = " T "
BOARD[18][91] = " T "

while 1:
    """main loop"""
    BOARD[17][0] = " T "
    BOARD[17][91] = " T "
    present_time = time.time()
    for i in variables.STAIR:
        b = Some(i[0], i[1], "===")
        b.draw()
    for i in variables.BRICKS:
        b = Some(i[0], i[1], "===")
        b.draw()
    for i in variables.BAADAL:
        b = Some(i[0], i[1], "str")
        b.draw()
    for i in variables.KHAMBA:
        b = Piller(i[0], i[1])
        b.draw()
    for i in variables.COIN:
        b = Some(i[0], i[1], " $ ")
        b.draw()
    for i in variables.GIFT:
        b = Some(i[0], i[1], "???")
        b.draw()
    for i in variables.POWERUP:
        b = Some(i[0], i[1], "POP")
        b.draw()

    if variables.COUNT == 5:
        for i in variables.EN:
            i.remove(i.pos_x, i.pos_y)
            i.sety(i.pos_x, i.pos_y)
            i.show(i.pos_x, i.pos_y)
            i.setx(i.pos_x)
        variables.COUNT = 0
    variables.COUNT += 1
    enemy_touch()
    TEMP_COUNT = 0
    if variables.TEMP_FLAG == 1:
        TEMP_COUNT += 1
        if TEMP_COUNT == 5:
            variables.TEMP_FLAG = 0
            TEMP_COUNT = 0

    collision_check_d()
    collision_check_a()

    if variables.MARIO_Y < 165:
        getinput()

    jumping()
    if variables.MARIO_X == 18:
        variables.LAST = "rest"
        jumping()
    coins()
    MARIO()
    if variables.MARIO_X == 22:
        variables.DEAD_FLAG = 1
        gameover()

    variables.EN = [item for item in variables.EN if item.flag != 1]

    variables.FLAG_D = 1
    variables.FLAG_A = 1
    collision_enemy()

    os.system('clear')
    if variables.MARIO_Y < 165:
        variables.TIMER = 100 - (int)(present_time - variables.START_TIME)

    if(variables.TIMER == 0 and variables.MARIO_Y < 165):
        variables.CHANCES = variables.CHANCES - 1
        variables.DEAD_FLAG_TIME = 1
        gameover()
    if(variables.TIMER <= 0 and variables.MARIO_Y >= 165 and variables.MARIO_Y < 186):
        variables.GAMEOVER_COUNT += 1
        if variables.GAMEOVER_COUNT == 2:
            variables.MARIO_Y += 1
            variables.SCENERY_BEGIN += 1
            variables.SCENERY_END += 1
            variables.GAMEOVER_COUNT = 0

    BOARD[variables.MARIO_X][variables.MARIO_Y] = variables.MARIO_STR
    drawboard(GAMEBOARD, variables.MARIO_Y, variables.SCENERY_BEGIN, variables.SCENERY_END)
    BOARD[variables.MARIO_X][variables.MARIO_Y] = "   "
    if variables.STAIR_COUNT == 5:
        variables.CONTROL += 1
        if mario_stair() == 1:
            variables.MARIO_X -= 1

        for i in variables.STAIR:
            BOARD[i[0]][i[1]] = "   "
        move_stair()
        variables.STAIR_COUNT = 0

    if(variables.MARIO_Y == 165 and variables.TIMER > 0 and variables.FLAG_POSITION < 18):
        variables.MARIO_Y = 165
        BOARD[variables.FLAG_POSITION][166] = "   "
        variables.FLAG_POSITION += 1
        BOARD[variables.FLAG_POSITION][166] = " > "
        if variables.FLAG_POSITION >= 18:
            variables.FLAG_DOWN = 1

    if(variables.MARIO_Y == 165 and variables.TIMER > 0 and variables.FLAG_DOWN == 1):
        variables.SCORE += variables.TIMER
        variables.TIMER -= 1
        variables.MARIO_Y = 165
#        os.system('aplay -q smb_stage_clear.wav&')
    if variables.MARIO_Y >= 144:
        if variables.BOSS_KILL < 3:
            variables.BOSS_COME = 1
        if variables.BOSS_KILL > 3:
            variables.BOSS_COME = 0

    if variables.MARIO_Y >= 186:
        variables.MARIO_Y = 186
        print(Fore.WHITE + "LEVEL COMPLETED")
#        os.system('killall aplay')
        break
    print(Fore.WHITE + "SCORE = ", variables.SCORE, end='|')
    print(Fore.WHITE + "LIFE X", variables.CHANCES, end='|')
    print(Fore.WHITE + "TIME = ", variables.TIMER)
    variables.STAIR_COUNT += 1
    variables.CONTROL_FLAG = 1
    boss(variables.GENERATE)
    time.sleep(0.07)
