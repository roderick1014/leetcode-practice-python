# 0053 - Maximum Subarray

'''
    Question:
        Given an integer array nums, find the subarray which has the largest sum and return its sum.
'''



class Solution(object):
    
    def maxSubArray(self, nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """

        max_val = nums[0]           # Initialization
        accumulated_val = nums[0]   # Initialization
        
        # The calculation starts from the first element, adding the values orderly.

        for idx in range(1, len(nums)):
            if accumulated_val <= 0:
                accumulated_val = 0
            accumulated_val += nums[idx]
            max_val = max(accumulated_val, nums[idx], max_val)
    
        return max_val
                

if __name__ == '__main__':
    nums = [-2,1]
    sol = Solution()
    ans = sol.maxSubArray(nums)
    print(ans)