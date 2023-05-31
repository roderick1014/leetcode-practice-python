# 0409 - Longest Palindrome

'''
    Question:
        Given a string s which consists of lowercase or uppercase letters, 
        return the length of the longest palindrome that can be built with 
        those letters.

        Letters are case sensitive, for example, "Aa" is not considered a 
        palindrome here.
'''

from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        for element in Counter(s).values():
            ans += (element // 2) * 2
        
        return min(ans + 1, len(s))  
        # !!! If the odd frequency isn't zero, the result will add 1.  !!!
        # (Since it absolutely can be placed to the middle position)
        # otherwise, the longest length of the palindrome will be same as len(s),
        # which implies there's no odd frequency there.

if __name__ == '__main__':
    s = 'aabb'
    sol = Solution()
    print(sol.longestPalindrome(s))