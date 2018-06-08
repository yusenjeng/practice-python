from stack import *

graph = {
    'A': set(['B', 'C', 'E']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F', 'G']),
    'D': set(['B', 'E']),
    'E': set(['A', 'B', 'D']),
    'F': set(['C']),
    'G': set(['C'])
}


def dfs(graph, startnode, targetnode):
    if startnode not in graph:
        return None

    visited = set()
    stack = Stack()
    stack.push((startnode, [startnode]))

    while (not stack.isEmpty()) or (len(visited) != len(graph)):

        current_node, path = stack.pop()
        if current_node in visited:
            continue

        visited.add(current_node)
        next_nodes = graph[current_node]
        next_nodes = next_nodes - visited
        for node in next_nodes:
            if node == targetnode:
                return path+[node]
            stack.push((node, path+[node]))

        print('Visit node:', current_node, ' Stack:', stack.items)
    pass


if __name__ == '__main__':
    path = dfs(graph, 'D', 'F')
    print(path)


