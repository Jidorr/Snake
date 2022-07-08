import sys
from board import Board
from snake import Snake


def createBoard():
    input_args = input("Enter the number of rows and columns of the board separated by a comma: ")
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
        try:
            s = input("Enter the snake coordinates separated by a comma and type 1 to stop (3 to 7 length): ")
            if s == '1':
                break
            if not (len(s.split(sep=',')) == 2):
                raise ValueError
            x, y = int(s.split(sep=',')[0]), int(s.split(sep=',')[1])
            if (0 <= x <= rows) and (0 <= y <= columns):
                pass
            else:
                raise ValueError
            snake.append([x, y])
            counter += 1

        except ValueError:
            print('Invalid snake configuration')
            sys.exit()
        
    
    if not 3 <= counter <= 7:
        print("Lenght of the snake has to be between 3 and 7")
        sys.exit()

    validateSnake(snake)
    snake_obj = Snake(snake)
    return snake_obj
    
def validateSnake(snake):
    for i,j in enumerate(snake):
        if i == len(snake)-1:
            break
        elif adjacent(snake[i], snake[i+1]):
            pass
        else: 
            print('Invalid snake configuration, not adjacent')
            sys.exit()
    dups = {tuple(x) for x in snake if snake.count(x) > 1}
    if len(dups) != 0:
        print('Invalid snake configuration, repeated coordinates')
        sys.exit()

def adjacent(a, b):
    '''
    Returns True if a and b are adjacent coordinates
    '''
    if a[0] == b[0] and abs(a[1] - b[1]) == 1:
        return True 
    elif a[1] == b[1] and abs(a[0] - b[0]) == 1:
        return True
    else:
        return False 

def getDepth():
    depth = input("Enter depth (1 to 20): ")
    try:
        depth = int(depth)
        if not 1 <= depth <= 20:
            raise ValueError

    except ValueError:
        print('Invalid depth')
        # rerun the program
        sys.exit()
    return depth