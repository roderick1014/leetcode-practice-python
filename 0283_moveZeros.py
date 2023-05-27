# 0283 - Move Zeros

'''
    Question:
        Given an integer array nums, move all 0's to the end
        of it while maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the array.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        for j in range(len(nums)):
            print(nums)
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

if __name__ == '__main__':
    nums = [0,0]
    nums = [1,0,0,3,12]

    sol = Solution()
    sol.moveZeroes(nums)
    print(nums)