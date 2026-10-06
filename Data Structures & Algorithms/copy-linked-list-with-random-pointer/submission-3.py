"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        newList = {}
        randomMap = {}
        oldHead = head
        prev = Node(x=0)
        returnable = prev
        ind = -1 
        while head:
            ind += 1
            newHead = Node(x=head.val)
            newList[ind] = newHead
            head.index = ind
            prev.next = newHead
            prev = newHead
            head = head.next
        while oldHead:
            if oldHead.random:
        
                randomMap[oldHead.index] = oldHead.random.index
            else:
                randomMap[oldHead.index] = None
            oldHead = oldHead.next

        for node, rand in randomMap.items():

            if rand is not None:
                newList[node].random = newList[rand]
            else:
                newList[node].random = None
        
        return returnable.next
    

        

        

            
            
        