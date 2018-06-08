import sys
import ctypes

class DynamicArray(object):

  def __init__(self):
    self.size = 0
    self.capacity = 1
    self.data = self.__make_array(self.capacity)

  def __len__(self):
    return self.size

  def __getitem__(self, index):

    if not (0 <= index < self.size):
      raise IndexError('Index is out of bound.')

    return self.data[index]

  def append(self, element):
    if self.size  >= self.capacity:
      self.__resize(2*self.capacity)    # 2x if the capacity is not enough

    self.data[self.size] = element
    self.size += 1
    pass

  def __resize(self, new_capacity):
    new_data = self.__make_array(new_capacity)
    for i in range(self.size):
      new_data[i] = self.data[i]
    self.data = new_data
    self.capacity = new_capacity
    pass

  def __make_array(self, capacity):
    return ( ctypes.py_object * capacity)()



arr = DynamicArray()

for i in range(90):
  arr.append(i)
  print('Len: {0:3d}; Capacity: {1:3d}; SysSize: {2:3d}'.format(len(arr), arr.capacity, sys.getsizeof(arr)))

a = 1
if not isinstance(a, str):
  raise TypeError('Input is not a string')
else:
  print(a)
