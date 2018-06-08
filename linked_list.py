
class Node(object):
    def __init__(self, value = 0):
        self.value = value
        self.nextnode = None

    def next(self):
        return self.nextnode



a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

print(a.value, a.nextnode.value, a)