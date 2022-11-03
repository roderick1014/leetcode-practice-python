# 0238 - Product of Array Except Self

'''
    Question:
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        You must write an algorithm that runs in O(n) time and "without using the division operation".
'''


class Solution(object):
    
    def productExceptSelf(self, nums):

        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans = [1] * len(nums) # Answer initialization.
        
        left_accumulation = 1
        right_accumulation = 1
        idx = 0
        
        # We can consider the final output values in the array to be the right-part accumulated multiplications times the left-part accumulated multiplications.
        # Two pointers traverse the array forwardly and backward once, accumulating the value (left-part and right-part).
        # Thus this operation can be done in O(n).

        while idx < len(nums):
            
            ans[idx] *= left_accumulation       # Start from the left-most element in the array.  (Like a pointer) 
            ans[-1-idx] *= right_accumulation   # Start from the right-most element in the array. (Like a pointer)
            left_accumulation *= nums[idx]      # Multiplication accumulation.
            right_accumulation *= nums[-1-idx]  # Multiplication accumulation.
            idx += 1

        return ans

        
        


if __name__ == '__main__':
    nums = [1,2,3,4]
    sol = Solution()
    ans = sol.productExceptSelf(nums)
    print(ans)