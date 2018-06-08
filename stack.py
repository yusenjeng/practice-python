

class Stack(object):
        def __init__(self):
            self.items = []

        def push(self, element):
                self.items.append(element)

        def pop(self):
                return self.items.pop()

        def size(self):
                return len(self.items)

        def isEmpty(self):
                return  self.items == []

        def peek(self):
                if self.isEmpty() == True:
                    return None
                return self.items[-1]


if __name__ == '__main__':
    stack = Stack()

    print( stack.isEmpty() )
    stack.push(1)
    print( stack.peek() )
    stack.push(2)
    print( stack.size() )
    print( stack.isEmpty() )
    print( stack.pop() )
    print( stack.size() )
    print( stack.pop() )
    print( stack.peek() )
