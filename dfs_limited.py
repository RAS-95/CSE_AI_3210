from collections import defaultdict
from collections import OrderedDict
from typing import Any
class Stack:
  def __init__(self):
    self.data = []
    
  def is_empty(self) -> bool:
    if len(self.data) == 0:
      return True
    return False

  def push(self,value:Any) -> None:
    self.data.append(value)

  def pop(self) -> Any:
    return self.data.pop()

  def stack_clear(self) -> None:
    self.data.clear()
  
  def stack_length(self) -> Any:
    return len(self.data)
  
  def stack_print(self) -> None:
    print(self.data)

class Graph:
  def __init__(self,directed):
    self.graph = defaultdict(dict)
    self.directed = directed
    self.parent = defaultdict(dict)

  def add_edge(self,u,v,weight):
    if self.directed:
      self.graph[u][v] = (weight)
    else:
      self.graph[u][v] = (weight)
      self.graph[v][u] = (weight)

  def dfs(self,current_node,goal_node,k):
    visited = []
    ara = []
    start_node = current_node
    stack = Stack()
    stack1 = Stack()
    stack.push((current_node,0,1))

    while not stack.is_empty():
      item = stack.pop()
      current_node = item[0]
      if current_node not in visited:
        stack1.push(current_node)
      stack.push((current_node,item[1]))

      if current_node == goal_node:
        cost = item[1]
        stack.stack_clear()

      else:
        if current_node in visited:
          stack.pop()
          stack1.pop()
          continue

        visited.append(current_node)
        if len(self.graph[current_node]) == 0:
          stack.pop()
          stack1.pop()
          continue
        for neighbour in self.graph[current_node]:
          if neighbour not in visited and item[2]<k:
            stack.push((neighbour,self.graph[current_node][neighbour]+item[1],item[2]+1))
    print("Total Cost : ",cost)
    for i in range(stack1.stack_length()):
      print(stack1.pop())
g = Graph(True)
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
k = int(input("Enter depth Limit : "))
g.dfs('S','G',k)