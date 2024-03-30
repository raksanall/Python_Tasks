# Given the head of a singly linked list, return true if it is a  palindrome or false otherwise.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        return arr==arr[::-1]

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false