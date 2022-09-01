# 0004 - Median of Two Sorted Arrays

'''
    Question:
        Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
        The overall run time complexity should be O(log (m+n)).
'''


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
    
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # Binary search with left & right partition comparison.
        total_length = len(nums1) + len(nums2)
        half = total_length // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            nums1_left = nums1[i] if i >= 0 else float("-infinity")
            nums1_right = nums1[i + 1] if (i + 1) < len(nums1) else float("infinity")

            nums2_left = nums2[j] if j >= 0 else float("-infinity")
            nums2_right = nums2[j + 1] if (j + 1) < len(nums2) else float("infinity")
            
            if nums1_left <= nums2_right and nums2_left <= nums1_right:

                if total_length % 2:
                    return min(nums1_right, nums2_right)
                
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            
            elif nums1_left > nums2_right:
                r = i - 1
            else:
                l = i + 1

if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))