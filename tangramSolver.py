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
        self.puzzle = grid              # The tangram puzzle
        self.puzzleWidth = len(grid[0])    # The X
        self.puzzleHeight = len(grid)    # The Y


        self.availablePieces = []
        for x in pieces:
            self.availablePieces.append(Tangram(x))
        self.counter = 0                # The number of choices
        self.emptyCells = 0             # The number of cells to fill

    # To check if two states are the same, we compare the puzzles' completion
    def equals(self, state):
        return self.puzzle == state.puzzle

    # Equivalent to printing, but specific to a state
    def show(self):
        for row in self.puzzle:
            for cell in row:
                if cell == -1:
                    print ' '       # Empty spaces remain empty
                else:
                    print 'Y'       # Eventually print the piece's number

    # Defines the cost of the state
    def cost(self, action):
        return 1

    # Defines the goal conditions
    def goal(self):
        # If there are no more available pieces and there are no more empty spaces.
        if not self.availablePieces and self.emptyCells == 0:
            return True
        return False

    # Defines the effects of the actions
    def executeAction(self, (action,x,y)):
        self.counter += 1

    # Defines the possible actions depending on the situation
    def possibleActions(self):
        actions = []
        # We go through each empty space of the puzzle
        for i in range(self.puzzleWidth):
            for j in range(self.puzzleHeight):
                # If the spot is empty
                if self.puzzle[i][j] == ' ':
                    # For each piece available
                    for currentPiece in self.availablePieces:
                        if currentPiece.getAvailable():
                            # For each orientation of the piece
                            for orientation in range(len(currentPiece)):
                                # Check if the piece fits
                                if self.pieceFits(currentPiece[orientation], i, j):
                                    currentPiece.setAvailable(False)    # Need to check if it does what it says
                                    actions.append((currentPiece[orientation], i, j))
        return actions

    # Determines if a given piece fits in a given area of the puzzle
    def pieceFits(self, (piece, x, y)):
        #Check if the top left corner of the piece fits in x,y
        if piece[0][0] == self.puzzle[y][x]:
            #if the top left corner fits, check the other coordinates of the piece
            for i in range(piece.dimY):
                for j in range(piece.dimX):
                    if piece[i][j] != self.puzzle[y+i][x+j]:
                        return False
            return True
        return False

