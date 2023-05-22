# 0203 - Remove Linked List Elements

'''
    Question:

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if not head:
            return None

        while head.val == val:
            if head.next:
                head = head.next
            else:
                return None

        dummy = head

        while head.next:
            if head.next.val == val:
                if head.next.next:
                    head.next = head.next.next
                    continue
                else:
                    if head.next.val != val:
                        break
                    else:
                        head.next = None
                        break
            head = head.next

        return dummy



def initLinkedList(head):

    node = ListNode(val = head[0])
    dummy = node
    for idx in range(1, len(head)):
        node.next = ListNode(val = head[idx])
        node = node.next
    return dummy

def printLinkedList(node):
    while node.next:
        print(node.val)
        node = node.next

if __name__ == '__main__':
    head = [1, 2, 6, 3, 4, 5, 6]
    val = 6

    # head = [7,7,7,7]
    # val = 7

    head = initLinkedList(head)
    # printLinkedList(head)

    sol = Solution()
    node = sol.removeElements(head, val)
    printLinkedList(node)
