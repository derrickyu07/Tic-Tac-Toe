
board = ["1","2","3","4","5","6","7","8","9"]

def printBoard(board):
    print("   |   |   \n " + board[0] + " | " + board[1] + " | " + board[2] + " \n   |   |   ")
    print("-----------")
    print("   |   |   \n " + board[3] + " | " + board[4] + " | " + board[5] + " \n   |   |   ")
    print("-----------")
    print("   |   |   \n " + board[6] + " | " + board[7] + " | " + board[8] + " \n   |   |   \n")

def playerTurn(player, board, num):
    while(True):
        squareNumber = input("Player " + str(num) + " type a number to put your symbol: ")
        try:
            squareNumber = int(squareNumber) - 1
            if not (board[squareNumber] == "X" or board[squareNumber] == "O"):
                board[squareNumber] = player
            else:
                print("There is already a symbol at that location.")
                continue
            break
        except:
            print("Invalid Input")
            continue

def result(num):
    if any(board[x] == board[x + 1] == board[x + 2] for x in range(0, 7, 3)) or any(board[x] == board[x + 3] == board[x + 6] for x in range(3)) or (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6]):
         return True


def round(board, num, symbol):
    printBoard(board)
    playerTurn(symbol, board, num)
    printBoard(board);
    return result(num)

tieCounter = 0
while True:
    if(round(board, 1, "X")):
        print("player 1 is the winner")
        break
    tieCounter += 1
    if tieCounter == 9:
        print("TIE")
        break
    if(round(board, 2, "O")):
        print("player 2 is the winner")
        break
    tieCounter += 1