# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode(0)
        ptr = result
        carry = 0

        while l1 or l2:
            sum = carry

            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            carry = sum // 10
            sum = sum % 10
            ptr.next = ListNode(sum)
            ptr = ptr.next

        if carry:
            ptr.next = ListNode(carry)

        return result.next