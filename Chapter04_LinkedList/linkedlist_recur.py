class LinkList:
    """递归实现链表的增删操作"""
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
        self.add(self._size - 1, e)

    def add(self, index, e):
        """在链表的index位置添加新的元素e"""
        if index < 0 or index > self._size:
            raise Exception("Illegal Index")
        # index = index + 1
        def add_recursion(self, head, index, e):
            if index == -1:
                addNode = self._Node(e)
                addNode.next = head.next
                head.next = addNode
            else:
                res = add_recursion(self, head.next, index - 1 , e)
                head.next = res
            return head
        add_recursion(self, self.dummy_head, index - 1, e)
        self._size += 1

    def remove(self, index):
        """从链表中删除第一个位置的元素"""
        if index < 0 or index > self._size:
            raise Exception("Illegal Index")
        def remove_recursion(head, index):
            if index == 0:
                delNode = head.next
                head.next = delNode.next
                delNode.next = None
            else:
                res = remove_recursion(head.next, index - 1)
                head.next = res
            return head
        res = remove_recursion(self.dummy_head, index)
        self._size -= 1

        return res

    def remove_First(self):
        """从链表中删除第一个位置的元素"""
        return self.remove(0)

    def remove_Last(self):
        """从链表中删除最后一个位置的元素"""
        return self.remove(self._size - 1)

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
    linked_list.remove_First()
    print(linked_list)
