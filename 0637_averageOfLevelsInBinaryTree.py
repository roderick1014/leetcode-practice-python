# 0637 - Average of Levels in Binary Tree

'''
    Question:
        Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
        Answers within 10-5 of the actual answer will be accepted.
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        # ! Removing the first element would be O(1) instead of O(N) time complexity if we apply deque instead of list.
        queue = deque()
        queue.append(root)
        ans = []
        # BFS - Breadth-First Search
        while len(queue):
            queue_len = len(queue)
            row_accumulation = 0.0
            for _ in range(queue_len):
                cur = queue.popleft()
                row_accumulation += cur.val
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            ans.append(row_accumulation / queue_len)
        return ans

if __name__ == '__main__':
    node = TreeNode(val = 3, left = TreeNode(val = 9), right = TreeNode(val = 20, left = TreeNode(val = 15), right = TreeNode(val = 7)))

    sol = Solution()
    print(sol.averageOfLevels(node))