# 0290 - Word Pattern

'''
    Question:
        Given a pattern and a string s, find if s follows the same pattern.

        Here follow means a full match, such that there is a bijection between
        a letter in pattern and a non-empty word in s.
'''

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        # Solution 2 - 2 recording list.
        s = s.split()
        if len(s) != len(pattern):
            return False
        rec_1 = []
        rec_2 = []
        for element in s:
            rec_1.append(s.index(element))
        for element in pattern:
            rec_2.append(pattern.index(element))

        return rec_1 == rec_2

        # Solution 1 - 1 recording list.
        # s = s.split()
        # if len(s) != len(pattern):
        #     return False
        # record = []
        # for element in s:
        #     record.append(s.index(element))
        # for idx in range(len(pattern)):
        #     if pattern.index(pattern[idx]) != record[idx]:
        #         return False

        # return True

        


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat fish"
    
    sol = Solution()
    print(sol.wordPattern(pattern, s))