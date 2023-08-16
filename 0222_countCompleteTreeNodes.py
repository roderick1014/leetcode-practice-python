# 0222 - Count Complete Tree Nodes

'''
    Given the root of a complete binary tree, return the number of the nodes in the tree.

    According to Wikipedia, every level, except possibly the last,
    is completely filled in a complete binary tree, and all nodes
    in the last level are as far left as possible.

    It can have between 1 and 2h nodes inclusive at the last level h.

    Design an algorithm that runs in less than O(n) time complexity.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# # Solution 1 - DFS + Recursive
# class Solution(object):
#     def countNodes(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """

#         ans = 0

#         def dfs(node):

#             if node:
#                 ans += 1
#                 self.countNodes(node.left)
#                 self.countNodes(node.right)

#         dfs(root)

#         return ans


# Solution 2 - Best
'''
    If left sub tree height equals right sub tree height then,
        a. left sub tree is perfect binary tree
        b. right sub tree is complete binary tree
    If left sub tree height greater than right sub tree height then,
        a. left sub tree is complete binary tree
        b. right sub tree is perfect binary tree
'''
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)

        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0

        return 1 + self.getDepth(root.left)



if __name__ == '__main__':
    root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5), right = TreeNode(val=3,left=TreeNode(val=6))))
    sol = Solution()
    print(sol.countNodes(root))