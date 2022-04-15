'''
  dijkstra algo
  sinbrive 2022/04
'''

class Graph:
  def __init__(self):
    self.vertices={}

  def addVertex(self,*vert):
    for v in vert:
      self.vertices[v]={}

  def addEdge(self, v1, v2, n):
    self.vertices[v1].update({v2:n})

  def printv(self):
    #for v in self.vertices.items():
    print()
    print(self.vertices)

 


# get shortest distances and predecessors vs. start node 
def dijkstra(G, start):

  unVisited = [node for node in G]
  distances = {}
  predecessors={}
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
    for n, w in graph[focusNode].items():
        new_dist = distances[focusNode] + w
        if new_dist < distances[n]:
          distances[n]= new_dist
          predecessors[n]=focusNode
          
  return distances, predecessors

# get shortest path
def shortestPath(G, start, end):
  dist, pred = dijkstra(G, start)
  current=end
  path=[]
  while True:
    path.insert(0, current)
    current = pred[current]
    if current == start:
      path.insert(0, current)
      break
  return path
  

graph = {'a':{'b':8,'c':6.5, 'i':6.7, 'f':7},
         'b':{'c':6.5, 'a':8},
         'c':{'d':4, 'b':6.5},
         'd':{'e':6, 'i':4},
         'e':{'d':6, 'j':10},
         'f':{'a':7, 'g':2.5},
         'g':{'f':2.5, 'h':4.5, 'i':5.5},
         'h':{'i':7, 'g':4.5,'j':10},
         'i':{'a':6.7, 'g':5.5, 'd':4, 'h':7},
         'j':{'h':10, 'e':10}
        }


g = Graph()

g.addVertex('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
g.addEdge('a', 'b', 8)
g.addEdge('a', 'c', 6.5)
g.addEdge('a', 'f', 7)
g.addEdge('a', 'i', 6.7)

g.addEdge('b', 'a', 8)
g.addEdge('b', 'c', 6.5)

g.addEdge('c', 'b', 6.5)
g.addEdge('c', 'd', 4)

g.addEdge('d', 'c', 4)
g.addEdge('d', 'e', 6)

g.addEdge('e', 'd', 6)
g.addEdge('e', 'j', 10)

g.addEdge('f', 'a', 7)
g.addEdge('f', 'g', 2.5)

g.addEdge('g', 'f', 2.5)
g.addEdge('g', 'i', 5.5)

g.addEdge('h', 'g', 4.5)
g.addEdge('h', 'i', 7)
g.addEdge('h', 'j', 10)

g.addEdge('i', 'a', 6.7)
g.addEdge('i', 'd', 4)
g.addEdge('i', 'g', 5.5)
g.addEdge('i', 'h', 7)

g.addEdge('j', 'e', 10)
g.addEdge('j', 'h', 10)

#g.printv()
      
#path = shortestPath(graph, 'a', 'j')
path = shortestPath(g.vertices, 'a', 'j')

print(path)
