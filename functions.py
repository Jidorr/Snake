import sys
from board import Board
from snake import Snake


def createBoard(input_args):
    try:
        rows = int(input_args.split(sep=',')[0])
        columns = int(input_args.split(sep=',')[1])
        if (1 <= rows <= 10) and (1 <= columns <= 10) and (len(input_args.split(sep=',')) == 2):
            board = Board(rows, columns)
            board.printBoardSize()
        else: 
            raise ValueError

    except ValueError:
        print('Invalid board format, has to be two integers separated by comma')
        # rerun the program
        sys.exit()
    
    return board