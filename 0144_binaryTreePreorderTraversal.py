# 



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # Solution 1 - Recursive
        ans = []
        if root is None:
            return ans
        
        self.preorder(root, ans)

        return ans

    def preorder(self, node, ans):
        if node:
            ans.append(node.val)
        if node.left:
            self.preorder(node.left, ans)
        if node.right:
            self.preorder(node.right, ans)
        
        
        # # Solution 2 - Iterative
        # if root is None:
        #     return []
        
        # stack, ans = [root], []

        # while stack:
        #     node = stack.pop()
        #     ans.append(node.val)
            
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return ans

            
        
        

if __name__ == '__main__':
    root = TreeNode(val = 1, right = TreeNode(val = 2, right=TreeNode(val = 3)))
    # root = TreeNode(val = 1)
    sol = Solution()
    print(sol.preorderTraversal(root))