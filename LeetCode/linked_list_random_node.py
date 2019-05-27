# Submission Link : https://leetcode.com/submissions/detail/231642422/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.ans = []
        while self.head:
            self.ans.append(self.head.val)
            self.head = self.head.next
        
        
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        return random.choice(self.ans)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
