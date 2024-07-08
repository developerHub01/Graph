class Graph:
  def __init__(self, graph, heuristic_list, start):
    self.graph = graph;
    self.heuristic_list = heuristic_list;
    self.goal = self.find_goal_node()
    self.open = [start]
    self.close = []
    
  def find_goal_node(self):
    for i in self.heuristic_list:
      if self.heuristic_list[i]==0:
        return i
      
  def find_best_node_index(self, list):
    current_index = len(list)-1
    best_node_index = current_index
    
    while current_index>=0:
      current_node = list[current_index]
      best_node = list[best_node_index]
      if self.heuristic_list[current_node] <= self.heuristic_list[best_node]:
        best_node_index = current_index
      current_index -= 1
    return best_node_index
  
  def find_path(self):
    if not len(self.open):
      print("Goal not found")
      return
    
    current_node_index = self.find_best_node_index(self.open)
    current_node = self.open[current_node_index]
    
    self.open.pop(current_node_index)
    self.close.append(current_node)
    
    if current_node == self.goal:
      return self.close
    
    for node in self.graph[current_node]:
      self.open.append(node)
      
    print(self.open)
    print(self.close)
    
    return self.find_path()

graph1 = {
    "s": ["a", "b"],
    "a": ["s", "c", "d"],
    "b": ["s", "e", "f"],
    "c": ["a"],
    "d": ["a"],
    "e": ["b", "h"],
    "f": ["b", "i", "g"],
    "i": ["f"],
    "g": ["f"],
  }

heuristic1 = {
    "s": 13,
    "a": 12,
    "b": 4,
    "c": 7,
    "d": 3,
    "e": 8,
    "f": 2,
    "h": 4,
    "i": 9,
    "g": 0,
  }

obj = Graph(graph1, heuristic1, "s")
print(obj.find_path())

graph1 = {
  "a": ["b", "c"],
  "b": ["a", "d", "e"],
  "c": ["a", "f", "g"],
  "d": ["b"],
  "e": ["b"],
  "f": ["c"],
  "g": ["c"],
}
heuristic1 = {
  "a":6,
  "b":4,
  "c":2,
  "d":7,
  "e":3,
  "f":1,
  "g":0,
}
obj = Graph(graph1, heuristic1, "a")
print(obj.find_path())