# -*- coding: utf-8 -*-
#
#  Class TangramSolver
# Author: Chali-Anne Lauzon
#         École Polytechnique de Montréal
#
# This class solves a tangram puzzle using a tree search

from astar_search import *
from tangram import *
from node import *
from state import *

class TangramSolver(object):
    def __init__(self, grid, pieces):
        self.puzzle = grid               # The tangram puzzle
        self.puzzleWidth = len(grid[0])  # The X
        self.puzzleHeight = len(grid)    # The Y


        self.availablePieces = []
        for x in pieces:
            self.availablePieces.append(Tangram(x))
        self.counter = 0                # The number of choices
        self.emptyCells = 0             # The number of cells to fill
        for i in range(self.puzzleHeight):
            self.emptyCells += self.puzzle[i].count('*')


    def show(self):
        for row in self.pieceOrigin:
            for cell in row:
                if cell == '*':
                    print '*',
                else:
                    print ' ',
            print

    # To check if two states are the same, we compare the puzzles' completion
    def equals(self, state):
        return self.puzzle == state.puzzle

    # Equivalent to printing, but specific to a state
    def show(self):
        for row in self.puzzle:
            for cell in row:
                if cell == -1:
                    print ' ',       # Empty spaces remain empty
                else:
                    print '{:2}'.format(cell),       # Eventually print the piece's number
            print

    # Defines the cost of the state
    def cost(self, action):
        return 1

    def heuristic(self):
        return 0

    # Defines the goal conditions
    def isGoal(self):
        # If there are no more available pieces and there are no more empty spaces.
        if self.emptyCells == 0:
            return True
        return False

    # Defines the effects of the actions
    def executeAction(self, (piece,row,column, index)):
        self.counter += 1

        # For each space of the piece
        for j in range(row,row + len(piece)):
            for i in range(column,column + len(piece[0])):
                self.puzzle[j][i] = index
                self.emptyCells -= 1

    # Defines the possible actions depending on the situation
    def possibleActions(self):
        actions = []
        # We go through each empty space of the puzzle
        for i in range(self.puzzleHeight):
            for j in range(self.puzzleWidth):
                # If the spot is empty
                #if self.puzzle[i][j] != ' ':
                    # For each piece available
                    for index, currentPiece in enumerate(self.availablePieces):
                        if currentPiece.getAvailable():
                            # For each orientation of the piece
                            for orientation in range(len(currentPiece.getOrientations())):
                                # Check if the piece fits
                                if self.pieceFits((currentPiece.getOrientations()[orientation], i, j)):
                                    currentPiece.setAvailable(False)    # Need to check if it does what it says
                                    actions.append((currentPiece.getOrientations()[orientation], i, j, index))
        return actions

    # Determines if a given piece fits in a given area of the puzzle
    def pieceFits(self, (piece, x, y)):
        #Check if the top left corner of the piece fits in x,y
        if piece[0][0] == self.puzzle[y][x]:
            #if the top left corner fits, check the other coordinates of the piece
            for i in range(len(piece)):
                for j in range(len(piece[i])):
                    if piece[i][j] == '*' and piece[i][j] != self.puzzle[y+j][x+i]:
                        return False
            return True
        return False


# Tests
a = TangramSolver([['*','*'],['*','*']],[[['*',' '],['*','*']], [['*']]])
print len(a.availablePieces)
solution = astar_search(a)