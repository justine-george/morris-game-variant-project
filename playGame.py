import ABOpening
import ABGame
from Utils import drawBoard, flipBoard, getBlackPieceCount, getWhitePieceCount

# depth of the min max tree
depth = 3

def game_over(board):
    white_count = getWhitePieceCount(board)
    black_count = getBlackPieceCount(board)
    if white_count <= 2 or black_count <= 2:
        return True
    return False

def get_winner(board):
    white_count = getWhitePieceCount(board)
    black_count = getBlackPieceCount(board)
    if white_count <= 2:
        return "Black"
    elif black_count <= 2:
        return "White"
    return "None"

def play():
    choice = input("Choose your side (w/b): ").lower()
    board = "xxxxxxxxxxxxxxxxxxxxx"  # Assuming 'x' represents an empty position
    total_moves = 0
    isMovesOver = False

    # ABOpening
    while total_moves < 16: # 8 pieces for each player
        if choice == 'w':
            if total_moves % 2 == 0:
                # generate white move and print
                board = getABOpeningBestBoard(board, choice)
                print("White played: ")
            else:
                # input prompt for a black response
                board = input("Enter Black's Response: ")
        elif choice == 'b':
            if total_moves % 2 == 1:
                # generate black move and print
                board = getABOpeningBestBoard(board, choice)
                print("Black played: ")
            else:
                # input prompt for a white response
                board = input("Enter White's Move: ")
        print(board)
        drawBoard(board)
        total_moves += 1

    # ABGame
    print("Enters Midgame!")
    while not game_over(board):
        if choice == 'w':
            if total_moves % 2 == 0:
                # generate white move and print
                board = getABGameBestBoard(board, choice)
                print("White played: ")
            else:
                # input prompt for a black response
                board = input("Enter Black's Response: ")
        elif choice == 'b':
            if total_moves % 2 == 1:
                # generate black move and print
                board = getABGameBestBoard(board, choice)
                print("Black played: ")
            else:
                # input prompt for a white response
                board = input("Enter White's Move: ")
        print(board)
        drawBoard(board)
        total_moves += 1
        if (total_moves == 60):
            isMovesOver = True
            break
    
    if isMovesOver:
        print("60 moves done, Black wins!")

    # game is over
    winner = get_winner(board)
    if winner == "None":
        print("It's a draw!")
    else:
        print(f"{winner} wins!")


# get best board position for the opening using alpha-beta pruning
def getABOpeningBestBoard(b, choice):
    if choice == 'w':
        # generate white move and print
        _, board = ABOpening.getMaxminEstimate(b, depth)
        return board
    else:
        flippedB = flipBoard(b)
        _, bestB = ABOpening.getMaxminEstimate(flippedB, depth)
        board = flipBoard(bestB)
        return board


# get best board position for the midgame using alpha-beta pruning
def getABGameBestBoard(b, choice):
    if choice == 'w':
        # generate white move and print
        _, board = ABGame.getMaxminEstimate(b, depth)
        return board
    else:
        flippedB = flipBoard(b)
        _, bestB = ABGame.getMaxminEstimate(flippedB, depth)
        board = flipBoard(bestB)
        return board


# start the game
play()