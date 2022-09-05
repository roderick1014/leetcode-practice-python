# 0104 - Maximum Depth of Binary Tree

'''
    Question:
        Given the root of a binary tree, return its maximum depth.
        A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Define of the tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Depth First Search is applied
    def maxDepth(self, root):   
        
        '''
            :type : TreeNode
            :rtype: TreeNode
        '''

        if not root:
            return 0
        return max(self.maxDepth(root.left) , self.maxDepth(root.right)) + 1      

if __name__ == '__main__':
    
    root = [3, 9, 20, None, None, 15, 7]
    
    leaf_1 = TreeNode(val = 9)
    leaf_2 = TreeNode(val = 20, left = TreeNode(val = 15), right = TreeNode(val = 7))
    tree = TreeNode(val = root[0], left = leaf_1, right = leaf_2)
    
    print(tree.val)
    print(tree.left.val)
    print(tree.right.val)
    print(tree.right.left.val)
    print(tree.right.right.val)

    sol = Solution()
    print(sol.maxDepth(tree))