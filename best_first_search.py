class Best_first_search:
  def __init__(self, graph, distance, start, end):
    self.graph = graph
    self.distance = distance
    self.start = start
    self.end = end
    
    self.open = graph[start]
    self.close = [start]
     
  def find_path(self): 
    if not len(self.open):
      print("Goal not found")
      return self.close

    min_node_index = len(self.open)-1
    min_node = self.open[min_node_index]
    
    while min_node_index>=0:
      if self.distance[self.open[min_node_index]] <= self.distance[min_node]:
        min_node = self.open[min_node_index]
      min_node_index -= 1
    
    self.open.remove(min_node)
    self.close.append(min_node)
    
    for node in self.graph[min_node]:
      self.open.append(node)
    
    if min_node == self.end: 
      return self.close
    return self.find_path()



graph1 = Best_first_search(
  {
    "s": ["a", "b"],
    "a": ["s", "c", "d"],
    "b": ["s", "e", "f"],
    "c": ["a"],
    "d": ["a"],
    "e": ["b", "h"],
    "f": ["b", "i", "g"],
    "i": ["f"],
    "g": ["f"],
  }, {
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
  }, "s", "g"
)    
  
print(graph1.find_path())