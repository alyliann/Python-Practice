# Implement BFS and DFS in the given python file

from collections import defaultdict

class Graph():
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.V = vertices

  def addEdge(self, u, v):
    self.graph[u].append(v)
    self.graph[v].append(u)

  def bfs_traversal(self):
    visited = [False for i in range(len(self.graph))]
    queue = []
    queue.append(0)

    while visited.count(False) > 0:
      vertex = queue[-1]
      if visited[vertex] != True:
        visited[vertex] = True # mark vertex as visited

      for adj in range(len(self.graph[vertex])):
        adjacent = self.graph[vertex][adj]
        if visited[adjacent] != True:
          queue.append(adjacent) # push adjacent node to queue
          visited[adjacent] = True # mark adjacent node as visited

    for node in queue:
      print(node, end=' ')

  def dfs_traversal(self):
    visited = [False for i in range(len(self.graph))]
    stack = []
    stack.append(0)

    while visited.count(False) > 0:
      vertex = stack[-1]
      if visited[vertex] != True:
        visited[vertex] = True # mark vertex as visited

      for adj in range(len(self.graph[vertex])):
        adjacent = self.graph[vertex][adj]
        if visited[adjacent] != True:
          stack.append(adjacent) # push adjacent node to stack
          visited[adjacent] = True # mark adjacent node as visited
          break

    for node in stack:
      print(node, end=' ')
    

##driver code for testing
g = Graph(5)

for i in range(5):
  for j in range(i+2, 5):
    g.addEdge(i, j)

print("Breadth-First Search")
g.bfs_traversal()
print("\nDepth-First Search")
g.dfs_traversal()