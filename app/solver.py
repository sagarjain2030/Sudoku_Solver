from .sudoku_class import sudoku_class as sc

def is_valid(board, row, col, num):
    """Check if placing a number on board[row][col] is valid."""
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    sudoku = sc(board)
    return False    
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# def parse_input(data):
#     """Parse string input into a 9x9 matrix."""
#     try:
#         rows = data.strip().split("\n")
#         board = [[int(cell) if cell.isdigit() else 0 for cell in row.split()] for row in rows]
#         if len(board) == 9 and all(len(row) == 9 for row in board):
#             return board
#     except:
#         return None
