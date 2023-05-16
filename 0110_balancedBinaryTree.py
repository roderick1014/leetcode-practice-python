# 0110 - Balanced Binary Tree

'''
    Question:
        Given a binary tree, determine if it is 
height-balanced
.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """     

        ans = True

        def dfs(node):            
            if node is None:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            nonlocal ans
            if abs(left_height - right_height) > 1:
                ans = False
            print(left_height, right_height, max(left_height, right_height))
            return max(left_height, right_height) + 1

        dfs(root)
        return ans



if __name__ == '__main__':
    tree = TreeNode(val = 3)
    tree.left = TreeNode(val = 9)
    tree.right = TreeNode(val = 20, left = TreeNode(val = 15), right = TreeNode(val = 7))

    sol = Solution()
    print(sol.isBalanced(tree))