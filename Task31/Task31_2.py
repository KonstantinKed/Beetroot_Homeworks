# if I understood the task correct Priority Queue best implemetnation over heap
# In this matter enqueu is a insert and degueu is del_max (since the priority
# determines its value

from Task31_1 import BinHeap

class PriorityQueue(BinHeap):

    def __init__(self):
        super().__init__()

    def enqueue(self, a):
        self.insert(a)

    def dequeue(self):
        self.del_max()


pq = PriorityQueue()
pq.build_heap([1,15,25,32, 43,45,65,75,10,100])
print(pq.heap_list)
pq.enqueue(150)
print(pq.heap_list)
pq.dequeue()
print(pq.heap_list)

