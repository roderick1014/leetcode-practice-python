# 0189 - Rotate Array

'''
    Question:
        Given an integer array nums, rotate the array to the right by k steps,
        where k is non-negative.

        *Follow up:
            - Try to come up with as many solutions as you can.
            - There are at least three different ways to solve this problem.
            - Could you do it in-place with O(1) extra space?
'''


class Solution(object):
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, nums, i, j) :

        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

            i += 1
            j -= 1



if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    nums = [1,2]
    k = 2
    sol = Solution()
    sol.rotate(nums, k)
    print(nums)