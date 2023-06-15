# Implemennt shortest_path in the given python file

from collections import defaultdict

class Graph():
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.V = vertices

  def addEdge(self, u, v):
    self.graph[u].append(v)
    self.graph[v].append(u)

  def shortest_path(self, start_node, end_node):
    if start_node == end_node:
      return 0

    visited = [False for i in range(len(self.graph))]
    distance_list = [float('inf') for i in range(len(self.graph))] # distance of each vertex from the starting node
    queue = [start_node]
    visited[start_node] = True
    distance_list[start_node] = 0
    
    while visited.count(False) > 0:
      vertex = queue[-1]
      distance = distance_list[vertex]+1
      if visited[vertex] != True:
        visited[vertex] = True # mark vertex as visited

      for adj in range(len(self.graph[vertex])):
        adjacent = self.graph[vertex][adj]
        if adjacent == end_node:
          return distance
        elif visited[adjacent] != True:
          queue.append(adjacent) # push adjacent node to queue
          visited[adjacent] = True # mark adjacent node as visited
          distance_list[adjacent] = distance

def main():
  ##driver code for testing
  g = Graph(5)

  for i in range(5):
    for j in range(i+2, 5):
      g.addEdge(i, j)

  start_node = int(input("Enter start vertex: "))
  end_node = int(input("Enter end vertex: "))
  print(g.shortest_path(start_node, end_node))

if __name__ == "__main__":
    main()