# You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).
# You are also given a 2D integer array edges, where edges[i] = [from_i, to_i] denotes that there is a unidirectional edge from from_i to to_i in the graph.
# Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.
# A node u is an ancestor of another node v if u can reach v via a set of edges.

from collections import defaultdict, deque

def get_ancestors(n, edges):
  graph = defaultdict(list)
  indegree = [0 for i in range(n)]
  queue = deque()
  ans = [[] for i in range(n)]
  
  for edge in edges:
    graph[edge[0]].append(edge[1]) # initialize directional graph
    indegree[edge[1]] += 1

  for i in range(len(indegree)):
    if indegree[i] == 0:
      queue.append(i)

  while len(queue) != 0:
    vertex = queue.popleft()

    for adj in graph[vertex]:
      indegree[adj] -= 1 # reduce adjacent vertices' indegrees by 1 each
      ans[adj].append(vertex)
      for ancestor in ans[vertex]:
        if ans[adj].count(ancestor) == 0:
          ans[adj].append(ancestor)
      if indegree[adj] == 0:
        queue.append(adj)
    ans[vertex] = sorted(ans[vertex])
  
  return ans

n = 8
edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]] # expected output: [[],[],[],[0,1],[0,2], [0,1,3],[0,1,2,3,4],[0,1,2,3]]
print(get_ancestors(n, edges))