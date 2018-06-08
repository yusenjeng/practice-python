def bubble_sort(ary):
    for n in range(len(ary), 0, -1):
        swapped = False
        for j in range(0, n - 1):
            if ary[j] > ary[j + 1]:
                ary[j], ary[j + 1] = ary[j + 1], ary[j]
                swapped = True

        if not swapped:
            break


def selection_sort(ary):
    for n in range(len(ary), 0, -1):
        max_i = 0
        for i in range(0, n):
            if ary[i] > ary[max_i]:
                max_i = i

        ary[max_i], ary[n - 1] = ary[n - 1], ary[max_i]


def insertion_sort(ary):
    for n in range(1, len(ary)):
        for i in range(n, 0, -1):
            if ary[i] < ary[i - 1]:
                ary[i], ary[i - 1] = ary[i - 1], ary[i]


def merge_sort(ary):
    if len(ary) > 1:
        mid = len(ary) / 2
        left_half = ary[:mid]
        right_half = ary[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                ary[k] = left_half[i]
                i += 1
            else:
                ary[k] = right_half[j]
                j += 1

            k += 1

        while i < len(left_half):
            ary[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            ary[k] = right_half[j]
            j += 1
            k += 1


def quick_sort(ary):
    quick_split(ary, 0, len(ary) - 1)


def quick_split(ary, head, tail):
    if head < tail:
        split = partition(ary, head, tail)
        quick_split(ary, head, split - 1)
        quick_split(ary, split + 1, tail)


def partition(ary, head, tail):
    pivot = ary[head]
    left_mark = head + 1
    right_mark = tail

    done = False

    while not done:
        while left_mark <= right_mark and ary[left_mark] <= pivot:
            left_mark += 1

        while right_mark >= left_mark and ary[right_mark] >= pivot:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            ary[left_mark], ary[right_mark] = ary[right_mark], ary[left_mark]

    ary[head], ary[right_mark] = ary[right_mark], ary[head]
    return right_mark


ary = [9, 8, 6, 5, 3, 2, 1, 4, 7]
bubble_sort(ary)
print(ary)

ary = [9, 8, 6, 5, 3, 2, 1, 4, 7]
selection_sort(ary)
print(ary)

ary = [9, 8, 6, 5, 3, 2, 1, 4, 7]
insertion_sort(ary)
print(ary)

ary = [9, 8, 6, 5, 3, 2, 1, 4, 7]
merge_sort(ary)
print(ary)

ary = [9, 8, 6, 5, 3, 2, 1, 4, 7]
quick_sort(ary)
print(ary)