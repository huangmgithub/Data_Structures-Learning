class Array:
    def __init__(self, arr=None,capacity=10):
        if isinstance(arr,list):
            self._data = arr[:]
            self._size = len(arr)
            return
        self._data = [None] * capacity
        self._size = 0
    def get_Size(self):
        """获得数组内元素数量"""
        return self._size
    def get_Capacity(self):
        """获得数组容量"""
        return len(self._data)
    def is_Empty(self):
        """查看数组是否为空"""
        if self._size == 0:
            return True
        return False
    def add_First(self, element):
        """添加元素到开头"""
        self.add(0, element)
    def add_Last(self,element):
        """添加元素到末尾"""
        # if self._size == len(self._data):
        #     raise Exception('Append failed, Array is Full')
        # self._data[self._size] = element
        # self._size += 1
        # 相同的效果
        self.add(self._size, element)
    def add(self, index, element):
        """指定位置添加元素"""
        if index < 0 or index > self._size:
            raise Exception('Insert failed, Require index >=0 and index <= size')
        #调整数组大小
        if self._size == len(self._data):
            if self._size == 0:
                self._resize(1)
            else:
                self._resize(2 * len(self._data)) #扩容

        i = self._size - 1
        while i >= index:
            self._data[i+1] = self._data[i]
            i -= 1
        self._data[index] = element
        self._size += 1
    def get(self, index):
        """获得index索引位置的元素"""
        if index < 0 or index >= self._size:
            raise Exception('Get Failed, Index is illegal')
        return self._data[index]
    def get_Last(self):
        """获得数组最后一个元素"""
        return self.get(self._size - 1)
    def get_First(self):
        """获得数组第一个元素"""
        return self.get(0)
    def set(self, index, element):
        """修改index索引位置的元素"""
        if index < 0 or index >= self._size:
            raise Exception('Get Failed, Index is illegal')
        self._data[index] = element
    def contains(self, element):
        """查找arr内是否存在元素element,返回bool值"""
        for i in range(self._size):
            if self._data[i] == element:
                return True
        return False
    def find(self, element):
        """# 查找数组中第一个element元素所在的索引，如果不存在元素，则返回-1"""
        for i in range(self._size):
            if self._data[i] == element:
                return i
        return -1
    def find_All(self, element):
        """查找数组中element元素所在的全部索引，如果不存在元素，则返回-1"""
        index_List = []
        for i in range(self._size):
            if self._data[i] == element:
                index_List.append(i)
        if len(index_List) > 0:
            return index_List
        return []
    def remove(self, index):
        """删除index索引位置的元素，返回删除元素"""
        if index < 0 or index >= self._size:
            raise Exception('Insert failed, Require index >=0 and index <= size')
        ret = self._data[index]
        i = index + 1
        while i < self._size:
            self._data[i - 1] = self._data[i]
            i += 1
        self._size -= 1
        self._data[self._size] = None
        # 调整数组大小
        # len(self._data)如果为1，len(self._data)//2就会为0
        if (self._size == len(self._data) // 4 and len(self._data) // 2 != 0):  #缩容
            self._resize(len(self._data) // 2)
        return ret
    def remove_First(self):
        """删除第一个元素，返回删除元素"""
        return self.remove(0)
    def remove_Last(self):
        """删除最后一个元素，返回删除元素"""
        return self.remove(self._size - 1)
    def remove_Element(self, element):
        """删除第一个element元素（通过元素）"""
        index = self.find(element)
        if index == -1:
            raise Exception('Get Failed, Element not in Array')
        self.remove(index)
    def remove_All_Element(self, element):
        """删除全部的element元素（通过元素）"""
        index_List = self.find_All(element)
        if len(index_List) == 0:
            raise Exception('Get Failed, Element not in Array')
        for index in reversed(index_List):
            self.remove(index)
    def _resize(self, new_capacity):
        """调整数组容量"""
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
    def swap(self, i, j):
        """数组两元素交换"""
        if i < 0 or i >= self._size or j < 0 or j >= self._size:
            self._data[i], self._data[j] = self._data[j], self._data[i]
    def __str__(self):
        """自定义打印"""
        StringList = []
        StringList.append("Array:size = %s, capacity = %d \n"
                          % (self._size,len(self._data)))
        StringList.append('[')
        for i in range(self._size):
            StringList.append("%s" % self._data[i])
            if i != self._size - 1:
                StringList.append(",")
        StringList.append(']')
        return "".join(StringList)


if __name__ == "__main__":
    array = Array(capacity=7)
    for i in [1,3,5,1,9,8,1]:
        array.add_Last(i)

    print(array)




