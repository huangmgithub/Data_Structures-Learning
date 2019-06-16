from Chapter02_Stack.base import Stackbase
from Chapter04_LinkedList.linkedlist import LinkList
from Chapter02_Stack.stack import ArrayStack

class LinkedListStack(Stackbase):
    def __init__(self):
        self._list = LinkList()

    def get_Size(self):
        return self._list.get_Size()

    def is_Empty(self):
        return self._list.is_Empty()

    def push(self, e):
        self._list.add_First(e)

    def pop(self):
        return self._list.remove_First()

    def peek(self):
        return self._list.get_First()

    def __str__(self):
        StringList = []
        cur = self._list.dummy_head.next
        StringList.append("Stack:Top")
        while cur:
            StringList.append("%s->" % cur)
            cur = cur.next
        StringList.append("None")
        return "".join(StringList)

if __name__ == "__main__":
    # stack = LinkedListStack()
    # for i in [1, 3, 5, 1, 9, 8, 1]:
    #     stack.push(i)
    #     print(stack)
    #
    # stack.pop()
    # print(stack)
    # print(stack.peek())
    # print(stack.get_Size())

    #数组栈和链表栈的比较
    from time import time
    import random

    def test_Stack(stack, opCount):
        start_time = time()
        for i in range(opCount):
            stack.push(random.randint(1, 2000))
        for i in range(opCount):
            stack.pop()
        return time() - start_time

    opCount = 1000000
    array_stack = ArrayStack()
    linked_list_stack = LinkedListStack()

    print("ArrayStack run time: %s" % test_Stack(array_stack, opCount))
    print("LinkedListStack run time: %s" % test_Stack(linked_list_stack, opCount))
