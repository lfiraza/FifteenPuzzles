import numpy as np

class Node:
    """Mainly classes for puzzle nodes"""
    def __init__(self, puzzle):
        self.__puzzle = puzzle

    def __inversionCount(self):
        puzzle = self.__puzzle.flatten()
        length = len(puzzle)
        inversionCounter = 0
        for i in range(0, length - 1):
                for j in range(i + 1, length):
                        if puzzle[j] and puzzle[i] and puzzle[i] > puzzle[j]:
                                inversionCounter += 1
        return inversionCounter

    def __positionNullFind(self):
        grid = len(self.__puzzle[0])
        row = len(self.__puzzle)

        for i in range(row - 1, -1, -1):
            for j in range(grid - 1, -1, -1):
                if self.__puzzle[i][j] == 0:
                    return row - i

    def __ifSolvable(self):
        inversion = self.__inversionCount()
        grid = len(self.__puzzle[0])
        if grid % 2:
                return not(inversion % 2)
        else:
                positionNull = self.__positionNullFind()
                if positionNull % 2:
                        return not(inversion % 2)
                else:
                        return (inversion % 2)

    def checkSolvability(self):
        return self.__ifSolvable()