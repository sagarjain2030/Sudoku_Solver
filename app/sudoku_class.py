class sudoku_class:
    def __init__(self, board):
        self.board = board
        self.cell_dict = dict()
        for row in range(9):
            for col in range(9):
                if(self.board[row][col] == 0):
                    self.cell_dict[(row, col)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                else:
                    self.cell_dict[(row, col)] = self.board[row][col]
        print("cell_dict is :", self.cell_dict)


    
