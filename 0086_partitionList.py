# 0086 - Partition List

'''
    Question:
        Given the head of a linked list and a value x,
        partition it such that all nodes less than x
        come before nodes greater than or equal to x.

        You should preserve the original relative order of the nodes
        in each of the two partitions.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if not head:
            return head

        dummy = left = ListNode(0)
        rec_node = cur = ListNode(0)


        while head:
            if head.val >= x:
                cur.next = head
                cur = cur.next
            else:
                left.next = head
                left = left.next
            head = head.next

        cur.next = None
        left.next = rec_node.next

        return dummy.next


def display(node_ref):
    rec = []
    node = node_ref
    while node:
        rec += node.val,
        node = node.next
    print(rec)

if __name__ == '__main__':
    head = ListNode(val = 1, next = ListNode(val = 4, next = ListNode(val = 3, next = ListNode(val = 2, next = ListNode(val = 5, next = ListNode(val = 2))))))
    display(head)
    x = 3
    sol = Solution()
    new_head = sol.partition(head, x)
    display(new_head)