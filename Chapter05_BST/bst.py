from collections import deque

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

    def preOrderNR1(self):
        """非递归实现前序遍历,DFS"""
        res = []
        if not self._root:
            return res

        stack = []
        stack.append(self._root)
        while stack:
            cur = stack.pop()
            res.append(cur.e)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

    def preOrderNR2(self):
        """前序②"""
        res = []
        if not self._root:
            return res

        stack = []
        cur = self._root
        stack.append(cur)
        while cur or stack:
            while cur:
                res.append(cur.e)
                if cur != self._root:
                    stack.append(cur)
                print(cur.e)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right

        return res

    def inOrderNR(self):
        """非递归实现中序遍历"""
        res = []
        if not self._root:
            return res

        stack = []
        cur = self._root
        stack.append(cur)
        while cur or stack:
            while cur:
                if cur != self._root:
                    stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.e)
            cur = cur.right
        return res

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

    def postOrderNR(self):
        """非递归实现后序遍历"""
        res = []
        if not self._root:
            return res

        stack = []
        output = []
        stack.append(self._root)
        while stack:
            cur = stack.pop()
            output.append(cur.e)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        while output:
            res.append(output.pop())
        return res

    def levelOrder(self):
        """层序遍历,BFS"""
        queue = deque()
        queue.append(self._root)
        while queue:
            cur = queue.popleft()
            print(cur.e)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

    def minimum(self):
        """二分搜索树节点最小值"""
        if not self._size:
            raise ValueError("BST is empty")
        return self._minimum(self._root).e

    def _minimum(self, node):
        if not node.left:
            return node
        return self._minimum(node.left)

    def maximum(self):
        """二分搜索树节点最大值"""
        if not self._size:
            raise ValueError("BST is empty")
        return self._maximum(self._root).e

    def _maximum(self, node):
        if not node.right:
            return node
        return self._maximum(node.right)

    def removeMin(self):
        """删除二分搜索树节点最小值"""
        ret = self.minimum()
        self._root = self._removeMin(self._root)
        return ret

    def _removeMin(self, node):
        if not node.left:
            rightNode = node.right
            node.right = None
            self._size -= 1
            return rightNode
        node.left = self._removeMin(node.left)
        return node

    def removeMax(self):
        """删除二分搜索树节点最大值"""
        ret = self.maximum()
        self._root = self._removeMax(self._root)
        return ret

    def _removeMax(self, node):
        if not node.right:
            leftNode = node.left
            node.left = None
            self._size -= 1
            return leftNode
        node.right = self._removeMax(node.right)
        return node

    def remove(self, e):
        """删除任意节点"""
        self._root = self._remove(self._root, e)


    def _remove(self, node,  e):
        if not node:
            return None
        if node.e > e:
            node.left = self._remove(node.left, e)
            return node
        elif node.e < e:
            node.right = self._remove(node.right, e)
            return node
        else: # node.e == e
            #待删除节点左子树为空的情况
            if not node.left:
                rigthNode = node.right
                node.right = None
                self._size -= 1
                return rigthNode
            # 待删除节点右子树为空的情况
            if not node.right:
                leftNode = node.left
                node.left = None
                self._size -= 1
                return leftNode
            # 待删除节点左右子树都不为空的情况
            # 找到比待删除节点大的最小节点，即待删除节点右子树的最小节点
            # 用这个节点代替待删除节点的位置
            successor = self._minimum(node.right)
            successor.right = self._removeMin(node.right)
            successor.left = node.left
            node.left = node.right = None

            return successor

    def generateBSTString(self, node, depth, res):
        """生成以node为根节点，深度为depth的描述二叉树的字符串"""
        if not node:
            res.append(self.generateDepthString(depth) + "None\n")
            return
        res.append(self.generateDepthString(depth) + str(node.e) + "\n")
        self.generateBSTString(node.left, depth + 1, res)
        self.generateBSTString(node.right, depth + 1, res)

    def generateDepthString(self, depth):
        res = ''
        for i in range(depth):
            res += '--'
        return res

    def __str__(self):
        stringList = []
        self.generateBSTString(self._root, 0, stringList)
        return "".join(stringList)


if __name__ == "__main__":
    bst = BST()
    nums = [28,16,13,22,30,29,43]
    for i in nums:
        bst.add(i)

    # bst.preOrder()
    # bst.preOrderNR()

    # bst.inOrder()
    # print(bst.inOrderNR())

    bst.postOrder()
    print(bst.postOrderNR())

    # bst.levelOrder()

    # print(bst.removeMax())
    # print(bst.removeMin())

    # bst.preOrder()
    # print('\n')
    # print(bst.preOrderNR1())
    # print('\n')
    # print(bst.preOrderNR2())
