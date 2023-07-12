# Author: Justine George - JXG210092 - CS 6364 - 0U2 - Su23

# Part III.a MiniMaxOpeningBlack

import sys

from MoveGenerator import (
    flipBoard,
    flipBoardList,
    generateMovesOpening,
    getBlackPieceCount,
    getWhitePieceCount,
)

# global variables
countStaticEstimate = 0


# Max min
def maxMin(b, currentDepth):
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
            (estimate, _) = minMax(y, currentDepth + 1)
            if estimate > v:
                v = estimate
                bestB = y
        return (v, bestB)


# Min max
def minMax(b, currentDepth):
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
            (estimate, _) = maxMin(y, currentDepth + 1)
            if estimate < v:
                v = estimate
                bestB = y
        return (v, bestB)


# ##################################################################################


# Static estimation for Opening
def getStaticEstimationOpening(b):
    global countStaticEstimate
    countStaticEstimate += 1
    return getWhitePieceCount(b) - getBlackPieceCount(b)


# helper methods
def getMinmaxEstimate(inputB):
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

print(inputB)
# calculate Minimax estimate
(estimate, bestB) = getMinmaxEstimate(inputB)
print(bestB)

# write into the output file
with open(outputFile, "w") as opFile:
    opFile.write("Board Position: " + bestB)
    opFile.write(
        "\nPositions evaluated by static estimation: " + str(countStaticEstimate) + "."
    )
    opFile.write("\nMINIMAX estimate: " + str(estimate) + ".")
