class Sudoku(object):
    def __init__(self, filename):
        self.puzzle = []
        self.read(filename)
    
    def __str__(self):
        string = ''
        for i in range(9):
            for j in range(9):
                string += '%s ' % self.puzzle[i][j]
                if j % 3 == 2 and j != 8:
                    string += '| '
                if j == 8:
                    string += '\n'
            
            if i % 3 == 2 and i != 8:
                string += '------|-------|------\n'
        
        return string
    
    def read(self, filename):
        with open(filename, 'r+') as input:
            for line in input:
                self.puzzle.append(line.split())


if __name__ == '__main__':
    s = Sudoku('sudoku1.txt')
    print s