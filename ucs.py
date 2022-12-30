from collections import defaultdict
from queue import PriorityQueue
from collections import OrderedDict

class Graph:
  def __init__(self,directed):
    self.graph = defaultdict(dict)
    self.directed = directed
    self.parent = defaultdict(dict)

  def add_edge(self,u,v,weight):
    if self.directed:
      #value = (weight,v)
      self.graph[u][v] = (weight)
    else:
      #value = (weight,v)
      self.graph[u][v] = (weight)
      #value = (weight,u)
      self.graph[v][u] = (weight)


  def ucs(self, current_node, goal_node):
    visited = []
    ara = []
    start_node = current_node
    queue = PriorityQueue()
    queue.put((0,current_node))

    while not queue.empty():
      item = queue.get()
      current_node = item[1]
      print(current_node,item[0])

      if current_node == goal_node:
        cost = item[0]
        cost1 = cost
        ara.append(goal_node)
        print(self.parent)
        while start_node != goal_node:
          for key,value in self.parent.items():
            if goal_node in self.graph[key] and cost1==self.parent[key][goal_node]:
              cost1 = cost1 - self.graph[key][goal_node]
              ara.append(key)
              goal_node = key

        queue.queue.clear()
      else:
        if current_node in visited:
          continue

        #print(current_node, end=" ")
        visited.append(current_node)
        
        for neighbour in self.graph[current_node]:
          self.parent[current_node][neighbour] = (self.graph[current_node][neighbour]+item[0])
          queue.put((self.graph[current_node][neighbour]+item[0],neighbour))
    print("Optimal Cost: ",cost)
    print("Optimal path: ", end=" ")
    print(ara[::-1],end=" ")

g = Graph(True)
#g.graph = defaultdict(list)
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

print(g.graph)
g.ucs('S','G')
#print(g.parent['F']['G'])