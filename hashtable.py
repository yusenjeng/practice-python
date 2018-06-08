class HashTable(object):
    def __init__(self, size):
        self.slots = [None] * size
        self.data = [None] * size
        self.size = size

    def hashfunc(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return self.hashfunc(old_hash + 1, size)

    def put(self, key, value):
        hashvalue = self.hashfunc(key, len(self.slots))

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
        else:

            if self.slots[hashvalue] == key:
                self.data[hashvalue] = value
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))

                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(hashvalue, len(self.slots))

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = value
                else:
                    self.data[nextslot] = value

    def get(self, key):
        start_slot = self.hashfunc(key, len(self.slots))
        data = None
        stop = False
        found = False

        curr_slot = start_slot
        while self.slots[curr_slot] is not None and not found and not stop:
            if self.slots[curr_slot] == key:
                found = True
                data = self.data[curr_slot]
            else:
                curr_slot = self.rehash(key, len(self.slots))
                if curr_slot == start_slot:
                    stop = True
        return data

    def delete(self, key):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


if __name__ == '__main__':
    h = HashTable(5)
    h[1] = 'one'
    h[2] = 'two'
    h[3] = 'three'

    print(h[1])