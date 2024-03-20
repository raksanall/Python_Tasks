# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer=head
        if head:
            while pointer.next:
                if pointer.val==pointer.next.val:
                    pointer.next=pointer.next.next
                else:
                    pointer=pointer.next
            return head
 

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]