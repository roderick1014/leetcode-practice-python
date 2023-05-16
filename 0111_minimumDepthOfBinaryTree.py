# 0111 - Minimum Depth of Binary Tree

'''
    Question:
        Given a binary tree, find its minimum depth.
        The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
        Note: A leaf is a node with no children.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return rightDepth + 1
        if root.right is None:
            return leftDepth + 1
        
        return min(leftDepth, rightDepth) + 1

if __name__ == '__main__':
    root = TreeNode(val = 3)
    root.left = TreeNode(val = 9)
    root.right = TreeNode(val = 20, left = TreeNode(val = 15), right = TreeNode(val = 7))
    
    sol = Solution()
    print(sol.minDepth(root))