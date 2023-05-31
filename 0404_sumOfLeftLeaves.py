# 0404 - Sum of Left Leaves

'''
    Question:
        Given the root of a binary tree, return the sum of all left leaves.
        A leaf is a node with no children. 
        A left leaf is a leaf that is the left child of another node.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


        # Solution 1 - Optimal
        if not root:
            return 0
        
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

        # Solution 2 - My sol
        # if not root:
        #     return 0

        # def dfs(node, summation, left):
        #     if node:
        #         if not node.left and not node.right:
        #             if left:
        #                 return node.val
        #             else:
        #                 return 0
                    
        #         return dfs(node.left, summation, 1) + dfs(node.right, summation, 0)
        #     else:
        #         return 0
        
        # return dfs(root, 0, 0)




if __name__ == '__main__':
    node = TreeNode(val = 3, left = TreeNode(val = 9), right = TreeNode(val = 20, left = TreeNode(val = 15), right = TreeNode(val = 7)))
    sol = Solution()
    print(sol.sumOfLeftLeaves(node))