class Queuebase:
    def enqueue(self, e):
        """入队"""
        raise NotImplementedError
    def dequeue(self):
        """出队"""
        raise NotImplementedError
    def get_Front(self):
        """获得队首元素"""
        raise NotImplementedError
    def get_Size(self):
        """获得队列内元素数量"""
        raise NotImplementedError
    def is_Empty(self):
        """查看队列是否为空"""
        raise NotImplementedError

