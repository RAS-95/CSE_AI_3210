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
  cnt = 1
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

  def dfs(self,current_node,goal_node,stack,cnt):
    stack.stack_print()
    visited = []
    ara = []
    start_node = current_node
    temp = 0

    while not stack.is_empty():
      item = stack.pop()
      current_node = item[0]
      if current_node == goal_node:
        cost = item[1]
        temp = 1
        stack.stack_clear()

      else:
        if current_node in visited:
          continue
        visited.append(current_node)
    if temp == 1:
      print("Total Cost : ",cost)
      return -1
      #for i in range(stack1.stack_length()):
      #  print(stack1.pop())
    else:
      print(cnt)
      return cnt+1

  def ids(self,current_node,goal_node):
    visited = []
    stack = Stack()
    start_node = current_node
    stack.push((start_node,0,1))
    stack1 = Stack()
    stack1.push((start_node,0))
    cnt = 1
    while True:
      if stack.is_empty():
        cnt = self.dfs(start_node,goal_node,stack1,cnt)
        print(cnt)
        visited = []
        stack = Stack()
        stack.push((start_node,0,1))
        stack1 = Stack()
        stack1.push((start_node,0))
        stack.stack_print()
        stack1.stack_print()
        print(visited)
        if cnt == -1:
          return
      else:
        item = stack.pop()
        current_node = item[0]
        level = item[2]
        if current_node in visited:
          continue
        visited.append(current_node)
        for neighbour in self.graph[current_node]:
          if neighbour not in visited and level<cnt:
            if item[2] != cnt-1:
              stack.push((neighbour,self.graph[current_node][neighbour]+item[1],item[2]+1))
            stack1.push((neighbour,self.graph[current_node][neighbour]+item[1]))

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
g.ids('S','G')