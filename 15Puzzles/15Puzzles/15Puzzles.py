#!/usr/local/bin/python3

from Node import Node
from Bfs import Bfs
from Dfs import Dfs
import numpy as np
import sys, getopt

def main(argv):
    start() 

def start():

    row = 4
    col = 4

    startPuzzle = np.array([[1,2,3],
                            [4,0,6],
                            [7,5,8]])

    endPuzzle = np.array([[1,2,3],
                          [4,5,6],
                          [7,8,0]])

    start = Node(startPuzzle)
    end = Node(endPuzzle)

    if start.checkSolvability():
        '''
        bfs = Bfs(start, end)
        bfs.solve()

        solutionNode = bfs.solutionNode
        '''

        dfs = Dfs(start, end)
        dfs.solve()
        solutionNode = dfs.solutionNode

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

    