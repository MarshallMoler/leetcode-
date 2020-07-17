'''删除链表的倒数第N个节点'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast_pointer = head
        slow_pointer = head
        count = 0
        for i in range(n):
            fast_pointer = fast_pointer.next
            count += 1
        if not fast_pointer:
            return slow_pointer.next
        while fast_pointer.next:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
        slow_pointer.next=slow_pointer.next.next
        return head
        
