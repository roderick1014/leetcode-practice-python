# 0219 - Contains Duplicate II

'''
    Question:
        Given an integer array nums and an integer k, 
        return true if there are two distinct indices
        i and j in the array such that nums[i] == nums[j]
        and abs(i - j) <= k.
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        hashmap = {}

        for idx in range(len(nums)):

            if nums[idx] in hashmap and abs(idx - hashmap[nums[idx]]) <= k:
                return True
            hashmap[nums[idx]] = idx

        return False
    
if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    k = 3
    
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))