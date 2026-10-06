# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n == 1:
            return None
        curr = head
        cnt = 0
        while curr:
            cnt += 1
            curr = curr.next
        curr = head
        fromBeg = cnt - n 
        cnt = 0
        prev = None
        if fromBeg == 0:
            return head.next
        while cnt < fromBeg:
            prev = curr
            curr = curr.next
            cnt += 1
        prev.next = curr.next
        return head

