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
        self.puzzleWidth = len(grid[0])  # The columns
        self.puzzleHeight = len(grid)    # The rows
        self.availablePieces = []
        count = 0
        for x in pieces:
            pieceId = [Tangram(x), count]
            self.availablePieces.append(pieceId)
            count += 1
        self.counter = 0                # The number of choices
        self.emptyCells = 0             # The number of cells to fill
        for i in range(self.puzzleHeight):
            self.emptyCells += self.puzzle[i].count('*')

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

    # Defines the effects of the actions
    def executeAction(self,(row,cell,orientation, id)):
        self.counter += 1
        # For each space of the piece
        for piece in self.availablePieces:
            if id == piece[1]:
                config = piece[0].getOrientations()[orientation]
                for pieceRow in range(len(config)):
                    for pieceCell in range(len(config[0])):
                        if config[pieceRow][pieceCell] == '*':
                            puzzleRow = pieceRow + row
                            puzzleCell = pieceCell + cell
                            self.puzzle[puzzleRow][puzzleCell] = id
                            self.emptyCells -= 1
                self.availablePieces.remove(piece)
        # self.availablePieces.remove(self.availablePieces[id])

    # Defines the possible actions depending on the situation
    def possibleActions(self):
        actions = []
        copyAvailablePieces = list(self.availablePieces)
        # We go through each space of the puzzle
        for row in range(self.puzzleHeight):
            for cell in range(self.puzzleWidth):
                if self.puzzle[row][cell] == '*':
                # For each piece available
                    for currentPiece in copyAvailablePieces:
                        # For each orientation of the piece
                        for orientation in range(len(currentPiece[0].getOrientations())):
                            # Check if the piece fits
                            if self.pieceFits((currentPiece[0].getOrientations()[orientation], row, cell)):
                                actions.append((row, cell,orientation, currentPiece[1]))
                                copyAvailablePieces.remove(currentPiece)
                                break

        return actions

    # Defines the goal conditions
    def isGoal(self):
        # If there are no more available pieces and there are no more empty spaces.
        return self.emptyCells == 0

    # Defines the cost of the state
    def cost(self, action):
        return 1

    def heuristic(self):
        return 0

    # Determines if a given piece fits in a given area of the puzzle
    def pieceFits(self, (piece, puzzleRow, puzzleCell)):
        #Check if the top left corner of the piece fits in x,y
        if piece[0][0] == self.puzzle[puzzleRow][puzzleCell] or piece[0][0] == ' ':
            #if the top left corner fits, check the other coordinates of the piece
            for i in range(len(piece)):
                for j in range(len(piece[0])):
                    if piece[i][j] == '*' and self.puzzle[puzzleRow+i][puzzleCell+j] != '*':
                        return False
            return True
        return False


# Tests


piece0 = [['*', ' '],['*','*'],['*','*']]
piece1 = [['*', ' '],['*','*'],['*',' ']]
piece2 = [[' ', '*'],['*','*'],['*',' ']]
piece3 = [[' ', '*'],['*','*'],['*',' ']]
piece4 = [[' ', '*'],[' ','*'],['*','*']]
piece5 = [[' ', '*'],[' ','*'],['*','*']]
piece6 = [[' ', '*'],[' ','*'],['*','*']]
piece7 = [[' ', '*'],[' ','*'],['*','*']]
piece8 = [['*'],['*']]
piece9 = [['*'],['*']]
piece10 = [['*'],['*']]
piece11 = [['*'],['*']]
piece12 = [['*', ' '],['*',' '],['*','*']]
piece13 = [['*', ' '],['*',' '],['*','*']]
piece14 = [['*', ' '],['*',' '],['*','*']]
piece15 = [['*', '*'],['*','*'],['*','*']]
piece16 = [['*', '*'],['*','*'],['*','*']]
piece17 = [['*', '*'],['*','*'],['*','*']]
piece18 = [['*', '*'],['*','*'],['*','*']]
piece19 = [['*', '*'],['*','*'],['*','*']]
piece20 = [['*', '*'],['*','*'],['*','*']]
piece21 = [['*']]
piece22 = [['*']]
piece23 = [['*']]
piece24 = [['*']]
piece25 = [['*']]
piece26 = [['*']]
piece27 = [['*']]
pieces = [piece0, piece1, piece2, piece3, piece4,
 piece5, piece6, piece7, piece8, piece9,
 piece10, piece11, piece12, piece13, piece14,
 piece15, piece16, piece17, piece18, piece19,
 piece20, piece21, piece22, piece23, piece24,
 piece25, piece26, piece27]

# columns : 17
# rows : 9
pattern = [
 [' ',' ','*','*',' ',' ','*','*',' ',' ',' ','*','*','*','*','*','*'],
 [' ',' ','*','*',' ',' ','*','*',' ',' ',' ','*','*','*','*','*','*'],
 [' ','*','*','*','*','*','*','*','*',' ',' ','*','*',' ',' ',' ',' '],
 [' ','*','*','*','*','*','*','*','*',' ',' ','*','*',' ',' ',' ',' '],
 ['*','*',' ',' ','*','*',' ',' ','*','*',' ','*','*',' ','*','*','*'],
 ['*','*',' ',' ','*','*',' ',' ','*','*',' ','*','*',' ','*','*','*'],
 ['*','*',' ',' ','*','*',' ',' ','*','*',' ','*','*',' ',' ','*','*'],
 ['*','*',' ',' ','*','*',' ',' ','*','*',' ','*','*','*','*','*','*'],
 ['*','*',' ',' ','*','*',' ',' ','*','*',' ','*','*','*','*','*','*']
]

a = TangramSolver(pattern,pieces)
b = TangramSolver([['*','*'],['*','*']],
                  [     [['*',' '],['*','*']],
                        [['*']]
                  ])
print "Test tangram b"
astar_search(b)
c = TangramSolver([['*','*'],['*','*'],['*','*']],
                  [     [['*'],['*']],
                        [['*'],['*']],
                        [['*']],
                        [['*']]
                  ])
print "Test tangram c"
astar_search(c)
d = TangramSolver([['*','*'],['*','*'],['*','*']],
                  [     [['*',' '],['*','*']],
                        [['*',' '],['*','*']],
                    ])
print "Test tangram d"
astar_search(d)
e = TangramSolver([['*','*'],['*','*'],['*','*']],
                  [     [['*',' '],['*','*'],['*','*']],
                        [['*']],
                    ])
print "Test tangram e"
astar_search(e)
f = TangramSolver([['*','*'],['*','*'],['*','*']],
                  [     [['*','*'],['*','*']],
                        [['*','*']],

                ])
print "Test tangram f"
astar_search(f)
g = TangramSolver([['*','*'],['*','*'],['*','*']],
                  [     [['*','*'],['*','*']],
                        [['*','*']],

                ])
print "Test tangram g"
astar_search(g)