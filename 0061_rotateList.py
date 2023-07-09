# 0061 - Rotate List

'''
    Question:
        Given the head of a linked list,
        rotate the list to the right by k places.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        # # Solution 2 - Cycle List (Smarter)
        # if not head:
        #     return None

        # lastElement = head
        # length = 1

        # while ( lastElement.next ):
        #     lastElement = lastElement.next
        #     length += 1

        # k = k % length

        # lastElement.next = head

        # tempNode = head
        # for _ in range( length - k - 1 ):
        #     tempNode = tempNode.next

        # answer = tempNode.next
        # tempNode.next = None

        # return answer

        # Solution 1 - My solution
        if not head or not head.next or not k:
            return head

        dummy = fast = slow = ListNode(val = -1, next = head)
        length = 0

        while fast.next:
            length += 1
            fast = fast.next

        k = k % length

        if not k:
            return head

        cut_point = length - k
        connect_point = fast
        fast = dummy

        for _ in range(cut_point):
            slow = slow.next
            fast = fast.next

        fast = fast.next
        slow.next = None
        connect_point.next = dummy.next
        dummy.next = fast

        return dummy.next

def display(node_ref):
    rec = []
    node = node_ref
    while node:
        rec += node.val,
        node = node.next
    print(rec)

if __name__ == '__main__':
    head = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val = 3, next = ListNode(val = 4, next = ListNode(val = 5)))))
    k = 2
    display(head)
    sol = Solution()
    new_head = sol.rotateRight(head, k)