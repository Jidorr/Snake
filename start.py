from sqlalchemy import func
import functions

def main():
    print("Welcome to the snake challenge")
    board = functions.createBoard()
    
    rows, columns = board.rows, board.columns

    snake_list = []
    snake = functions.createSnake(snake_list, rows, columns, board)
    
    depth = functions.getDepth()
    snake.depth = depth
    snake.moveHead()

if __name__ == "__main__":
    main()
