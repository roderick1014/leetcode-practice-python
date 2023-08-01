# 0114 - Flatten Binary Tree to Linked List.

'''
    Question:
        Given the root of a binary tree, flatten the tree into a "linked list":

        - The "linked list" should use the same TreeNode class where the right child pointer points 
        to the next node in the list and the left child pointer is always null.

        - The "linked list" should be in the same order as a pre-order traversal of the binary tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        if not root:
            return None

        # Solve the right sub-tree first.
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root

if __name__ == '__main__':
    pass