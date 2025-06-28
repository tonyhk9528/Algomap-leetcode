# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        balanced = [True]

        def get_height(node):
            if not node:
                return 0

            left_height = get_height(node.left)
            if balanced[0] is False:
                return 0

            right_height = get_height(node.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0

            return 1 + max (left_height, right_height)

        get_height(root)
        return balanced[0] 