class Graph:
    def __init__(self, n):
        self.v=n
        self.doublelist= [[] for i in range(n)]
  
    def addEdge(self,tailVertex,head_vertex):
        self.doublelist[tailVertex].append(head_vertex)
    def BFS(self , starting):
        visited=  [False] * self.v
        queue= []
        queue.append(starting)
        visited[starting]=True
        while(not (len(queue)==0)):
            print(queue[0],end=" ")
            place=queue[0]
            queue.pop(0)
            for i in range(len(self.doublelist[place])):
                if (visited[self.doublelist[place][i]] == False):
                 queue.append(self.doublelist[place][i])
                 visited[self.doublelist[place][i]] = True
  
  
  

  
  
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.doublelist)
print("")
g.BFS(2)