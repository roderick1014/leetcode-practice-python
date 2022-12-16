# 0268 - Missing Number

'''
    Question:
        Given an array nums containing n distinct numbers in the range [0, n], 
        return the only number in the range that is missing from the array.
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # ========== Method 1 ===========
        # ans = len(nums)

        # for i in range(ans):

        #     ans ^= i ^ nums[i]  
        #     # Do the XOR operation with each index and the element, which uses O(1) extra space and O(n) time complexity
        
        # return ans
        # ===============================

        # ========== Method 2 ===========

        # Calculate the Gauss' Formula and compare with the sum of list.
        return ((len(nums) * (len(nums) + 1)) // 2 - sum(nums))
        # ===============================


if __name__ == '__main__':
    
    nums = [3, 0, 1]
    sol = Solution()
    print(sol.missingNumber(nums))
