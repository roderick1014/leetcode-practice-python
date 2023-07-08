# 0082 - Remove Duplicates from Sorted Array

'''
    Question:
        Given the head of a sorted linked list,
        delete all nodes that have duplicate numbers,
        leaving only distinct numbers from the original list.
        
        Return the linked list sorted as well.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # Solution 1 - My solution.
        if not head:
            return head
        
        if not head.next:
            return head
        
        dummy = ListNode(val = None, next = head)
        
        duplicate = False
        l = dummy
        r = dummy.next
        
        while r.next:
            if duplicate == True:
                if r.val != r.next.val:
                    r = r.next
                    l.next = r
                    duplicate = False
                else:
                    r = r.next
                    l.next = r
            
            else:
                if r.val == r.next.val:
                    duplicate = True
                    r = r.next
                    l.next = r
                else:
                    l = l.next
                    r = r.next
                    
        if duplicate == True:
            l.next = None
        
        return dummy.next
    
        # Solution 2 - while loop in while loop
        
        # dummy = pre = ListNode(0)
        # dummy.next = head
        # while head and head.next:
        #     if head.val == head.next.val:
        #         while head and head.next and head.val == head.next.val:
        #             head = head.next
        #         head = head.next
        #         pre.next = head
        #     else:
        #         pre = pre.next
        #         head = head.next
        # return dummy.next

def displayList(node_ref):
    container = []
    node = node_ref
    while node:
        container.append(node.val)
        node = node.next
    print(container)

if __name__ == '__main__':
    # node = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val = 3, next = ListNode(val = 3, next = ListNode(val = 4, next = ListNode(val = 4, next = ListNode(val = 5))))))) 
    node = ListNode(val = 1, next = ListNode(val = 1))
    displayList(node)
    sol = Solution()
    new_node = sol.deleteDuplicates(node)
    displayList(new_node)