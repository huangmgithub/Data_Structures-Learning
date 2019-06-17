from Chapter04_LinkedList.Leet_code_question.listNode import ListNode

class Solution1:
    def __init__(self, head):
        self.head = head

    def removeElements(self, val):
        while self.head and self.head.val == val:
            delNode = self.head
            self.head = self.head.next
            delNode.next = None

        if not self.head: #链表为空
            return None

        prev = self.head
        while prev.next:
            if prev.next.val == val:
                delNode = prev.next
                prev.next = delNode.next
                delNode.next = None
            else:
                prev = prev.next

        return self.head

if __name__ == "__main__":
    nums = [1,2,6,3,4,5,6]
    head = ListNode(nums)
    print(head)

    solution1 = Solution1(head=head)
    print(solution1.removeElements(6))
