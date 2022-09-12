# 0083 - Remove Duplicates from Sorted List


'''
    Question:
        Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        
        '''
            : type: ListNode
            : rtype: ListNode
        '''
        
        # Example: 1, 1, 1, None
        current = head
        # Condition: If the current node exists.
        while current:
            # Condition: If the next node exists and the value of the next node is the same as the current node.    
            while current.next and current.next.val == current.val: # 1st time: 1, 1, None ; 2st time: 1, None 
                current.next = current.next.next # node replacement
            current = current.next

        return head



if __name__ == '__main__':
    node_1 = ListNode(val = 1)
    node_2 = ListNode(val = 1)
    node_3 = ListNode(val = 1)
    node_1.next = node_2
    node_2.next = node_3
    
    # Additional.
    # node_4 = ListNode(val = 3)
    # node_5 = ListNode(val = 3)
    # node_3.next = node_4
    # node_4.next = node_5

    sol = Solution()
    output = sol.deleteDuplicates(node_1)
    # print(output.val, output.next.val, output.next.next.val)
    sample_output = output
    while sample_output:
        print(sample_output.val)
        sample_output = sample_output.next
