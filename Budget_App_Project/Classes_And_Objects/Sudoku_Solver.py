# This line starts a definition of a container (class) called Board
# The Board will hold and manage a Sudoku puzzle
class Board:
    # This function creates a new Board. It takes a Sudoku puzzle as input
    # and stores it for later use
    def __init__(self, board):
        self.board = board
        
    # This function determines how the Board looks when printed
    # It converts the Sudoku numbers into a nice-looking grid
    def __str__(self):
        board_str = '' # Start with an empty string
        for row in self.board: # Go through each row in the puzzle
            # For each number in the row:
            # - If it's not zero, show the number
            # - If it's zero (empty cell), show an asterisk (*)
            row_str = [str(i) if i != 0 else '*' for i in row]
            # Join all these characters with spaces and add a new line
            board_str += ' '.join(row_str) + '\n'
        return board_str # Return the completed string representation
        
    # This function looks for an empty cell (represented by 0) in the puzzle
    def find_empty_cell(self):
        # Look through each row and its contents
        for row, contents in enumerate(self.board):
            try:
                # Try to find a zero (empty cell) in this row
                col = contents.index(0)
                # If found, return the position (row, column)
                return row, col
            except ValueError:
                # If no zero in this row, just continue to the next row
                pass
        # If we went through all rows and found no zeros, return None
        # This means the puzzle is completely filled
        return None

    # This function checks if a number can be placed in a specific row
    def valid_in_row(self, row, num):
        # Return True if the number is not already in the row
        return num not in self.board[row]

    # This function checks if a number can be placed in a specific column
    def valid_in_col(self, col, num):
        # Check each row at the specific column position
        # If ALL cells in that column don't have the number, return True
        return all(self.board[row][col] != num for row in range(9))

    # This function checks if a number can be placed in a 3x3 square
    def valid_in_square(self, row, col, num):
        # Find the top-left corner of the 3x3 square that contains the cell
        row_start = (row // 3) * 3  # Integer division to get 0, 3, or 6
        col_start = (col // 3) * 3  # Integer division to get 0, 3, or 6
        
        # Check every cell in the 3x3 square
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                # If the number is already in the square, return False
                if self.board[row_no][col_no] == num:
                    return False
        # If the number is not found in the square, return True
        return True

    # This function combines all three checks to see if a number can be placed in a cell
    def is_valid(self, empty, num):
        # Unpack the row and column from the empty cell position
        row, col = empty
        # Check if the number works in the row
        valid_in_row = self.valid_in_row(row, num)
        # Check if the number works in the column
        valid_in_col = self.valid_in_col(col, num)
        # Check if the number works in the 3x3 square
        valid_in_square = self.valid_in_square(row, col, num)
        # Return True only if ALL three checks pass
        return all([valid_in_row, valid_in_col, valid_in_square])

    # This function solves the Sudoku puzzle using a strategy called "backtracking"
    def solver(self):
        # Find the next empty cell. The := is a special operator that assigns and returns a value
        # If there are no empty cells (None), the puzzle is solved!
        if (next_empty := self.find_empty_cell()) is None:
            return True
            
        # Try each number from 1 to 9 in the empty cell
        for guess in range(1, 10):
            # Check if this number is valid in this position
            if self.is_valid(next_empty, guess):
                # If valid, put the number in the cell
                row, col = next_empty
                self.board[row][col] = guess
                
                # Now recursively try to solve the rest of the puzzle
                if self.solver():
                    # If the recursive call succeeds, the whole puzzle is solved!
                    return True
                    
                # If we get here, the current guess didn't work out
                # Reset the cell back to empty (0) and try the next number
                self.board[row][col] = 0
                
        # If no number from 1-9 works in this cell, something is wrong earlier
        # Return False to trigger backtracking
        return False

# This function is the main entry point for solving a Sudoku puzzle
def solve_sudoku(board):
    # Create a Board object with the puzzle
    gameboard = Board(board)
    # Print the original puzzle
    print(f'Puzzle to solve:\n{gameboard}')
    
    # Try to solve the puzzle
    if gameboard.solver():
        # If solved, print the solution
        print(f'Solved puzzle:\n{gameboard}')
    else:
        # If not solvable, print an error message
        print('The provided puzzle is unsolvable.')
        
    # Return the board (either solved or in its current state)
    return gameboard

# Here's an example Sudoku puzzle to solve
# 0 represents empty cells
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

# Call the function to solve the puzzle
solve_sudoku(puzzle)