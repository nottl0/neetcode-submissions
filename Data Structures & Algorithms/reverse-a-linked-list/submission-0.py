# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nexx = None
        prev = None
        while head:
            nexx = head.next
            head.next = prev
            prev = head
            head = nexx 
        return prev


