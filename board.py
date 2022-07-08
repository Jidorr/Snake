class Board:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
    
    def printBoardSize(self):
        print(f'Rows: {self.rows} \nColumns: {self.columns}')