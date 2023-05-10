# 0066 - Plus One

'''
    Question:
        You are given a large integer represented as an integer array digits, 
        where each digits[i] is the ith digit of the integer. 
        
        The digits are ordered from most significant to least significant in left-to-right order. 
        The large integer does not contain any leading 0's.
        Increment the large integer by one and return the resulting array of digits.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        right = len(digits) - 1

        return self.plus(digits, right)
      
    
    def plus(self, digits, right):
        
        digits[right] = digits[right] + 1
        
        if digits[right] == 10:
            
            if right == 0:
                digits[right] = 0
                digits.insert(0, 1)
                return digits
            
            digits[right] = 0
            self.plus(digits, right - 1)

        return digits


if __name__ == '__main__':
    
    digits = [4,3,2,1]
    # digits = [9, 9]
    sol = Solution()
    print(sol.plusOne(digits))