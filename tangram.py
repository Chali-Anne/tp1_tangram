# -*- coding: utf-8 -*-
#
#  Class Tangram
# Author: Marie-France Miousse
#         École Polytechnique de Montréal
#
# This class represents a tangram piece

class Tangram(object):
    def __init__(self, piece):
        self.available = True       # A boolean to check if the piece has been used
        self.pieceOrigin = piece    # The original array that represents the piece
        self.orientations = []      # All of the possible orientations of the starting piece
        self.dimX = len(piece)      # Length
        self.dimY = len(piece[0])   # Height

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
            self.orientations.append(self.pieceOrigin)
            rotation90 = zip(*self.pieceOrigin[::-1])
            rotation180 = zip(*rotation90[::-1])
            rotation270 = zip(*rotation180[::-1])
            # If the first rotation gives the same thing as the original, there is only one possibility
            if rotation90 == self.pieceOrigin:
                return
            # If the first rotation is not the same as the original or the third, all possibilities are unique
            elif rotation90 != self.pieceOrigin and rotation90 != rotation270:
                self.orientations.extend((rotation90, rotation180, rotation270))
            # If the second rotation is the same as the original, there are only two possibilities
            elif self.pieceOrigin == rotation180:
                self.orientations.extend((rotation90))
            else:
                return

    def show(self):
        for row in self.grid:
            for cell in row:
                if cell != 0:
                    print '*'

    def getAvailable(self):
        return self.available

    # Sets if the piece has been used or not
    def setAvailable(self, available):
        self.available = available