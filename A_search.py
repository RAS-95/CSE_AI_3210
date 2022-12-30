from collections import defaultdict
from collections import OrderedDict
from queue import PriorityQueue
class Graph:
  def __init__(self,directed):
    self.graph = defaultdict(dict)
    self.directed = directed
    self.parent = defaultdict(dict)
    self.heuristic = defaultdict(dict)

  def add_edge(self,u,v,weight):
    if self.directed:
      #value = (weight,v)
      self.graph[u][v] = (weight)
    else:
      #value = (weight,v)
      self.graph[u][v] = (weight)
      #value = (weight,u)
      self.graph[v][u] = (weight)

  def add_heuristic(self,node,value):
    self.heuristic[node] = (value)


  def ucs(self, current_node, goal_node):
    visited = []
    ara = []
    start_node = current_node
    h_value = self.heuristic[current_node]
    e_function = 0 + h_value
    queue = PriorityQueue()
    queue.put((e_function,current_node,0))

    while not queue.empty():
      item = queue.get()
      current_node = item[1]
      print(current_node,item[2])

      if current_node == goal_node:
        cost = item[2]
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
          val = self.graph[current_node][neighbour]+item[2]
          self.parent[current_node][neighbour] = (val)
          queue.put((self.heuristic[neighbour]+val,neighbour,val))
    print("Optimal Cost: ",cost)
    print("Optimal path: ", end=" ")
    print(ara[::-1],end=" ")

g = Graph(True)
#g.graph = defaultdict(list)
#g.add_edge('S', 'A', 5)
#g.add_edge('S', 'B', 2)
#g.add_edge('S', 'C', 4)
#g.add_edge('A', 'D', 9)
#g.add_edge('A', 'E', 4)
#g.add_edge('D', 'H', 7)
#g.add_edge('E', 'G', 6)
#g.add_edge('B', 'G', 6)
#g.add_edge('C', 'F', 2)
#g.add_edge('F', 'G', 1)
infinity = 100000009

g.add_heuristic('S',8)
g.add_heuristic('A',8)
g.add_heuristic('B',4)
g.add_heuristic('C',3)
g.add_heuristic('D',infinity)
g.add_heuristic('E',infinity)
g.add_heuristic('G',0)


g.add_edge('S','A',1)
g.add_edge('S','B',5)
g.add_edge('S','C',8)
g.add_edge('A','D',3)
g.add_edge('A','E',7)
g.add_edge('A','G',9)
g.add_edge('B','G',4)
g.add_edge('C','G',5)

print(g.graph)
print(g.heuristic)
g.ucs('S','G')
q = [1,2,3,4,5]
print(q.pop(2))
print(q)