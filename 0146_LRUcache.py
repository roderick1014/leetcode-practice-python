# 0146 - LRU Cache

'''
    Question:
        Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

        Implement the LRUCache class:

        LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
        int get(int key) Return the value of the key if the key exists, otherwise return -1.
        void put(int key, int value) Update the value of the key if the key exists.
        Otherwise, add the key-value pair to the cache.
        If the number of keys exceeds the capacity from this operation, evict the least recently used key.
        The functions get and put must each run in O(1) average time complexity.
'''

class ListNode:
    def __init__(self, key, value):
        # Double linked list.
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# Remember to connect the previous node and next node when processing double linked list.
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = dict()
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            node = self.dict[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.dict:
            node = self.dict[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value
        else:
            if len(self.dict) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key, value)
            self.dict[key] = node
            self.insertIntoHead(node)

    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertIntoHead(self, node):
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node

    def removeFromTail(self):
        if len(self.dict) == 0: return
        tail_node = self.tail.prev
        del self.dict[tail_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    pass