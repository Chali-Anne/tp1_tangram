# -*- coding: utf-8 -*-
#
#  Class TangramSolver
# Author: Chali-Anne Lauzon
#         École Polytechnique de Montréal
#
# This class solves a tangram puzzle using a tree search

from astar_search import *
from tangram import *

class TangramSolver(object):
    def __init__(self, grid, pieces):
        self.puzzle = grid      # The tangram puzzle
        self.availablePieces = []
        for x in pieces:
            self.availablePieces.append(Tangram(x))