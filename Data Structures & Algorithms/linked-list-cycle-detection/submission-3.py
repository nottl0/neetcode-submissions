# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head.next or not head.next.next:
            return False
        fast = head.next
        faster = head.next.next
        while faster:
            if fast == faster:
                return True
            try:
                fast = fast.next
                faster = faster.next.next
            except:
                return False
        return False