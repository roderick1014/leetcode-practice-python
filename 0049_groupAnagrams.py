# 0049 - Group Anagrams

'''
    Question:
        Given an array of strings strs, group the anagrams together. 
        You can return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters
        of a different word or phrase, typically using all the original letters exactly once.
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # Solution 2 - Hashmap & Transform to List
        strs_table = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string not in strs_table:
                strs_table[sorted_string] = []

            strs_table[sorted_string].append(string)

        return list(strs_table.values())

        # Solution 1 - Hashmap & List Recording Simultaneously
        # record_map = dict()
        # ans = []
        # map_index = 0

        # for string in strs:
        #     sorted_string = ''.join(sorted(string))
        #     if sorted_string not in record_map:
        #         record_map[sorted_string] = map_index
        #         ans.append([string])
        #         map_index += 1
        #     else:
        #         ans[record_map[sorted_string]].append(string)
        # return ans

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    
    sol = Solution()
    print(sol.groupAnagrams(strs))