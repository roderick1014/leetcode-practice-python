# 0129 - Sum Root to Leaf Numbers

'''
    Question:
    
        You are given the root of a binary tree containing digits from 0 to 9 only.
        Each root-to-leaf path in the tree represents a number.
        For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
        Return the total sum of all root-to-leaf numbers. 
        Test cases are generated so that the answer will fit in a 32-bit integer.
        A leaf node is a node with no children.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # My solution - DFS + Recursion
                
        self.ans = 0
        
        def dfs(node, acc):
            if node:
                acc = acc * 10 + node.val
                if not node.left and not node.right: self.ans += acc
                dfs(node.left, acc)
                dfs(node.right, acc)
        
        dfs(root, 0)
        
        return self.ans
    
if __name__ == '__main__':
    root = TreeNode(val = 0, left = TreeNode(val = 1))
    sol = Solution()
    print(sol.sumNumbers(root))