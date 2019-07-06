from Chapter08_SegmentTree.segment_tree import SegmentTree

class NumArray:
    """
    update每一次都是O(n)的复杂度
    m次就是m × n的复杂度，leetcode显示超时
    """
    def __init__(self, arr):
        """
        sum统计前i个元素的和
        sum[0] = 0 sum[1] = array[0]
        sum[i] = arr[0..i - 1]的和
        :param arr:
        """
        self._data = [None] * (len(arr))
        for i in range(len(arr)):
            self._data[i] = arr[i]

        self.sum = [None] * (len(arr) +1)
        self.sum[0] = 0
        for i in range(1, len(arr) + 1):
            self.sum[i] = self.sum[i - 1] + arr[i - 1]

    def sum_range(self, i, j):  #O(n)
        return self.sum[j + 1] - self.sum[i]

    def update(self, index, val): # 最坏O(n)
        self._data[index] = val
        for i in range(index + 1, len(self.sum)):
                self.sum[i] = self.sum[i - 1] + self._data[i - 1]

class NumArray2:
    """使用线段树解决此问题"""
    def __init__(self, arr, merger = lambda x,y : x+y):
        self.segment_tree = SegmentTree(arr, merger)

    def sum_range(self, i, j): # O(logn)
        return self.segment_tree.query(i, j)

    def update(self, index, val): # O(logn)
        """更新index的值"""
        self.segment_tree.set(index, val)

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    num_array = NumArray(nums)
    print(num_array.sum_range(0,3))

    num_array2 = NumArray2(nums)
    print(num_array2.sum_range(0, 3))