from Chapter08_SegmentTree.segment_tree import SegmentTree

class NumArray:
    def __init__(self, arr, merger = lambda x,y : x+y):
        self.segment_tree = SegmentTree(arr, merger)

    def sum_range(self, i, j):
        return self.segment_tree.query(i, j)

class NumArray2:
    def __init__(self, arr):
        """
        sum统计前i个元素的和
        sum[0] = 0 sum[1] = array[0]
        sum[i] = arr[0..i - 1]的和
        :param arr:
        """
        self.sum = [None] * (len(arr) +1)
        self.sum[0] = 0
        for i in range(1, len(arr) + 1):
            self.sum[i] = self.sum[i - 1] + arr[i - 1]

    def sum_range(self, i, j):
        return self.sum[j + 1] - self.sum[i]


if __name__ == "__main__":

    nums = [-2, 0, 3, -5, 2, -1]
    # num_array = NumArray(nums)
    # print(num_array.sum_range(0, 2))
    # print(num_array.sum_range(2, 5))
    # print(num_array.sum_range(0, 5))

    num_array_2 = NumArray2(nums)
    print(num_array_2.sum_range(0, 2))
    print(num_array_2.sum_range(2, 5))
    print(num_array_2.sum_range(0, 5))