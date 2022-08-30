# 0001 - twoSum

'''
    Question:
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
'''

class Solution:
    
    def twoSum(self, nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        HashMap = {}
        for index in range(len(nums)):
            if (target - nums[index]) in HashMap:
                return [HashMap.get(target - nums[index]), index]
                # record.get -> obtain the index (which is value in the hashmap) of the recorded number in the hashmap.
            else:
                HashMap[nums[index]] = index
        return None

if __name__ == '__main__':
    nums = [11, 3, 7, 2]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))