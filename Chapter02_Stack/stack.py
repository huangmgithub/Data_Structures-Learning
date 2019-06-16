from Chapter02_Stack.base import Stackbase
from Chapter01_Array.array import Array

class ArrayStack(Stackbase):
    def __init__(self,capacity=0):
        self._array = Array(capacity)

    def push(self, e):
        """向栈中添加元素"""
        self._array.add_Last(e)

    def pop(self):
        """从栈中取出元素"""
        return self._array.remove_Last()

    def peek(self):
        """获得栈顶元素"""
        return self._array.get_Last()

    def get_Size(self):
        """获得栈中元素数量"""
        return self._array.get_Size()

    def is_Empty(self):
        """栈是否为空"""
        return self._array.is_Empty()

    def get_capacity(self):
        return self._array.get_Capacity()

    def __str__(self):
        StringList = []
        StringList.append("Stack:size = %s, capacity = %d \n"
                          % (self._array.get_Size(), self._array.get_Capacity()))
        StringList.append('[')
        for i in range(self._array.get_Size()):
            StringList.append("%s" % self._array.get(i))
            if i != self._array.get_Size() - 1:
                StringList.append(",")
        StringList.append('] top')
        return "".join(StringList)

if __name__ == "__main__":
    stack = ArrayStack()
    for i in [1,3,5,1,9,8,1]:
        stack.push(i)

    print(stack)
    stack.pop()
    print(stack)