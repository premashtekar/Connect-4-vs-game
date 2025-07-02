import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]
rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵":
                print("", gameBoard[x][y], end=" |")
            elif gameBoard[x][y] == "🔴":
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
        print()
    print("   +----+----+----+----+----+----+----+")

def modifyTurn(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

def get_column_index(letter):
    return possibleLetters.index(letter.upper())

def find_lowest_empty_row(col):
    for row in range(rows - 1, -1, -1):
        if gameBoard[row][col] == "":
            return row
    return -1

def check_winner(player):
    # Check horizontal
    for r in range(rows):
        for c in range(cols - 3):
            if all(gameBoard[r][c + i] == player for i in range(4)):
                return True

    # Check vertical
    for r in range(rows - 3):
        for c in range(cols):
            if all(gameBoard[r + i][c] == player for i in range(4)):
                return True

    # Check diagonal (positive slope)
    for r in range(rows - 3):
        for c in range(cols - 3):
            if all(gameBoard[r + i][c + i] == player for i in range(4)):
                return True

    # Check diagonal (negative slope)
    for r in range(3, rows):
        for c in range(cols - 3):
            if all(gameBoard[r - i][c + i] == player for i in range(4)):
                return True
    return False

def is_board_full():
    return all(gameBoard[0][c] != "" for c in range(cols))

turnCounter = 0
while True:
    printGameBoard()
    current_player = "🔵" if turnCounter % 2 == 0 else "🔴"
    player_name = "Player 1 (Blue)" if current_player == "🔵" else "Player 2 (Red)"

    while True:
        move = input(f"{player_name}, choose a column (A-G): ").upper()
        if move not in possibleLetters:
            print("Invalid input. Please choose a column A-G.")
            continue

        col = get_column_index(move)
        row = find_lowest_empty_row(col)
        if row == -1:
            print("Column is full. Choose another column.")
            continue

        modifyTurn((row, col), current_player)
        break

    if check_winner(current_player):
        printGameBoard()
        print(f"{player_name} wins!")
        break

    if is_board_full():
        printGameBoard()
        print("It's a draw!")
        break

    turnCounter += 1
