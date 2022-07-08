class Board:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.board = [rows, columns]
    
    def printBoardSize(self):
        print(f'Board size: {self.board}')