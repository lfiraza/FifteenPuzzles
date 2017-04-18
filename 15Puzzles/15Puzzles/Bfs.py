import numpy as np
from Node import Node
from queue import Queue
import time

class Bfs(object):
    """description of class"""

    def __init__(self, startNode, endNode, settings):
        self.__start = startNode
        self.__end = endNode
        self.__visited = {}
        self.__queue = Queue()
        self.solutionNode = None
        self.__settings = settings

    def solve(self):
        self.__queue.put(self.__start)
        moves = np.array(['G', 'D', 'L', 'P'])

        if(self.__settings[0]!='R'):
            moves = self.__settings

        while not self.__queue.empty():
            lastNode = self.__queue.get()
            if lastNode == self.__end: 
                self.solutionNode = lastNode
                break
            if lastNode.hash in self.__visited: continue
            children = lastNode.getChildren()
            if(self.__settings[0]=='R'):
                np.random.shuffle(moves)

            for move in moves:
                if move in children:
                    newNode = Node(children[move], lastNode, move)
                    if newNode.hash in self.__visited: continue
                    self.__queue.put(newNode)

            self.__visited[lastNode.hash] = None