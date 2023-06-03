# 0055 - Jump Game

'''
    You are given an integer array nums.
    You are initially positioned at the array's first index,
    and each element in the array represents your maximum jump length at that position.

    Return true if you can reach the last index, or false otherwise.
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Solution 1 - Greedy Algorithm. Time Complexity: O(n), Space Complexity: O(1)

        max_idx = 0 # max_idx indicates the maximum index we can reach so far.

        for idx, val in enumerate(nums):
            if idx > max_idx:
                return False
            max_idx = max(max_idx, idx + val)
            if max_idx >= len(nums) - 1:
                return True
        return True
    
        # # Solution 2 - Dynamic Programming.

        # dp = [0] * len(nums)
        # dp[0] = nums[0]

        # # dp[idx] represents the farest index that we can reach from idx.
        # for idx in range(1, len(nums) - 1):
            
        #     if dp[idx - 1] < idx:
        #         return False
            
        #     dp[idx] = max(idx + nums[idx], dp[idx - 1])

        #     if dp[idx] >= (len(nums) - 1):
        #         return True
        # return dp[len(dp) - 2] >= len(dp) - 1

if __name__ == '__main__':
    nums = [2,3,1,1,4]

    sol = Solution()
    print(sol.canJump(nums))