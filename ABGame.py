# Author: Justine George - JXG210092 - CS 6364 - 0U2 - Su23

# Part II.b Alpha-Beta Game

import sys

from Utils import (
    drawBoard,
    generateMovesMidgameEndgame,
    getBlackMovesMidgameEndgame,
    getBlackPieceCount,
    getMaxDepth,
    getMillCount,
    getMobilityCount,
    getPositionScore,
    getScoreForMetrics,
    getWhitePieceCount,
)

# global variables
countStaticEstimate = 0
maxDepth = getMaxDepth()

# Max min
def maxMin(b, alpha, beta, currentDepth):
    # if leaf node
    if currentDepth == maxDepth:
        # get black moves
        L = getBlackMovesMidgameEndgame(b)

        return (getStaticEstimationMidgameEndgame(b, L), b)
    else:
        v = float("-inf")

        # get white moves
        L = generateMovesMidgameEndgame(b)

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
        # get black moves
        L = getBlackMovesMidgameEndgame(b)

        return (getStaticEstimationMidgameEndgame(b, L), b)
    else:
        v = float("inf")

        # get black moves
        L = getBlackMovesMidgameEndgame(b)

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


# Static estimation for MidgameEndgame
# L - the MidgameEndgame positions generated from b by a black move
def getStaticEstimationMidgameEndgame(b, L):
    global countStaticEstimate
    countStaticEstimate += 1

    # number of black moves
    numBlackMoves = len(L)

    # pieceCount
    whitePieceCount = getWhitePieceCount(b)
    blackPieceCount = getBlackPieceCount(b)

    # millCount
    whiteMillCount = getMillCount(b, "W")
    blackMillCount = getMillCount(b, "B")

    # mobilityCount
    whiteMobilityCount = getMobilityCount(b, "W")
    blackMobilityCount = getMobilityCount(b, "B")

    # positionscore
    whiteScore = getPositionScore(b, "W")
    blackScore = getPositionScore(b, "B")

    # other metrics
    # otherScoreW = getScoreForMetrics(b, "W")
    # otherScoreB = getScoreForMetrics(b, "B")

    if blackPieceCount <= 2:
        return 100000
    elif whitePieceCount <= 2:
        return -100000
    elif numBlackMoves == 0:
        return 100000
    else:
        # Calculate delta values
        delta_piece_count = (whitePieceCount - blackPieceCount) / 3
        delta_mill_count = (whiteMillCount - blackMillCount) / 6
        delta_mobility_count = (whiteMobilityCount - blackMobilityCount) / 15
        delta_position_score = (whiteScore - blackScore) / 12
        # numBlackMoves = numBlackMoves / 2
        # delta_other_score = otherScoreW - otherScoreB

        # Save delta values to files
        with open("midgame/delta_piece_count_midgame_endgame.txt", "a") as f:
            f.write(str(delta_piece_count) + ",")
        with open("midgame/delta_mill_count_midgame_endgame.txt", "a") as f:
            f.write(str(delta_mill_count) + ",")
        with open("midgame/delta_mobility_count_midgame_endgame.txt", "a") as f:
            f.write(str(delta_mobility_count) + ",")
        with open("midgame/delta_position_score_midgame_endgame.txt", "a") as f:
            f.write(str(delta_position_score) + ",")
        with open("midgame/number_black_moves.txt", "a") as f:
            f.write(str(numBlackMoves) + ",")

        return (
            delta_piece_count
            + delta_mill_count
            + delta_mobility_count
            + delta_position_score
            # + delta_other_score
            - numBlackMoves
        )


# helper methods
# alpha-beta
def getMaxminEstimate(inputB, depth):
    global maxDepth
    maxDepth = depth
    return maxMin(inputB, float("-inf"), float("inf"), 0)


# ##################################################################################

# # sys.argv[1:] contains command line arguments
# inputFile = sys.argv[1]
# outputFile = sys.argv[2]
# maxDepth = int(sys.argv[3])

# # read contents from the input file
# inputB = ""
# with open(inputFile, "r") as f:
#     inputB = inputB + f.read()

# print("\nInput:")
# drawBoard(inputB)

# # calculate Minimax estimate
# (estimate, bestB) = getMaxminEstimate(inputB)

# print("\nOutput:")
# drawBoard(bestB)

# # write into the output file
# with open(outputFile, "w") as opFile:
#     opFile.write("Board Position: " + bestB)
#     opFile.write(
#         "\nPositions evaluated by static estimation: " + str(countStaticEstimate) + "."
#     )
#     opFile.write("\nMINIMAX estimate: " + str(estimate) + ".")
#     print(
#         "\nPositions evaluated by static estimation: " + str(countStaticEstimate) + "."
#     )
#     print("MINIMAX estimate: " + str(estimate) + ".\n")
