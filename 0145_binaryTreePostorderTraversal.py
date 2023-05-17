# 0145 - Binary Tree Postorder Traversal

'''
    Question:
        Given the root of a binary tree, return the postorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root is None:
            return ans
        
        self.postorder(root, ans)

        return ans

    def postorder(self, node, ans):
        if node.left:
            self.postorder(node.left, ans)
        if node.right:
            self.postorder(node.right, ans)
        if node:
            ans.append(node.val)
            
        

if __name__ == '__main__':
    # root = TreeNode(val = 1, right = TreeNode(val = 2, right=TreeNode(val = 3)))
    root = TreeNode(val = 3, right = TreeNode(val = 2), left = TreeNode(val = 1))
    sol = Solution()
    print(sol.postorderTraversal(root))