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
        self.puzzle = grid      # The tangram puzzle
        self.availablePieces = []
        for x in pieces:
            self.availablePieces.append(Tangram(x))
        self.counter = 0        # The number of choices
        self.emptyCells = 0     # The number of cells to fill

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
