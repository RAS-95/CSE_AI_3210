from collections import defaultdict
from collections import OrderedDict
class Graph:
  def __init__(self):
    self.graph1 = defaultdict(dict)
    self.graph2 = defaultdict(dict)
    self.parent = defaultdict(dict)

  def add_edge(self,u,v,weight):
    self.graph1[u][v] = (weight)
    self.graph2[v][u] = (weight)

  def bidirectional(self,current_node,goal_node):
    visited1 = []
    visited2 = []
    queue = []
    stack = []

    queue.append((current_node,0))
    stack.append((goal_node,0))

    while len(queue) != 0:

      # For BFS
      item1 = queue.pop(0)
      current_node1 = item1[0]
      print("BFS : ",current_node1)

      if current_node1 in visited2:
        print("Goal Node is Found")
        queue.clear()
        stack.clear()
        continue
      else:
        if current_node1 in visited1:
          continue

        visited1.append(current_node1)

        for neighbour1 in self.graph1[current_node1]:
          queue.append((neighbour1,self.graph1[current_node1][neighbour1]))

      # For DFS

      item2 = stack.pop(-1)
      current_node2 = item2[0]
      print("DFS : ", current_node2)

      if current_node2 in visited1:
        print("Goal node is found")
        queue.clear()
        stack.clear()
        continue

      else:
        if current_node2 in visited2:
          continue

        visited2.append(current_node2)

        for neighbour2 in self.graph2[current_node2]:
          stack.append((neighbour2,self.graph2[current_node2][neighbour2]))
g = Graph()
g.graph1
g.graph2
g.add_edge('S', 'A', 5)
g.add_edge('S', 'B', 2)
g.add_edge('S', 'C', 4)
g.add_edge('A', 'D', 9)
g.add_edge('A', 'E', 4)
g.add_edge('D', 'H', 7)
g.add_edge('E', 'G', 6)
g.add_edge('B', 'G', 6)
g.add_edge('C', 'F', 2)
g.add_edge('F', 'G', 1)

g.bidirectional('S','G')