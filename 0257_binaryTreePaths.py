# 0257 - Binary Tree Paths

'''
    Question:
        Given the root of a binary tree, return all root-to-leaf paths in any order.

        A leaf is a node with no children.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        ans = []
        
        if not root.left and not root.right:
            ans.append(str(root.val))
            return ans
        
        self.findPath(root, ans, '')
        
        return ans

    def findPath(self, node, ans, record_val):
        if node:
            if not node.left and not node.right:
                ans.append(record_val + str(node.val))

            if node.left:
                self.findPath(node.left, ans, record_val + str(node.val) + '->')
            if node.right:
                self.findPath(node.right, ans, record_val + str(node.val) + '->')
        
        


if __name__ == '__main__':
    root = TreeNode(val = 1, left = TreeNode(val = 2, right=TreeNode(val = 5)), right = TreeNode(val = 3))
    sol = Solution()
    print(sol.binaryTreePaths(root))