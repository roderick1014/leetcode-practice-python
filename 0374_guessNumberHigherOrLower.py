# 0374 - Guess Number Higher or Lower

'''
    Question:
        We are playing the Guess Game. The game is as follows:

        I pick a number from 1 to n. You have to guess which number I picked.

        Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

        You call a pre-defined API int guess(int num), which returns three possible results:

        -1: Your guess is higher than the number I picked (i.e. num > pick).
        1: Your guess is lower than the number I picked (i.e. num < pick).
        0: your guess is equal to the number I picked (i.e. num == pick).
        Return the number that I picked.
'''

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        upper = n
        lower = 1
        while (lower <= upper):
            mid = (upper + lower) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                upper = mid - 1
            else:
                lower = mid + 1
            
if __name__ == '__main__':
    pass