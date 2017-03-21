import numpy as np
from Node import Node
from queue import PriorityQueue

class AStar(object):
    """description of class"""
    def __init__(self, startNode, endNode):
        self.__start = startNode
        self.__end = endNode
        self.__visited = []
        self.__queue = PriorityQueue()
        self.solutionNode = None

    def solve(self):
        selfCounter = 1
        self.__queue.put((self.__manhattan(self.__start), 0, self.__start))

        while not self.__queue.empty():
            _, _, lastNode = self.__queue.get()

            if lastNode == self.__end: 
                self.solutionNode = lastNode
                break
            if lastNode in self.__visited: continue
            children = lastNode.getChildren()
            for move, puzzles in children.items():
                newNode = Node(puzzles, lastNode, move)
                if newNode in self.__visited: continue
                self.__queue.put((self.__manhattan(newNode), selfCounter, newNode))
                selfCounter += 1
            self.__visited.append(lastNode)

    def __manhattan(self, node):
        score = 0
        puzzles = node.getPuzzles()
        for i in range(1, len(puzzles)*len(puzzles[0])):
            rowNode, colNode = node.positionValue(i)
            rowEnd, colEnd = self.__end.positionValue(i)
            score += abs(rowEnd - rowNode) + abs(colEnd - colNode)
        return score


