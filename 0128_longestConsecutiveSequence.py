# 0128 - Longest Consecutive Sequence

'''
    Question:
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
        You must write an algorithm that runs in O(n) time.
'''

class Solution(object):
   
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
            
        nums = sorted(set(nums))   # Eliminate the repeated values and sort the array.
        longest_consecutive_length = 1
        current_val = nums[0]
        current_length = 1
        
        for idx in range(1, len(nums)):
            
            if current_val + 1 == nums[idx]:
                current_length += 1
            else:
                current_length = 1
                
            current_val = nums[idx]
            longest_consecutive_length = max(current_length, longest_consecutive_length)
        
        return longest_consecutive_length




if __name__ == '__main__':

    nums = [100,4,200,1,3,2]
    sol = Solution()
    ans = sol.longestConsecutive(nums)
    print(ans)