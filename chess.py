def can_place(board, row, col):
    for r in range(row):
        if board[r] == col or \
                board[r] - r == col - row or \
                board[r] + r == col + row:
            return False
    return True

def solve(board, row=0, solutions=[]):
    if row == 8:
        solutions.append(board[:])
    else:
        for col in range(8):
            if can_place(board, row, col):
                board[row] = col
                solve(board, row+1, solutions)

def print_board(board, num, file):
    file.write(f"Solution {num}\n")
    file.write("+" + "---+" * 8 + "\n")
    for row in range(8):
        line = "|"
        for col in range(8):
            if board[row] == col:
                line += " H |"
            else:
                line += "   |"
        file.write(line + "\n")
        file.write("+" + "---+" * 8 + "\n")
    file.write("\n")

board = [-1] * 8
solutions = []
solve(board, 0, solutions)

with open(r"D:\solutions.txt", "w") as file:
    for i, solution in enumerate(solutions):
        print_board(solution, i+1, file)
