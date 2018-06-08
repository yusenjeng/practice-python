from graph import Graph
from graph import Vertex
from queue import Queue


def buildGraph(filename):
    buckets = {}
    g = Graph()

    f = open(filename, 'r')
    for line in f:
        word = line[:-1]
        for i in range(len(line)):
            key = word[:i] + '_' + word[i+1:]
            # print(key, word)
            if key in buckets:
                buckets[key].append(word)
            else:
                buckets[key] = [word]

    for key in buckets.keys():
        for w1 in buckets[key]:
            for w2 in buckets[key]:
                if w1 != w2:
                    g.addEdge(w1, w2)
                    # print('add edge', w1, w2)

    f.close()
    return g


def bfs(g, start, end):
    vertex_queue = Queue()
    vertex_queue.enqueue(start)

    visited = set()
    visited.add(start.id)

    curr_vertex = None
    while vertex_queue.size() > 0:
        curr_vertex = vertex_queue.dequeue()

        if curr_vertex.id == end.id:
            break

        # print(curr_vertex.id, curr_vertex.getNeighbors())

        for nbr in curr_vertex.getNeighbors():
            if nbr in visited:
                continue
            v = g.getVertex(nbr)
            v.prev_vertex = curr_vertex
            vertex_queue.enqueue(v)

        visited.add(curr_vertex.id)
        print('visited size', len(visited))

    print('========')
    while curr_vertex is not None:
        print(curr_vertex.id)
        curr_vertex = curr_vertex.prev_vertex


g = buildGraph('4words.txt')
start = g.getVertex('FOOL')
end = g.getVertex('SAGE')

# print(start.id, start.getNeighbors())

bfs(g, start, end)
