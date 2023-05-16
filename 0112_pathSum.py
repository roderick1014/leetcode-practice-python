# 0112 - Path Sum

'''
    Question:
        Given the root of a binary tree and an integer targetSum,
        return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
        A leaf is a node with no children.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    '''
            Do the subtraction while traversing to each node, once it reaches the leave, 
            check if the leave value is same as the remaining value.
    '''
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        if root is None:
            return False
        
        # If reaches the leave and the value are the same, it indicates that there's is a "root-to-leaf path".
        if root.val == targetSum and not (root.left or root.right): 
            return True
               
        targetSum -= root.val    
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
if __name__ == '__main__':
    tree = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
    # tree = TreeNode(val = 5,
    #                 left=TreeNode(val = 4, left=TreeNode(val = 11, left=TreeNode(val = 7), right=TreeNode(val = 2)),
    #                 right=TreeNode(val=8, left=TreeNode(val=13), right=TreeNode(val=4, right=TreeNode(val=1)))))
    targetSum = 3
    sol = Solution()
    print(sol.hasPathSum(tree, targetSum))