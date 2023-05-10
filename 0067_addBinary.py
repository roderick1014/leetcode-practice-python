# 0067 - Add Binary

'''
    Question:
        Given two binary strings a and b, return their sum as a binary string.
        
        Input: a = "1010", b = "1011"
        Output: "10101"
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        ans = ''

        right_a = len(a) - 1
        right_b = len(b) - 1
        carry = '0'

        while right_a > -1 or right_b > -1:
            if right_a > -1 and right_b > -1:
                
                if a[right_a] == b[right_b]:

                    if a[right_a] == '1':   #        a   b   c        ans   carry
                        if carry == '1':    # case   1   1   1   ->    1      1
                            ans = '1' + ans
                            carry = '1'
                        else:               # case   1   1   0   ->    0      1
                            ans = '0' + ans
                            carry = '1'
                    else:                   
                        if carry == '1':    # case   0   0   1   ->    1      0
                            ans = '1' + ans
                            carry = '0'
                        else:               # case   0   0   0   ->    0      0
                            ans = '0' + ans

                else:   # case '1' and '0'
                    if carry == '1':        # case   1   0   1   ->    0      1
                        ans = '0' + ans
                        carry = '1'
                    else:                   # case   1   0   0   ->    1      0
                        ans = '1' + ans
                        carry = '0'
            elif right_a > -1 and right_b < 0:

                if a[right_a] == '1':
                    if carry == '1':        # case   1   x   1   ->    0      1
                        ans = '0' + ans
                        carry = '1'
                    else:                   # case   1   x   0   ->    1      0
                        ans = '1' + ans
                        carry = '0'
                else:
                    if carry == '1':        # case   0   x   1   ->    1      0
                        ans = '1' + ans
                        carry = '0'
                    else:                   # case   0   x   0   ->    0      0
                        ans = '0' + ans
                        carry = '0'
            elif right_b > -1 and right_a < 0:

                if b[right_b] == '1':
                    if carry == '1':        # case   1   x   1   ->    0      1
                        ans = '0' + ans
                        carry = '1'
                    else:                   # case   1   x   0   ->    1      0
                        ans = '1' + ans
                        carry = '0'
                else:
                    if carry == '1':        # case   0   x   1   ->    1      0
                        ans = '1' + ans
                        carry = '0'
                    else:                   # case   0   x   0   ->    0      0
                        ans = '0' + ans
                        carry = '0'
            
                
            # print(f'r_a: {a[right_a]}, r_b: {b[right_b]}, ans: {ans}, carry: {carry}')
            
            right_a -= 1
            right_b -= 1

        if carry == '1':
            ans = '1' + ans
            return ans
        else:
            return ans


if __name__ == '__main__':
    
    sol = Solution()
    
    # a = "11"
    # b = "1"

    a = "1010"
    b = "1011"

    print(sol.addBinary(a, b))