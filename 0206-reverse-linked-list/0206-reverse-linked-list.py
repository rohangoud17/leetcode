# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = []
        while head:
            new_list.append(head.val)
            head = head.next
        
        result_head = None
        for item in new_list:
            newNode = ListNode(item)
            newNode.next = result_head
            result_head = newNode

            
        return result_head
        