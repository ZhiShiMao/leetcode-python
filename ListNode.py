from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, nums: List):
        next = None
        for num in nums[::-1]:
            node = cls(num, next)
            next = node
        return next

    def to_list(self):
        node = self
        ret = []
        while node:
            ret.append(node.val)
            node = node.next
        return ret
