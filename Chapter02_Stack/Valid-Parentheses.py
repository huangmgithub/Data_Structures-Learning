from Chapter02_Stack.stack import ArrayStack

class Solution:
    def __init__(self, string):
        self.string = string
        self.stack = ArrayStack()
    def is_Valid(self):
        for i in range(len(self.string)):
            c = self.string[i]
            if c == "(" or c == "[" or c == "{":
                self.stack.push(c)
            else:
                if self.stack.is_Empty():
                    return False
                top = self.stack.pop()
                if c == ")" and top != "(":
                    return False
                if c == "]" and top != "[":
                    return False
                if c == "}" and top != "{":
                    return False
        return self.stack.is_Empty() #最后判断栈是否为空




