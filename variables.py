"""hardcoding variables"""
import time

COUNT = 0
STAIR_COUNT = 0
BOARD = []
DEAD_FLAG_ENEMY = 0
COLUMN = 0
BRICKS = []
KHAMBA = []
SCENERY_BEGIN = 0
SCENERY_END = 30
JUMP = False
BRICKS = [[15, 5], [15, 6], [15, 7], [15, 8], [15, 15], [15, 16], [15, 43], [15, 44], [3, 10],
          [3, 11], [3, 12], [3, 13], [17, 64], [18, 65], [16, 70], [16, 71], [16, 72], [16, 73],
          [3, 14], [15, 45], [11, 10], [11, 11], [7, 9], [7, 8], [7, 7], [18, 60], [17, 61],
          [16, 75], [16, 76], [12, 71], [12, 70], [12, 69], [12, 72], [9, 71], [5, 75], [6, 75],
          [7, 75], [8, 75], [9, 75], [10, 75], [9, 76], [10, 76], [9, 77], [10, 77], [9, 78],
          [10, 78], [9, 79], [10, 79], [9, 80], [10, 80], [9, 81], [10, 81], [9, 82], [10, 82],
          [9, 83], [10, 83], [9, 84], [10, 84], [9, 85], [10, 85], [9, 86], [10, 86], [9, 87],
          [9, 88], [10, 88], [9, 89], [10, 89], [8, 89], [7, 89], [6, 89], [5, 89], [18, 120],
          [16, 122], [15, 123], [14, 124], [13, 125], [12, 126], [11, 127], [17, 121], [10, 87],
          [10, 128], [10, 133], [11, 134], [12, 135], [13, 136], [14, 137], [15, 138], [16, 139],
          [17, 140], [18, 141], [10, 155], [10, 156], [10, 157], [10, 158], [16, 180], [16, 181],
          [16, 182], [15, 183], [15, 184], [15, 185], [14, 183], [14, 184], [14, 185], [13, 183],
          [13, 184], [13, 185], [13, 188], [13, 189], [13, 190], [14, 188], [14, 189], [16, 74],
          [14, 190], [15, 188], [15, 189], [15, 190], [16, 191], [16, 192], [16, 193], [12, 190],
          [12, 189], [12, 188], [12, 187], [12, 186], [12, 185], [12, 184], [12, 183], [10, 189],
          [11, 189], [11, 188], [11, 187], [11, 186], [11, 185], [11, 184], [11, 183], [10, 190],
          [10, 188], [10, 187], [10, 186], [10, 185], [10, 184], [10, 183], [12, 190], [11, 190]]
BAADAL = []
KHAMBA = [[18, 27], [18, 37], [18, 102], [18, 159]]
LIS = [[18, 18], [18, 31], [18, 38], [18, 59], [2, 10], [11, 71], [15, 72], [18, 101], [18, 116]]
CHAR = "]"
MARIO_Y = 1
MARIO_X = 18
FLAG_D = 1
FLAG_A = 1
HEIGHT = 0
LAST = "rest"
SCORE = 0
CHANCES = 5
DEAD_FLAG = 0
TOUCH = 0
COIN = [[14, 6], [14, 7], [14, 8], [14, 15], [14, 16], [6, 9], [6, 8], [6, 7], [5, 6], [5, 5],
        [18, 41], [8, 76], [8, 77], [8, 78], [8, 79], [8, 80], [8, 81], [8, 82], [8, 83], [8, 84],
        [8, 85], [8, 86], [8, 87], [8, 88], [7, 76], [7, 77], [7, 78], [7, 79], [7, 80], [7, 81],
        [7, 82], [7, 83], [7, 84], [7, 85], [7, 86], [7, 87], [7, 88], [18, 128], [17, 128],
        [16, 128], [15, 128], [14, 128], [18, 127], [17, 127], [16, 127], [15, 127], [14, 127],
        [18, 126], [17, 126], [16, 126], [15, 126], [14, 126], [18, 125], [5, 7],
        [17, 125], [16, 125], [15, 125], [14, 125], [18, 124], [17, 124], [16, 124], [15, 124],
        [18, 123], [17, 123], [16, 123], [18, 122], [17, 122], [18, 121]]
SCORE = 0
TIMER = 100
START_TIME = time.time()
DEAD_FLAG_TIME = 0
GIFT = [[15, 7]]
MARIO_STR = "/o\\"
POWERUP = []
STAIR = [[19, 130], [19, 131], [15, 130], [15, 131], [11, 130], [11, 131], [7, 130],
         [7, 131], [3, 130], [3, 131]]
EN = []
SPECIAL = [[15, 15]]
TEMP_FLAG = 0
TEMP_COUNT = 0
GAMEOVER_COUNT = 0
FLAG_POSITION = 5
FLAG_DOWN = 0
SPRING = 0
BOSS_KILL = 0
GENERATE = 150
BOSS_FLAG = 0
BOSS_COME = 0
CONTROL = 0
CONTROL_FLAG = 0