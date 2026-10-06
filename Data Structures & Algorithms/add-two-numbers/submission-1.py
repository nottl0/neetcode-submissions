# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prevhead = ListNode(0)
        head = prevhead
        while l1 or l2:
            if not l1:
                val1 = 0
            else:
                val1 = l1.val
            if not l2:
                val2 = 0
            else:
                val2 = l2.val
            rem = (val1 + val2+carry)%10
            whole = (val1 + val2 + carry)//10
            #value = rem + carry
            carry = whole
            head.next = ListNode(val=rem)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            head = head.next

        if carry > 0:
            head.next = ListNode(val=carry)

        return prevhead.next