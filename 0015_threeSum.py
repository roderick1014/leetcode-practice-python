# 0015 - Three Sum

'''
    Question:
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets.
'''


class Solution(object):
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums = sorted(nums)

        for l_ptr in range(len(nums) - 2):
            if l_ptr > 0 and nums[l_ptr] == nums[l_ptr - 1]: # To avoid checking duplicate.
                continue
            m_ptr, r_ptr = l_ptr + 1, len(nums) - 1

            while m_ptr < r_ptr: # If r_ptr < m_ptr, the iteration finishes.

                current_sum = nums[l_ptr] + nums[m_ptr] + nums[r_ptr]
                
                if current_sum < 0:
                    m_ptr += 1
                elif current_sum > 0:
                    r_ptr -= 1
                else:
                    res.append([nums[l_ptr], nums[m_ptr], nums[r_ptr]])

                    while m_ptr < r_ptr and nums[m_ptr] == nums[m_ptr + 1]: # To avoid checking duplicate.
                        m_ptr += 1
                    while m_ptr < r_ptr and nums[r_ptr] == nums[r_ptr - 1]: # To avoid checking duplicate.
                        r_ptr -= 1
                    m_ptr += 1
                    r_ptr -= 1
                
        return res

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    # nums = [0,0,0,0]
    # nums = [0,0,0]
    # nums = [0,1,1]
    sol = Solution()
    ans = sol.threeSum(nums)
    print(ans)