class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.connectedTo = {}
        self.prev_vertex = None

    def addNeighbor(self, neighborId, weight=0):
        self.connectedTo[neighborId] = weight

    def getNeighbors(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighborId):
        return self.connectedTo[neighborId]

    def __str__(self):
        return str(self.id) + ' connected to ' + str(self.connectedTo.keys())


class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def addVertex(self, id):
        self.num_vertices += 1
        newVertex = Vertex(id)
        self.vertices[id] = newVertex
        return newVertex

    def addEdge(self, fromId, toId, weight=0):
        fromVertex = self.getVertex(fromId)
        toVertex = self.getVertex(toId)
        if fromVertex is None:
            fromVertex = self.addVertex(fromId)
        if toVertex is None:
            toVertex = self.addVertex(toId)
        fromVertex.addNeighbor(toId, weight)

    def getVertex(self, id):
        if id in self.vertices:
            return self.vertices[id]
        return None

    def getVertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values)

    def __contains__(self, id):
        return id in self.vertices



if __name__ == '__main__':
    g = Graph()

    for i in range(6):
        g.addVertex(i)

    g.addEdge(0, 1, 10)

    g.addEdge(0, 9, 10)

    print(g.getVertices())
    print(g.getVertex(0))
