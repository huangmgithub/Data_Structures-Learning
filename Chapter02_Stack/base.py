class Stackbase:
    def push(self, e):
        """向栈中添加元素"""
        raise NotImplementedError

    def pop(self):
        """从栈中取出元素"""
        raise NotImplementedError

    def peek(self):
        """获得栈顶元素"""
        raise NotImplementedError

    def get_Size(self):
        """获得栈的大小"""
        raise NotImplementedError

    def is_Empty(self):
        """栈是否为空"""
        raise NotImplementedError