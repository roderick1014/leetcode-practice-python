# 0058 - Length of Last Word

'''
    Question: 
        Given a string s consisting of words and spaces, 
        return the length of the last word in the string. 
        A word is a maximal substring consisting of non-space characters only.

'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Solution 1 - Faster but more memory.
        s = s.replace(' ', '*').split('*')
        
        idx = len(s) - 1

        while idx > -1:

            if s[idx] != '':
                return len(s[idx])
            idx -= 1
        
        return -1

        # Solution 2 - One liner, slower but less memory.
        # return len(s.split()[-1])


if __name__ == '__main__':
    s = "Hello World"
    s = "   fly me   to   the moon  "
    s = 'a'

    sol = Solution()
    print(sol.lengthOfLastWord(s))