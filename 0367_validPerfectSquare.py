# 0367 - Valid Perfect Square

'''
    Question:
        Given a positive integer num, return true if num is a perfect square or false otherwise.

        A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

        You must not use any built-in library function, such as sqrt.
'''

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        upper = num
        target = upper
        lower = 0
        while target > 1:

            if target * target == num and round(target, 10).is_integer:
                return True
            
            elif target * target < num:
                lower = target
                target = (upper + lower) / 2

            elif target * target > num:
                upper = target
                target = (upper + lower) / 2

            # if (target == lower) or (target == upper):
            #     return True
            
        return False

if __name__ == '__main__':
    n = 16
    sol = Solution()
    print(sol.isPerfectSquare(n))