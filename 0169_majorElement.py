# 0169 - Majority Element

'''
    Question:
        Given an array nums of size n, return the majority element.
        The majority element is the element that appears more than [n / 2] times.
        You may assume that the majority element always exists in the array.

        ! solve the problem in linear time and in O(1) space !
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Solution - 1 → Time complexity: O(n), Space complexity: O(1)
        candidate = nums[0]
        count = 1

        for idx in range(1, len(nums)):
            if candidate != nums[idx]:
                count -= 1
                if count == 0:
                    candidate = nums[idx]
                    count += 1
            else:
                count += 1

        return candidate
    
        # Solution - 2 → Time complexity: At least O(nlog(n)), Space complexity: (log(n))
        # return sorted(nums)[len(nums) // 2]


if __name__ == '__main__':
    nums = [8,8,7,7,7]
    sol = Solution()
    print(sol.majorityElement(nums))