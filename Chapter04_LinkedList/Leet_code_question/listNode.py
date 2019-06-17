class ListNode:
    def __init__(self, x=None, next_node=None):
        self.next = next_node
        if not isinstance(x,list):
            self.val = x
        else:
            self.arr = x
            #链表节点的构造函数
            #使用arr为参数，创建一个链表，当前的ListNode为链表头节点
            if not self.arr:
                raise Exception("Array is Empty")
            self.val = self.arr[0]
            cur = self
            for i in range(1, len(self.arr)):
                cur.next = ListNode(self.arr[i])
                cur = cur.next

    def __str__(self):
        """以当前节点为头节点的链表信息字符串"""
        StringList = []
        cur = self
        while cur:
            StringList.append("%s->" % cur.val)
            cur = cur.next
        StringList.append("None")
        return "".join(StringList)

if __name__ == "__main__":
    nums = [1,2,6,3,4,5,6]
    head = ListNode(nums)
    print(head)