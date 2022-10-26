# 0008 - Merge Two Sorted Array

'''
    Question:
        Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
        and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
        The final sorted array should not be returned by the function, but instead be "stored inside the array nums1".
        To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
        and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1_idx = m - 1           # Point to the right-most element.
        nums2_idx = n - 1           # Point to the right-most element.
        right_ptr = m + n - 1       # Start sorting from the right-most element of nums1. 
        # ↑ It will -1 every loop until reaching the left-most element of nums1 eventually.
        
        while nums2_idx >= 0:
            if nums1_idx >= 0 and nums1[nums1_idx] > nums2[nums2_idx]:
                nums1[right_ptr] = nums1[nums1_idx]
                right_ptr -= 1
                nums1_idx -= 1
            else:
                nums1[right_ptr] = nums2[nums2_idx]
                right_ptr -= 1
                nums2_idx -= 1
            

if __name__ == '__main__':

    sol = Solution()
    nums1 = [1,2,3,0,0,0]   # The part '0' is stored for the merging operation
    m = 3                   # Effective length of the nums1.
    nums2 = [2,5,6]
    n = 3                   # Effective length of the nums2.
    sol.merge(nums1, m, nums2, n)
    print(nums1)
    