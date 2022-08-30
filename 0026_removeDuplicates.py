# 0026 removeDuplicates

'''
    Question:
        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-placesuch that each 
        unique element appears only once. The relative order of the elements should be kept the same.
        
        Since it is impossible to change the length of the array in some languages, you must instead have the 
        result be placed in the first part of the array nums. More formally, if there are k elements after removing 
        the duplicates, then the first k elements of nums should hold the final result. It does not matter what you
         leave beyond the first k elements.
        
        Return k after placing the final result in the first k slots of nums.
        Do "not" allocate extra space for another array. 
        You must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 1

        for index in range(len(nums) - 1):
            if nums[index] != nums[index + 1]:
                nums[k] = nums[index + 1]
                k += 1
        # for i in range(len(nums[k:])):    # For display
        #     nums[k + i] = '_'             # For display
        # print('After removing: ', nums)   # For display

        return k

        

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print('Before removing: ', nums)
    sol = Solution()
    print('Unique elements: ', sol.removeDuplicates(nums))
    