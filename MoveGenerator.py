# Author: Justine George - JXG210092 - CS 6364 - 0U2 - Su23

# Move generator for Morris Variant


def generateMovesOpening(b):
    return generateAdd(b)


def generateMovesMidgameEndgame(b):
    # if the board has 3 white pieces
    if getWhitePieceCount(b) == 3:
        return generateHopping(b)
    return generateMove(b)


def generateAdd(b):
    L = []
    # for each location on the board
    for location in range(len(b)):
        if b[location] == "x":
            # copy board, updating b[location] with "W"
            bList = list(b)
            bList[location] = "W"
            bCopy = "".join(bList)
            if closeMill(location, bCopy):
                generateRemove(bCopy, L)
            else:
                L.append(bCopy)
    return L


def generateHopping(b):
    L = []
    # for each location m on the board
    for m in range(len(b)):
        if b[m] == "W":
            # for each location n on the board
            for n in range(len(b)):
                if b[n] == "x":
                    # copy board, updating b[m] with "x" and b[n] with "W"
                    bList = list(b)
                    bList[m] = "x"
                    bList[n] = "W"
                    bCopy = "".join(bList)
                    if closeMill(n, bCopy):
                        generateRemove(bCopy, L)
                    else:
                        L.append(bCopy)
    return L


def generateMove(b):
    L = []
    # for each location on the board
    for location in range(len(b)):
        if b[location] == "W":
            # find neighbors
            n = getNeighborsList(location)
            for j in range(len(n)):
                if b[n[j]] == "x":
                    # copy board, updating b[location] with "x" and new position with "W"
                    bList = list(b)
                    bList[location] = "x"
                    bList[n[j]] = "W"
                    bCopy = "".join(bList)
                    if closeMill(n[j], bCopy):
                        generateRemove(bCopy, L)
                    else:
                        L.append(bCopy)
    return L


def generateRemove(b, L):
    # for each location on the board
    isPositionAdded = False
    for location in range(len(b)):
        if b[location] == "B":
            if not closeMill(location, b):
                bList = list(b)
                bList[location] = "x"
                bCopy = "".join(bList)
                L.append(bCopy)
                isPositionAdded = True
    if not isPositionAdded:
        L.append(b)


def getNeighborsList(j):
    neighbors = {
        0: [1, 6],
        1: [0, 11],
        2: [3, 7],
        3: [2, 10],
        4: [5, 8],
        5: [4, 9],
        6: [0, 7, 18],
        7: [2, 6, 8, 15],
        8: [4, 7, 12],
        9: [5, 10, 14],
        10: [3, 9, 11, 17],
        11: [1, 10, 20],
        12: [8, 13],
        13: [12, 14, 16],
        14: [9, 13],
        15: [7, 16],
        16: [13, 15, 17, 19],
        17: [10, 16],
        18: [6, 19],
        19: [16, 18, 20],
        20: [11, 19],
    }
    return neighbors[j]


def closeMill(j, b):
    c = b[j]  # C is either "B" or "W"
    mill_positions = {
        0: [(6, 18)],
        1: [(11, 20)],
        2: [(7, 15)],
        3: [(10, 17)],
        4: [(8, 12)],
        5: [(9, 14)],
        6: [(0, 18), (7, 8)],
        7: [(6, 8), (2, 15)],
        8: [(6, 7), (4, 12)],
        9: [(10, 11), (5, 14)],
        10: [(9, 11), (3, 17)],
        11: [(9, 10), (1, 20)],
        12: [(4, 8), (13, 14)],
        13: [(12, 14), (16, 19)],
        14: [(12, 13), (5, 9)],
        15: [(2, 7), (16, 17)],
        16: [(15, 17), (13, 19)],
        17: [(15, 16), (3, 10)],
        18: [(0, 6), (19, 20)],
        19: [(13, 16), (18, 20)],
        20: [(18, 19), (1, 11)],
    }
    for position in mill_positions[j]:
        if b[position[0]] == c and b[position[1]] == c:
            return True
    return False


# helper methods
def getWhitePieceCount(b):
    return b.count("W")


def getBlackPieceCount(b):
    return b.count("B")


# invert board colors in the list of boards
def flipBoardList(Ltemp):
    L = []
    for tempb in Ltemp:
        L.append(flipBoard(tempb))
    return L


# invert board color
def flipBoard(board):
    newBoard = ""
    for piece in board:
        if piece == "W":
            newBoard += "B"
        elif piece == "B":
            newBoard += "W"
        else:
            newBoard += piece
    return newBoard


#  returns the number of pieces in mill formation
def getMillCount(b, piece):
    millCount = 0
    for j in range(len(b)):
        if b[j] == piece:
            if closeMill(j, b):
                millCount += 1
    return millCount


# return the mobilityCount of a board
# ie. for a board WxxxxxxxxxxxxxxxBxxxx, W's mobility is 2, B's mobility is 4.
def getMobilityCount(b, piece):
    if piece == "W":
        enemyPiece = "B"
    elif piece == "B":
        enemyPiece = "W"

    mobilityCount = 0
    for j in range(len(b)):
        if b[j] == piece and not closeMill(j, b):
            neighborList = getNeighborsList(j)
            potentialMobility = len(neighborList)
            for neighbor in neighborList:
                if b[neighbor] == enemyPiece:
                    potentialMobility -= 1
                elif b[neighbor] == piece:
                    potentialMobility -= 1
                elif b[neighbor] == "x":
                    potentialMobility -= 0
            mobilityCount += potentialMobility
    return mobilityCount


# get a score based on the position of pieces on the board
def getPositionScore(b, piece):
    positionScore = 0
    for j in range(len(b)):
        if b[j] == piece:
            neighborList = getNeighborsList(j)
            positionScore += len(neighborList)
    return positionScore
