# 0206 - Reverse Linked List

'''
    Question:
        Given the head of a singly linked list, reverse the list, and return the reversed list.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        previous_node = None
        while head:
            temp = head
            head = head.next
            temp.next = previous_node
            previous_node = temp
            # -------------------------
            # tmp_1 = current_node        
            # tmp_2 = previous_node       
            # tmp_3 = current_node.next    
            # previous_node = tmp_1
            # current_node.next = tmp_2
            # current_node = tmp_3
            # -------------------------
            # previous_node, current_node.next, current_node = current_node, previous_node , current_node.next
        return previous_node

def init_list(input):

    dummy = linked_list = ListNode(val = input[0])
    for idx in range(1, len(input)):
        linked_list.next = ListNode(val = input[idx])
        linked_list = linked_list.next
    return dummy

def display_list(input):
    display = input
    display_str = ''
    while display:
        current_str = str(display.val) + ' '
        display_str += current_str
        display = display.next
    print(display_str)

if __name__ == '__main__':

    head = [1, 2, 3, 4, 5]

    link_list = init_list(head)
    display_list(link_list)

    sol = Solution()
    new_link_list = sol.reverseList(link_list)
    display_list(new_link_list)
        