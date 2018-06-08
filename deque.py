

class Deque(object):
    def __init__(self):
        self.items = []

    def addFront(self, element):
        self.items.insert(0, element)

    def addRear(self, element):
        self.items.append(element)

    def removeFront(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def removeRear(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

deque = Deque()

deque.addFront(3)
deque.addFront(2)
deque.addFront(1)
deque.addRear(4)
deque.addRear(5)
deque.addRear(6)
print( deque.size(), deque.isEmpty() )
print( deque.removeFront() )
print( deque.removeFront() )
print( deque.removeFront() )
print( deque.removeRear() )
print( deque.removeRear() )
print( deque.removeRear() )
print( deque.size(), deque.isEmpty() )
