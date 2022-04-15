'''
  dijkstra algo
  sinbrive 2022/04
'''

from graph import Graph


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

# using given graph
g = Graph(graph)

path = g.shortestPath('a', 'j')

print('with ready graph: ',path)

# using constructed graph
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


path = g.shortestPath('a', 'j')

print('with made graph:', path)

