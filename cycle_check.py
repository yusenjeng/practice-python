

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def cycle_check_single_linked_list(startnode):

    slow_node = startnode
    fast_node = startnode

    while True:

        if slow_node.next_node is None:
            return False
        if fast_node.next_node is None or fast_node.next_node.next_node is None:
            return False

        slow_node = slow_node.next_node
        fast_node = fast_node.next_node.next_node

        print(slow_node.value, fast_node.value)

        if fast_node.value == slow_node.value:
            return True

    return False

# a-b-c-d-g-a
#      \e-f

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
# c.next_node = e
# e.next_node = f
d.next_node = g
# g.next_node = a


print( cycle_check_single_linked_list(a) )