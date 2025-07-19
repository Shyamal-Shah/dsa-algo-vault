from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        dec = 0
        while head:
            dec = (dec << 1) | head.val
            head = head.next
        return dec


if __name__ == "__main__":
    head = ListNode()
    print(Solution().getDecimalValue(head))
