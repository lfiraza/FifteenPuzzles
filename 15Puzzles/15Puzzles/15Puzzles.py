#!/usr/local/bin/python3

from Node import Node
from Bfs import Bfs
from Dfs import Dfs
from AStar import AStar
import numpy as np
import sys, getopt, time

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
    print("     1 - Manhattan Distance")
    print("     2 - Inversion Counter")
    print("     3 - Euclidean Distance")
    print("     4 - Chebyshev Distance")


def start(method, settings):

    startFullTime = time.perf_counter()

    row = 4
    col = 4

    startPuzzle = np.array([[2,3,1],
                            [0,4,5]])

    endPuzzle = np.array([[1,2,3],
                          [4,5,0]])

    start = Node(startPuzzle)
    end = Node(endPuzzle)

    solutionNode = None
    visitedNodes = 0

    if start.checkSolvability():
        
        if method == "bfs":
            bfs = Bfs(start, end, settings)
            bfs.solve()
            solutionNode = bfs.solutionNode
            visitedNodes = bfs.counterNodes
        elif method == "dfs":
            dfs = Dfs(start, end, settings)
            dfs.solve()
            solutionNode = dfs.solutionNode
            visitedNodes = dfs.counterNodes
        elif method == "astar":
            astar = AStar(start, end, settings)
            astar.solve()
            solutionNode = astar.solutionNode
            visitedNodes = astar.counterNodes
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

    fullTime = "%.4f" % (time.perf_counter() - startFullTime)

    print()
    print("Stats:")
    print('Full Time: ', fullTime, ' sec')
    if start.checkSolvability():
        print('Steps to solution: ', len(solutionMoves))
        print('Visited nodes: ', visitedNodes)

if __name__ == "__main__":
    main(sys.argv[1:])

    