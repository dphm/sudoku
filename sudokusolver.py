class SudokuSolver(object):
    def __init__(self, sudoku):
        self.puzzle = sudoku.puzzle
        self.domain = [[[d for d in range(1, 10)] for col in range(9)] for row in range(9)]
        self.reduce_domain()
    
    def reduce_domain(self):
        for i in range(9):
            for j in range(9):
                entry = self.puzzle[i][j]
                if entry != '_':
                    self.domain[i][j] = [entry]
    
    #TODO: rows, columns, constraints
    #TODO: search algorithm/backtracking/forward checking
    
    def get_squares(self):
        squares = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = []
                for row in self.puzzle[i:i+3]:
                    for entry in row[j:j+3]:
                        square.append(entry)
                squares.append(square)
        return squares
