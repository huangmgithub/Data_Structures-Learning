from Chapter04_LinkedList.Leet_code_question.listNode import ListNode

class Solution2:
    def __init__(self, head):
        self.head = head
        self.dummy_head = ListNode(next_node=self.head)

    def removeElements(self, val):
        prev = self.dummy_head
        while prev.next:
            if prev.next.val == val:
                delNode = prev.next
                prev.next = delNode.next
                delNode.next = None
            else:
                prev = prev.next

        return self.dummy_head.next

