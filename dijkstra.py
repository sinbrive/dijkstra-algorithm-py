
# directed weighted graph
graph = {'a':{'b':10,'c':3},
         'b':{'c':1,'d':2},
         'c':{'b':4,'d':8,'e':2},
         'd':{'e':7},
         'e':{'d':9}
        }

# undirected weighted graph (SNT example)
graph2 = {'a':{'b':8,'c':6.5, 'i':6.7, 'f':7},
         'b':{'c':6.5},
         'c':{'d':4},
         'd':{'e':6, 'i':4},
         'e':{'j':10},
         'f':{'g':2.5},
         'g':{'h':4.5, 'i':5.5},
         'h':{'j':10},
         'i':{'h':7},
         'j':{'h':10, 'e':10}
        }

def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unVisited = graph
    infinity = 9999999
    path = []
  
    # initialisation : 0 for start and infinity for other
    for node in unVisited:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    # go through unvisited nodes
    while unVisited:
        focusNode = None
        # select focus node (that with the shortest distance)
        for node in unVisited:
            if focusNode is None:
                focusNode = node
            elif shortest_distance[node] < shortest_distance[focusNode]:
                focusNode = node
        # for this focus node, check each children weight (= distance(focus, child))
        for childNode, weight in graph[focusNode].items():
            if weight + shortest_distance[focusNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[focusNode]
                predecessor[childNode] = focusNode
        # don't come back anymore to this focusNode
        unVisited.pop(focusNode)
      
    print('distance from start:'+str(shortest_distance), '\n')
    print('predecessors:'+str(predecessor), '\n')

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]), '\n')
        print('The path is ' + str(path))


dijkstra(graph2, 'a', 'j')
