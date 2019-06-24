from Chapter01_Array.array import Array

class MaxHeap:
    def __init__(self, arr=None, capacity=None):
        if isinstance(arr, Array):
            self._data = arr
            # heapify
            for i in range(self._parent(arr.get_Size() - 1), -1, -1):
                self._sift_down(i)
            return
        if not capacity:
            self._data = Array()
        else:
            self._data = Array(capacity)

    def size(self):
        """返回堆中元素的个数"""
        return self._data.get_Size()

    def is_Empty(self):
        """返回布尔值，表示堆中是否为空"""
        return self._data.is_Empty()

    def _parent(self, index):
        """返回完全二叉树的数组表示中，一个索引所表示的元素的父节点的索引"""
        if index == 0:
            raise ValueError("index-0 doesn't have parent.")
        return (index - 1) // 2

    def _left_child(self, index):
        """返回该索引对应元素的左孩子的索引"""
        return index * 2 + 1

    def _right_child(self, index):
        """返回该索引对应元素的右孩子的索引"""
        return index * 2 + 2

    def add(self, e):
        """向堆中添加元素"""
        self._data.add_Last(e) # 添加
        self._sift_up(self._data.get_Size() - 1) # 上浮

    def _sift_up(self, k):
        """上浮，为满足堆的大小性质"""
        while k > 0 and self._data.get(self._parent(k)) < self._data.get(k):
            # 不可以是根节点元素(没有父节点) & 父节点元素小于该节点元素
            self._data.swap(k, self._parent(k))
            k = self._parent(k)

    def _find_max(self):
        """查找堆中的最大元素"""
        if not self._data.get_Size():
            raise ValueError("Can not find max when heap is empty.")
        return self._data.get(0)

    def _extract_max(self):
        """取出堆中的最大元素"""
        ret = self._find_max()
        self._data.swap(0, self._data.get_Size() - 1) #末尾元素与最大值交换位置
        self._data.remove_Last() #删除在末尾的最大值
        self._sift_down(0)
        return ret

    def _sift_down(self, k):
        """下移，为满足堆的大小性质"""
        while self._left_child(k) < self._data.get_Size():
            j = self._left_child(k)
            if j + 1 < self._data.get_Size() and self._data.get(j + 1) > self._data.get(j):
                # 判断是否存在右孩子，然后判断右孩子是否大于左孩子
                # data[j]是左孩子和右孩子中的最大值
                j = self._right_child(k)
            if self._data.get(k) >= self._data.get(j): #不大于
                break
            self._data.swap(k, j)
            k = j

    def replace(self, e):
        """取出堆中的最大元素，并且替换成元素e"""
        ret = self._find_max()
        self._data.set(0 ,e) #替换
        self._sift_down(0) #下移
        return ret

if __name__ == "__main__":
    # import random
    # n = 100000
    # max_heap = MaxHeap()
    # for i in range(n):
    #     max_heap.add(random.randint(0,2000))
    #
    # arr = []
    # for i in range(1000):
    #     arr.append(max_heap._extract_max())
    #
    # for i in range(1, 1000):
    #     if arr[i - 1] < arr[i]:
    #         raise Exception("Error")
    # print("Test MaxHeap completed.")

    # Test heapify
    import random
    n = 100000
    test_arr = Array()
    for i in range(n):
        test_arr.add_Last(random.randint(0, 2000))

    print(test_arr)
    max_heap = MaxHeap(test_arr)

    arr = []
    for i in range(1000):
        arr.append(max_heap._extract_max())

    for i in range(1, 1000):
        if arr[i - 1] < arr[i]:
            raise Exception("Error")
    print("Test MaxHeap completed.")
