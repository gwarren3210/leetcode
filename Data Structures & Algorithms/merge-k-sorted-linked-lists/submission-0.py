# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        lists.sort(key=lambda x:x.val)
        head = lists[0]
        lists[0] = head.next
        if lists[0] == None: lists = lists[1:]
        head.next = self.mergeKLists(lists) 
        return head