# 0205 - Isomorphic Strings

'''
    Question:
        Given two strings s and t, determine if they are isomorphic.

        Two strings s and t are isomorphic if the characters in s can be replaced to get t.

        All occurrences of a character must be replaced with another character while preserving
        the order of characters. No two characters may map to the same character,
        but a character may map to itself.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Solution - 2 (list.index() return the first index of the required element.)

        map1 = []
        map2 = []

        for idx in s:
            map1.append(s.index(idx))

        for idx in t:
            map2.append(t.index(idx))

        if map1 == map2:
            return True

        return False

    # Solution - 1
    #     return self.xForm(s) == self.xForm(t)

    # def xForm(self, s):
    #     if not s:
    #         return None

    #     hash_map = dict()
    #     represent = []

    #     for idx in range(len(s)):
    #         if s[idx] in hash_map:
    #             represent.append(hash_map[s[idx]])
    #         else:
    #             hash_map[s[idx]] = idx
    #             represent.append(idx)

    #     return represent

if __name__ == '__main__':
    # s = "egg"
    # t = "add"
    s = "aba"
    t = "aab"

    sol = Solution()
    print(sol.isIsomorphic(s, t))