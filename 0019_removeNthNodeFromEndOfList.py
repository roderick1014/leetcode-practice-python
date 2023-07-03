# 0019 - Remove Nth Node From End of List.

'''
    Question:
        Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # Solution 2 - Easier Two Pointer
        fast, slow = head, head

        for _ in range(n):
            fast = fast.next

        # if fast pointer reach the end, implis n will remove first node.
        if not fast: return head.next

        # when the fast pointer reach the end, the slow pointer reach the position before the target we are going to remove.
        while fast.next:
            fast, slow = fast.next, slow.next

        slow.next = slow.next.next

        return head

        # # Solution 1 - My solution (One pass)
        # if not head.next:
        #     return

        # dummy = fast = slow = ListNode(val = -1, next = head)
        # slow_idx, fast_idx = 0, 0
        # find_rm = False

        # while slow:
        #     if find_rm:
        #         if slow_idx == n - 1:
        #             print(slow_idx)
        #             slow.next = slow.next.next
        #             print(slow.val, slow.next.val)
        #             return dummy.next
        #         slow_idx += 1
        #         slow = slow.next
        #     else:
        #         if not fast:
        #             n = fast_idx - n
        #             find_rm = True
        #             continue

        #         elif not fast.next:
        #             n = fast_idx - n + 1
        #             find_rm = True
        #             continue

        #         fast = fast.next.next
        #         fast_idx += 2


if __name__ == '__main__':
    head = ListNode(val = 1, next = ListNode(val = 2))
    n = 2
    sol = Solution()
    head = sol.removeNthFromEnd(head, n)
    print(head.val, head.next.val)