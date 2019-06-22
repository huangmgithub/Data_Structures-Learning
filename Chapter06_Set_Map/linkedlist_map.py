from Chapter06_Set_Map.base import MapBase

class LinkedListMap(MapBase):
    class _Node:
        def __init__(self, key=None, value=None, next_node=None):
            self.key = key
            self.value = value
            self.next = next_node
        def __str__(self):
            return "Key:{},Value:{}".format(str(self.key), str(self.value))

    def __init__(self):
        self._dummy_head = self._Node()
        self._size = 0

    def get_Node(self, key):
        """获得节点"""
        cur = self._dummy_head.next
        while cur:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

    def get_Size(self):
        """大小"""
        return self._size

    def is_Empty(self):
        """是否为空"""
        if self._size == 0:
            return True
        return False

    def contains(self, key):
        """包含"""
        if self.get_Node(key):
            return True
        return False

    def get(self, key):
        """查询节点"""
        node = self.get_Node(key)
        return node.value if node is not None else None

    def add(self, key, value):
        """增加节点"""
        node = self.get_Node(key)
        if not node:
            self._dummy_head.next = self._Node(key, value, self._dummy_head.next)
            self._size += 1
        else:
            node.value = value  #重复则将新value替换旧的

    def remove(self, key):
        """删除节点"""
        prev = self._dummy_head
        while prev.next:
            if prev.next.key == key:
                break
            prev = prev.next

        if prev.next:
            delNode = prev.next
            prev.next = delNode.next
            delNode.next = None
            self._size += 1
            return delNode.value
        return None

    def set(self, key, value):
        """修改节点"""
        node = self.get_Node(key)
        if not node:
            raise ValueError("Key {} does not exist".format(str(key)))
        node.value = value

if __name__ == "__main__":
    with open('shakes.txt') as f:
        words = f.read()
    words = words.split()

    import time
    start_time = time.time()
    linked_list_map = LinkedListMap()
    for word in words:
        if linked_list_map.contains(word):
            linked_list_map.set(word, linked_list_map.get(word) + 1)
        else:
            linked_list_map.add(word, 1)
    for word in words:
        print("Key:{},Value:{}".format(word,str(linked_list_map.get(word))))

    print('Total words: ', len(words))
    print('Unique words: ', linked_list_map.get_Size())
    print('Total Time： %s' % str(time.time() - start_time))

