# 0033 - Search in Rotated Sorted Array

'''
    Question:
        There is an integer array nums sorted in ascending order (with distinct values).
        Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
        Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
        You must write an algorithm with O(log n) runtime complexity.
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l_ptr = 0
        r_ptr = len(nums) - 1

        while l_ptr <= r_ptr:

            m_ptr = (l_ptr + r_ptr) // 2

            if nums[m_ptr] == target:
                return m_ptr
            if nums[l_ptr] == target:
                return l_ptr
            if nums[r_ptr] == target:
                return r_ptr
            
            if nums[m_ptr] > nums[l_ptr]:
                
                if nums[m_ptr] > target and target > nums[l_ptr]:
                    r_ptr = m_ptr - 1
                else:
                    l_ptr = m_ptr + 1
            
            else:
                
                if target > nums[m_ptr] and nums[r_ptr] > target:
                    l_ptr = m_ptr + 1
                else:
                    r_ptr = m_ptr - 1
            
        return -1

if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 5
    sol = Solution()
    print(sol.search(nums, target))