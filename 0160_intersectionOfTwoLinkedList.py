# 0160 - Intersection of Two Linked list

'''
    Question:
        Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
        If the two linked lists have no intersection at all, return null.
''' 


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            print(pa.val, pb.val)
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa
            

if __name__ == '__main__':
    intersectVal = 2
    listA = [1, 9, 1, 2, 4]
    listB = [3, 2, 4]
    skipA = 3
    skipB = 1
    head_1 = ListNode(val = listA[0], next = ListNode(val = 9, next = ListNode(val = 1)))
    head_2 = ListNode(val = 3)
    intersection = ListNode(val = 2, next = ListNode(val = 4))
    head_1.next.next.next = intersection
    head_2.next = intersection

    sol = Solution()
    print(sol.getIntersectionNode(head_1, head_2).val)