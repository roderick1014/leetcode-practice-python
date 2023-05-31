# 0415 - Add Strings

'''
    Question:
        Given two non-negative integers, num1 and num2 represented as string, 
        return the sum of num1 and num2 as a string.

        You must solve the problem without using any built-in library for handling 
        large integers (such as BigInteger). You must also not convert the inputs to integers directly.
'''


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        def str2int(num):
            result  = 0
            for n in num:
                result = result * 10 + ord(n) - ord('0')
            return result
        
        return str(str2int(num1) + str2int(num2))
    
if __name__ == '__main__':
    num1 = "11"
    num2 = "123"
    sol = Solution()
    print(sol.addStrings(num1, num2))
