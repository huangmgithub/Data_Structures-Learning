class LinkList:
    class _Node:
        """节点"""
        def __init__(self, e=None, next_node=None):
            self.e = e
            self.next = next_node
        def __str__(self):
            return str(self.e)

    def __init__(self):
        self.dummy_head = self._Node()
        self._size = 0

    def get_Size(self):
        """获得链表中元素"""
        return self._size

    def is_Empty(self):
        """返回链表是否为空"""
        if self._size == 0:
            return True
        return False

    def add_First(self, e):
        """在链表头添加新的元素e"""
        self.add(0, e)

    def add_Last(self, e):
        """在链表末尾添加新的元素e"""
        self.add(self._size, e)

    def add(self, index, e):
        """在链表的index位置添加新的元素e"""
        if index < 0 or index > self._size:
            raise Exception("Illegal Index")
        prev = self.dummy_head
        for i in range(index):
            prev = prev.next #一直向前移动
        node = self._Node(e)
        node.next = prev.next
        prev.next = node
        self._size += 1

    def get(self, index):
        """获得链表中第index个位置的元素e"""
        if index < 0 or index >= self._size:
            raise Exception("Illegal Index")
        cur = self.dummy_head.next
        for i in range(index):
            cur = cur.next
        return cur.e

    def get_First(self):
        """获得链表第一个元素"""
        return self.get(0)

    def get_Last(self):
        """获得链表最后一个元素"""
        return  self.get(self._size - 1)

    def set(self, index, e):
        """修改链表中第index个位置的元素e"""
        if index < 0 or index >= self._size:
            raise Exception("Illegal Index")
        cur = self.dummy_head.next
        for i in range(index):
            cur = cur.next
        cur.e = e

    def contains(self, e):
        """查找链表中是否有元素e"""
        cur = self.dummy_head.next
        while cur:
            if cur.e == e:
                return True
            cur = cur.next
        return False

    def remove(self, index):
        """从链表中删除index位置的元素"""
        if index < 0 or index >= self._size:
            raise Exception("Illegal Index")
        prev = self.dummy_head
        for i in range(index):
            prev = prev.next
        retNode = prev.next
        prev.next = retNode.next
        retNode.next = None
        self._size -= 1

        return retNode.e
    def remove_First(self):
        """从链表中删除第一个位置的元素"""
        return self.remove(0)

    def remove_Last(self):
        """从链表中删除最后一个位置的元素"""
        return self.remove(self._size - 1)

    def remove_Element(self, e):
        """删除链表中的元素"""
        prev = self.dummy_head
        while prev.next:
            if prev.next.e == e:
                delNode = prev.next
                prev.next = delNode.next
                delNode.next = None
            else:
                prev = prev.next

    def __str__(self):
        StringList = []
        cur = self.dummy_head.next
        while cur:
            StringList.append("%s->" % cur)
            cur = cur.next
        StringList.append("None")
        return "".join(StringList)

if __name__ == "__main__":
    linked_list = LinkList()
    for i in range(5):
        linked_list.add_First(i)
        print(linked_list)
    linked_list.add(2,666)
    print(linked_list)
    linked_list.remove_Element(2)
    print(linked_list)



