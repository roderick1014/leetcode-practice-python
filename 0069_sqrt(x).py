# 0069 - Sqrt(x)

'''
    Question: 
        Given a non-negative integer x, return the square root 
        of x rounded down to the nearest integer. 
        The returned integer should be non-negative as well.

         - You must not use any built-in exponent function or operator.

         - For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        upper = x
        target = upper
        lower = 0
        while target != 0:

            if target * target == x:
                return target
            
            elif target * target < x:
                lower = target
                target = (upper + lower) // 2

            elif target * target > x:
                upper = target
                target = (upper + lower) // 2

            if (target == lower) or (target == upper):
                return target
            
        return target



if __name__ == '__main__':
    
    x = 169

    sol = Solution()
    print(sol.mySqrt(x))