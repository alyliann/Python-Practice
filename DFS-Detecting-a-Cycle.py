# Implement isCyclicUtil in the given python file

from collections import defaultdict

class Graph():
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.V = vertices

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def isCyclicUtil(self, v, visited, recStack):
    visited = [False for i in range(len(self.graph))]
    stack = []
    stack.append(0)

    while visited.count(False) > 0:
      vertex = stack[-1]
      if visited[vertex] == True:
        return True
      else:
        visited[vertex] = True # mark vertex as visited

      for adj in range(len(self.graph[vertex])):
        adjacent = self.graph[vertex][adj]
        if adjacent >= len(self.graph):
          continue
        elif visited[adjacent] != True:
          stack.append(adjacent) # push adjacent node to stack
          break
        else:
          return True

    return False

  def isCyclic(self):
    visited = [False] * self.V
    recStack = [False] * self.V
    for node in range(self.V):
      if visited[node] == False:
        return self.isCyclicUtil(node, visited, recStack)

##driver code for testing
g = Graph(int(input("Enter the number of vertices: ")))
new_edge = [int(x) for x in input("Enter edge in format 'v1 v2' (-1 -1 to stop): ").split()]
while new_edge[0] != -1:
  g.addEdge(new_edge[0], new_edge[1])
  new_edge = [int(x) for x in input("Enter edge in format 'v1 v2' (-1 -1 to stop): ").split()]

print(g.isCyclic()) #4 vertices: 01, 12, 23