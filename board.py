"""drawing board again"""
from colorama import Fore
from variables import BOARD as gameboard, MARIO_Y


def drawboard(board, column, scenery_begin, scenery_end):
    """drawing board"""
    hline = '--------------------------------------------------------------------------------------------'
    print(Fore.WHITE + hline)
    for pos_x in range(21):  # no of rows shown on screen
        print('!', end=' ')
        if (MARIO_Y - scenery_begin) < 15:
            for pos_y in range(scenery_begin, scenery_end):
                if board[pos_x][pos_y] == "===":
                    if pos_x <= 18:
                        print(Fore.CYAN + '%s' % (board[pos_x][pos_y]), end='')
                    else:
                        print(Fore.RED + '%s' % (board[pos_x][pos_y]), end='')
                elif(board[pos_x][pos_y] == "/o\\" or board[pos_x][pos_y] == "|O|"):
                    print(Fore.BLUE + '%s' % (board[pos_x][pos_y]), end='')
                elif board[pos_x][pos_y] == " $ ":
                    print(Fore.YELLOW + '%s' % (board[pos_x][pos_y]), end='')

                else:
                    print(Fore.WHITE + '%s' % (board[pos_x][pos_y]), end='')
        else:
            for pos_y in range(column - 15, 30 + column - 15):
                if board[pos_x][pos_y] == "===":
                    if pos_x <= 18:
                        print(Fore.CYAN + '%s' % (board[pos_x][pos_y]), end='')
                    else:
                        print(Fore.RED + '%s' % (board[pos_x][pos_y]), end='')
                elif(board[pos_x][pos_y] == "/o\\" or board[pos_x][pos_y] == "|O|"):
                    print(Fore.BLUE + '%s' % (board[pos_x][pos_y]), end='')
                elif board[pos_x][pos_y] == " $ ":
                    print(Fore.YELLOW + '%s' % (board[pos_x][pos_y]), end='')

                else:
                    print(Fore.WHITE + '%s' % (board[pos_x][pos_y]), end='')
        print('!')


def getnewboard():
    """this function initialises a matrix of 20rows and 50 col"""
    for i in range(30):
        gameboard.append(['   '] * 500)
    return gameboard
