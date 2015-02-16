# -*- coding: utf-8 -*-
#
#  Class main
# Author: Chali-Anne Lauzon
#         Marie-France Miousse
#         École Polytechnique de Montréal
#
# This is the main class. It just makes it easier to find.
from tangramPuzzle import *

# This method is mandatory. It is like the «main» of a C++ or Java program.
def search(pattern, pieces):
    temp = TangramPuzzle(pattern, pieces);
    start_time = timeit.default_timer();
    hillclimbing_search(temp);
    elapsed = timeit.default_timer() - start_time;
    print str(elapsed) + " secondes";
    
print "Tests hill-climbing"
pattern1 = [ [' ',' ',' ',' ','*','*',' ',' ',' ',' '],
[' ',' ',' ',' ','*','*',' ',' ',' ',' '],
[' ',' ','*','*','*','*','*','*',' ',' '],
[' ',' ',' ','*','*','*','*',' ',' ',' '],
[' ',' ',' ',' ','*','*',' ',' ',' ',' '],
[' ',' ',' ',' ','*','*',' ',' ',' ',' '],
[' ',' ',' ',' ','*','*',' ',' ',' ',' '],
[' ',' ',' ','*','*','*','*',' ',' ',' '],
[' ','*','*','*','*','*','*','*','*',' ']]
piece0 = [['*',' ',' '],['*','*',' '],['*','*','*']]
piece1 = [['*',' ',' '],['*','*',' '],['*','*','*']]
piece2 = [['*','*'],['*','*']]
piece3 = [['*','*'],['*','*']]
piece4 = [['*','*']]
piece5 = [['*','*']]
piece6 = [['*',' '],['*','*']]
piece7 = [['*',' '],['*','*']]
piece8 = [['*']]
piece9 = [['*']]
pieces = [piece0, piece1, piece2, piece3, piece4, piece5, piece6, piece7, piece8, piece9]
search(pattern1,pieces)