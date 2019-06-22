from Chapter06_Set_Map.base import MapBase

class BSTMap(MapBase):
    class _Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

        def __str__(self):
            return "Key:{},Value:{}".format(str(self.key), str(self.value))

    def __init__(self):
        self._root = None
        self._size = 0

    def get_Size(self):
        """大小"""
        return self._size

    def is_Empty(self):
        """是否为空"""
        if self._size == 0:
            return True
        return False

    def add(self, key ,value):
        self._root = self._add(self._root, key, value)

    def _add(self, node, key, value):
        if not node:
            self._size += 1
            return self._Node(key, value)
        if node.key > key:
            node.left = self._add(node.left, key, value)
        elif node.key < key:
            node.right = self._add(node.right, key, value)
        else:
            node.value = value
        return node

    def get_Node(self, node, key):
        if not node:
            return None
        if node.key == key:
            return node
        elif node.key > key:
            return self.get_Node(node.left, key)
        else:
            return self.get_Node(node.right, key)

    def contains(self, key):
        """包含"""
        if self.get_Node(self._root, key):
            return True
        return False

    def get(self, key):
        node = self.get_Node(self._root, key)
        return node.value if node is not None else None

    def set(self, key, value):
        node = self.get_Node(self._root, key)
        if not node:
            raise ValueError("Key {} does not exist".format(str(key)))
        node.value = value

    def remove(self, key):
        node = self.get_Node(self._root, key)
        if node:
            self._root = self._remove(self._root, key)
            return node.value
        return None

    def _remove(self, node, key):
        if not node:
            return None
        if node.key > key:
            node.left = self._remove(node.left, key)
            return node
        elif node.key < key:
            node.right = self._remove(node.right, key)
            return node
        else:
            # 待删除节点左子树为空的情况
            if not node.left:
                rightNode = node.right
                node.right = None
                self._size -= 1
                return rightNode
            # 待删除节点右子树为空的情况
            if not node.right:
                leftNode = node.left
                node.left = None
                return leftNode
            # 待删除节点左右子树都不为空的情况
            # 找到比待删除节点大的最小节点，即待删除节点右子树的最小节点
            # 用这个节点代替待删除节点的位置
            successor = self._minimum(node.right)
            successor.right = self._removeMin(node.right)
            successor.left = node.left
            node.left = node.right = None

            return successor

    def minimum(self):
        if not self._size:
            raise ValueError("BST is empty")
        return self._minimum(self._root).key

    def _minimum(self, node):
        if not node.left:
            return node
        return self._minimum(node.left)

    def removeMin(self):
        """删除二分搜索树节点最小值"""
        ret = self.minimum()
        self._root = self._removeMin(self._root)
        return ret

    def _removeMin(self, node):
        """删除二分搜索树节点最小值"""
        if not node.left:
            rightNode = node.right
            node.right = None
            self._size -= 1
            return rightNode
        node.left = self._removeMin(node.left)
        return node

if __name__ == "__main__":
    with open('shakes.txt') as f:
        words = f.read()
    words = words.split()

    import time
    start_time = time.time()
    bst_map = BSTMap()
    for word in words:
        if bst_map.contains(word):
            bst_map.set(word, bst_map.get(word) + 1)
        else:
            bst_map.add(word, 1)
    for word in words:
        print("Key:{},Value:{}".format(word,str(bst_map.get(word))))

    print('Total words: ', len(words))
    print('Unique words: ', bst_map.get_Size())
    print('Total Time： %s' % str(time.time() - start_time))

