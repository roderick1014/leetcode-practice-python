# 0035 - searchInsert

'''
    Question:
        Given a sorted array of distinct integers and a target value, return the index if the target is found. 
        If not, return the index where it would be if it were inserted in order.
        You must write an algorithm with O(log n) runtime complexity.
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1 # -1 because list starts from 0.
        while (left <= right):
            middle = (right + left) // 2
            
            if target == nums[middle]:
                return middle
            
            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return left

if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 7
    sol = Solution()
    print(sol.searchInsert(nums, target))