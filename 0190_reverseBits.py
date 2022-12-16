# 0190 - Reverse Bits

'''
    Question:
        Reverse bits of a given 32 bits unsigned integer.
'''

class Solution:

    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):  # 32 bits unsigned integer
            ans = (ans << 1) + (n & 1)    # Shift 1 bit left and add the current left-most bit to the right. Ex: 1110 -> 1101
            n >>= 1                     # Shift number n by each iteration.                                        
        return ans

if __name__ == '__main__':
    n = 4294967293
    print('{0:032b}'.format(n))
    sol = Solution()
    ans = sol.reverseBits(n)
    print('{0:032b}'.format(ans))