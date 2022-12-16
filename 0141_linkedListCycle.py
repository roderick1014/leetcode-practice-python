# 0141 - Linked List Cycle

'''
    Question:
        Given head, the head of a linked list, determine if the linked list has a cycle in it.
        There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
        Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
        Note that pos is not passed as a parameter.
        Return true if there is a cycle in the linked list. Otherwise, return false.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def hasCycle(self, head):
        
        while(head):
            if head.val is not 'inf':
                head.val = 'inf'
                head = head.next
            else:
                return True

        return False


if __name__ == '__main__':
    
    head = [3, 2, 0, 4]
    sol = Solution()
    sol.hasCycle()