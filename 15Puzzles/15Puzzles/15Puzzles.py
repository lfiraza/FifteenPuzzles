#!/usr/local/bin/python3

from Node import Node
from Bfs import Bfs
from Dfs import Dfs
from AStar import AStar
import numpy as np
import sys, getopt

def main(argv):

    method = ''
    settings = ''

    try:
        opts, args = getopt.getopt(argv, "hb:d:n:", ["help", "bfs=", "dfs=", "nn="])
    except getopt.GetoptError as error:
        print(error)
        sys.exit(2)

    if len(opts) == 0:
        help()
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
        elif opt in ("-b", "--bfs"):
            method = 'bfs'
            settings = arg
        elif opt in ("-d", "--dfs"):
            method = 'dfs'
            settings = arg
        elif opt in ("-n", "--nn"):
            method = 'astar'
            settings = arg
        else:
            assert False, "Error"

    start(method, settings)

def help():
    print("Usage: ./15Puzzles OPTION [VALUE]")
    print("Options:")
    print("     -h --help   this help")
    print("     -b --bfs    breadth-first search")
    print("     -d --dfs    depth first search")
    print("     -n --nn     A*")
    print("Values:")
    print(" For BFS and DFS is possible ordering moves")
    print("     Example: ./15Puzzles -b GDPL or ./15Puzzles -b R")
    print("     G - Top")
    print("     D - Down")
    print("     P - Right")
    print("     L - Left")
    print(" For A* is possible select heuristic")
    print("     Example: ./15Puzzles -n 1")


def start(method, settings):

    row = 4
    col = 4

    startPuzzle = np.array([[2,6,1],
                            [0,7,8],
                            [3,5,4]])

    endPuzzle = np.array([[1,2,3],
                          [4,5,6],
                          [7,8,0]])

    start = Node(startPuzzle)
    end = Node(endPuzzle)

    solutionNode = None

    if start.checkSolvability():
        
        if method == "bfs":
            bfs = Bfs(start, end)
            bfs.solve()
            solutionNode = bfs.solutionNode
        elif method == "dfs":
            dfs = Dfs(start, end)
            dfs.solve()
            solutionNode = dfs.solutionNode
        elif method == "astar":
            astar = AStar(start, end)
            astar.solve()
            solutionNode = astar.solutionNode
        else:
            print("Unknow method")
            sys.exit(3)

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

    