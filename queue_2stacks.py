from stack import *


class Queue2Stacks(object):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, element):
        self.stack1.push(element)

    def dequeue(self):
        if self.isEmpty():
            return None

        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push( self.stack1.pop() )

        return self.stack2.pop()

    def size(self):
        return self.stack1.size() + self.stack2.size()

    def isEmpty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()


if __name__ == '__main__':
    que = Queue2Stacks()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    print( que.size(), que.isEmpty() )
    print( que.dequeue() )
    print( que.dequeue() )
    que.enqueue(4)
    que.enqueue(5)
    print( que.dequeue() )
    print( que.dequeue() )
    print( que.dequeue() )
    print( que.size(), que.isEmpty() )
