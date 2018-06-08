

class Queue(object):
    def __init__(self):
        self.items = []
        pass

    def enqueue(self, element):
        self.items.append(element)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []



if __name__ == '__main__':
    queue = Queue()
    print( queue.isEmpty() )
    print( queue.size() )

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print( queue.size() )
    print( queue.dequeue() )
    print( queue.dequeue() )
    print( queue.dequeue() )
    print( queue.dequeue() )
