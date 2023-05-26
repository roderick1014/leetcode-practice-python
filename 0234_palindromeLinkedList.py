# 0234 - Palindrome Linked List

'''
    Question:
        Given the head of a singly linked list, 
        return true if it is a palindrome or false otherwise.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


        # # Solution 3 - Floyd's Cycle Detection Algorithm (Optimal)
        if not head:
            return True
        
        slow = head 
        fast = head
        prev = None
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr

        while prev:
            if head.val != prev.val: return False
            head = head.next
            prev = prev.next
        return True

        # # Solution 2 - Stack
        # stack = []
        # curr = head
        
        # while curr:
        #     stack.append(curr.val)
        #     curr = curr.next
        # curr = head
        
        # while curr:
        #     if curr.val != stack.pop():
        #         return False        
        #     curr = curr.next
        # return True

        # # Solution 1 - Record the values to the list and apply palindrome checking algorithm.
        # record = []
        
        # while head:
        #     record.append(head.val)
        #     head = head.next

        # if (len(record) % 2) == 0:
        #     mid = (len(record) - 1) // 2
        #     left = mid
        #     right = mid + 1

        #     while right < len(record):
        #         if record[left] != record[right]:
        #             return False
        #         left -= 1
        #         right += 1
        # else:
        #     mid = len(record) // 2
        #     left = mid - 1
        #     right = mid + 1

        #     while right < len(record):
        #         if record[left] != record[right]:
        #             return False
        #         left -= 1
        #         right += 1

        # return True

        


if __name__ == '__main__':
    head = [1,2,2,1]
    node = ListNode(val = 1,
                    next = ListNode(val = 2,
                                    next = ListNode(val = 2, 
                                                    next = ListNode(val = 1))))
    # node = ListNode(val = 1,
    #                 next = ListNode(val = 0,
    #                                 next = ListNode(val = 0)))

    sol = Solution()
    print(sol.isPalindrome(node))
