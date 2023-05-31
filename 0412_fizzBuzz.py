# 0412 - Fizz Buzz

'''
    Question:
        Given an integer n, return a string array answer (1-indexed) where:

        - answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        - answer[i] == "Fizz" if i is divisible by 3.
        - answer[i] == "Buzz" if i is divisible by 5.
        - answer[i] == i (as a string) if none of the above conditions are true.
'''

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
		
        for x in range(1, n + 1):
            if x % 15 == 0:
                arr.append('FizzBuzz')
            elif x % 3 == 0:
                arr.append('Fizz')
            elif x % 5 == 0:
                arr.append('Buzz')
            else:
                arr.append(str(x))
			
        return arr
