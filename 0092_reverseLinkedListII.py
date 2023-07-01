# 0092 - Reverse Linked List II

'''
    Given the head of a singly linked list and two integers left and right
    where left <= right, reverse the nodes of the list from position left
    to position right, and return the reversed list.
'''

from collections import deque

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        # Solution 3 - Operation without store elements and faster.
        if left == right: return head

        pre = dummy = ListNode(val = -1, next = head)
        cnt = 0

        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        new_head = None

        # Conduct reverse operation from the starting point.
        for _ in range(right - left + 1):
            next = cur.next
            cur.next = new_head
            new_head = cur
            cur = next

        # Link to the ending point.
        pre.next.next = cur         # the latter part of the none reversed list.
        pre.next = new_head

        return dummy.next

        # # Solution 2 - Operation without store elements.
        # if left == right: return head

        # cur = dummy = ListNode(val = -1, next = head)
        # cnt = 0

        # while cur:

        #     # Record the node before the starting point.
        #     if cnt == left - 1:
        #         rec_left = cur

        #     # Record the node next to the ending point.
        #     if cnt == right:
        #         rec_right = cur.next
        #         break

        #     cur = cur.next
        #     cnt += 1

        # cur = rec_left.next
        # new_head = rec_right

        # # Conduct reverse operation from the starting point.
        # while cur != rec_right:
        #     next = cur.next
        #     cur.next = new_head
        #     new_head = cur
        #     cur = next

        # # Link to the ending point.
        # rec_left.next = new_head

        # return dummy.next

        # # Solution 1 - Store the nodes in the list. (Space is not good enough)
        # if left == right: return head

        # cur = dummy = ListNode(val = -1, next = head)
        # cnt = 0
        # node_queue = deque()

        # while cur:
        #     # Record the node before the starting point.
        #     if cnt == left - 1:
        #         rec_left = cur

        #     # Record the node next to the ending point.
        #     if cnt == right + 1:
        #         rec_right = cur
        #         break

        #     # Record the target sub-linkedlist.
        #     if left <= cnt <= right:
        #         node_queue.append(cur.val)

        #     cur = cur.next
        #     cnt += 1

        # # Conduct reverse operation from the starting point.
        # for _ in range(len(node_queue)):
        #     rec_left.next = ListNode(val = node_queue.pop())
        #     rec_left = rec_left.next

        # # Link to the ending point.
        # rec_left.next = rec_right

        # return dummy.next
def display_nodes(node):
    k = node
    a = []
    while k:
        a.append(k.val)
        k = k.next
    print(a)

if __name__ == '__main__':
    sol = Solution()
    node = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val = 3, next = ListNode(val = 4, next = ListNode(val = 5)))))
    sol.reverseBetween(node, 2, 4)