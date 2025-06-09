# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        d = ListNode(next=head)
        a = d
        b = d

        for i in range(n):
            a = a.next
        
        while a:
            b = b.next
            a = a.next
        
        b.next = b.next.next
    
        return b