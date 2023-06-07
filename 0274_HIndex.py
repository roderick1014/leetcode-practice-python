# 0274 - H-Index.

'''
    Question:
        Given an array of integers citations where citations[i] is
        the number of citations a researcher received for their ith paper,
        return the researcher's h-index.

        According to the definition of h-index on Wikipedia:
            The h-index is defined as the maximum value of h such that
            the given researcher has published at least h papers that
            have each been cited at least h times.
'''

from collections import Counter

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        # Solution 2 - Check sorted value and index (More efficient)
        ans = 0
        for idx, citation in enumerate(sorted(citations, reverse=True)):
            if idx < citation:
                ans += 1
            else:
                return ans
        return ans

        # # Solution 1 - Check sorted value and index
        # if len(citations) == 1 and citations[0] > 0:
        #     return 1

        # citations = sorted(citations, reverse=True)

        # if citations[-1] >= len(citations):
        #     return len(citations)

        # for idx in range(len(citations)):
        #     if citations[idx] < idx + 1:
        #         return idx

if __name__ == '__main__':
    citations = [3,0,6,1,5]
    sol = Solution()
    print(sol.hIndex(citations))