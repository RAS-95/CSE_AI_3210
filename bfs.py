from collections import defaultdict
from collections import OrderedDict
from typing import Any
class Queue:
  def __init__(self):
    self.data = []

  def is_empty(self) -> bool:
    if len(self.data) == 0:
      return True
    return False

  def enqueue(self,value:Any) -> None:
    self.data.insert(0,value)

  def dequeue(self) -> Any:
    return self.data.pop()

  def peek(self) -> Any:
    if not self.is_empty():
      return self.data[-1]
    return

  def is_clear(self) -> Any:
    for i in range(len(self.data)):
      self.data.pop()
class Graph:
  def __init__(self,directed):
    self.graph = defaultdict(list)
    self.directed = directed
    self.parent = defaultdict(list)

  def add_edge(self,u,v,weight):
    if self.directed:
      value = (weight,v)
      self.graph[u].append(value)
    else:
      value = (weight,v)
      self.graph[u].append(value)
      value = (weight,u)
      self.graph[v].append(value)

  def bfs(self,current_node,goal_node):
    visited = []
    ara = []
    is_queue = []
    start_node = current_node
    queue = Queue()
    queue.enqueue((0,current_node))
    
    while not queue.is_empty():
      item = queue.dequeue()
      current_node = item[1]

      if current_node == goal_node:
        cost = item[0]
        print(self.parent.items())
        parent1 = OrderedDict(reversed(list(self.parent.items())))
        ara.append(goal_node)
        while start_node != goal_node:
          for key,value in parent1.items():
            if goal_node in value:
              goal_node = key
              ara.append(goal_node)

        queue.is_clear()

      else:
        if current_node in visited:
          continue

        visited.append(current_node)
        for neighbour in self.graph[current_node]:
          value = (neighbour[1])
          if neighbour[1] in is_queue:
            continue
          else:
            is_queue.append(value)
            self.parent[current_node].append(value)
            queue.enqueue((neighbour[0]+item[0],neighbour[1]))
    print("Optimal Cost: ",cost)
    print("Optimal path: ", end=" ")
    print(ara[::-1],end=" ")

g = Graph(True)
# Inserting Starting Node, Destination, Edge Cost

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

g.bfs('S','G')