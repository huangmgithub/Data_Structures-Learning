class BST:
    class _Node:
        def __init__(self, e):
            self.e = e
            self.right = None
            self.left = None

    def __init__(self):
        self._root = None
        self._size = 0

    def get_Size(self):
        return self._size

    def is_Empty(self):
        if self._size == 0:
            return True
        return False

    def add(self, e):
        self._root = self._add(self._root, e)

    def _add(self, node, e):
        """向以node为根的二分搜索树中插入元素E,递归实现"""
        # # 递归终止条件
        # if node.e == e:
        #     return
        # elif node.e > e and not node.left:
        #     node.left = self._Node(e)
        #     self._size += 1
        #     return
        # elif node.e < e and not node.right:
        #     node.right = self._Node(e)
        #     self._size += 1
        #     return
        # # 递归条件
        # if node.e > e:
        #     self._add(node.left, e)
        # else:
        #     self._add(node.right, e)

        #另一种简单写法
        if not node:
            self._size += 1
            return self._Node(e)
        if node.e > e:
            node.left = self._add(node.left, e)
        else:
            node.right = self._add(node.right, e)

        return node

    def contains(self, e):
        """二分搜索树中是否包含元素e"""
        return self._contains(self._root, e)

    def _contains(self, node, e):
        """查看以node为根的二分搜索树中是否包含元素e, 递归实现"""
        if not node:
            return False
        if node.e == e:
            return True
        elif node.e < e:
            return self._contains(node.left, e)
        else:
            return self._contains(node.right, e)

    def preOrder(self):
        """二分搜索树的前序遍历"""
        self._preOrder(self._root)

    def _preOrder(self, node):
        """前序遍历以node为根的二分搜索树，递归算法"""
        if not node:
            return
        print(node.e)
        self._preOrder(node.left)
        self._preOrder(node.right)

    def inOrder(self):
        """二分搜索树的中序遍历"""
        self._inOrder(self._root)

    def _inOrder(self, node):
        if not node:
            return
        self._inOrder(node.left)
        print(node.e)
        self._inOrder(node.right)

    def postOrder(self):
        """二分搜索树的后序遍历"""
        self._postOrder(self._root)

    def _postOrder(self, node):
        if not node:
            return
        self._postOrder(node.left)
        self._postOrder(node.right)
        print(node.e)


    def generateBSTString(self, node, depth, res):
        """生成以node为根节点，深度为depth的描述二叉树的字符串"""
        if not node:
            res.append(self.generateDepthString(depth) + "None\n")
            return
        res.append(self.generateDepthString(depth) + str(node.e) + "\n")
        self.generateBSTString(node.left, depth + 1, res)
        self.generateBSTString(node.right, depth + 1, res)

    def generateDepthString(self, depth):
        stringList = []
        for i in range(depth):
            stringList.append("--")
        return "".join(stringList)

    def __str__(self):
        stringList = []
        self.generateBSTString(self._root, 0, stringList)
        return "".join(stringList)


if __name__ == "__main__":
    bst = BST()
    nums = [5,1,6,8,9,2,10]
    for i in nums:
        bst.add(i)

    bst.preOrder()

    bst.inOrder()









