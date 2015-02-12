# -*- coding: utf-8 -*-
#
#  Class Tangram
# Author: Marie-France Miousse
#         École Polytechnique de Montréal
#
# This class represents a tangram piece

class Tangram(object):
    def __init__(self, piece):
        self.dimX = len(piece[0])   # Length
        self.dimY = len(piece)      # Height
        self.available = True       # A boolean to check if the piece has been used
        self.pieceOrigin = piece    # The original array that represents the piece
        self.orientations = []      # All of the possible orientations of the starting piece
        self.possibleOrientation()

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

    def show(self):
        for row in self.pieceOrigin:
            for cell in row:
                if cell == '*':
                    print '*',
                else:
                    print ' ',
            print

    def getAvailable(self):
        return self.available

    # Sets if the piece has been used or not
    def setAvailable(self, available):
        self.available = available

    def getOrientations(self):
        return self.orientations