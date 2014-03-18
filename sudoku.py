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
       
       Blank entries have a value of 0.
       Valid entries have a value between 1-9.
    """
    
    def __init__(self, filename):
        self.__puzzle = None
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
        with open(filename, 'r+') as f:
            self.__puzzle = [[int(x) for x in line.split()] for line in f]
    
    def get_entry(self, i, j):
        return self.__puzzle[i][j]
    
    def set_entry(self, i, j, entry):
        self.__puzzle[i][j] = entry

    def blank_entry(self, i, j):
        return self.get_entry(i, j) == 0
    
    def get_row(self, i):
        return self.__puzzle[i]
    
    def get_column(self, j):
        column = []
        for row in self.__puzzle:
            column.append(row[j])
        return column
    
    def get_square(self, i):
        self.__update_squares()
        return self.__squares[i]
        
    def __update_squares(self):
        squares = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = []
                for row in self.__puzzle[i:i+3]:
                    for entry in row[j:j+3]:
                        square.append(entry)
                squares.append(square)
        self.__squares = squares

    def get_puzzle(self):
        return list(self.__puzzle)

if __name__ == '__main__':
    s = Sudoku('sudoku1.txt')
    print s
