# 0014 - longestCommonPrefix

'''
    Question:
        Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution:

    def longestCommonPrefix(self, strs):

        """
        :type strs: List[str]
        :rtype: str: List
        """

        if not strs:
            return ""
        shortest = min(strs, key = len) 
        # Add key argument to obtain the shortest string in the strs.
        for index, character in enumerate(shortest):
            # Take the shortest string to be the reference, since the longest common prefix string is depending on the shortest word.
            for word in strs:   # Check the character in each word. (ex: 'f' in 'flower', 'flow' and 'flight'... )
                if word[index] != character:
                    return shortest[:index]
        return shortest

if __name__ == '__main__':
    input = ['flower', 'flow', 'flight']
    sol = Solution()
    print(sol.longestCommonPrefix(input))