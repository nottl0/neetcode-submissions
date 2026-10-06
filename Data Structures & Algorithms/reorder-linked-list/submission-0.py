# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        len_list = 0
        while curr:
            curr = curr.next
            len_list += 1
        half = len_list - (len_list // 2)

        curr = head
        count = 0
        while curr:
            prev = curr
            curr = curr.next
            count += 1
            if count == half:
                prev.next = None
                break
        # while head:
        #     print(head.val)
        #     head = head.next
        prev = None
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        # while prev:
        #     print(prev.val)
        #     prev = prev.next
        while prev and head:
            prev_prev = prev.next
            head_next = head.next
            prev.next, head.next = head.next, prev
            prev = prev_prev
            head = head_next
        # if prev:
        #     head.next = prev
        # elif head:
        #     prev.next = head









