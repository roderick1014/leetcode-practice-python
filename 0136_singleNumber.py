# 0136 - Single Number

'''
    Question:
        Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
        You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Solution 1 - while loop (With sorting O(nlon(n)))
        # if len(nums) == 1:
        #     return nums[0]
        # l = 0
        # r = len(nums) - 1
        # nums = sorted(nums)

        # while r != l:
        #     if (nums[l] != nums[l + 1]) and (nums[l + 1] != None):
        #         if l == 0:
        #             return nums[l]
        #         return nums[l]

        #     l += 2
        # return nums[-1]

        # Solution 2 - XOR operation
        # Do XOR operation to every elements, the remaining vale is the 'single number' → O(n)
        uniqNumber = 0
        for val in nums:
            uniqNumber ^= val
        return uniqNumber

if __name__ == '__main__':
    # nums = [4,1,2,1,2]
    nums = [-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354]
    sol = Solution()
    print(sol.singleNumber(nums))