from queue import *

graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}


def bfs(graph, startnode, targetnode):
    if not startnode in graph:
        return None

    visited = set()
    queue = Queue()
    queue.enqueue((startnode, [startnode]))

    while (not queue.isEmpty()) or (len(visited) != len(graph)):

        current_node, path = queue.dequeue()
        if current_node in visited:
            continue

        visited.add(current_node)
        next_nodes = graph[current_node]
        for node in next_nodes:
            if node == targetnode:
                return path + [node]
            queue.enqueue((node, path + [node]))

        print('Visit node:', current_node, ' Queue:', queue.items)
    pass


if __name__ == '__main__':
    path = bfs(graph, 'D', 'G')
    print(path)
