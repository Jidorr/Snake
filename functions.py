import sys
from board import Board
from snake import Snake


def createBoard():
    input_args = input("Enter the number of rows and columns separated by a comma: ")
    try:
        rows = int(input_args.split(sep=',')[0])
        columns = int(input_args.split(sep=',')[1])
        if (1 <= rows <= 10) and (1 <= columns <= 10) and (len(input_args.split(sep=',')) == 2):
            board = Board(rows, columns)
        else: 
            raise ValueError

    except ValueError:
        print('Invalid board format, has to be two integers separated by comma')
        # rerun the program
        sys.exit()
    
    return board


def createSnake(snake, rows, columns):
    counter = 0
    while True:
        s = input("Enter the snake coordinates separated by a comma and type 1 to stop (3 to 7 length): ")
        if s == '1':
            break
        x, y = int(s.split(sep=',')[0]), int(s.split(sep=',')[1])
        if not (len(s.split(sep=',')) == 2):
            raise ValueError
        elif (0 <= x <= rows) and (0 <= y <= columns):
            pass
        else:
            raise ValueError

        snake.append([x, y])
        counter += 1
    
    if not 3 <= counter <= 7:
        print("Lenght of the snake has to be between 3 and 7")
    