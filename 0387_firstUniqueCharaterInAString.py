# 0387 - First Unique Charater in a String

'''
    Question:
        Given a string s, find the first non-repeating character in it 
        and return its index. If it does not exist, return -1.
'''

from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        record = Counter(s)
        for idx in range(len(s)):
            if record[s[idx]] == 1:
                return idx
        return -1

if __name__ == '__main__':
    s = "loveleetcode"
    sol = Solution()
    print(sol.firstUniqChar(s))