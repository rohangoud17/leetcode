# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        new_list = []
        while head:
            new_list.append(head.val)
            head = head.next
        
        left = 0
        right = len(new_list) -1
        while left < right and new_list[left] == new_list[right]:
            left += 1
            right -= 1
        return left >= right
        