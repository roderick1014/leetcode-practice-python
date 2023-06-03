# 0045 - Jump Game II

'''
    Question:
        You are given a 0-indexed array of integers nums of length n. 
        You are initially positioned at nums[0].

        Each element nums[i] represents the maximum length of a forward jump from index i. 
        In other words, if you are at nums[i], you can jump to any nums[i + j] where:

        - 0 <= j <= nums[i] and i + j < n
        
        Return the minimum number of jumps to reach nums[n - 1]. 
        The test cases are generated such that you can reach nums[n - 1].
'''

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        steps = 0
        end = 0
        max_idx = 0

        for idx in range(len(nums) - 1):
            max_idx = max(nums[idx] + idx, max_idx)
            
            if max_idx >= len(nums) - 1:
                steps += 1
                return steps
            
            # If we reach the end of the current level, we have to take a new step.
            if idx == end:  
                steps += 1
                end = max_idx

        return steps

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    nums = [1,2,3]

    sol = Solution()
    print(sol.jump(nums))