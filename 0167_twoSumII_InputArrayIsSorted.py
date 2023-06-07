# 0167 - Two Sum II - Input Array is Sorted

'''
    Question:
        Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
        find two numbers such that they add up to a specific target number.

        Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
        Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

        The tests are generated such that there is exactly one solution.
        You may not use the same element twice.
        Your solution must use only constant extra space.
'''


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Solution 1 - Two Pointer
        left = 0
        right = len(numbers) - 1
        while left < right:
            summation = numbers[left] + numbers[right]
            if summation == target:
                return [left + 1, right + 1]
            elif summation > target:
                right -= 1
            else:
                left += 1

        # # Solution 2 - Binary Search
        # for i in range(len(numbers)):
        #     l, r = i+1, len(numbers)-1
        #     tmp = target - numbers[i]
        #     while l <= r:
        #         mid = l + (r-l)//2
        #         if numbers[mid] == tmp:
        #             return [i+1, mid+1]
        #         elif numbers[mid] < tmp:
        #             l = mid+1
        #         else:
        #             r = mid-1

if __name__ == '__main__':
    numbers = [2,7,11,15]
    target = 9
    numbers = [-1,0]
    target = -1
    sol = Solution()
    print(sol.twoSum(numbers, target))