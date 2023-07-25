# 0117 - Populating Next Right Pointers in Each Node II.

'''
    Question:
        Given a binary tree
        Populate each next pointer to point to its next right node. 
        If there is no next right node, the next pointer should be set to NULL.

        Initially, all next pointers are set to NULL.


'''

"""
# Definition for a Node.
"""

from collections import deque

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if not root:
            return None

        dummy = Node(float('-inf')) 
        queue = deque([root])
        
        while queue:
            length = len(queue)
            prev = dummy
            for _ in range(length):
                cur_node = queue.popleft()
                if cur_node.left:
                    queue.append(cur_node.left)
                    prev.next = cur_node.left
                    prev = prev.next        
                if cur_node.right:
                    queue.append(cur_node.right)
                    prev.next = cur_node.right
                    prev = prev.next
        return root
        
if __name__ == '__main__':
    root = Node(val=1, left = Node(val = 2, left = Node(val = 4), right = Node(val = 5)), right = Node(val = 2, right = Node(val = 7)))
    sol = Solution()
    sol.connect(root)