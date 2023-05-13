# 0108 - Convert Sorted Array to Binary Search Tree

'''
    Question:
        Given an integer array nums where the elements are sorted in ascending order,
        convert it to a "height-balanced" binary search tree.

        Definition of a height-balanced binary search tree:
            The difference of the height of left sub-tree and right sub-tree are <= 1.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return None

        root_idx = len(nums) // 2
        # Note that if the idx exceeds the bound of the list by 'nums[root_idx + 1:]', 
        # it will return a empty list '[]'.
        return TreeNode(
                            val = nums[root_idx],
                            left = self.sortedArrayToBST(nums[:root_idx]),
                            right = self.sortedArrayToBST(nums[root_idx + 1:])
                        )

if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    sol = Solution()
    print(sol.sortedArrayToBST(nums).val)