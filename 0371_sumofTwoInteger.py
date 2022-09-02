# 0371 - Sum of Two Integer

'''
    Question:
        Given two integers a and b, return the sum of the two integers without using the operaters + and -.
'''

class Solution:

    def getSum(self, a: int, b: int) -> int:
        
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff                   # Every operations needs to be masked for the 32 bits bounding.
        a = a & mask                        # Bound the length of sum and carry to 32 bits by setting up a mask.  
        while b:                            # Finsh addition when there's no carry (b is addition number initially).
            sum = (a ^ b) & mask            # '^' -> XOR operation.
            carry = ((a & b) << 1) & mask   # Obtain the carry by AND operation and shift left the value for one bit, we will add this value later. 
            print(sum)
            print(carry)
            a = sum
            b = carry

        if (a >> 31) & 1:                   # Check the sign bit, we will do two's complement if it's a negative integer.
            return ~(a ^ mask)              # Two's complement operation.
        return a


if __name__ == '__main__':
    a = 8888
    b = 9999
    sol = Solution()
    print(sol.getSum(a, b))