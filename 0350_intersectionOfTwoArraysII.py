# 0350 - Intersection of Two Arrays

'''
    Question:
        Given two integer arrays nums1 and nums2, 
        return an array of their intersection. 
        
        Each element in the result must appear as many times 
        as it shows in both arrays and you may return the result in any order.

        Follow up:

             - What if the given array is already sorted? How would you optimize your algorithm?
             - What if nums1's size is small compared to nums2's size? Which algorithm is better?
             - What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

from collections import Counter

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # # Solution 3 - Sort the array and apply two pointers
        # # Space (without counting output as space): O(sorting)
        # # Time: O(MlogM + NlogN), where M <= 1000 is length of nums1 array, N <= 1000 is length of nums2 array.
        # nums1.sort()
        # nums2.sort()
        
        # ans = []
        # i = j = 0
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     elif nums1[i] > nums2[j]:
        #         j += 1
        #     else:
        #         ans.append(nums1[i])
        #         i += 1
        #         j += 1
        # return ans


        # Solution 2 - Counter returns a hashmap with the frequency that each value appears
        # Space: O(min(M, N)), Time: O(M + N), where M <= 1000 is length of nums1 array, N <= 1000 is length of nums2 array.
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans

        # # Solution 1 - Handmade hashmap counter
        # ans = []
        # hash_map = dict()

        # if len(nums1) == len(nums2):
        #     for element in nums1:
        #         if element not in hash_map:
        #             hash_map[element] = 1
        #         else:
        #             hash_map[element] += 1
        #     for element in nums2:
        #         if element in hash_map and hash_map[element] != 0:
        #             hash_map[element] -= 1
        #             ans.append(element)
        # elif len(nums1) < len(nums2):
        #     for element in nums1:
        #         if element not in hash_map:
        #             hash_map[element] = 1
        #         else:
        #             hash_map[element] += 1
        #     for element in nums2:
        #         if element in hash_map and hash_map[element] != 0:
        #             hash_map[element] -= 1
        #             ans.append(element)

        # elif len(nums1) > len(nums2):
        #     for element in nums2:
        #         if element not in hash_map:
        #             hash_map[element] = 1
        #         else:    
        #             hash_map[element] += 1
        #     for element in nums1:
        #         if element in hash_map and hash_map[element] != 0:
        #             hash_map[element] -= 1
        #             ans.append(element)

        # return ans

if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    # nums1 = [4,9,5]
    # nums2 = [9,4,9,8,4]

    sol = Solution()
    print(sol.intersection(nums1, nums2))