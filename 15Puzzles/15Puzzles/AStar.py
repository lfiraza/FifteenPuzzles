import numpy as np
from Node import Node
from queue import PriorityQueue
import math

class AStar(object):
    """description of class"""
    def __init__(self, startNode, endNode, idH):
        self.__start = startNode
        self.__end = endNode
        self.__visited = {}
        self.__queue = PriorityQueue()
        self.solutionNode = None
        self.idH = idH
        self.counterNodes = 0

    def solve(self):
        selfCounter = 1

        score = self.__score(self.__start, self.idH)

        self.__queue.put((score, 0, self.__start))

        while not self.__queue.empty():
            _, _, lastNode = self.__queue.get()

            if lastNode == self.__end: 
                self.solutionNode = lastNode
                break
            if lastNode.hash in self.__visited: continue
            children = lastNode.getChildren()
            for move, puzzles in children.items():
                newNode = Node(puzzles, lastNode, move)
                if newNode.hash in self.__visited: 
                    continue
                score = self.__score(newNode, self.idH)
                self.__queue.put((score, selfCounter, newNode))
                selfCounter += 1
            self.__visited[lastNode.hash] = None
            self.counterNodes += 1

    def __score(self, node, id):
        score = 0

        if id == '1':
            score = self.__manhattan(node)
        elif id == '2':
            score = self.__inversion(node)
        elif id == '3':
            score = self.__euclidean(node)
        elif id == '4':
            score = self.__chebyshev(node)
        else:
            score = self.__manhattan(node)

        return score

    def __manhattan(self, node):
        score = 0
        puzzles = node.getPuzzles()
        for i in range(1, len(puzzles)*len(puzzles[0])):
            rowNode, colNode = node.positionValue(i)
            rowEnd, colEnd = self.__end.positionValue(i)
            score += abs(rowEnd - rowNode) + abs(colEnd - colNode)
        return score

    def __inversion(self, node):
        return node.inversionCount()

    def __euclidean(self, node):
        score = 0
        puzzles = node.getPuzzles()
        for i in range(1, len(puzzles)*len(puzzles[0])):
            rowNode, colNode = node.positionValue(i)
            rowEnd, colEnd = self.__end.positionValue(i)
            score += math.sqrt((rowEnd - rowNode)**2 + (colEnd - colNode)**2)
        return score

    def __chebyshev(self, node):
        score = 0
        puzzles = node.getPuzzles()
        for i in range(1, len(puzzles)*len(puzzles[0])):
            rowNode, colNode = node.positionValue(i)
            rowEnd, colEnd = self.__end.positionValue(i)
            score += ((rowEnd - rowNode) + (colEnd - colNode)) - 1 * min((rowEnd - rowNode), (colEnd - colNode))
        return score



