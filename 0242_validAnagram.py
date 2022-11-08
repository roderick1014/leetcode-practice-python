# 0242 - Valid Anagram

'''
    Question:
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)



if __name__ == '__main__':
    # s = "anagram"
    # t = "nagaram"
    s = "rat"
    t = "car"
    sol = Solution()
    print(sol.isAnagram(s, t))