class Snake:
    movements = {"R": [1, 0], "D": [0, 1], "L": [-1, 0], "U": [0, -1]}

    def __init__(self, snake: list):
        self.snake = snake

    def printSnakeConfig(self):
        print(f'Snake configuration: {self.snake}')
