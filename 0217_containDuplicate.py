# 0217 - Contain Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Don't use hashmap, it takes too much space

        return len(nums) != len(set(nums))  
        # "set" in python creates a container that stores non-repeat numbers.
        # If the number in the list is repeated, the extra number will be reduced and create a non-repeat set of number after set() operation.

if __name__ == '__main__':

    nums = [1,1,1,3,3,4,3,2,4,2]
    sol = Solution()
    ans = sol.containsDuplicate(nums)
    print(ans)