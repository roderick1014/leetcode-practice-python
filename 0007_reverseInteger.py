# 0007 - Reverse Integer

'''
    Question:
        Given a signed 32-bit integer x, return x with its digits reversed. 
        If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''

class Solution(object):
    
    def reverse(self, x):
        
        """
        :type x: int
        :rtype: int
        """
        
        reverse_num = 0

        while x != 0:
            
            if x < 0:
                reverse_num = reverse_num * 10 + x % -10    
                x = - (x // -10)

            else:
                reverse_num = reverse_num * 10 + x % 10
                x = x // 10
        
        return reverse_num if -(2**31)-1 < reverse_num < 2**31 else 0

if __name__ == '__main__':
    x = 1534236469
    sol = Solution()
    print(sol.reverse(x))