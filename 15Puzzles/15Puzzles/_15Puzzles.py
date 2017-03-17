from Node import Node
import numpy as np

row = 4
col = 4

startPuzzle = np.array([[1,0],
                        [3,2]])

endPuzzle = np.array([[1,2],
                      [3,0]])

if __name__ == "__main__":
    node = Node(startPuzzle)
    print(node.checkSolvability())
