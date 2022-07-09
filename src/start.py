import functions

def main():
    print("Welcome to the snake challenge")
    # Creating a new board object
    board = functions.createBoard()
    rows, columns = board.rows, board.columns

    # Creating a new snake object
    snake_list = []
    snake = functions.createSnake(snake_list, board)
    
    # Defining depth
    depth = functions.getDepth()
    snake.depth = depth

    # Getting number of different paths (currently hardcoded to depth=3)
    functions.numberOfAvailableDifferentPaths(snake, board, depth)

if __name__ == "__main__":
    main()
