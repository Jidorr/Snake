import functions

class Snake:
    def __init__(self, snake: list, board: object):
        self.snake = snake
        self.board = board
        self.depth = int()
        self.counter = 0
        
    def printSnakeConfig(self):
        print(f'Snake configuration: {self.snake}')

    def getEmptyAdjacentCells(self):
        '''
        Gets all empty adjacent cells from the snake's head
        '''
        coordinate = self.snake[0]
        x, y = coordinate[0], coordinate[1]
        adjacent_positions = [[row + x ,col + y] for row in (-1,0,1) for col in (-1,0,1) if [row + x ,col + y] != [x,y]]
        new_list = [i for i in adjacent_positions if not functions.isOutOfBoard(i, self.board.rows, self.board.columns)]
        empty_cells = [i for i in new_list if not functions.cellIsOccupied(i, self.snake)]
        for i,j in enumerate(empty_cells):
            if functions.adjacent(coordinate, empty_cells[i]):
                pass
            else: 
                empty_cells.remove(j)
        return empty_cells


    def moveSnake(self, newHead = 0):
        '''
        Moves the snake to new head position
        Arg1: newhead list coordinate
        '''
        self.snake.pop()
        self.snake.insert(0, newHead)
