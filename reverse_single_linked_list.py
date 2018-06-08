class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def reverse_single_linked_list(startnode):
    curr_node = startnode
    last_node = None
    while curr_node is not None:
        next_node = curr_node.next_node

        curr_node.next_node = last_node

        last_node = curr_node
        curr_node = next_node

    return last_node


def print_singled_list(startnode):
    curr_node = startnode
    while curr_node is not None:
        print(curr_node.value)
        curr_node = curr_node.next_node


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

print_singled_list(a)
head_node = reverse_single_linked_list(a)
print_singled_list(head_node)