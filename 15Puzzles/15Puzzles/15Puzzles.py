#!/usr/local/bin/python3

from Node import Node
from Bfs import Bfs
from Dfs import Dfs
from AStar import AStar
from Gui import MainWindow
import numpy as np
import sys, getopt, time, ctypes, sip

def main(argv):

    method = ''
    settings = ''
    gui = False
    stdinRead = False

    try:
        opts, args = getopt.getopt(argv, "hgrb:d:n:", ["help", "gui", "read", "bfs=", "dfs=", "nn="])
    except getopt.GetoptError as error:
        print(error)
        sys.exit(2)

    if len(opts) == 0:
        start("astar", '1', True, False)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
        elif opt in ("-g", "--gui"):
            gui = True
        elif opt in ("-r", "--read"):
            stdinRead = True
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

    start(method, settings, gui, stdinRead)

def help():
    print("Usage: ./15Puzzles OPTION [VALUE]")
    print("Options:")
    print("     -h --help   this help")
    print("     -g --gui   run with gui")
    print("     -r --read   read from stdin")
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


def start(method, settings, gui, stdinRead):

    if gui:
        from PyQt5 import QtGui, QtCore, QtWidgets
        sip.setapi('QDate', 2)
        sip.setapi('QDateTime', 2)
        sip.setapi('QString', 2)
        sip.setapi('QTextStream', 2)
        sip.setapi('QTime', 2)
        sip.setapi('QUrl', 2)
        sip.setapi('QVariant', 2)

    startPuzzle = None
    endPuzzle = None

    row = 0
    col = 0


    if not stdinRead:
        row = 4
        col = 4

        startPuzzle = np.array([[0,1,2,7],
                            [8,9,12,10],
                            [13,3,6,4],
                            [15,14,11,5]])

        endPuzzle = np.zeros((col,row), int)

        element = 1
        for i in range(row):
                for j in range(col):
                    endPuzzle[i][j] = element
                    element += 1

        endPuzzle[-1][-1] = 0

    else:

        iteration = 0
        for line in sys.stdin:
            if not iteration:
                row = line[0]
                col = line[1]
                
            else:
                for i in range(col):
                    startPuzzle[iteration-1][i] = line[i]
            
            iteration += 1
            
        endPuzzle = np.zeros((col,row), np.uint8)

        element = 1
        for i in range(row):
                for j in range(col):
                    endPuzzle[i][j] = element
                    element += 1

        endPuzzle[-1][-1] = 0
         

    start = Node(startPuzzle)
    end = Node(endPuzzle)

    solutionNode = None
    visitedNodes = 0

    startFullTime = time.perf_counter()

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

    if gui and start.checkSolvability():
        app = QtWidgets.QApplication(sys.argv)
        app.setApplicationName("15Puzzles")
        main = MainWindow(row, col, startPuzzle, 0, solutionMoves)
        main.show()
        app.exec_()

if __name__ == "__main__":
    main(sys.argv[1:])    