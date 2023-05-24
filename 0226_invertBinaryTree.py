# 0226 - Invert Binary Tree


'''
    Question:
        Given the root of a binary tree, invert the tree, and return its root.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    
if __name__ == '__main__':
    root = [2,1,3]
    tree_1 = TreeNode(val = root[0], left = TreeNode(val = root[1]), right = TreeNode(val = root[2]))
    
    sol = Solution()   
    sol.invertTree(tree_1)
    print(tree_1.val, tree_1.left.val, tree_1.right.val)