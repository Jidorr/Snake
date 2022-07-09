import sys
from board import Board
from snake import Snake


def createBoard():
    '''
    Asks user for input to create a new Board object
    Raises ValueError if conditions are not met
    '''
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
        # Exit the program
        sys.exit()
    
    return board

def createSnake(snake, board):
    '''
    Asks user for input to create a new Snake object
    Arg1: snake list
    Arg2: board object
    Raises ValueError if conditions are not met
    '''
    counter = 0
    while True:
        try:
            s = input("Enter the snake coordinates separated by a comma and type 1 to stop (3 to 7 length): ")
            if s == '1':
                break
            if not (len(s.split(sep=',')) == 2):
                raise ValueError
            x, y = int(s.split(sep=',')[0]), int(s.split(sep=',')[1])
            if (0 <= x <= board.rows) and (0 <= y <= board.columns):
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
    snake_obj = Snake(snake, board)
    return snake_obj
    
def validateSnake(snake):
    '''
    Validates the adjacency of all the snake cells
    Arg1: snake list
    '''
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
    Arg1: a list coordinate
    Arg2: b list coordinate
    '''
    if a[0] == b[0] and abs(a[1] - b[1]) == 1:
        return True 
    elif a[1] == b[1] and abs(a[0] - b[0]) == 1:
        return True
    else:
        return False 

def getDepth():
    '''
    Asks user for input to set depth value
    Raises ValueError if conditions are not met
    '''
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

def isOutOfBoard(coordinate, rows, columns):
    '''
    Checks if cell is out of board
    Arg1: cell coordinate list
    Arg2: board rows
    Arg3: board columns
    '''
    x, y = coordinate[0], coordinate[1]
    if ((0 <= x < rows) and (0 <= y < columns)):
        return False
    else:
        return True

def cellIsOccupied(cell, snake):
    '''
    Checks if cell is occupied by another cell
    Arg1: cell coordinate list
    Arg2: snake list
    '''
    if cell in snake:
        return True
    else:
        return False


def loop_rec(depth, snake, board):
    '''
    Recursive function to return all available different paths
    ** Not finished **
    Arg1: int depth
    Arg2: snake object
    Arg3: board object
    '''
    def recurse(depth, newSnake, move_options=0, paths=[]):
        if depth == snake.depth:
            move_options = snake.getEmptyAdjacentCells()
            snake_copy = snake.snake.copy()
            newSnake = Snake(snake_copy, board)
            recurse(depth-1, newSnake, move_options, paths)
        elif depth < 0:
            return paths
        elif depth == 0:
            paths = []
            for cell in move_options:
                paths.append(cell)
            recurse(depth-1, newSnake, move_options, paths)
        else:
            for option in move_options:
                newSnake.moveSnake(option)
                move_options = newSnake.getEmptyAdjacentCells()
                recurse(depth-1, newSnake, move_options, paths)
    recurse(depth, snake)



def numberOfAvailableDifferentPaths(snake, board, depth):
    '''
    Gets the available different paths
    ** Currently hardcoded to depth = 3 **
    Arg1: snake list
    '''
    llista = []
    for move_option in snake.getEmptyAdjacentCells():
        snake.moveSnake(move_option)
        for move_option in snake.getEmptyAdjacentCells():
            snake.moveSnake(move_option)
            for move_option in snake.getEmptyAdjacentCells():
                llista.append(move_option)
    print(f'Number of available different paths: {len(llista)}')