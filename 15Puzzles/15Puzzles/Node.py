import numpy as np

class Node:
    """
    Mainly classes for puzzle nodes
    """

    def __init__(self, puzzle, parent=None, move=None):
        self.__puzzle = puzzle
        self.children = {}
        self.positionNull = self.__positionNull()
        self.__setChildren()
        self.parent = parent
        self.move = move

    def __inversionCount(self):
        puzzle = self.__puzzle.flatten()
        length = len(puzzle)
        inversionCounter = 0
        for i in range(0, length - 1):
                for j in range(i + 1, length):
                        if puzzle[j] and puzzle[i] and puzzle[i] > puzzle[j]:
                                inversionCounter += 1
        return inversionCounter

    def __positionNullFromBottom(self):
        row = len(self.__puzzle)
        return row - self.positionNull[0]

    def __ifSolvable(self):
        inversion = self.__inversionCount()
        grid = len(self.__puzzle[0])
        if grid % 2:
                return not(inversion % 2)
        else:
                positionNull = self.__positionNullFromBottom()
                if positionNull % 2:
                        return not(inversion % 2)
                else:
                        return (inversion % 2)

    def checkSolvability(self):
        return self.__ifSolvable()

    def __positionNull(self):
        grid = len(self.__puzzle[0])
        row = len(self.__puzzle)

        for i in range(row - 1, -1, -1):
            for j in range(grid - 1, -1, -1):
                if self.__puzzle[i][j] == 0:
                    return i, j

    def __setChildren(self):
        positionNull = {'row': self.positionNull[0], 
                        'col': self.positionNull[1]}

        grid = len(self.__puzzle[0])
        row = len(self.__puzzle)

        puzzle = np.copy(self.__puzzle)

        if positionNull['row'] == 0:
            puzzle[0][positionNull['col']], puzzle[1][positionNull['col']] = puzzle[1][positionNull['col']], puzzle[0][positionNull['col']]
            self.children['D'] = np.copy(puzzle)
            puzzle[0][positionNull['col']], puzzle[1][positionNull['col']] = puzzle[1][positionNull['col']], puzzle[0][positionNull['col']]
        elif positionNull['row'] == row-1:
            puzzle[positionNull['row']][positionNull['col']], puzzle[positionNull['row']-1][positionNull['col']] = puzzle[positionNull['row']-1][positionNull['col']], puzzle[positionNull['row']][positionNull['col']]
            self.children['G'] = np.copy(puzzle)
            puzzle[positionNull['row']][positionNull['col']], puzzle[positionNull['row']-1][positionNull['col']] = puzzle[positionNull['row']-1][positionNull['col']], puzzle[positionNull['row']][positionNull['col']]
        else:
            puzzle[positionNull['row']][positionNull['col']], puzzle[positionNull['row']+1][positionNull['col']] = puzzle[positionNull['row']+1][positionNull['col']], puzzle[positionNull['row']][positionNull['col']]
            self.children['D'] = np.copy(puzzle)
            puzzle[positionNull['row']][positionNull['col']], puzzle[positionNull['row']+1][positionNull['col']] = puzzle[positionNull['row']+1][positionNull['col']], puzzle[positionNull['row']][positionNull['col']]
            puzzle[positionNull['row']][positionNull['col']], puzzle[positionNull['row']-1][positionNull['col']] = puzzle[positionNull['row']-1][positionNull['col']], puzzle[positionNull['row']][positionNull['col']]
            self.children['G'] = np.copy(puzzle)
            puzzle[positionNull['row']][positionNull['col']], puzzle[positionNull['row']-1][positionNull['col']] = puzzle[positionNull['row']-1][positionNull['col']], puzzle[positionNull['row']][positionNull['col']]

        if positionNull['col'] == 0:
            puzzle[positionNull['row']][0], puzzle[positionNull['row']][1] = puzzle[positionNull['row']][1], puzzle[positionNull['row']][0]
            self.children['P'] = np.copy(puzzle)
            puzzle[positionNull['row']][0], puzzle[positionNull['row']][1] = puzzle[positionNull['row']][1], puzzle[positionNull['row']][0]

        elif positionNull['col'] == grid-1:
            puzzle[positionNull['row']][positionNull['col']], puzzle[positionNull['row']][positionNull['col']-1] = puzzle[positionNull['row']][positionNull['col']-1], puzzle[positionNull['row']][positionNull['col']]
            self.children['L'] = np.copy(puzzle)
            puzzle[positionNull['row']][positionNull['col']], puzzle[positionNull['row']][positionNull['col']-1] = puzzle[positionNull['row']][positionNull['col']-1], puzzle[positionNull['row']][positionNull['col']]

        else:
            puzzle[positionNull['row']][positionNull['col']], puzzle[positionNull['row']][positionNull['col']+1] = puzzle[positionNull['row']][positionNull['col']+1], puzzle[positionNull['row']][positionNull['col']] 
            self.children['P'] = np.copy(puzzle)
            puzzle[positionNull['row']][positionNull['col']], puzzle[positionNull['row']][positionNull['col']+1] = puzzle[positionNull['row']][positionNull['col']+1], puzzle[positionNull['row']][positionNull['col']] 

            puzzle[positionNull['row']][positionNull['col']], puzzle[positionNull['row']][positionNull['col']-1] = puzzle[positionNull['row']][positionNull['col']-1], puzzle[positionNull['row']][positionNull['col']]
            self.children['L'] = np.copy(puzzle)
            puzzle[positionNull['row']][positionNull['col']], puzzle[positionNull['row']][positionNull['col']-1] = puzzle[positionNull['row']][positionNull['col']-1], puzzle[positionNull['row']][positionNull['col']]


    def getChildren(self):
        return self.children

    def getPuzzles(self):
        return self.__puzzle

    def __eq__(self, other):
        return (self.__puzzle==other.getPuzzles()).all()

    def __str__(self):
        return np.array_str(self.__puzzle)
