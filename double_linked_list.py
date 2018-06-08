

class DoubleLinkedListNode(object):
    def __init__(self, value=''):
        self.value = value
        self.next_node = None
        self.prev_node = None


class DoubleLinkedList(object):

    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def insert(self, node):
        pass

    def delete(self, node):
        pass


a = DoubleLinkedListNode('a')
b = DoubleLinkedListNode('b')
c = DoubleLinkedListNode('c')

a.next_node = b
b.prev_node = a
b.next_node = c
c.prev_node = b