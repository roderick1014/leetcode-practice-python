# 0094 - Binary Tree Inorder Traversal

'''
    Question:
        Given the root of a binary tree, 
        return the inorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root:
                return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
                
        else:
            return []
        
    # My Solution - Longer lines ...
    #     inorder_sequence = []
    #     if root:
    #         self.checkNode(root, inorder_sequence)
    #         # inorder_sequence.append(root.val)

    #     return inorder_sequence

    # def checkNode(self, sub_root, inorder_sequence):
        
    #     if sub_root.left is not None:
    #         self.checkNode(sub_root.left, inorder_sequence)
    #         # self.checkNode()
    #         # inorder_sequence.append(sub_root.left.val)

    #     inorder_sequence.append(sub_root.val)

    #     if sub_root.right is not None:
    #         self.checkNode(sub_root.right, inorder_sequence)
    #         # inorder_sequence.append(sub_root.right.val)
        
    #     return inorder_sequence


if __name__ == '__main__':
    root = [1, None, 2, 3]
    tree = TreeNode(val = root[0],
                    left=None, 
                    right = TreeNode(
                                val = 2,
                                left = TreeNode(val = root[3]),
                                right = None)
                                    )
    tree = TreeNode(val = 1, left=TreeNode(val = 2))
    
    sol = Solution()
    print(tree.val)
    print(sol.inorderTraversal(tree))
