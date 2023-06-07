# 0151 - Reverse Words in A String

'''
    Question:
        Given an input string s, reverse the order of the words.
        A word is defined as a sequence of non-space characters.

        The words in s will be separated by at least one space.
        Return a string of the words in reverse order concatenated by a single space.

        Note that s may contain leading or trailing spaces or multiple spaces between two words.
        The returned string should only have a single space separating the words. Do not include any extra spaces.
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s.split()
        s.reverse()
        return ' '.join(s)

        # Solution - One liner
        # return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    sol = Solution()
    s = "the sky is blue"
    print(sol.reverseWords(s))