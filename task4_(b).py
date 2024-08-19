# -*- coding: utf-8 -*-
"""Task4 (b).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rmC4UNTaG283rxJi5Y08_d4j40Sp_C63
"""

# Algorithm Dijkstra's shortest

from collections import defaultdict
import sys

class Heap():                                 # Heap class
    def __init__(self):                       
        self.array = []                       # Initialize array 
        self.size = 0                         # Initialize size as 0
        self.pos = []                         # Initialize pos
 
    def newMinHeapNode(self, v, dist):        # Function v as vertex   , dist as distance
        minHeapNode = [v, dist]
        return minHeapNode

    def swapMinHeapNode(self, a, b):          # Function to swap two nodes
        t = self.array[a]
        self.array[a] = self.array[b]         # of min-heap. Needed for min heapify
        self.array[b] = t
 
    def minHeapify(self, idx):                # A standard function to heapify at given idx  # This function also updates the position of the nodes # is used to decrement key()
        smallest = idx
        left = 2*idx + 1
        right = 2*idx + 2
 
        if (left < self.size and self.array[left][1] < self.array[smallest][1]):
            smallest = left
 
        if (right < self.size and self.array[right][1] < self.array[smallest][1]):
            smallest = right
 
        if smallest != idx:                    # The nodes to be swapped in min # heap if idx is not smallest  # Swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest
 
            self.swapMinHeapNode(smallest, idx) # Swap nodes
            self.minHeapify(smallest)
 
    def extractMin(self):                       # Function to extract the minimum # node from heap

        if self.isEmpty() == True:              # Return NULL heap is empty
            return
 
        root = self.array[0]                    # Store the root node
 
        lastNode = self.array[self.size - 1]    # Replace root node with last node
        self.array[0] = lastNode
 
        self.pos[lastNode[0]] = 0               # Update position of last node
        self.pos[root[0]] = self.size - 1
 
        self.size -= 1                          # Reduce heap size and heapify root
        self.minHeapify(0)
 
        return root
 
    def isEmpty(self):                          # Function to check if array is empty or not
        if self.size == 0:
          return True
        else:
          return False
 
    def decreaseKey(self, v, dist):
 
        i = self.pos[v]                                # Get the index of v in  heap array
 
        self.array[i][1] = dist                        # Get the node and update its dist value
        
        while (i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]):                                                      # Travel up while the complete tree is    # not hepified. This is a O(Logn) loop
 
            self.pos[ self.array[i][0] ] = (i-1)//2    # Swap this node with its parent
            self.pos[ self.array[(i-1)//2][0] ] = i
            self.swapMinHeapNode(i, (i - 1)//2 )

            i = (i - 1) // 2;                          # move to parent index

    def isInMinHeap(self, v):                          # A utility function to check if a given # vertex 'v' is in min heap or not
        if self.pos[v] < self.size:
          return True
        else:
          return False
 
def printArr(dist, n):                                # function to print vertex and distance from sourse
    print ("Vertex\tDistance from source")
    for i in range(n):
        print ("%d\t\t%d" % (i,dist[i]))

class Graph():                                                    # Graph class
    def __init__(self, V):
        self.V = V                                                
        self.graph = defaultdict(list)
 
    def addEdge(self, src, dest, weight):                         # Adds an edge to an undirected graph
 
        newNode = [dest, weight]                                  # Add an edge from src to dest.  A new node
        self.graph[src].insert(0, newNode)                        # is added to the adjacency list of src. The   # node is added at the beginning. The first
                                                                  # element of the node has the destination   # and the second elements has the weight
        newNode = [src, weight]                                   # Since graph is undirected, add an edge
        self.graph[dest].insert(0, newNode)                       # from dest to src also
 
    def dijkstra(self, src):                                      # The main function that calculates distances # of shortest paths from src to all vertices.  # It is a O(ELogV) function
    
        V = self.V                                                 # Get the number of vertices in graph
        dist = []                                                  # dist values used to pick minimum  # weight edge in cut
 
        minHeap = Heap()                                           # minHeap represents set E

        for v in range(V):                                         #  Initialize min heap with all vertices.          # dist value of all vertices
            dist.append(1e7)
            minHeap.array.append( minHeap.newMinHeapNode(v, dist[v]))
            minHeap.pos.append(v)
 
        minHeap.pos[src] = src                                     # Make dist value of src vertex as 0 so # that it is extracted first
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src])
 
        minHeap.size = V;                                           # Initially size of min heap is equal to V
 
        while minHeap.isEmpty() == False:                           # In the following loop, # min heap contains all nodes # whose shortest distance is not yet finalized.
 
            newHeapNode = minHeap.extractMin()                      # Extract the vertex # with minimum distance value
            u = newHeapNode[0]
 
            for pCrawl in self.graph[u]:            # Traverse through all adjacent vertices of  # u (the extracted vertex) and update their  # distance values
                v = pCrawl[0]
 
                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less
                # than its previously calculated distance
                if (minHeap.isInMinHeap(v) and dist[u] != 1e7 and pCrawl[1] + dist[u] < dist[v]):
                        dist[v] = pCrawl[1] + dist[u]
                        minHeap.decreaseKey(v, dist[v])                        # update distance value # in min heap also
        printArr(dist,V)

# I will test the software to test the above functions
graph = Graph(5)
graph.addEdge(0, 1, 1) 
graph.addEdge(0, 2, 8)
graph.addEdge(0, 3, 3)
graph.addEdge(1, 2, 2)          #(vertex, which vertex will go to, distance)
graph.addEdge(2, 3, 4)
graph.addEdge(2, 4, 1)
graph.addEdge(3, 4, 9)
graph.dijkstra(0)