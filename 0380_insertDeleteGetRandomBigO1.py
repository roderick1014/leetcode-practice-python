# 380. Insert Delete GetRandom O(1).

'''
    Implement the RandomizedSet class:

    - RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present.
        Returns true if the item was not present, false otherwise.
    - bool remove(int val) Removes an item val from the set if present.
        Returns true if the item was present, false otherwise.
    - int getRandom() Returns a random element from the current set of elements
        (it's guaranteed that at least one element exists when this method is called).
        Each element must have the same probability of being returned.
    - You must implement the functions of the class such that each function works in
        average O(1) time complexity.
'''

'''
    A set is implemented essentially the same as a dict in python,
    so the time complexity of add / delete is on average O(1).
    When it comes to the random function, however, we run into the problem of needing to convert
    the data into a python list in order to return a random element.
    That conversion will add a significant overhead to getRandom, thus slowing the whole thing down.
'''

import random

class RandomizedSet(object):

    def __init__(self):
        self.data_map = {}
        self.data = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.data_map:
            return False

        self.data_map[val] = len(self.data) # represented as {val : index}
        self.data.append(val)

        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.data_map:
            return False

        last_elem_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]

        # to operate "pop()" operation, we have to switch the element at the end of the list,
        # re-assigning the variables to the position and apply pop() operation.
        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list

        self.data[-1] = val

        # remove the last element in the list
        self.data.pop()

        # remove the element to be removed from the dictionary
        self.data_map.pop(val)
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.data)

if __name__ == '__main__':
    # Your RandomizedSet object will be instantiated and called as such:
    randomizedSet = RandomizedSet();
    randomizedSet.insert(1) # Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomizedSet.remove(2) # Returns false as 2 does not exist in the set.
    randomizedSet.insert(2) # Inserts 2 to the set, returns true. Set now contains [1,2].
    randomizedSet.getRandom() # getRandom() should return either 1 or 2 randomly.
    randomizedSet.remove(1) # Removes 1 from the set, returns true. Set now contains [2].
    randomizedSet.insert(2) # 2 was already in the set, so return false.
    randomizedSet.getRandom() # Since 2 is the only number in the set, getRandom() will always return 2.