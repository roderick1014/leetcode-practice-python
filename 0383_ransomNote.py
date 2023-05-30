# 0383 - Ransom Note

'''
    Question:
        Given two strings ransomNote and magazine,
        return true if ransomNote can be constructed
        by using the letters from magazine and false otherwise.
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        if ransomNote in magazine:
            return True

        record_freq = dict()

        # record how many times each character appears
        for char in ransomNote:
            if char in record_freq:
                record_freq[char] += 1
            else:
                record_freq[char] = 1

        # list.count() returns the frequency of each character in magazine.
        for char in record_freq:
            if magazine.count(char) < record_freq[char]:
                print(magazine.count(char))
                return False

        return True

if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "aab"

    sol = Solution()
    print(sol.canConstruct(ransomNote, magazine))