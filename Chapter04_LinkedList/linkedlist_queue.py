from Chapter03_Queue.base import Queuebase

class LinkedListQueue(Queuebase):
    class _Node:
        """节点"""
        def __init__(self, e=None, next_node=None):
            self.e = e
            self.next = next_node
        def __str__(self):
            return str(self.e)

    def __init__(self):
        self._head = None
        self._tail = None #与队列的tail
        self._size = 0

    def get_Size(self):
        return self._size

    def is_Empty(self):
        if self._size == 0:
            return True
        return False

    def enqueue(self, e):
        # 说明self._head也为空
        if not self._tail:
            self._tail = self._Node(e)
            self._head = self._tail
        else:
            self._tail.next = self._Node(e)
            self._tail = self._tail.next

        self._size += 1

    def dequeue(self):
        if self.is_Empty():
            raise Exception('cannot dequeue from a empty queue')
        retNode = self._head
        self._head = self._head.next
        retNode.next = None
        if not self._head:
            self._tail = None

        self._size -=1
        return retNode.e

    def get_Front(self):
        """获得队首元素"""
        if self.is_Empty():
            raise Exception('cannot dequeue from a empty queue')
        return self._head.e

    def __str__(self):
        StringList = []
        StringList.append("Queue: front")
        cur = self._head
        while cur:
            StringList.append("%s->" % cur)
            cur = cur.next
        StringList.append("None tail")
        return "".join(StringList)

if __name__ == "__main__":
    queue = LinkedListQueue()
    for i in range(10):
        queue.enqueue(i)
        if i % 3 == 2:
            queue.dequeue()
        print(queue)