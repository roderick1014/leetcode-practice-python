# 0392 - Is Subsequence


'''
    Question:
        Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

        A subsequence of a string is a new string that is formed from the original string by
        deleting some (can be none) of the characters without disturbing the relative positions
        of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if not s:
            return True

        if len(s) == 1 and len(t) == 1:
            return s == t

        ptr_t = ptr_s = 0

        while ptr_t < len(t):
            if s[ptr_s] == t[ptr_t]:
                ptr_s += 1
            if ptr_s == len(s):
                return True
            ptr_t += 1
        return False

        # Solution 2 - Cleaner
        # ptr_t, ptr_s = 0, 0

        # while ptr_t < len(t) and ptr_s < len(s):
        #     if s[ptr_s] == t[ptr_t]:
        #         ptr_s += 1
        #     ptr_t += 1
        # return ptr_s == len(s)

if __name__ == '__main__':
    s = "bb"
    t = "ahbgdc"
    # s = "axc"
    # t = "ahbgdc"
    # s = "abc"
    # t = "ahbgdc"
    s = "b"
    t = "abc"

    sol = Solution()
    print(sol.isSubsequence(s, t))