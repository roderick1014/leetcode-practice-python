# 0101 - Symmetric Tree

'''
    Question:
        Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        return self.checkSymmetric(root.left, root.right)

    def checkSymmetric(self, subTree_1, subTree_2):

        if subTree_1 == None and subTree_2 == None:
            return True
        if subTree_1 == None or subTree_2 == None:
            return False

        return (subTree_1.val == subTree_2.val) and self.checkSymmetric(subTree_1.left, subTree_2.right) and self.checkSymmetric(subTree_1.right,subTree_2.left)

if __name__ == '__main__':
    root = [1,2,2,3,4,4,3]
    root = [1,2,2,None,3,None,3]
    tree = TreeNode(val = root[0],
                    left = TreeNode(val = root[1], left = TreeNode(val = root[3]), right = TreeNode(val = root[4])),
                    right = TreeNode(val = root[2], left = TreeNode(val = root[5]), right = TreeNode(val = root[6])))

    sol = Solution()
    print(sol.isSymmetric(tree))