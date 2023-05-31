# 0349 - Intersection of Two Arrays

'''
    Question:
        Given two integer arrays nums1 and nums2, 
        return an array of their intersection. 
        
        Each element in the result must be unique 
        and you may return the result in any order. 
'''

from collections import Counter

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # Solution 1 - Sort the array and apply two pointers
        # Space (without counting output as space): O(sorting)
        # Time: O(MlogM + NlogN), where M <= 1000 is length of nums1 array, N <= 1000 is length of nums2 array.
        nums1.sort()
        nums2.sort()
        
        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] == nums2[j] and nums1[i] not in ans:
                ans.append(nums1[i])
                i += 1
                j += 1
            else:
                i += 1
                j += 1
        return ans


        # # Solution 2 - Counter returns a hashmap with the frequency that each value appears
        # # Space: O(min(M, N)), Time: O(M + N), where M <= 1000 is length of nums1 array, N <= 1000 is length of nums2 array.
        # ans = []
        # for x in nums2:
        #     if x in nums1 and x not in ans:
        #         ans.append(x)
        # return ans


if __name__ == '__main__':
    # nums1 = [1,2,2,1]
    # nums2 = [2,2]
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]

    sol = Solution()
    print(sol.intersection(nums1, nums2))