import sys

from regex import S
from board import Board
from snake import Snake
import functions

def main():
    print("Welcome to the snake challenge")
    board = functions.createBoard()
    board.printBoardSize()
    rows, columns = board.rows, board.columns

    snake_list = []
    functions.createSnake(snake_list, rows, columns)
    snake = Snake(snake_list)
    snake.printSnakeConfig()

if __name__ == "__main__":
    main()
