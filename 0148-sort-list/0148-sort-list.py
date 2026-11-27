# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:

        # List empty hai ya ek hi node hai toh already sorted hai
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        # Slow middle tak jayega aur fast double speed se
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # List ko beech se tod diya
        right = slow.next
        slow.next = None

        # Dono halves ko alag alag sort karenge
        left = self.sortList(head)
        right = self.sortList(right)

        # Ab sorted lists ko merge karna hai
        dummy = ListNode(0)
        current = dummy

        while left and right:

            # Jo value chhoti hai uski node pehle jod do
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # Jo nodes bach gayi hain unko end mein jod do
        current.next = left if left else right

        return dummy.next