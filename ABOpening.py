# Author: Justine George - JXG210092 - CS 6364 - 0U2 - Su23

# Part II.a Alpha-Beta Opening

import sys

from Utils import (
    drawBoard,
    flipBoard,
    flipBoardList,
    generateMovesOpening,
    getBlackPieceCount,
    getWhitePieceCount,
)

# global variables
countStaticEstimate = 0


# Max min
def maxMin(b, alpha, beta, currentDepth):
    # if leaf node
    if currentDepth == maxDepth:
        return (getStaticEstimationOpening(b), b)
    else:
        v = float("-inf")

        # get white moves
        L = generateMovesOpening(b)

        # for each position after a possible white move
        bestB = ""
        for y in L:
            (estimate, _) = minMax(y, alpha, beta, currentDepth + 1)
            if estimate > v:
                v = estimate
                bestB = y
                if v >= beta:
                    return (v, bestB)
                else:
                    alpha = max(v, alpha)
        return (v, bestB)


# Min max
def minMax(b, alpha, beta, currentDepth):
    # if leaf node
    if currentDepth == maxDepth:
        return (getStaticEstimationOpening(b), b)
    else:
        v = float("inf")

        # get black moves
        tempb = flipBoard(b)
        Ltemp = generateMovesOpening(tempb)
        L = flipBoardList(Ltemp)

        # for each position after a possible black move
        bestB = ""
        for y in L:
            (estimate, _) = maxMin(y, alpha, beta, currentDepth + 1)
            if estimate < v:
                v = estimate
                bestB = y
                if v <= alpha:
                    return (v, bestB)
                else:
                    beta = min(v, beta)
        return (v, bestB)


# Static estimation for Opening
def getStaticEstimationOpening(b):
    global countStaticEstimate
    countStaticEstimate += 1
    return getWhitePieceCount(b) - getBlackPieceCount(b)


# helper methods
# alpha-beta
def getMaxminEstimate(inputB):
    return maxMin(inputB, float("-inf"), float("inf"), 0)


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
