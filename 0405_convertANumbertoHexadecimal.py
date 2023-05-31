# 0405 - Convert a Number to Hexadecimal

'''
    Question:
        Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

        All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

        Note: You are not allowed to use any built-in library method to directly solve this problem.
'''


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0: return '0'
        hex_digits = '0123456789abcdef'
        result = ''
        
        # if negative (two's compliment)
        if num < 0: num = num + (1 << 32)
        while num > 0:
            digit = num % 16
            num = (num - digit) // 16 # (value - remainder) / 16 => next remain digit
            result += hex_digits[digit]
        return result[::-1]

if __name__ == '__main__':
    sol = Solution()
    num = 26
    print(sol.toHex(num))