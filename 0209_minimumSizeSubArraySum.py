# 0209 - Minimum Size Subarray Sum

'''
    Question:
        Given an array of positive integers nums and a positive integer target, return
        the minimal length of a subarray whose sum is greater than or equal to target. 
        If there is no such subarray, return 0 instead.
'''

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
            
        l = 0
        r = 0
        curr = 0
        min_len = len(nums) + 1 # initialize it as the maximum capacity + 1

        for r in range(len(nums)):
            
            curr += nums[r]
            while curr >= target:
                min_len = min(min_len, r - l + 1)
                curr -= nums[l]
                l += 1

        return 0 if min_len == len(nums) + 1 else min_len

if __name__ == '__main__':
    sol = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    print(sol.minSubArrayLen(target, nums))