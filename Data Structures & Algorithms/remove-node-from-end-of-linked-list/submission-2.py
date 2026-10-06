# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = []
        init_head = head
        while head:
            l.append(head)
            head = head.next
        # one el in list
        if len(l) == 1:
            return None
        # first el in list
        elif len(l) == n:
            init_head = init_head.next
        # last el in list
        elif n == 1:
            l[len(l) - 1 - 1].next = None
        else: 
            l[len(l) - n - 1].next = l[len(l) - n].next
        return init_head