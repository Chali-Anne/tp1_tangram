from astar_search import *

class Tangram(object):
    def __init__(self, piece):
        self.counter = 0
        self.pieceOrigin = piece
        self.orientations = []
        self.dimX = len(piece)
        self.dimY = len(piece[0])

    def isFull(self):
        return self.dimX*self.dimY == sum(x.count('*') for x in self.pieceOrigin)

    def possibleOrientation(self):
        if self.dimX == self.dimY and self.isFull():
            self.orientations.append(self.pieceOrigin)
            return
        else:
            self.orientations.append(self.pieceOrigin)
            rotation90 = zip(*self.pieceOrigin[::-1])
            rotation180 = zip(*rotation90[::-1])
            rotation270 = zip(*rotation180[::-1])
            if rotation90 == self.pieceOrigin:
                return
            elif rotation90 != self.pieceOrigin and rotation90 != rotation270:
                self.orientations.extend((rotation90, rotation180, rotation270))
            elif self.pieceOrigin == rotation180:
                self.orientations.extend((rotation90))
            else:
                return

    def show(self):
        for row in self.grid:
            for cell in row:
                if cell != 0:
                    print '*',
                else:
                    print '{:2}'.format(cell),
            print

a = [['*','*','*'],['*','*','*']]
print a