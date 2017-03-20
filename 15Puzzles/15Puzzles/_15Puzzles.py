from Node import Node
from Bfs import Bfs
import numpy as np

row = 4
col = 4

startPuzzle = np.array([[1,2,3],
                        [3,4,5],
                        [6,0,7]])

endPuzzle = np.array([[1,2,3],
                      [3,4,5],
                      [6,7,0]])

if __name__ == "__main__":
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

        del bfs
        del solutionNode

        print("Ruchy:")
        for i in range(len(solutionMoves)-1, -1, -1):
            print(solutionMoves[i])
        
        print("Stany:")
        print(startPuzzle)
        for i in range(len(solutionStates)-1, -1, -1): 
            print(solutionStates[i])
    else:
        print("Układ nierozwiązywalny")

    