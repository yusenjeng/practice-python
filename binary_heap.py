class BinaryHeap(object):
    def __init__(self):
        self.heap = []
        self.size = 0
        pass

    def bubble_up(self, index):
        parent_index = self.get_parent(index)
        while parent_index >= 0:

            if self.heap[index] < self.heap[parent_index]:
                tmp = self.heap[index]
                self.heap[index] = self.heap[parent_index]
                self.heap[parent_index] = tmp

            index = parent_index
            parent_index = self.get_parent(parent_index)

    def get_parent(self, index):
        return (index - 1) // 2

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.bubble_up(self.size-1)


    def get_min_child(self, index):
        child_index = index * 2 + 1
         if child_index + 1 >= self.size:
            return child_index
        if self.heap[child_index] < self.heap[child_index + 1]:
            return child_index
        return child_index + 1

    def bubble_down(self, index=0):
        while index * 2 + 1 < self.size:
            child_index = self.get_min_child(index)

            if self.heap[index] > self.heap[child_index]:
                tmp = self.heap[index]
                self.heap[index] = self.heap[child_index]
                self.heap[child_index] = tmp

            index = child_index

    def delete_min(self):
        ret = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self.bubble_down(0)
        return ret

    def buildHeap(self, alist):

        index = (len(alist) - 1) // 2

        self.size = len(alist)
        self.heap = alist
        while index >= 0:
            self.bubble_down(index)
            index -= 1

    def findMin(self):
        return self.heap[0]

    def isEmpty(self):
        return self.size < 1

    def size(self):
        return self.size

    def show(self):
        print(self.heap)


if __name__ == '__main__':

    heap = BinaryHeap()
    heap.buildHeap([9, 6, 5, 2, 3, 1, 4, 8])
    heap.show()
    heap.delete_min()
    heap.show()
    heap.delete_min()
    heap.show()

    heap = BinaryHeap()
    heap.insert(9)
    heap.insert(6)
    heap.insert(5)
    heap.insert(2)
    heap.insert(3)
    heap.insert(1)
    heap.insert(4)
    heap.insert(8)
    heap.show()
