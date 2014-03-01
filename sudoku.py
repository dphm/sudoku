from sudokusolver import SudokuSolver

class Sudoku(object):
    """3x3 Sudoku puzzle with the following format:
           | 0 1 2 | 3 4 5 | 6 7 8
         --|-------|-------|------
         0 | _ _ _ | _ _ _ | _ _ _
         1 | _ _ _ | _ _ _ | _ _ _
         2 | _ _ _ | _ _ _ | _ _ _
         --|-------|-------|------
         3 | _ _ _ | _ _ _ | _ _ _
         4 | _ _ _ | _ _ _ | _ _ _
         5 | _ _ _ | _ _ _ | _ _ _
         --|-------|-------|------
         6 | _ _ _ | _ _ _ | _ _ _
         7 | _ _ _ | _ _ _ | _ _ _
         8 | _ _ _ | _ _ _ | _ _ _
    """
    
    def __init__(self, filename):
        self.__puzzle = []
        self.__squares = []
        self.__read(filename)
    
    def __str__(self):
        string = ''
        for i in range(9):
            for j in range(9):
                string += '%s ' % self.__puzzle[i][j]
                if j % 3 == 2 and j != 8:
                    string += '| '
                if j == 8:
                    string += '\n'
            
            if i % 3 == 2 and i != 8:
                string += '------|-------|------\n'
        
        return string
    
    def __read(self, filename):
        with open(filename, 'r+') as input:
            for line in input:
                self.__puzzle.append(line.split())
    
    def get_entry(self, i, j):
        return self.__puzzle[i][j]
    
    def set_entry(self, i, j, entry):
        self.__puzzle[i][j] = entry
    
    def get_square(self, i):
        self.__update_squares()
        return self.__squares[i]
        
    def __update_squares(self):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = []
                for row in self.__puzzle[i:i+3]:
                    for entry in row[j:j+3]:
                        square.append(entry)
                self.__squares.append(square)


if __name__ == '__main__':
    s = Sudoku('sudoku1.txt')
    print s
