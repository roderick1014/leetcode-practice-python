# 0021 - mergeTwoLists

'''
    Question:
        Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
        Return the head of the merged linked list.


'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def setupListNode(input):
    currentlist = newlist = ListNode()

    for i in range(len(input)):

        currentlist.val = input[i]
        if (i + 1) == len(input):
            break
        currentlist.next = ListNode()
        currentlist = currentlist.next

    return newlist

def displayListNode(input):
    while input:
        print(input.val)
        input = input.next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
        if list1 or list2:
            cur.next = list1 if list1 else list2
        
        return dummy.next

if __name__ == '__main__':
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    list1 = setupListNode(list1)
    list2 = setupListNode(list2)

    # displayListNode(list1)
    # displayListNode(list2)

    sol = Solution()
    ans = sol.mergeTwoLists(list1, list2)
    displayListNode(ans)