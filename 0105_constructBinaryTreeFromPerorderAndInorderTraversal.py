# 0105 - Construct Binary Tree from Preorder and Inorder Traversal

'''
    Question:
        Given two integer arrays preorder and inorder where preorder is the
        preordertraversal of a binary tree and inorder is the inorder traversal
        of the same tree, construct and return the binary tree.
'''

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Solution 2 - hashmap and iterator

        '''
            Obtain the root from preorder and refer the index of inorder node.
            Then divide and conquer the problem.
        '''

        # we use deque() because .popleft() operation is O(1).
        preorder = collections.deque(preorder)
        # create an inorder_map with (value:index) pair
        inorder_map = {n:i for i, n in enumerate(inorder)}

        def build_tree(start, end):
            if start > end: return None
            root_index = inorder_map[preorder.popleft()]
            root = TreeNode(
                                val = inorder[root_index],
                                left = build_tree(start, root_index - 1),
                                right = build_tree(root_index + 1, end),
                            )
            return root

        return build_tree(0, len(inorder)-1)

        # Solution 1 - short recursive solution
        # if inorder:
        #     index = inorder.index(preorder.pop(0))
        #     root = TreeNode(val = inorder[index])
        #     root.left = self.buildTree(preorder, inorder[0:index])
        #     root.right = self.buildTree(preorder, inorder[index+1:])
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
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    sol =  Solution()
    tree = sol.buildTree(preorder, inorder)
    print(displayTree(tree))