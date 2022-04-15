class Graph:
  def __init__(self):
    self.vertices={}

  def addVertex(self,*vert):
    for v in vert:
      self.vertices[v]={}

  def addEdge(self, v1, v2, n):
    self.vertices[v1].update({v2:n})

  def getGraph(self):
    return self.vertices

  def printv(self):
    print(self.vertices)

 