# Complete the topological_sort function in the given python file such that the inputted graph is printed out in topological order.

from collections import defaultdict

class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
      visited = [False for i in range(self.V)]
      stack = []
      vertex = 0
      for i in range(self.V):
        if not visited[i]:
          self.topological_sort_helper(i, visited, stack)

      print(stack)
        
    def topological_sort_helper(self, node, visited, stack):
      visited[node] = True
      for adj in self.graph[node]: # iterate through adjacent vertices
        if not visited[adj]:
          self.topological_sort_helper(adj, visited, stack)
      stack.insert(0, node)

g = Graph(int(input("Enter the number of vertices: ")))
new_edge = [int(x) for x in input("Enter edge in format 'v1 v2' (-1 -1 to stop): ").split()]
while new_edge[0] != -1:
    g.addEdge(new_edge[0], new_edge[1])
    new_edge = [int(x) for x in input("Enter edge in format 'v1 v2' (-1 -1 to stop): ").split()]

g.topological_sort()
