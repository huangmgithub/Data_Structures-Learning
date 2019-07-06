class SegmentTree:
    def __init__(self, arr, merger):
        """线段树相当于将数组用一棵树重新表示"""
        if not isinstance(arr,list) or not arr or not merger:
            raise ValueError('Can not initialize empty array.')
        self._data = arr[:]
        self._merger = merger  # 合并方式：最大值，最小值等功能
        self._tree = [None] * 4 * len(arr)
        self._build_segment_tree(tree_index = 0, l = 0, r = len(arr) - 1)

    def get_index(self, index):
        if index < 0 or index >= len(self._data):
            raise Exception('Get Failed, Index is illegal')
        return self._data[index]

    def get_size(self):
        return self._data.get_Size()

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _build_segment_tree(self, tree_index, l, r):
        """在tree_index的位置创建区间[l..r]的线段树"""
        if l == r:
            self._tree[tree_index] = self._data[l]
            return
        left_tree_index = self._left_child(tree_index)
        right_tree_index = self._right_child(tree_index)

        mid = (l + r) // 2
        self._build_segment_tree(left_tree_index, l, mid)
        self._build_segment_tree(right_tree_index, mid + 1, r)

        self._tree[tree_index] = self._merger(self._tree[left_tree_index], self._tree[right_tree_index])

    def query(self, query_l, query_r):
        """查询"""
        if query_l < 0 or query_l >= len(self._data) or \
                query_r < 0 or query_r >= len(self._data) or query_l > query_r:
            raise ValueError("Index is illegal")
        return self._query(0, 0, len(self._data) - 1, query_l, query_r)

    def _query(self, tree_index, l, r, query_l, query_r):
        """在以treeID为根的线段树中[l...r]的范围内，搜索区间[query_l...query_r]"""
        if l == query_l and r == query_r:
            return self._tree[tree_index]

        left_tree_index = self._left_child(tree_index)
        right_tree_index = self._right_child(tree_index)
        mid = (l + r) // 2

        if query_l >= mid + 1:
            return self._query(right_tree_index, mid + 1, r, query_l, query_r)
        elif query_r <= mid:
            return self._query(left_tree_index, l, mid, query_l, query_r)

        left_result = self._query(left_tree_index, l, mid, query_l, mid)
        right_result = self._query(right_tree_index, mid + 1, r, mid + 1, query_r)
        return self._merger(left_result, right_result)


    def set(self, index, e):
        """将index位置的值更新为e"""
        if index < 0 or index >= len(self._data):
            raise Exception('Get Failed, Index is illegal')
        self._data[index] = e
        self._set(0, 0, len(self._data) - 1, index, e)

    def _set(self, tree_index, l, r, index, e):
        """在tree_index为根的线段树中更新index的值为e"""
        if l == r:
            self._tree[tree_index] = e  #先更新最底层的索引的值
            return
        mid = (l + r) // 2
        left_tree_index = self._left_child(tree_index)
        right_tree_index = self._right_child(tree_index)

        if index >= mid + 1: #在右子树
            self._set(right_tree_index, mid + 1, r, index, e)
        else:
            self._set(left_tree_index, l, mid, index, e)

        #更新各个区间的索引的值
        self._tree[tree_index]  = self._merger(self._tree[left_tree_index], self._tree[right_tree_index])


    def __str__(self):
        res = []
        res.append('[')
        for i in range(len(self._tree)):
            res.append(str(self._tree[i]))
            if i != len(self._tree) - 1:
                res.append(",")
        res.append(']')
        return "".join(res)

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    merger = lambda a,b: a + b
    segment_tree = SegmentTree(nums, merger)
    print(segment_tree)
    print(segment_tree.query(0,2))

