import numpy as np
from Node import Node
from queue import Queue

class Bfs(object):
    """description of class"""

    def __init__(self, startNode, endNode):
        self.__start = startNode
        self.__end = endNode
        self.__visited = []
        self.visitedNodeCounter = 0
        self.__queue = Queue()
        self.solutionNode = None

    def solve(self):
        self.__queue.put(self.__start)

        while not self.__queue.empty():
            lastNode = self.__queue.get()
            if lastNode == self.__end: 
                self.solutionNode = lastNode
                del self.__queue
                del self.__visited
                break
            if lastNode in self.__visited: continue
            children = lastNode.getChildren()
            for move, puzzles in children.items():
                newNode = Node(puzzles, lastNode, move)
                if newNode in self.__visited: continue
                self.__queue.put(newNode)
            self.__visited.append(lastNode)
            self.visitedNodeCounter += 1
