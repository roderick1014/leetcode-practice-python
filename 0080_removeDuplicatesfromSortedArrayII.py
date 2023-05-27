# 0080 - Remove Duplicates from Sorted Array II

'''
    Question:
        Given an integer array nums sorted in non-decreasing order,
        remove some duplicates in-place such that each unique element
        appears at most twice. The relative order of the elements should
        be kept the same.

        Return k after placing the final result in the first k slots of nums.
        Do not allocate extra space for another array.
        You must do this by modifying the input array in-place with O(1) extra memory.
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Solution 2 - Time complexity: O(n), Space complexity: O(1)
        # Initialize an integer k that updates the kth index of the array...
        # only when the current element does not match either of the two previous indexes. ...
        ptr = 0
        for element in nums:
            if ptr < 2 or element != nums[ptr - 2]:
                nums[ptr] = element
                ptr += 1
        return ptr

        # Solution 1 - While loop
        # current = nums[0]
        # count = 1
        # offset = 0
        # ptr = 1

        # while (ptr + offset) < len(nums):
        #     print(nums)
        #     if nums[ptr + offset] == current:
        #         count += 1
        #     else:
        #         current = nums[ptr + offset]
        #         count = 1

        #     if count == 3:
        #         while (ptr + offset) < len(nums):
        #             if current != nums[ptr + offset]:
        #                 count = 1
        #                 current = nums[ptr + offset]
        #                 nums[ptr] = nums[ptr + offset]
        #                 break
        #             else:
        #                 offset += 1
        #     if (ptr + offset) == len(nums):
        #         break
        #     if offset:
        #         nums[ptr] = nums[ptr + offset]

        #     ptr += 1

        # for idx in range(ptr, ptr + offset):
        #     nums[idx] = '_'

        # print(nums)

        # return ptr

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    nums = [0,0,1,1,1,1,2,3,3]
    # nums = [1,1,1]


    sol = Solution()
    print(sol.removeDuplicates(nums))