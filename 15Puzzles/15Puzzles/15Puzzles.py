#!/usr/bin/python3

from Node import Node
from Bfs import Bfs
import numpy as np
import sys, getopt

def main(argv):

    method = ''
    order = ''

    try:
        opts, args = getopt.getopt(argv,"hb:d:n:",["help","bfs=","dfs=","nn="])
    except getopt.GetoptError:
        print("15puzzle: An options error")
        print("Try './15puzzle.py --help' for more information.")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
                  print("Usage: 15puzzle [OPTION] ORDER/HEURISTIC_ID")
                  print("   -b / --bfs order    Breadth-first search")
                  print("   -b / --bfs order    Depth First Search")
                  print("   -n / --nn heuristic id  A* search")
                  print("   -h / --help")
                  print("ORDER: Example - GDLP \n   G - Top\n   D - Down\n    L - Left\n    P - Right\n  R - Random")
                  sys.exit()
        elif opt in ("-b", "--bfs"):
                  method = "bfs"
                  order = arg
                  start()
        elif opt in ("-d", "--dfs"):
                  print("This method is unsupported")
                  sys.exit()
                  method = "dfs"
                  odrder = arg
        elif opt in ("-n", "--nn"):
                  print("This method is unsupported")
                  sys.exit()
                  method = "astar"
                  odrder = arg
        else:
                  print("15puzzle: An options error")
                  print("Try '15puzzle.py --help' for more information.")
                  sys.exit(2)


            

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

    