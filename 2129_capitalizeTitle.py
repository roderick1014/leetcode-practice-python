# 2129 - capitalizeTitle

'''
    Question:
        You are given a string title consisting of one or more words separated by a single space, where 
        each word consists of English letters. Capitalize the string by changing the capitalization of 
        each word such that:
        
        If the length of the word is 1 or 2 letters, change all letters to lowercase.
        Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
        Return the capitalized title.
'''

class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        return ' '.join([word.lower() if len(word) < 3 else word.title() for word in title.split(' ')])


if __name__ == '__main__':
    input = 'i lOve leetcode'
    sol = Solution()
    print(sol.capitalizeTitle(input))