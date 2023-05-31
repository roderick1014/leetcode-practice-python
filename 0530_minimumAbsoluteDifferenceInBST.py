# 0530 - Minimum Absolute Difference in BST

'''
    Question:
        Given the root of a Binary Search Tree (BST), 
        return the minimum absolute difference between 
        the values of any two different nodes in the tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        '''
            The minimum absolute difference will appear in 
            right sub-tree or left sub-tree since the root
            value is the closest value to the sub-tree.
        '''
        
        def trackBound(node, low, high):
            if not node: return high - low
            left = trackBound(node.left, low, node.val)
            right = trackBound(node.right, node.val, high)
            return min(left, right)
        return trackBound(root, float('-inf'), float('inf'))
            


if __name__ == '__main__':
    # node = TreeNode(val = 4)
    # node.left = TreeNode(val = 2,left = TreeNode(val = 1), right = TreeNode(val = 3))
    # node.right = TreeNode(val = 6)

    node = TreeNode(val=1,right = TreeNode(val = 3,left = TreeNode(val=2)))
    sol = Solution()
    print(sol.getMinimumDifference(node))