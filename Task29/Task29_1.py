

def binary_search_rec(array, item, first = 0, last=None):
    if last is None:
        last = len(array) - 1
    if first > last:
        return False

    midpoint = (first + last) // 2
    if array[midpoint] == item:
        return midpoint
    if item < array[midpoint]:
        binary_search_rec(array, item, first = 0, last = midpoint-1)
    return binary_search_rec(array, item, midpoint+1, last)


print(binary_search_rec([-100, -1.5, 2, 3, 4, 6, 31, 101], 6))