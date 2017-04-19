import numpy as np
from Node import Node
import sys
from queue import Queue
from multiprocessing.dummy import Process

class Bfs(object):
    """description of class"""

    def __init__(self, startNode, endNode, settings):
        self.__start = startNode
        self.__end = endNode
        self.__visited = {}
        self.__queue = Queue()
        self.solutionNode = None
        self.__settings = settings
        self.counterNodes = 0
        self._moves = np.array(['G', 'D', 'L', 'P'])
        

    def solve(self):
        self.__queue.put(self.__start)

        if(self.__settings[0]!='R'):
            self._moves = self.__settings

        processes = []

        for i in range(4):
            p = Process(target=self.bfsLoop)
            processes.append(p)

        [x.start() for x in processes]
        [x.join() for x in processes]
        

    def bfsLoop(self):

        while not self.__queue.empty():
            lastNode = self.__queue.get()
            if lastNode == self.__end: 
                self.solutionNode = lastNode
                break
                
            if lastNode.hash in self.__visited: continue
            children = lastNode.getChildren()
            if(self.__settings[0]=='R'):
                np.random.shuffle(self._moves)

            for move in self._moves:
                if move in children:
                    newNode = Node(children[move], lastNode, move)
                    if newNode.hash in self.__visited: continue
                    self.__queue.put(newNode)

            self.__visited[lastNode.hash] = None
            self.counterNodes += 1

       
