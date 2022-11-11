# 0647 - Palindromic Substrings

'''
    Questions:
        Given a string s, return the number of palindromic substrings in it.
        A string is a palindrome when it reads the same backward as forward.
        A substring is a contiguous sequence of characters within the string.
'''

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)
        cnt = 0
    
        for idx in range(length * 2):
            l_ptr = idx // 2
            r_ptr = (idx + 1) // 2
            while l_ptr >= 0 and r_ptr < length and s[l_ptr] == s[r_ptr]:
                cnt += 1
                l_ptr -= 1
                r_ptr += 1
        
        return cnt
                
if __name__ == '__main__':
    s = 'aabaca'
    sol = Solution()
    print(sol.countSubstrings(s))