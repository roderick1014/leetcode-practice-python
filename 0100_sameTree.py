# 0100 - Same Tree

'''
    Question:
        Given the roots of two binary trees p and q, write a function to check if they are the same or not.
        Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        # We focus on if the current nodes are "not equal" and return False.
        # Otherwise, the function will keep traverse the tree until

        if p == None and q == None:     # If both nodes are None.
            return True
        if p == None or q == None:      # If one of the node in the traversing pair is None.
            return False
        if p.val != q.val:              # If the existing nodes are not equal.
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



if __name__ == '__main__':
    p = [1,2,3]
    q = [1,2,3]

    # p = [1,2,1]
    # q = [1,1,2]

    tree_1 = TreeNode(val = p[0], left = TreeNode(val = p[1]), right = TreeNode(val = p[2]))
    tree_2 = TreeNode(val = q[0], left = TreeNode(val = q[1]), right = TreeNode(val = q[2]))
    sol = Solution()
    print(sol.isSameTree(tree_1, tree_2))