# 0106 - Construct Binary Tree from Inorder and Postorder Traversal

'''
    Question:
        Given two integer arrays inorder and postorder where inorder is the
        inorder traversal of a binary tree and postorder is the postorder
        traversal of the same tree, construct and return the binary tree.
'''

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """"
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        # # Solution 2 - hashmap and iterator

        # '''
        #     Obtain the root from preorder and refer the index of inorder node.
        #     Then divide and conquer the problem.
        # '''

        # create an inorder_map with (value:index) pair
        inorder_map = {n:i for i, n in enumerate(inorder)}

        def build_tree(start, end):
            if start > end: return None
            root_index = inorder_map[postorder.pop()]
            # The order of left, right is important since it's postorder not preorder now.
            root = TreeNode(
                                val = inorder[root_index],
                                right = build_tree(root_index + 1, end),
                                left = build_tree(start, root_index - 1),
                            )
            return root

        return build_tree(0, len(inorder)-1)

        # # Solution 1 - short recursive solution
        # if inorder:
        #     index = inorder.index(postorder.pop())
        #     root = TreeNode(inorder[index])
        #     root.right = self.buildTree(inorder[index+1:], postorder)
        #     root.left = self.buildTree(inorder[0:index], postorder)
        #     return root

def displayTree(root):
    if not root:
        return []
    else:
        result = [root.val]
        result.append(displayTree(root.left))
        result.append(displayTree(root.right))
        return result

if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    sol =  Solution()
    tree = sol.buildTree(inorder, postorder)
    print(displayTree(tree))