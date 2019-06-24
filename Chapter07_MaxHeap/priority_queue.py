from Chapter07_MaxHeap.max_heap import MaxHeap
from Chapter03_Queue.base import Queuebase

class PriorityQueue(Queuebase):
    def __init__(self):
        self._max_heap = MaxHeap()

    def get_Size(self):
        return self._max_heap.size()

    def is_Empty(self):
        return self._max_heap.is_Empty()

    def get_Front(self):
        return self._max_heap._find_max()

    def enqueue(self, e):
        self._max_heap.add(e)

    def dequeue(self):
        return self._max_heap._extract_max()
