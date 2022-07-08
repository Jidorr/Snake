from sqlalchemy import func
import functions

def main():
    print("Welcome to the snake challenge")
    board = functions.createBoard()
    
    rows, columns = board.rows, board.columns

    snake_list = []
    snake = functions.createSnake(snake_list, rows, columns)
    
    depth = functions.getDepth()
    snake.depth = depth

    board.printBoardSize()
    snake.printSnakeConfig()
    print("Depth:", depth)
if __name__ == "__main__":
    main()
