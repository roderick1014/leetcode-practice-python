# 0028 - Find the Index of the First Occurence in a String

'''
    Question:
        Given two strings needle and haystack, 
        return the index of the first occurrence of needle in haystack, 
        or -1 if needle is not part of haystack.

'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle in haystack:
            # .find() function returns the index where the sub-string begins.
            return haystack.find(needle)
        else:
            return -1

if __name__ == '__main__':
    
    haystack = "sadbutsad"
    needle = "sad"

    sol = Solution()
    print(sol.strStr(haystack, needle))
