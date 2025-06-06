# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur1 = list1 
        cur2 = list2

        head = ListNode()
        cur3 = head

        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur3.next = cur1
                cur3 = cur1
                cur1 = cur1.next
                
            else:
                cur3.next = cur2
                cur3 = cur2
                cur2 = cur3.next

            
        cur3.next = cur1 if cur1 else cur2
                
    
        return head.next