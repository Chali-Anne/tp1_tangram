# Hill-climbing Search
#
# Author: Michel Gagnon
#         michel.gagnon@polytml.ca

from node import *
from state import *
import random

# We did this in 61 steps in a tree search.
def hillclimbing_search(initialState,maxSteps = 100):
    step = 0
    node = Node(initialState)

    possibleSolutions = []
    candidates = []

    while step < maxSteps:
        if node.state.isGoal():
            node.state.show()
            print 'Steps:', step
            return node
        else:
            candidates = node.expand()
            possibleSolutions = possibleSolutions + candidates

            # If we're stuck at a local minima, we take a random set of 5 previous states we passed.
            if not candidates:
                print "Stuck at step : ", step
                try:
                    candidates = random.sample(possibleSolutions,5)
                except:
                    candidates = possibleSolutions
                # We only keep the solutions that aren't tried more than 2 times.
                possibleSolutions = [x for x in possibleSolutions if x not in candidates]
            try:
                candidates.sort(cmp = lambda n1,n2: -1 if n1.h < n2.h else (1 if n1.h > n2.h else 0))
                node = candidates.pop(0)
            except:
                print "List is empty --> No solution is found"
                node.state.show()
                return None
            step += 1
    node.state.show()
    print "No solution was found"
    return None
