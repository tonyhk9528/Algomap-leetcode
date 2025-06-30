# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        max_d = [0]

        def get_height(node):
            if node is None:
                return 0

            left_height = get_height(node.left)
            right_height = get_height(node.right)
            curr_d = left_height + right_height 

            max_d[0] = max(curr_d, max_d[0])

            return 1 + max(left_height, right_height)

        get_height(root)
        return max_d[0]
        