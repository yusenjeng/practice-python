class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def nth_to_last_node(start_node, n):
    head_node = start_node
    tail_node = start_node

    while n > 1:
        tail_node = tail_node.next_node
        n -= 1

        if tail_node is None:
            raise LookupError('Length of the linked-list is shorter than n.')

    while tail_node.next_node is not None:
        head_node = head_node.next_node
        tail_node = tail_node.next_node

    return head_node.value


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e
e.next_node = f
f.next_node = g


print( nth_to_last_node(a, 3) )