import sys
from board import Board
from snake import Snake
import functions

def main():
    print("Welcome to the snake challenge")
    b = input("Enter the number of rows and columns separated by a comma: ")
    board = functions.createBoard(b)

    #s = input("Enter the number of rows and columns separated by a comma: ")

if __name__ == "__main__":
    main()
