
graph = {'a':{'b':10,'c':3},
         'b':{'c':1,'d':2},
         'c':{'b':4,'d':8,'e':2},
         'd':{'e':7},
         'e':{'d':9}
        }

graph2 = {'a':{'b':8,'c':6.5, 'i':6.7, 'f':7},
         'b':{'c':6.5},
         'c':{'d':4},
         'd':{'e':6, 'i':4},
         'e':{'j':10},
         'f':{'g':2.5},
         'g':{'h':4.5, 'i':5.5},
         'h':{'j':10},
         'i':{'d':4, 'h':7, 'g':5.5},
         'j':{'h':10, 'e':10}
        }

def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    nonVisited = graph
    infinity = 9999999
    path = []
    for node in nonVisited:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while nonVisited:
        focusNode = None
        for node in nonVisited:
            if focusNode is None:
                focusNode = node
            elif shortest_distance[node] < shortest_distance[focusNode]:
                focusNode = node

        for childNode, cost in graph[focusNode].items():
            if cost + shortest_distance[focusNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = cost + shortest_distance[focusNode]
                predecessor[childNode] = focusNode
        nonVisited.pop(focusNode)
      
    print(str(shortest_distance))
    print()
    print(str(predecessor))
    print()

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
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))


dijkstra(graph2, 'a', 'j')
