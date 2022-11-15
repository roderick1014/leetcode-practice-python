# 0153 -  Find Minimum in Rotated Sorted Array

'''
    Question:
        Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
            → [4,5,6,7,0,1,2] if it was rotated 4 times.
            → [0,1,2,4,5,6,7] if it was rotated 7 times.
        You must write an algorithm that runs in O(log n) time.
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, len(nums)-1

        while left < right:

            mid = (left + right) // 2
                               
            if nums[mid] > nums[right]:                
                left = mid + 1

            else:
                right = mid

        return nums[left]
                

if __name__ == '__main__':
    nums = [3,4,5,1,2]
    sol = Solution()
    ans = sol.findMin(nums)
    print(ans)