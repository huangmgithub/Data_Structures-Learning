from Chapter01_Array.array import Array
from Chapter03_Queue.base import Queuebase

class ArrayQueue(Queuebase):
    """数组队列"""
    def __init__(self,capacity=10):
        self._array = Array(capacity)
    def enqueue(self, e):
        """入队"""
        self._array.add_Last(e)
    def dequeue(self):
        """出队"""
        return self._array.remove_First()
    def get_Front(self):
        """获得队首元素"""
        return self._array.get_First()
    def get_Size(self):
        """获得队列内元素数量"""
        return self._array.get_Size()
    def is_Empty(self):
        """查看队列是否为空"""
        return self._array.is_Empty()
    def get_Capacity(self):
        """查看队列的容量"""
        return self._array.get_Capacity()
    def __str__(self):
        StringList = []
        StringList.append("Queue:size = %s, capacity = %d \n"
                          % (self.get_Size(), self.get_Capacity()))
        StringList.append('front [')
        for i in range(self.get_Size()):
            StringList.append("%s" % self._array.get(i))
            if i != self.get_Size() - 1:
                StringList.append(",")
        StringList.append('] tail')
        return "".join(StringList)

class LoopQueue(Queuebase):
    """循环队列"""
    def __init__(self, capacity=10):
        """浪费一个空间"""
        self._data = [None] * (capacity + 1)
        self._front = 0
        self._tail = 0
        self._size = 0
    def get_Capacity(self):
        """查看队列的容量"""
        return len(self._data) - 1
    def is_Empty(self):
        """查看队列是否为空"""
        if self._front == self._tail:
            return True
        return False
    def get_Size(self):
        """获得队列内元素数量"""
        return self._size
    def enqueue(self, e):
        """入队"""
        if (self._tail + 1) % len(self._data) == self._front:
            self._resize(self.get_Capacity() * 2)
        self._data[self._tail] = e
        self._tail  = (self._tail + 1) % len(self._data) #处于循环队列
        self._size += 1
    def dequeue(self):
        """出队"""
        if self.is_Empty():
            raise Exception('cannot dequeue from a empty queue')
        ret = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._size == self.get_Capacity() // 4 and self.get_Capacity() // 2 != 0:
            self._resize(self.get_Capacity() // 2)
        return ret
    def get_Front(self):
        """获得队首元素"""
        if self.is_Empty():
            raise Exception('Queue is empty')
        return self._data[self._front]
    def _resize(self, newCapacity):
        """调整队列容量"""
        newData = [None] * (newCapacity + 1)
        for i in range(self._size):
            newData[i] = self._data[(i + self._front) % len(self._data)]  #front不在0的位置
        self._data = newData
        self._front = 0
        self._tail = self._size
    def __str__(self):
        StringList = []
        StringList.append("Loop_Queue:size = %s, capacity = %d \n"
                          % (self.get_Size(), self.get_Capacity()))
        StringList.append('front [')
        for i in range(self._size):
            StringList.append("%s" % self._data[(i + self._front) % len(self._data)])
            if i != self._size - 1:
                StringList.append(",")
        StringList.append('] tail')
        return "".join(StringList)

if __name__ == "__main__":
    # array_queue = ArrayQueue()
    # for i in [1,3,5,1,9,8,1]:
    #     array_queue.enqueue(i)
    #
    # loop_queue = LoopQueue()
    # for i in range(10):
    #     loop_queue.enqueue(i)
    #     if i % 3 == 2:
    #         loop_queue.dequeue()
    #     print(loop_queue)

    # 数组队列和循环队列的比较
    from time import time
    import random
    def test_enqueue(queue, opCount):
        start_time = time()
        for i in range(opCount):
            queue.enqueue(random.randint(1, 2000))
        return time() - start_time

    def test_dequeue(queue, opCount):
        start_time = time()
        for i in range(opCount):
            queue.dequeue()
        return time() - start_time

    opCount = 10000
    array_queue = ArrayQueue()
    loop_queue = LoopQueue()

    print('array_queue enqueue: %s' % test_enqueue(array_queue, opCount))
    print('loop_queue enqueue: %s' % test_enqueue(loop_queue, opCount))

    print('array_queue dequeue: %s' % test_dequeue(array_queue, opCount))
    print('loop_queue dequeue: %s' % test_dequeue(loop_queue, opCount))
