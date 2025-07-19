from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sorted_list = None
        head = sorted_list
        while list1 and list2:
            val = -1
            if list1.val <= list2.val:
                val = list1.val
                list1 = list1.next
            elif list2.val <= list1.val:
                val = list2.val
                list2 = list2.next
            next = ListNode(val, None)
            if sorted_list:
                sorted_list.next = next
            else:
                head = next
            sorted_list = next

        while list1:
            next = ListNode(list1.val, None)
            if sorted_list:
                sorted_list.next = next
            else:
                head = next
            sorted_list = next
            list1 = list1.next
        while list2:
            next = ListNode(list2.val, None)
            if sorted_list:
                sorted_list.next = next
            else:
                head = next
            sorted_list = next
            list2 = list2.next
        return head


if __name__ == "__main__":
    head = Solution().mergeTwoLists(
        None, ListNode(1, ListNode(3, ListNode(4)))
    )
    while head:
        print(head.val)
        head = head.next
    # head = Solution().mergeTwoLists(
    #     ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))
    # )
    # while head:
    #     print(head.val)
    #     head = head.next
