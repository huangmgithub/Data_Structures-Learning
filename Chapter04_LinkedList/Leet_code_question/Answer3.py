from Chapter04_LinkedList.Leet_code_question.listNode import ListNode

def generateDepthString(depth):
    stringList = []
    for i in range(depth):
        stringList.append('--')
    return ''.join(stringList)

def removeElements(head, val, depth):
    """
    使用递归解决链表删除元素问题
    增加depth递归深度来进行调试
    """
    if not head:
        return None
    head.next = removeElements(head.next, val, depth + 1)
    if head.val == val:
        return head.next
    else:
        return head

if __name__ == "__main__":
    nums = [1,2,6,3,4,5,6]
    head = ListNode(nums)
    print(head)
    removeElements(head, 6, 0)
    print(head)

