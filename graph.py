class Graph:
  def __init__(self, vert={}):
    self.vertices = vert

  def addVertex(self,*vert):
    for v in vert:
      self.vertices[v] = {}

  def addEdge(self, v1, v2, n):
    self.vertices[v1][v2] = n  # self.vertices[v1].update({v2:n})

  def getGraph(self):
    return self.vertices

  def printv(self):
    print(self.vertices)

  def dijkstra(self, start):
    unVisited = [node for node in self.vertices]
    distances = {}
    predecessors = {}
    infinity = 999999
  
    # init distances : 0 for start node and inifnite for other
    for node in unVisited:
      if node == start:
        distances[node] = 0
      else:
        distances[node] = infinity
        
    # go through unvisited nodes
    while unVisited:  
      # node with min distance search (->focusNode)
      m = infinity
      focusNode = None
      for n, w in distances.items():
        if n not in unVisited: continue
        if w <= m:
          m = w
          focusNode = n   
          
      # remove this focusNode
      unVisited.remove(focusNode)
      
      # update distance with the focusNode neighbors 
      for n, w in self.vertices[focusNode].items():
          new_dist = distances[focusNode] + w
          if new_dist < distances[n]:
            distances[n]= new_dist
            predecessors[n]=focusNode
            
    return distances, predecessors
    
  def shortestPath(self, start, end):
    dist, pred = self.dijkstra(start)
    current=end
    path=[]
    while True:
      path.insert(0, current)
      current = pred[current]
      if current == start:
        path.insert(0, current)
        break
    
    return dist[end], path
  
 