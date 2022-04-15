

'''
max = 0
for node in graph:
  for i in graph[node].items():
    max = max + i[1]
max += 1
print(max)

list=[node for node in graph]
list2 = [[graph[node][s] for s in graph[node] ] for node in graph ]
print( list2)
'''

# get shorted distances and predecessors vs. start node 
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

path = shortestPath(graph, 'a', 'j')

print(path)

      
