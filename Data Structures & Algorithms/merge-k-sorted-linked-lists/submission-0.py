# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        total = []
        heads = []
        for node in lists:
            while node:
                heads.append(node.val)
                node = node.next
        k = len(heads)
        heapq.heapify(heads)
        prev = ListNode()
        headnode = prev
        while k > 0:
            el = heapq.heappop(heads)
            node = ListNode(val=el)
            prev.next = node
            prev = node
            k -= 1
            
        return headnode.next