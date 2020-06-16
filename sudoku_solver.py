# Developer - Vishaal Padma Kumar
# Sudoku Solver
# A simple sudoku solver that uses the backtracking algorithm

# example sudoku board
test_board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

# 3 functions are requried -
# 1. A helper function to check if the current state of the board is valid
# 2. A recursive function that enters a value in a slot and checks if board
#    is valid. If it is isn't then we go back a step i.e. backtracking
# 3. A function that finds the next empty spot to run the algorithm

def rec_solver (board):
    empty_pos = empty_positon(board)
    if not empty_pos:
        return True
    else:
        row, column = empty_pos

    for num in range(1, 10):
        if is_valid(board, num, (row,column)):
            board[row][column] = num
            if rec_solver(board):
                return True
            board[row][column] = 0
    return False

# The helper function:
# In this case position is tuple whose first value is the row index and
# second value is the column index
def is_valid(board, val, position):
    row = position[0]
    col = position[1]
    # Checking if the same value is present in the same row, column, or square
    # Step 1: Checking row
    for i in range(len(board[0])):
        if board[row][i] == val and i != col:
            return False
    # Step 2: Checking column
    for i in range(len(board)):
        if board[i][col] == val and i != row:
            return False
    # Step 3: Checking same square
    sq_row = row // 3 # Row Index of Square
    sq_col = col // 3 # Column Index of Square
    for i in range(sq_row * 3, sq_row * 3 + 3):
        for j in range(sq_col * 3, sq_col * 3 + 3):
            if board[i][j] == val and (i, j) != position:
                return False
    return True

# The helper function that finds the next empty stop to fill
def empty_positon(board):
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
    return None

# Printing functions
def print_sudoku(board):
    print(" - - - - - - - - - - ")
    for i in range(len(board[0])):
        if i != 0 and i % 3 == 0:
            print(" - - - - - - - - - - ")
        for j in range(len(board)):
            if j % 3 == 0:
                print("|{}".format(board[i][j]), end="")
            elif j % 3 == 2:
                print("{}|".format(board[i][j]), end = "")
            else:
                print(" {} ".format(board[i][j]), end="")
        print()

print("\n This is the input sudoku board :-")
print_sudoku(test_board)
print("\n \n This is the output board :-")
rec_solver(test_board)
print_sudoku(test_board)
