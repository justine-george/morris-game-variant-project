# Author: Justine George - JXG210092 - CS 6364 - 0U2 - Su23

# Part III.b MiniMaxGameBlack

import sys

from Utils import (
    drawBoard,
    flipBoard,
    flipBoardList,
    generateMovesMidgameEndgame,
    getBlackPieceCount,
    getWhitePieceCount,
)

# global variables
countStaticEstimate = 0


# Max min
def maxMin(b, currentDepth):
    # if leaf node
    if currentDepth == maxDepth:
        # get black moves
        tempb = flipBoard(b)
        Ltemp = generateMovesMidgameEndgame(tempb)
        L = flipBoardList(Ltemp)

        return (getStaticEstimationMidgameEndgame(b, L), b)
    else:
        v = float("-inf")

        # get white moves
        L = generateMovesMidgameEndgame(b)

        # for each position after a possible white move
        bestB = ""
        for y in L:
            (estimate, _) = minMax(y, currentDepth + 1)
            if estimate > v:
                v = estimate
                bestB = y
        return (v, bestB)


# Min max
def minMax(b, currentDepth):
    # if leaf node
    if currentDepth == maxDepth:
        # get black moves
        tempb = flipBoard(b)
        Ltemp = generateMovesMidgameEndgame(tempb)
        L = flipBoardList(Ltemp)

        return (getStaticEstimationMidgameEndgame(b, L), b)
    else:
        v = float("inf")

        # get black moves
        tempb = flipBoard(b)
        Ltemp = generateMovesMidgameEndgame(tempb)
        L = flipBoardList(Ltemp)

        # for each position after a possible black move
        bestB = ""
        for y in L:
            (estimate, _) = maxMin(y, currentDepth + 1)
            if estimate < v:
                v = estimate
                bestB = y
        return (v, bestB)


# Static estimation for MidgameEndgame
# L - the MidgameEndgame positions generated from b by a black move
def getStaticEstimationMidgameEndgame(b, L):
    global countStaticEstimate
    countStaticEstimate += 1
    numWhitePieces = getWhitePieceCount(b)
    numBlackPieces = getBlackPieceCount(b)
    numBlackMoves = len(L)

    if numBlackPieces <= 2:
        return 10000
    elif numWhitePieces <= 2:
        return -10000
    elif numBlackMoves == 0:
        return 10000
    else:
        return 1000 * (numWhitePieces - numBlackPieces) - numBlackMoves


# helper methods
def getMaxminEstimate(inputB):
    return minMax(inputB, 0)


# ##################################################################################

# sys.argv[1:] contains command line arguments
inputFile = sys.argv[1]
outputFile = sys.argv[2]
maxDepth = int(sys.argv[3])

# read contents from the input file
inputB = ""
with open(inputFile, "r") as f:
    inputB = inputB + f.read()

print("Input:")
drawBoard(inputB)

# calculate Minimax estimate
(estimate, bestB) = getMaxminEstimate(inputB)

print("\nOutput:")
drawBoard(bestB)

# write into the output file
with open(outputFile, "w") as opFile:
    opFile.write("Board Position: " + bestB)
    opFile.write(
        "\nPositions evaluated by static estimation: " + str(countStaticEstimate) + "."
    )
    opFile.write("\nMINIMAX estimate: " + str(estimate) + ".")
