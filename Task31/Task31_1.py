   # p - position
# 2p - left child 2p + 1 right child
from typing import List


class BinHeap:

    def __init__(self) -> None:
        self.heap_list: List[int] = [0]
        self.current_size: int = 0

    def perc_up(self, i) -> None:  # if child id bigger than parent
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:   # if child id bigger than parent
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i //= 2

    def insert(self, k) -> None: # insert remain the same
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_down(self, i) -> None:
        while (i * 2) <= self.current_size:
            mc = self.max_child(i)   # detect the index of max child
            if self.heap_list[i] < self.heap_list[mc]: # if root is smaller than than biggest child - we swap
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    # def min_child(self, i) -> int:
    #     if i * 2 + 1 > self.current_size:
    #         return i * 2
    #     if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
    #         return i * 2
    #     else:
    #         return i * 2 + 1

    def max_child(self, i) -> int:   # DETECT MAX CHILD
        if i * 2 + 1 > self.current_size:
            return i * 2
        if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

    # def del_min(self) -> int:
    #     ret_val = self.heap_list[1]
    #     self.heap_list[1] = self.heap_list[self.current_size]
    #     self.current_size -= 1
    #     self.heap_list.pop()
    #     self.perc_down(1)
    #     return ret_val

    def del_max(self) -> int:  # method to delete max element. Equals to del_min but perc_down condition adjusted
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def build_heap(self, items: List[int]) -> None:
        i = len(items) // 2  # to detect location of the lowest level parents
        self.current_size = len(items)
        self.heap_list = [0] + items[:]
        while i > 0:
            self.perc_down(i)
            i -= 1



bh = BinHeap()
heap = bh.build_heap([17,3,2,7,26,1, 25, 100, 19])
print(bh.heap_list)
print(bh.del_max())
print(bh.heap_list)
