"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None 
        curr = head
        pointer_map = {}

        while curr:
            new = Node(curr.val)
            pointer_map[curr] = new
            curr = curr.next
        
        curr = head

        while curr:
            if curr.next:
                pointer_map[curr].next = pointer_map[curr.next]
            else:
                pointer_map[curr].next = None
            if curr.random:
                pointer_map[curr].random = pointer_map[curr.random]
            else: 
                pointer_map[curr].random = None
        
            curr = curr.next

        return pointer_map[head]