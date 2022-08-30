# 0020 - Valid Parentheses

'''
    Question:
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.
'''

class Solution(object):
    def isValid(self, s):

        """
        :type s: str
        :rtype: bool
        """

        stack = [0]
        brackets_map = {0 : None, '{' : '}', '[' : ']', '(' : ')'}
        for character in s:
            if character in brackets_map:
                stack.append(character)
            else:
                if brackets_map[stack.pop()] != character:
                    return False
        return stack == [0]

if __name__ == '__main__':
    input = '()[]{}'
    sol = Solution()
    print(sol.isValid(input))