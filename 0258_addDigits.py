# 0258 - Add Digits

'''
    Question:
        Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
        
        Follow up: Do it without any loop/recursion in O(1) runtime?
'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        # Solution 2 - (Optimal solution without for/while loop, Time Complexity -> O(1))
        return 9 if (num % 9 == 0) and (num != 0) else num % 9
    
        # Solution 1 - While loop
        # if not num:
        #     return 0
        
        # while (num // 10) != 0:
        #     num = (num % 10) + (num // 10)
        # return num 

if __name__ == '__main__':
    num = 0
    
    sol = Solution()
    print(sol.addDigits(num))