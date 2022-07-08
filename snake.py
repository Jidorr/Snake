import sys
from sqlalchemy import func
import functions

class Snake:
    movements = {"R": [1, 0], "D": [0, 1], "L": [-1, 0], "U": [0, -1]}

    def __init__(self, snake: list, board: object):
        self.snake = snake
        self.board = board
        self.depth = int()

    def printSnakeConfig(self):
        print(f'Snake configuration: {self.snake}')

    def getEmptyAdjacentCells(self):
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

    def moveHead(self):
        move_options = self.getEmptyAdjacentCells()
        for option in move_options:
            self.moveBody()
            self.snake[0] = option
            print(self.snake)
            break
    
    def moveBody(self):
        self.snake.pop()
        self.snake.insert(0, 0)



