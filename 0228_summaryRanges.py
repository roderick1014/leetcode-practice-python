# 0228 - Summary Ranges

'''
    Question:
        You are given a sorted unique integer array nums.

        A range [a,b] is the set of all integers from a to b (inclusive).

        Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

        Each range [a,b] in the list should be output as:

         - "a->b" if a != b
         - "a" if a == b
'''


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        start = 0
        end = 0

        result = []

        while end < len(nums):

            if end + 1 < len(nums) and nums[end] + 1 == nums[end + 1]:
                end = end + 1

            else:
                if start == end:
                    result.append(str(nums[start]))
                    start = start + 1
                    end = end + 1
                else:
                    result.append(str(nums[start]) + '->' + str(nums[end]))
                    start = end + 1
                    end = end + 1
        return result

if __name__ == '__main__':
    nums = [0,2,3,4,6,8,9]

    sol = Solution()
    print(sol.summaryRanges(nums))