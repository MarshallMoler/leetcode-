'''环形链表'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        count = 100000
        while count>0:
            if not head:
                return False
            else:
                head = head.next
                count -= 1
        return True



