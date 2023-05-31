# 0345 - Reverse Vowels of a String

'''
    Question:
        Given a string s, reverse only all the vowels
        in the string and return it.

        The vowels are 'a', 'e', 'i', 'o', and 'u',
        and they can appear in both lower and upper cases,
        more than once.
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        l, r = 0, n - 1
        vowels = "aeiouAEIOU"
        s = list(s)
        while l < r:

            while l < r and s[l] not in vowels:
                l += 1

            while r > l and s[r] not in vowels:
                r -= 1
 
            s[l], s[r] = s[r], s[l]
            
            l += 1
            r -= 1
            
        return ''.join(s)

if __name__ == '__main__':
    s = "hello"
    sol = Solution()
    print(sol.reverseVowels(s))
    
    