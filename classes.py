"""classes defined"""
from variables import BOARD

class Some():
    """Draw any character"""
    def __init__(self, pos_x, pos_y, string):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.string = string

    def draw(self):
        """draw string on BOARD"""
        BOARD[self.pos_x][self.pos_y] = self.string


class Player:
    """Player initialise"""
    def __init__(self, start):
        self.start = start


class Piller():
    """Draw obstacles"""
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self):
        """draw obstacle on BOARD"""
        BOARD[self.pos_x][self.pos_y] = "| |"
        BOARD[self.pos_x - 1][self.pos_y] = "| |"
        BOARD[self.pos_x - 2][self.pos_y] = "---"


class Enemy:
    """Enemy class"""
    def __init__(self, pos_x, pos_y, stri, stri2):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.string = stri
        self.speed = 1
        self.stri2 = stri2
        self.flag = 0

    def show(self, pos_x, pos_y):
        """draw enemy on BOARD"""
        BOARD[pos_x][pos_y] = self.string
        BOARD[pos_x - 1][pos_y] = self.stri2

    def setx(self, pos_x):
        """set x coordinate"""
        self.pos_x = pos_x

    def remove(self, pos_x, pos_y):
        """delete charcter from BOARD"""
        BOARD[pos_x][pos_y] = "   "
        BOARD[pos_x - 1][pos_y] = "   "
        self.pos_x += 0


    def sety(self, pos_x, pos_y):
        """set y coordinate"""
        if BOARD[self.pos_x][self.pos_y + self.speed] == '   ':
            self.pos_y = pos_y + self.speed
        if BOARD[self.pos_x][self.pos_y + self.speed] == ' $ ':
            self.pos_y = pos_y + self.speed

        if BOARD[self.pos_x +1][self.pos_y +self.speed] == '   ':
            if BOARD[self.pos_x][self.pos_y + self.speed] == ' $ ':
                pass
            else:
                self.speed = -1 * self.speed
        if BOARD[self.pos_x][self.pos_y + self.speed] != '   ':
            if BOARD[self.pos_x][self.pos_y + self.speed] == ' $ ':
                pass
            else:
                self.speed = -1 * self.speed
