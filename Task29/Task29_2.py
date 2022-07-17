import timeit

def fibonacci_search(array, item):
    size = len(array)
    start = -1
    f0 = 0
    f1 = 1
    f2 = 1
    while (f2 < size):  # we move over fibonacci numbers to reach first number bigger than size of searchable array
        f0 = f1
        f1 = f2
        f2 = f1 + f0
    while (f2 > 1):  # when f2 is 1 or smaller, it means we come close to the end ot the list. Therefore code at line 24 start to work:
        index = min(start + f0, size - 1)  # choose minimum between sum (start + maxf0) and (size -1)
        if array[index] < item:  # if element of detected index smaller than searching item we decrease fibonacci numbers at one step
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif array[index] > item: # if element of detected index bigger than searching item we decrease fibonacci numbers at two steps
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (array[size - 1] == item):  # to check if the last elements is the item we search
        return size - 1
    return -1 # which means not found

print(fibonacci_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 101))


# _______ COMPARISON WITH SEQUENTIAL AND BINARY SEARCH __________
# the best is binary search
# second is linear search
# third is fibonacci search


def sequential_search(array, item):
    pos = 0
    found = False
    while pos < len(array) and not found:
        if array[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


def binary_search(array, item):
    first = 0
    last = len(array) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if array[midpoint] == item:
            found = True
        else:
            if item < array[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found


if __name__ == "__main__":
    seq_timer = timeit.timeit(
        stmt="sequential_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 6)",
        number=100,
        setup="from __main__ import sequential_search"
    )
    print(seq_timer)

    bin_timer = timeit.timeit(
        stmt="binary_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 6)",
        number=100,
        setup="from __main__ import binary_search"
    )
    print(bin_timer)

    fibonacci_search_timer = timeit.timeit(
        stmt="fibonacci_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 6)",
        number=100,
        setup="from __main__ import fibonacci_search"
    )
    print(fibonacci_search_timer)