# 0009 - Palindrome Number

'''
    Question:
        Given an integer x, return true if x is palindrome integer.
        An integer is a palindrome when it reads the same backward as forward.
'''

class Solution(object):
    def isPalindrome(self, x):
        
        """
        :type x: int
        :rtype: bool
        """
                
        if x < 0 or (x % 10 == 0 and x > 0):
            return False

        reverse = 0
        
        # We will measure the integer by check the reverse of it, which fits the feature of the palindrome number.
        # The stopping condition is that we've reverse the integer to its middle point (ex: '1' in 151).

        # To make sure that we have reach the middle point, we can infer that if the reverse number is larger than
        # or equal to the integer in the reverse process. (ex: 151 reversing to '1' and '51')

        while x > reverse:
            reverse = reverse * 10 + x % 10 # Reverse the integer of the last digit.   
            x = x // 10                     # Ex: 1st iteration - 15951 & _____ -> 1595  &   1  
                                            #     2st iteration - 1595  &   1   -> 159   &  15
                                            #     3st iteration - 159   &  15   -> 15    &  159  (reverse > x occurs!)
        return reverse == x or x == reverse // 10

if __name__ == '__main__':
    input = -121
    sol = Solution()
    print(sol.isPalindrome(input))
