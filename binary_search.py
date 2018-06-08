def binary_search(ary, tar):
    head = 0
    tail = len(ary) - 1

    found = False
    while head <= tail and not found:
        mid = (head + tail) / 2

        if ary[mid] == tar:
            found = True
        elif ary[mid] < tar:
            head = mid + 1
        elif ary[mid] > tar:
            tail = mid - 1

    return found


def binary_search_recursive(ary, tar):
    if len(ary) == 0:
        return False

    mid = len(ary) / 2
    if ary[mid] == tar:
        return True
    elif ary[mid] < tar:
        return binary_search_recursive(ary[mid+1:], tar)
    elif ary[mid] > tar:
        return binary_search_recursive(ary[:mid], tar)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(a, 0))
print(binary_search(a, 1))
print(binary_search(a, 3))
print(binary_search(a, 4))
print(binary_search(a, 11))

print(binary_search_recursive(a, 0))
print(binary_search_recursive(a, 1))
print(binary_search_recursive(a, 3))
print(binary_search_recursive(a, 4))
print(binary_search_recursive(a, 11))
