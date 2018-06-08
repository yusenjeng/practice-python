

def pair_sum(data_array, target_value):
  if not  isinstance(target_value, int):
    raise TypeError('The target_value value must be a integer')
  if not  isinstance(data_array, list):
    raise TypeError('The data_array  must be a list')
  if len(data_array) < 1:
    raise ValueError('The length of data_array must be greater than 0.')

  count = 0;
  good_pairs = {}
  for i in range(len(data_array)):
    for j in range(i, len(data_array)):
      if data_array[i]+data_array[j] == target_value:
        key1 = (data_array[i], data_array[j])
        key2 = (data_array[j], data_array[i])
        if key1 in good_pairs:
          continue
        else:
          count += 1
          good_pairs[key1] = True
          good_pairs[key2] = True

  return count


def pair_sum_better(data_array, target_value):
  if not  isinstance(target_value, int):
    raise TypeError('The target_value value must be a integer')
  if not  isinstance(data_array, list):
    raise TypeError('The data_array  must be a list')
  if len(data_array) < 1:
    raise ValueError('The length of data_array must be greater than 0.')

  visited = set()
  valid_pairs = set()

  for i in range(len(data_array)):
    needed =  target_value - data_array[i]

    if needed in visited:
      valid_pairs.add( (min(data_array[i], needed), max(data_array[i], needed)) )
    else:
      visited.add(data_array[i])

    pass

  print(valid_pairs)
  return len(valid_pairs)


print( pair_sum_better([1,2,3,1], 3) )
print( pair_sum_better([1,3,2,2], 4) )
print( pair_sum_better([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10) )