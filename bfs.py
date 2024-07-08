class Graph:
  def __init__(self):
    self.graph = {}
  
  
  def add_graph(self, graph):
    self.graph = graph
    
    
  def add_adjacency(self, u, v):
    if u not in self.graph:
      self.graph[u] = []

    if isinstance(v, list):
      self.graph[u] += v
    else:
      self.graph[u].append(v);
      
   
  def bfs(self):
    while len(self.queue):
      current_node = self.queue.pop(0)
      self.result.append(current_node)
      
      for i in self.graph[current_node]:
        if i in self.visited: continue
        self.visited[i] = True
        self.queue.append(i)
        # self.bfs()
  
  
  def traverse(self, start):
    self.visited = {}
    self.queue = [start]
    self.visited[start] = True
    self.result = []
    
    self.bfs()
    
    return self.result;
  
 
# way - 1 to utilize that class
graph1 = Graph()
graph1.add_graph(
  {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
  }
)
print(graph1.traverse("A"))


# way - 2 to utilize that class
graph2 = Graph();
graph2.add_adjacency(1, [2, 6])
graph2.add_adjacency(2, [1, 3, 4])
graph2.add_adjacency(3, [2])
graph2.add_adjacency(4, [2, 5])
graph2.add_adjacency(5, [4, 8])
graph2.add_adjacency(6, [1, 7, 9])
graph2.add_adjacency(7, [6, 8])
graph2.add_adjacency(8, [5, 7])
graph2.add_adjacency(9, [6])
print(graph2.traverse(1))