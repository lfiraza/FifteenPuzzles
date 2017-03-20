#!/usr/bin/python3

from Node import Node
from Bfs import Bfs
import numpy as np
import sys, getopt

def main(argv):
    start()


            

def start():

    row = 4
    col = 4

    startPuzzle = np.array([[0, 1, 2], 
                            [3, 4, 5]])

    endPuzzle = np.array([[1, 2, 3], 
                          [4, 5, 0]])

    start = Node(startPuzzle)
    end = Node(endPuzzle)

    if start.checkSolvability():
        bfs = Bfs(start, end)
        bfs.solve()

        solutionNode = bfs.solutionNode

        solutionStates = []
        solutionMoves = []

        while solutionNode.parent:
            solutionStates.append(solutionNode.getPuzzles())
            solutionMoves.append(solutionNode.move)
            solutionNode = solutionNode.parent

        print(len(solutionMoves))
        for i in range(len(solutionMoves) - 1, -1, -1):
            print(solutionMoves[i], end="")

        print()
    else:
        print(-1)

if __name__ == "__main__":
    main(sys.argv[1:])

    