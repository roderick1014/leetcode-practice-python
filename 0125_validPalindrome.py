# 0125 - Valid Palindrome

'''
    Question:
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
        Alphanumeric characters include letters and numbers.
        Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        l_ptr = 0
        r_ptr = len(s) - 1
        
        while l_ptr < r_ptr:

                while not s[l_ptr].isalnum() and l_ptr < r_ptr:
                    l_ptr += 1

                while not s[r_ptr].isalnum() and l_ptr < r_ptr:
                    r_ptr -= 1

                if not s[l_ptr].lower() == s[r_ptr].lower():
                    return False

                l_ptr += 1
                r_ptr -= 1
        
        return True

    
if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    # s = "race a car"
    # s = " "
    sol = Solution()
    print(sol.isPalindrome(s))