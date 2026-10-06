# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# 2 - 4 - 6 - 8
# 8 - 6 - 4 - 2
# 2 - 4 - 6 - 8
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        start = head
        l = []
        while head:
            l.append(head)
            head = head.next
        s = 0
        e = len(l) - 1
        while s < e:
            prev = l[s]
            prev.next = l[e]
            l[e].next = l[s+1]
            s += 1
            e -= 1
        l[s].next = None
            

            