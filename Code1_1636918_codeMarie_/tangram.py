# -*- coding: utf-8 -*-
#
#  Class Tangram
# Author: Chali-Anne Lauzon
#         Marie-France Miousse
#         École Polytechnique de Montréal
#
# This class represents a tangram piece for an A* tree search

class Tangram(object):
    def __init__(self, piece):
        self.dimX = len(piece[0])   # Length
        self.dimY = len(piece)      # Height
        self.pieceOrigin = piece    # The original array that represents the piece
        self.orientations = []      # All of the possible orientations of the starting piece
        self.possibleOrientation()
        self.nbCells = 0
        self.countCells()

    # The key to a tangram piece will be the number of cells it occupies. May change.
    def getKey(tangram):
        return tangram.nbCells

    def __repr__(self):
        return '{} : cells : {}'.format(self.show(),self.nbCells)

    # Check if the array is filled with '*'. If so, it returns true.
    def isFull(self):
        return self.dimX*self.dimY == sum(x.count('*') for x in self.pieceOrigin)

    # Fills the list of possible orientations
    def possibleOrientation(self):
        # If the array is full and is a square, just add the original piece
        if self.dimX == self.dimY and self.isFull():
            self.orientations.append(self.pieceOrigin)
            return
        else:
            temp = zip(*self.pieceOrigin[::-1])
            for i in range(0,4):
                temp = zip(*temp[::-1])
                if not self.orientations.__contains__(temp):
                    self.orientations.append(temp)
            return

    def countCells(self):
        for y in range(self.dimY):
            for x in range(self.dimX):
                if self.pieceOrigin[y][x] == '*':
                    self.nbCells += 1

    def show(self):
        for row in self.pieceOrigin:
            for cell in row:
                if cell == '*':
                    print '*',
                else:
                    print ' ',
            print

    def getOrientations(self):
        return self.orientations
