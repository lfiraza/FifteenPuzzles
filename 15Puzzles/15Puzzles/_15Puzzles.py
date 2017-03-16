import numpy as np

row = 4
col = 4

startPuzzle = np.array([[1,2,3,4],
                        [5,6,7,8],
                        [9,10,11,12],
                        [13,15,14,0]])

endPuzzle = np.array([[1,2,3,4],
                        [5,6,7,8],
                        [9,10,11,12],
                        [13,14,15,0]])



def inversionCount(puzzle):
        puzzle = puzzle.flatten()
        length = len(puzzle)
        inversionCounter = 0
        for i in xrange(0, length - 1):
                for j in xrange(i + 1, length):
                        if puzzle[j] and puzzle[i] and puzzle[i] > puzzle[j]:
                                inversionCounter += 1
        return inversionCounter

def positionNullFind(puzzle):
        grid = len(puzzle[0])
        row = len(puzzle)

        for i in xrange(row - 1, 0, -1):
                for j in xrange(grid - 1, 0, -1):
                        if puzzle[i][j] == 0:
                                return row - i

def ifSolvable(puzzle):
        inversion = inversionCount(puzzle)
        grid = len(puzzle[0])
        if grid % 2:
                return not(inversion % 2)
        else:
                positionNull = positionNullFind(puzzle)
                if positionNull % 2:
                        return not(inversion % 2)
                else:
                        return (inversion % 2)


print ifSolvable(startPuzzle)
