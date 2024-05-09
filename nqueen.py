class NQueens:
    def __init__(self, n):
        self.n = n
        self.columns = [-1] * n  # To store column positions of queens
        self.solutions = []
    
    def is_safe(self, row, col):
        """ Check if placing a queen at (row, col) is safe """
        return all(col != self.columns[r] and abs(row - r) != abs(col - self.columns[r]) for r in range(row))
    
    def solve(self, row):
        """ Backtracking or Branch and Bound approach to solve the n-queens problem """
        if row == self.n:
            self.solutions.append(self.columns[:])  # Found a valid placement for all queens
            return
        
        for col in range(self.n):
            if self.is_safe(row, col):
                self.columns[row] = col
                self.solve(row + 1)
                self.columns[row] = -1
    
    def print_solutions(self):
        """ Print all solutions found """
        for solution in self.solutions:
            board = [['.' for _ in range(self.n)] for _ in range(self.n)]
            for row, col in enumerate(solution):
                board[row][col] = 'Q'
            for row in board:
                print(' '.join(row))
            print()
        print(f"Total solutions found: {len(self.solutions)}")

if __name__ == "__main__":
    n = int(input("Enter the number of queens (n): "))
    queens = NQueens(n)
    
    solving_method = input("Choose solving method (backtracking / branch_and_bound): ").strip().lower()
    
    if solving_method == "backtracking" or solving_method == "branch_and_bound":
        queens.solve(0)
    else:
        print("Invalid solving method specified.")
        exit(1)
    
    queens.print_solutions()
