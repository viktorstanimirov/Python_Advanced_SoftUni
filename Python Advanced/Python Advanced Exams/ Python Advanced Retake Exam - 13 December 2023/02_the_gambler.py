def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def find_player(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'G':
                return i, j


def move_player(matrix, direction):
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    row, col = find_player(matrix)
    matrix[row][col] = '-'

    row_move, col_move = directions[direction]
    new_row, new_col = row + row_move, col + col_move

    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix):
        return new_row, new_col

    return row, col


size = int(input())
matrix = [list(input()) for _ in range(size)]

total_amount = 100
jackpot_won = False

while True:
    command = input()
    if command == 'end':
        break

    row, col = move_player(matrix, command)

    if matrix[row][col] == 'W':
        total_amount += 100
    elif matrix[row][col] == 'P':
        total_amount -= 200
        if total_amount <= 0:
            print("Game over! You lost everything!")
            exit()
    elif matrix[row][col] == 'J':
        jackpot_won = True
        total_amount += 1000
        break

    matrix[row][col] = 'G'


if jackpot_won:
    print(f"You win the Jackpot!\nEnd of the game. Total amount: {total_amount}$")
else:
    print(f"End of the game. Total amount: {total_amount}$")

print_matrix(matrix)